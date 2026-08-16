---
title: "Basic pattern matches and conditions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-pattern-matches-and-conditions.html"
content_id: "urduSt8vEvg04UrWHW7UNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:38.873570+00:00"
---

# Basic pattern matches and conditions

We've now reviewed the basics of creating a CodeXM checker, so let's go ahead and extend them.

CodeXM comes with some predefined patterns, but you can define your own as well.
This allows you to match more complex code.
In `NO_GOTO`, when code matches a `goto` statement in the source code, it generates an event.

To illustrate, let's write a simple checker called `VAR_DECL` to detect all declarations of variables.

**Use case:**
:   Find variable declarations.

    For example, you might want to verify that variables are initialized at declaration time.
    Uninitialized variables can lead to unexpected and erroneous values, and even to crashes.

We can use the basic structure of a CodeXM checker and start off with a stock checker definition
(like we did in the `NO_GOTO` example):

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "VAR_DECL";
    reports =
    for code in globalset allFunctionCode where code matches /* something */ : {
        events = [
            {
                description = "Variable declared.";
                location = code.location;
            }
        ]
    };
};
```

This time, instead of matching `goto` statements, we want to match variable declarations.
To do this, we use the aptly named `variableDeclaration` pattern in the following way:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "VAR_DECL";
    reports =
        for code in globalset allFunctionCode
            where code matches variableDeclaration : {
                events = [
                    {
                        description = "Variable declared.";
                        location = code.location;
                    }
                ]
            };
};
```

Note:
Just like the `gotoStatement` pattern, the `variableDeclaration` pattern is provided by the CodeXM C/C++ library.
The use of this library is specified by the `include` directive shown at the top of the code sample.

This checker is complete. You can run it by following the same steps you followed for your `NO_GOTO` checker,
as previously described in Running your CodeXM checker.

Going to the next level of complexity, let's say we want to determine whether the variable is initialized or not.
To check for this, we can make a new checker by enhancing our current `VAR_DECL` checker.

In CodeXM, when a pattern matches some code, the pattern doesn't just return `true`.
More usefully, we get access to the matched code, along with properties about that code. By adding `as <name>` to the end of a
`matches` operator, we tell CodeXM to assign a name to the result, so that we can refer to the result later on.

Our work-in-progress checker follows:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "UNINIT_VAR";
    reports =
        for code in globalset allFunctionCode
            where code matches variableDeclaration as decl:
        {
            events = [
                {
                    description = "Variable declared.";
                    location = code.location;
                }
            ]
        };
};
```

In the example above, the variable `code` can refer to any sort of code:
`if` statements, assignment expressions, function calls, and yes, variable declarations.
But `decl` will only ever be a variable declaration because it is the result of a match for that particular C or C++ pattern.
So we can use `decl` to access properties of a variable declaration in order to check for further conditions.

Now that we know we have a variable declaration, we want to decide if this is the kind of declaration we're interested in: that is, a declaration without an initialization.
The general pattern for narrowing down a search in this way looks like the following code fragment:

[image: CXM code follows]

```
            where code matches variableDeclaration as decl
            && /* ... examine the declaration ... */ : {
```

Seeing the general form above, we know we want to only consider variable declarations that are uninitialized.
It turns out that `variableDeclaration` has a property, `initializer`, whose value is `null` when a variable isn't initialized at declaration time.
Pattern properties, such as fields in a record or attributes in an object, are specified by a dot notation.
So to express that a variable does not have an initializer, we use the following code:

[image: CXM code follows]

```
            where code matches variableDeclaration as decl
            && (decl.initializer == null) : {
```

Combining all of the above, the code for the `UNINIT_VAR` checker should now look like the following:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "UNINIT_VAR";
    reports =
        for code in globalset allFunctionCode
            where code matches variableDeclaration as decl
            && (decl.initializer == null) :
        {
            events = [
                {
                    description = "Variable "
                                  + decl.variable
                                  + " is declared but not initialized.";
                    location = code.location;
                }
            ]
        };
};
```
