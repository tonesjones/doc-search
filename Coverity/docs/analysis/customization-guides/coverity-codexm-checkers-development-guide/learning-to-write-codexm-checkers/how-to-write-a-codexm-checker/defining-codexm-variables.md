---
title: "Defining CodeXM variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defining-codexm-variables.html"
content_id: "KeAC4xg9eso2kbAGcBwV3Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:44.825753+00:00"
---

# Defining CodeXM variables

Like most common programming languages, CodeXM has the concept of variables.

*Unlike* most common programming languages, where you can change the value of a variable once it has been declared,
when you declare a variable in CodeXM you must assign it a value, and thereafter you cannot assign a new value to it.
The value of a CodeXM variable is effectively constant.

In CodeXM, you can define global and local variables, and the two have similar—though not identical—syntax.
They are also placed in two different locations within a file.

## Global variables

To define a global variable, you place it outside of a checker. This global variable is accessible (or, *in scope)* from any part of the file
in which the variable is declared. The following code shows the syntax for defining a global variable:

[image: CXM code follows]

```
    let variableName = value;
```

Always close a global variable declaration with a semicolon ( `;` ).

The following code fragment is an example of a global declaration as it might appear in CodeXM code:

[image: CXM code follows]

```
    let defect_message = "A defect was found.";
```

## Local variables

You define a local variable within the body of a checker or a function.
The following code shows the syntax for defining a local variable:

[image: CXM code follows]

```
    let variableName = value in
        /* Some expression where the variable is used */
```

The variable takes on the value computed, just as in the global case, but its value is available (in scope)
only within the expression that follows the keyword `in`.

The following example demonstrates variables local to particular `for` loops:

[image: CXM code follows]

```
    for sw in globalset allFunctionCode % switchStatement :
        let sw_cases =
            for vcs in sw.caseList % caseStatement
                where vcs.valueExpression matches intLiteral as lit :
                    lit
        in
            for c in sw_cases where c.value < 0 :
                // Do something with cases that have negative values.
```

Reviewing what the example shows, the first line identifies all `switch` statements (which we refer to, individually,
as `sw`). The first `for` loop enumerates all the `case` statements within a given instance
of `sw`, looking specifically for those that have an integer literal expression (for example, `case 42:`)
and then collecting that set into a variable named `sw_cases`.

In the lines that follow the third `in` (the one on its own line), `sw_cases` is used in the next
`for` loop to inspect each such integer to see if its value is less than zero.

The variable `vcs` is defined only within the first of the nested `for` loops, and the variable
`c` is defined only within the second.
The variable `sw` is available to both of the nested `for` loops, but it is available
nowhere outside the enclosing `for` loop that begins this code fragment.
