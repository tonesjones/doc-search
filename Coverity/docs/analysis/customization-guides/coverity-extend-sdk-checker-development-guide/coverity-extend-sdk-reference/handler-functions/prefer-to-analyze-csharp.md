---
title: "PREFER_TO_ANALYZE_CSHARP"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prefer_to_analyze_csharp.html"
content_id: "lcWtl1na5fDUM94IJ72QhQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:14.502208+00:00"
---

# PREFER_TO_ANALYZE_CSHARP

**Synopsis**

```
PREFER_TO_ANALYZE_CSHARP()
```

**Description**

This function makes the checker analyze C#-based output in the intermediate directory. By
default, checkers otherwise analyze the C/C++ output.

Example:

```
START_EXTEND_CHECKER( cs1, simple );
PREFER_TO_ANALYZE_CSHARP();
ANALYZE_TREE()
{
  ...
```

The following error occurs if the intermediate directory does not contain C# output:

```
[ERROR] This program operates on Static C# 
but specified intermediate directory int-dir 
only contains data for C/C++.
```

Note: If you have both C# and C/C++ output in your intermediate directory and want to use your
checker on the C/C++, you can use the following option on the command line to override
`PREFER_TO_ANALYZE_CSHARP`: `--cpp`

For
example:

```
> checker-name --dir <intermediate_directory> --cpp
```

On
the other hand, if you want to analyze C# output with a checker that does not call
`PREFER_TO_ANALYZE_CSHARP`, you can use the following option to
override the default behavior of the checker: `--cs`

For
example:

```
> checker-name --dir <intermediate_directory> --cs
```
