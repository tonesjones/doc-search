---
title: "Using the 'exists' expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-exists-expression.html"
content_id: "sWlunTklycbXppsZhDLcNw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:44.075708+00:00"
---

# Using the 'exists' expression

Imagine that you want to write a checker to find all `switch` statements that don't have a `default` clause.

**Use case:**
:   Find `switch` statements that lack a `default` clause.

    A missing `default` clause is not only poor logic; it can lead to crashes.

The following code outline is an initial pass for such a checker:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "SWITCH_NO_DEFAULT";
    reports =
        for code in globalset allFunctionCode
            where code matches switchStatement as sw
            && /* ... we’re getting to this part next ... */ :
                {
                    events = [
                        {
                            description = "Switch without default";
                            location = sw.location;
                        }
                    ];
                };
};
```

Thus far, the code shown above finds all instances of `switch` statements.
We need to narrow the search. The variable `sw` is a `switchStatement` object, so it has a property called
`caseList`, which contains all the switch statements, including the default case.

We might be inclined to search `sw.caselist` for `defaultStatement`—but this just
returns the statement itself, when what we want to know is *whether* such a statement is present.
The `exists` expression comes to our aid.

A CodeXM `exists` expression looks like a `for-in` loop (to help illustrate what it does).
It differs from the `for` loop in that it returns `true` if there is *at least* one object that satisfies the condition.
It returns `false` otherwise.

The following code fragment shows how an `exists` expression is constructed:

[image: CXM code follows]

```
    exists t in sw.caseList
        where t matches defaultStatement
```

Actually, we want to also use the logical NOT operator, `!`, to find the `switch` statement
that does *not* contain a `default` clause.
So the completed checker looks like the following code:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "SWITCH_NO_DEFAULT";
    reports =
        for code in globalset allFunctionCode
            where code matches switchStatement as sw
            && ( ! (exists t in sw.caseList where t matches defaultStatement) ) :
                {
                    events = [
                        {
                            description = "Switch without default";
                            location = sw.location;
                        }
                    ];
                };
};
```

Note:
The space after the NOT operator `!` is not strictly required, but
we put it there to make the operator stand out. While you are reading code, neglecting to notice a NOT in a condition can lead to great confusion.
