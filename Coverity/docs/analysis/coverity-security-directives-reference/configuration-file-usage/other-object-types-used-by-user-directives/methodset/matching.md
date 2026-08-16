---
title: "matching"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/matching.html"
content_id: "qzFteMg8jinhF1Cmz27SCg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:27.132695+00:00"
---

# matching

A `matching MethodSet` matches method names by using a Perl-style regular expression.

## Fields

A `matching MethodSet` has a single field.

`matching`
:   A JSON string that contains a regular
    expression. It matches any method whose mangled name
    satisfies the regular expression. The entire name must be matched; a
    substring match is insufficient.

    See the MethodName section for a description of the mangled
    name format.

## Examples

The following `matching MethodSet` example matches any method named
`print()` in `mypackage.MyClass`, regardless of
the method’s signature (for example,
`mypackage.MyClass.print(int)int` and
`mypackage.MyClass.print(java.lang.String)void`).

```
{ "matching": "mypackage\\.MyClass\\.print\\(.*" }
```

Note: While `.` (a dot) and `$` (a dollar sign) are
characters that can appear in mangled names, they are also regex metacharacters and
so must be backslash-escaped. Since a backslash is a metacharacter in JSON, it too
must be escaped. Hence, when using one of these characters as a literal in a regex
context, you need to escape it by prefixing it with *two* backslashes
(`\\.` or `\\$`) as in the example above. If
instead, the regex above were `mypackage.MyClass.print.*`, it would
match mangled names such as `mypackageXMyClass.print(char)void`.
