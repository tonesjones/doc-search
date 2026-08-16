---
title: "importStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/importstatement.html"
content_id: "PIaOqEuJstbIpkxKAoFL4w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:24.772902+00:00"
---

# importStatement

Matches `import` statements.

This pattern only matches nodes of type `statement`.

## Properties

`importStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `moduleSpecification` | `string?` | The name of the imported module; `null` if there is no name |
| `target` | `expression?` | The name of the target variable in a named import—for example, `Sys> in import sys as Sys`; `null` if there is none |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches statements that import from a module named `sys`:

[image: CXM code follows]

```
    pattern sysImport {
        importStatement {
            .moduleSpecification == "sys"
        }
    };
```
