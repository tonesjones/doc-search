---
title: "The node-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-node-type.html"
content_id: "qeeXNEgsVBjWvzr5Wcdu8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:05.589008+00:00"
---

# The node-type

The target code that CodeXM analyzes is represented by a variety of Abstract Syntax Tree (AST) node types.
An `astnode` is the root of this class hierarchy.

Tip:
The various language libraries provide meaningful subtypes that are particular to the target language.
As such, you are seldom likely to deal with these more abstract node types.
Instead you might deal with patterns with names such as—for example—`ifStatement`
or `binaryExpression`.
The abstract node types can sometimes be useful; for example, as parameter types to certain CodeXM functions,
or when you must specify a return type and no more specific type is exposed by the language library.

## Syntax

Each of the node types is represented by its corresponding keyword.

  
 [image: Syntax diagram, node-type]   

```
node-type ::=
      'astnode'
    | 'ctorinit'
    | 'declaration'
    | 'expression'
    | 'initializer'
    | 'statement'
```

## Details

`astnode`
:   An abstract, general-purpose base type.

    The remaining node types described in this section have more specialized purposes than `astsnode` does.

    Remember:
    The `astnode` type is available in every language library,
    and its properties are described in each language-library reference.

`ctorinit`
:   A *constructor initializer*.
    Constructors and destructors are features of some object-oriented programming languages, notably C#.

`declaration`
:   Code used to define an entity such as a variable or a function.
    In some languages, a variable declaration is constructed like an assignment statement, but in others it is not:
    so a declaration is not a statement *per se*.

    In a language whose variable declarations *do* look and behave like statements,
    the `initializer` is a subtype of
    `expression`.

`expression`
:   A portion of target code to evaluate.
    For example (to continue using an `if` statement as an illustration)
    the condition of an `if` statement is an expression.

    Quite frequently an expression is composed of subexpressions.
    For example, the expression `x + 2*y` is itself composed of two subexpressions:
    the identifier `x`
    and the subexpression `2*y`,
    which in turn can be broken down into constituent subexpressions: the integer literal `2` and the identifier
    `y`.

    Expressions of arbitrary complexity are possible, limited only by the capabilities of the language CodeXM is examining.

`initializer`
:   An expression used to set the initial value of a variable.

`statement`
:   A complete statement in the language being analyzed.
    Many languages permit *compound* statements; in particular, most flow-of-control statements can contain subordinate statements.
    For example, an `if` statement is—in many languages—a statement that contains one or two
    subordinate statements: the statement that is executed if the if-condition is `true`,
    and the statement, if present, that is executed if the condition is `false`.
