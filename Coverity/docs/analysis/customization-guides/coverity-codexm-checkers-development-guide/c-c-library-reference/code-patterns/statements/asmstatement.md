---
title: "asmStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/asmstatement.html"
content_id: "jVPlY4aZlrBZ32_dlTcMVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:51.484676+00:00"
---

# asmStatement

Matches `asm` statements (C++ only) and their associated assembly source.

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `sourceString` | `expression` | The assembly source code contained within the `asm` statement |
| `gccOperands` | `list<record>?` | Additional GNU Compiler Collection operands, such as `infile` and `outfile`. If the compiler is not GCC-based, this property is `null`. |
| `kind` | `enum (see below)` | Specifies the development framework. |

The `kind` property can be one of the following:

- `` `ADK_GNU` ``
- `` `ADK_MICROSOFT` ``
- `` `ADK_PREPROCESSOR_DIRECTIVE` ``
- `` `ADK_STANDARD` ``

**Inherits properties from:**

- astnode
- statement

## Example

The `asmStatement` pattern matches an
`asm statement` such as the following:

  
 [image: C++ code follows]   

```
asm (
    "movl %1, %%eax;"
    "movl %%eax, %0;"
    :"=r"(y)          // y is output operand
    :"r"(x)           // x is input operand
    :"%eax"           // %eax is clobbered register
z);
```

In this example, the `.sourceString` contains the entire assembly string
`"mov1 %1, %%eax; movl %%eax, %0"`
(which will have been string-glued by the compiler).
Since this example illustrates a GCC-based `asm` statement,
the `.gccOperands` list contains
`y` and `x`, and
`.kind` is set to `` `ADK_STANDARD` ``.
