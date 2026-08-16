---
title: "Extensions to JSON supported by the configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extensions-to-json-supported-by-the-configuration-file.html"
content_id: "vmfO47sqQs99HX_ezPiODQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:29.818885+00:00"
---

# Extensions to JSON supported by the configuration file

Though the directive language is based on JSON, it also supports the following
extensions, all of which retain the property that the file format is a subset of
JavaScript. If you intend to use more standard JSON-processing tools, you might want to
avoid using these extensions.

- Comments are allowed, both single-line comments that start with
  `//` and extend to the end of the line, and multiline
  comments that start with `/*` and end with
  `*/`.
- In standard JSON, field names must appear within double quotes. In an analysis
  configuration file, you may omit the quotes if the name conforms to the
  customary rules for identifiers: that is, if the name matches the following
  regular expression (regex):

  `^[a-zA-Z_][a-zA-Z0-9_]*$`

  All field names in this file format conform to that regex, so none of them
  requires quotes in the configuration file. However, quoting them is permissible,
  and conforms to standard JSON.
- String literals can be extended across multiple lines (without introducing
  newlines into the string contents) by joining quoted string literal fragments
  with the `+` token, optionally surrounded by white space
  (including newlines). A string value can be composed of any number of
  concatenated fragments. This syntax follows that of JavaScript string
  concatenation.
- Objects and arrays can have a final, optional comma ( `,`
  ).
