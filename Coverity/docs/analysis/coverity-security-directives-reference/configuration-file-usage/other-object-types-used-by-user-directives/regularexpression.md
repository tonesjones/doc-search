---
title: "RegularExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regularexpression.html"
content_id: "GyYeQpvS2ZDfw8DypZ7AUA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:36.798136+00:00"
---

# RegularExpression

**Used by these objects:**
`AnnotationSet`, `IssueTypeDefinition`

A `RegularExpression` value is a JSON string that represents a regular
expression (regex) in [Perl syntax](http://perldoc.perl.org/perlre.html). Typically, a regular expression can match a
substring of a target string. The regular expression can include anchors (such as an
opening `^` or closing `$`) to explicitly specify the
beginning of a target string, the end of the target string, or both.

Because the backslash is an escaping character in both JSON strings and Perl
regular-expression syntax, a backslash used in a Perl regular expression needs to be
escaped with *another* backslash in the JSON string. In a Perl regular expression,
for example, a two-backslash sequence (`\\`) matches a single backslash
in the target string—so to match a single backslash, a
`RegularExpression` value requires *four* backslash characters:
`\\\\`.
