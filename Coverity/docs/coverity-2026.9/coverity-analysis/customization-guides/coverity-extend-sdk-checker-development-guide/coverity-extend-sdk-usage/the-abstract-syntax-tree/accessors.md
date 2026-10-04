---
title: "Accessors"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/accessors.html"
content_id: "u9Ln0DLwfMKPgToHiw4Sgg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:54.149887+00:00"
---

# Accessors

In addition to the patterns, there are a variety of functions that perform various
queries on the AST. This section covers some of the more common functions. See Accessors for more information.

Several accessors return information about the current function being analyzed.

Table 1. Accessors for functions

|  |  |
| --- | --- |
| `current_function_get_name` | name of current function |
| `current_function_get_return_type` | return type of current function |
| `current_file_get_name` | file containing current function |
| `print_tree` | Returns detailed information on the node, including the type of pattern |

Others return information about a specific AST.

Table 2. Other accessors

|  |  |
| --- | --- |
| `get_type_of_tree` | get expression's type |
| `get_size_of_type` | representation size of a type |
