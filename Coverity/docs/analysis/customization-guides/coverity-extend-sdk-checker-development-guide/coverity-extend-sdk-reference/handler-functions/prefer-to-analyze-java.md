---
title: "PREFER_TO_ANALYZE_JAVA"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prefer_to_analyze_java.html"
content_id: "PN27QuA0BCqFeR_Qg6ZN1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:15.150762+00:00"
---

# PREFER_TO_ANALYZE_JAVA

**Synopsis**

```
PREFER_TO_ANALYZE_JAVA()
```

**Description**

This function makes the checker analyze Java-based output in the intermediate directory.
By default, checkers otherwise analyze the C/C++ output.

Example:

```
START_EXTEND_CHECKER( java1, simple );
PREFER_TO_ANALYZE_JAVA();
ANALYZE_TREE()
{
  ...
```

The following error occurs if the intermediate directory does not contain Java
output:

```
[ERROR] This program operates on Static Java 
but specified intermediate directory int-dir 
only contains data for C/C++.
```

Note: If you have both Java and C/C++ output in your intermediate directory and want to use your
checker on the C/C++, you can use the following option on the command line to override
`PREFER_TO_ANALYZE_JAVA`: `--cpp`

For
example:

```
> checker-name --dir <intermediate_directory> --cpp
```

On
the other hand, if you want to analyze Java output with a checker that does not call
`PREFER_TO_ANALYZE_JAVA`, you can use the following option to
override the default behavior of the checker: `--java`

For
example:

```
> checker-name --dir <intermediate_directory> --java
```
