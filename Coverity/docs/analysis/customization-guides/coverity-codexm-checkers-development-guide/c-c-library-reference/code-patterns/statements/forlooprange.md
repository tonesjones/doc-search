---
title: "forLoopRange"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forlooprange.html"
content_id: "BrO3u94wC3UiL47HxCLVbg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:58.410401+00:00"
---

# forLoopRange

Matches range-based `for` loops.
(This kind of `for` loop was introduced in C++11.)

Does not match any C-language code.

See also forLoopSimple, which matches
the classic `for` loop construct in either C or C++.

## Properties

`forLoopRange` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum forLoopKind` | The kind of loop: always `` `range` ``; see forLoopKind |
| `loopVariable` | `variable?` | The name of the loop control variable, if one was specified; `null` otherwise |
| `collectionExpression` | `expression` | The collection of things being enumerated. This is either a variable or a literal. |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently this is a `blockStatement`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following C++ code:

  
 [image: C++ code follows]   

```
for ( int x : arrayInts ) {
    doSomething(x);
};
```

... is matched by a `forLoopRange` CodeXM pattern.
In this example, the properties of this pattern are returned as follows:

1. `.kind` is `` `range` ``.
2. `.loopVariable` is the variable `x`.
3. `.collection` is the variable `arrayInts`.
4. `.bodyStatement` is the `blockStatement` that contains the function call `doSomething(x)`.

The following pattern detects any range-based `for` loop:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches forLoopRange
    };
```

A common coding mistake is the "do-nothing" `for` loop—that is, where the developer mistakenly types a semicolon
immediately after the `for` condition, as in this C++ expression:

  
 [image: C++ code follows]   

```
for ( int x: arrayInts );
```

The following CodeXM pattern can detect such a mistake:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches forLoopRange {
            .bodyStatement == emptyStatement
        }
    };
```

As a matter of C++ best practices, it is safe and efficient to make the loop variable of
a range-based `for` loop
a `const` reference, as in the following example:

  
 [image: C++ code follows]   

```
for ( auto const &x : vec ) {
    // ...
};
```

This protects you against unnecessary copying and accidental modification of the member that the loop variable refers to.
The following pattern detects any range-based `for` loop in which
the loop variable has not been declared with a `const` reference type:

  
 [image: CXM code follows]   

```
    pattern nonConstRefLoopVar {
        forLoopRange {
            .loopVariable.type != referenceType {
                .referenceOfType == constOf(anyType);
            }
        }
                };
```
