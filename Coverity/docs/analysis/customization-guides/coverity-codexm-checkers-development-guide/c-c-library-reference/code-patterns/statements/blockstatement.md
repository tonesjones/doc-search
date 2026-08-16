---
title: "blockStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/blockstatement.html"
content_id: "emWPwNG_n6az_SQjdQKV9A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:52.310556+00:00"
---

# blockStatement

Matches a sequence of statements enclosed by curly braces.

This pattern only matches nodes of type `statement`.

## Properties

`blockStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `containedStatements` | `list<statement>` | An ordered list of the statements that the block contains |

**Inherits properties from:**

- astnode
- statement

## Example

For the following `blockStatement`, `.containedStatements` contains only a
`simpleStatement`—specifically, an `assignmentOperator`,
`x = 1;` in the target code:

  
 [image: C/C++ code follows]   

```
{
    x = 1;
}
```

The following code shows a `blockStatement` whose
`.containedStatements` contains only an empty list:

  
 [image: C/C++ code follows]   

```
{
}
```

The following CodeXM pattern matches blocks that contain only an empty statement (for example,
`{ ; }`):

  
 [image: CXM code follows]   

```
    pattern emptyBlockStatement {
        blockStatement as bstmt where
            bstmt.containedStatements.length == 1 &&
                bstmt.containedStatements matches emptyStatement
};
```
