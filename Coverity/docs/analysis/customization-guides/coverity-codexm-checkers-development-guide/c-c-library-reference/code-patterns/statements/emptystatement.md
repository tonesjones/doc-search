---
title: "emptyStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/emptystatement.html"
content_id: "qv__pEjDG5JTLyYafDbpQw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:56.707464+00:00"
---

# emptyStatement

Matches empty statements.

An empty statement can be a line with no executable code that is terminated by a semicolon;
non-executable code enclosed by curly braces; or an implied branch of an `if` statement.

See also blockStatement.

## Properties

`emptyStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicit` | `bool` | Indicates whether the empty statement is implicit or not. |

**Inherits properties from:**

- astnode
- statement

## Example

Within a function, a semicolon without any code preceding it parses as an `emptyStatement`:

  
 [image: C/C++ code follows]   

```
/* No code here */ ;        // Matched by emptyStatement.
```

An `emptyStatement` can be inside
a `blockStatement,` matched by
`blockStatement { .containedStatements == emptyStatement }`:

  
 [image: C/C++ code follows]   

```
{
    ;    // Matched
}
```

CAUTION:

The following C/C++ code *does not* match `emptyStatement`.
Instead, this is a `blockStatement` where the list
of `.containedStatements` is empty:

  
 [image: C/C++ code follows]   

```
{
    // Not matched
}
```

A `for` loop with an empty body can be matched by
`forLoop { .bodyStatement == emptyStatement }`:

  
 [image: C/C++ code follows]   

```
for ( i = 0; i < max; i++ ) ;    // Matched by emptyStatement
```

The following CodeXM pattern matches any empty statement:

  
 [image: CXM code follows]   

```
    for c in mycodes {
        where c matches emptyStatement
    };
```

To match an empty statement located inside a `for` loop, use a CodeXM pattern such as the following:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches forLoop {
            .bodyStatement == emptyStatement
        }
    };
```

To match any implicit empty statement, you can use this CodeXM pattern:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches emptyStatement {
            .isImplicit == true
        }
    };
```
