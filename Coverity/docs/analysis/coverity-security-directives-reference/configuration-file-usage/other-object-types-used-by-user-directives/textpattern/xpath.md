---
title: "xpath"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/xpath.html"
content_id: "EQC8s9F6nB6XaxuJ2qetvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:41.722172+00:00"
---

# xpath

An `xpath TextPattern` describes an Xpath 1.0 expression that can be used
to match elements in an XML document.

If this pattern is applied to an input that is not parsable as XML, it will not
match.

## Fields

The `xpath TextPattern` object has a single field:

`xpath`
:   A string value that specifies an Xpath expression.

## Examples

```
{ "xpath" : "/Catalog/Product[@name = \"soup\"]" },
```

```
{ "xpath" : "/*[local-name()='project']/*[local-name()='dependencies'] and child::*[local-name()='artifactId']" },
```

Notice that the double quotes in the Xpath expression have been escaped for JSON,
using a backslash.

Tip: The `local-name()` function can be a convenient way to
ignore the stricter namespace-specific element matching.
