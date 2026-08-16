---
title: "Common properties of symbols"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/common-properties-of-symbols.html"
content_id: "KKiAyxvmqQG~yydew8c9Hw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:58.495105+00:00"
---

# Common properties of symbols

In addition to the properties that are specific to each pattern,
all symbol patterns have the properties that are listed here.

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string?` | The string used as an unqualified name for the symbol; `null` if there is none |
| `mangledName` | `string?` | The internal "mangled" name used for the symbol (the mangled name includes type and scope information, to disambiguate this instance of the identifier); `null` if the mangled name is not available |
| `location` | `sourceloc` | The location where this symbol was declared |
| `type` | `type` | The Go type declared for this symbol |
| `access` | `enum AccessKeyword` | The scoping keywords associated with the symbol, such as `` `public` `` or `` `private` `` |
| `is_file_or_readonly` | `bool` | `true` if the symbol has a `final` specifier |
| `scopeList` | `list<string>` | A list of the class names and namespaces that enclose the symbol |
