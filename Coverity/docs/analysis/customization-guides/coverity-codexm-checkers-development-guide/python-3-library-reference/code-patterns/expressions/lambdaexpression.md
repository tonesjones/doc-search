---
title: "lambdaExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/lambdaexpression.html"
content_id: "PG6VLv12rZi703_jRPchGg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:42.776770+00:00"
---

# lambdaExpression

Matches lambda expressions.

Python lambda expressions are represented by closures and have function definitions of their own.

**Python 1 and Python 2:**
The lambda expression `lambda x=1 : x`
is represented by the following abstract syntax:

```
    {
        _python_( function.__defaults__ = None ) ,
        ( ( function.__annotations__ = {} ) ,
        ( ( function.__doc__ = None ) , function ) )_
    }
```

**Python 3:**
The lambda expression `lambda x=1 : x`
is represented by the following abstract syntax:

```
    (
        function.__defaults__ = { 1 } ) ,
        ( ( function.__doc__ = None ) ,
        function
    )
```

In either case, you can use the assignmentOperator pattern to match
the assignments that are implicit in the lambda expression.

This pattern only matches nodes of type `expression`.

## Properties

`lambdaExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `annotationsAssignmentOperator` | `assignmentOperator?` | The assignment of the `function.__annotations__` property (Python 3); `null` if this is not present |
| `defaultsAssignmentOperator` | `assignmentOperator` | The default argument values, `function.__defaults__` |
| `docStringAssignmentOperator` | `assignmentOperator` | The lambda doc string, `function.__doc__` |
| `functionSymbol` | `symbol` | The symbol of the lambda expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches a lambda expression that accepts two arguments:

[image: CXM code follows]

```
    pattern twoArgumentLambda {
        lambdaExpression {
            .functionSymbol == functionSymbol {
                .explicitParameterCount == 2
            }
        }
    };
```

## See also

listComprehension,
mapComprehension,
setComprehension,
tupleComprehension
