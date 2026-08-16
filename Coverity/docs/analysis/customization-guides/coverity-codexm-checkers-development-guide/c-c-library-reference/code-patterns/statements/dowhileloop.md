---
title: "doWhileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dowhileloop.html"
content_id: "g8BJPc541XLs5his8OCqZg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:55.904379+00:00"
---

# doWhileLoop

Matches `do ... while` loops.

This pattern only matches nodes of type `statement`.

## Properties

`doWhileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition that causes the loop to terminate |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently this is a `blockStatement`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following C/C++ fragment matches `doWhileLoop`:

  
 [image: C/C++ code follows]   

```
do {
    DoSomethingWith( cachedResult );
} while ( cachedResult = SomeFunction() );
```

The `doWhileLoop` pattern sets the following properties:

- `.conditionExpression` is the condition expressed in parentheses; namely,
  `cachedResult = SomeFunction()`.
- `.bodyStatement` is the `DoSomethingWith()` call inside the loop.

A special case of the `do ... while` loop is the non-looping `do ... while`.
This can be used for the following reasons:

- It allows either `break` or `continue` to act as a well-structured
  `goto`—that is, a jump whose range is limited.
- It can be used with preprocessor function-like macros whose declaration must end in a semicolon
  (that is, the syntax of these macros is consistent with an actual function declaration).

The following pattern code detects a `do ... while` loop whose condition
is always `false`:

  
 [image: CXM code follows]   

```
    // Some idioms to say "false" in C and C++
    pattern alwaysFalseConstant =
        | booleanLiteral {.isTrue == false}
        | intLiteral     {.valueInt == 0}
        | binaryOperator {
              .lhsExpression == intLiteral{.valueInt != 0};
              .operator == `==`;
              .rhsExpression == intLiteral{.valueInt == 0}
          }
        | binaryOperator {
              .lhsExpression == intLiteral{.valueInt == 0};
              .operator == `==`;
              .rhsExpression == intLiteral.valueInt != 0}
          };
                
    /*
        Use of the do-while(0) idiom (a non-loop) has many uses,
        but sometimes requires added scrutiny
    */
    pattern doWhileNonLoop {
        doWhileLoop {
            .conditionExpression == alwaysFalseConstant
        }
    };
```
