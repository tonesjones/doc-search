---
title: "Common properties of symbols"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/common-properties-of-symbols.html"
content_id: "ewpHDwIgPx~B5qKN~ah9GQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:59.852892+00:00"
---

# Common properties of symbols

In addition to the properties that are specific to each pattern,
all symbol patterns have the properties that are listed here.

| Name | Type | Description |
| --- | --- | --- |
| `access` | `enum AccessKeyword` | The scoping keywords associated with the symbol, such as `` `public` `` or `` `private` `` |
| `identifier` | `string?` | The string used as an unqualified name for the symbol; `null` if there is none |
| `is_file_or_readonly` | `bool` | `true` if the symbol has a `final` specifier (applies only to C++ source) |
| `language` | `enum` | Restricts reports to a particular source language. Can be one of `` `C` ``, `` `C++` ``, `` `Objective-C` ``, `` `Objective-C++ ``, `` `CUDA (Host)` ``, or `` `CUDA (Device)` ``. |
| `location` | `sourceloc` | The location where this symbol was declared |
| `mangledName` | `string?` | The internal "mangled" name used for the symbol (the mangled name includes type and scope information, to disambiguate this instance of the identifier); `null` if the mangled name is not available |
| `scopeList` | `list<string>` | A list of the class names and namespaces that enclose the symbol |
| `type` | `type` | The C/C++ type declared for this symbol |

## Example

The following CodeXM code snippet would retrieve issue reports only from CUDA Host functions:

[image: CXM code follows]

```
    report = for f in globalset allFunctionDefinitions where f.functionSymbol.language == `CUDA (Host)`:
        ...
```
