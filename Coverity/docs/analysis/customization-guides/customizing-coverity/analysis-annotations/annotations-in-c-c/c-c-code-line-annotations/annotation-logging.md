---
title: "Annotation logging"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/annotation-logging.html"
content_id: "9G5jNc~NkkOxJwKpEBDGdA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:20.636058+00:00"
---

# Annotation logging

When Coverity Analysis applies a `//coverity` code-line annotation to C/C++ code,
it logs that occurrence in a CSV file named applied-annotations.csv.

The applied-annotations.csv file is written to the specified output directory.
It is not created if no code-line annotations are applied.

The annotations file contains the following columns:

- `file`
- `line`
- `tag`
- `checker`
- `mergeKey`
- `triage`

The meaning of each column is as follows:

file
:   The name of the source file.

line
:   The number of the line where the annotation was appplied.

tag
:   The string used by the annotation.

    For example, if the annotation was `//coverity[var_deref_op]` the value of `tag` will be `var_deref_op`.

checker
:   The name of the checker that reported the defect.

    For example, `FORWARD_NULL`.

mergeKey
:   The *merge key* (as displayed in reports by Coverity Connect) of the defect for which the annotation was applied.

triage
:   The triage category that was applied.

    This value is one of the following:
    `Intentional`, `False Positive`, or `SUPPRESS`.

    Note:
    `SUPPRESS` is not a classification used by Coverity Connect.
    Instead, this category prevents the defect from being reported at all.
    It shown in all caps to emphasize this distinction.
    For more about this classification, see The SUPPRESS classification.

The following shows a sample applied-annotations.csv file:

```
file,line,tag,checker,mergeKey,triage
/path/to/test.c,5,forward_null,FORWARD_NULL,35be2b579ff2c32af6f2ce0916ce8fb1,False Positive
/path/to/test.c,11,var_deref_op,FORWARD_NULL,a1f5c6d9a44f41d3d61083ca1dc38646,Intentional
```
