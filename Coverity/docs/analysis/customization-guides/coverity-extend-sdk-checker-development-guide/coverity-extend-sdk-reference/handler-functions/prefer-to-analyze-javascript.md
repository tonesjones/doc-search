---
title: "PREFER_TO_ANALYZE_JAVASCRIPT"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prefer_to_analyze_javascript.html"
content_id: "MSqdv9qVlccuChhrkhHfkg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:15.833499+00:00"
---

# PREFER_TO_ANALYZE_JAVASCRIPT

**Synopsis**

```
PREFER_TO_ANALYZE_JAVASCRIPT()
```

**Description**

This function makes the checker analyze JavaScript-based output in the intermediate
directory. By default, checkers otherwise analyze the C/C++ output.

Example:

```
START_EXTEND_CHECKER( js1, simple );
PREFER_TO_ANALYZE_JAVASCRIPT();
ANALYZE_TREE()
{
  ...
```

Note: If you have both JavaScript and C/C++ output in your intermediate directory and want to use
your checker on the C/C++, you can use the following option on the command line to
override `PREFER_TO_ANALYZE_JAVASCRIPT`: `--cpp`

For
example:

```
> checker-name --dir <intermediate_directory> --cpp
```

On
the other hand, if you want to analyze JavaScript output with a checker that does
not call `PREFER_TO_ANALYZE_JAVASCRIPT`, you can use the following
option to override the default behavior of the checker:
`--javascript`

For
example:

```
> checker-name --dir <intermediate_directory> --javascript
```
