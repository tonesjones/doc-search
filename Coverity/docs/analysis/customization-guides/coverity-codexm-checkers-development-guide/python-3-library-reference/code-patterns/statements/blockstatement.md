---
title: "blockStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/blockstatement.html"
content_id: "luM8RrGmoKmrolJ8Np_Esg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:19.953536+00:00"
---

# blockStatement

Matches block statements; that is, statements that contain a sequence of other statements.

In Python, a block is also referred to as a *suite*.

This pattern only matches nodes of type `statement`.

## Properties

`blockStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `containedStatements` | `list<statement>` | The statements that the block contains |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a `blockStatement` that contains a single `passStatement`:

[image: CXM code follows]

```
    pattern passStatementBlock {
        blockStatement as blk where
            blk.containedStatements.length == 1
            && blk.containedStatements[0] matches passStatement
    };
```
