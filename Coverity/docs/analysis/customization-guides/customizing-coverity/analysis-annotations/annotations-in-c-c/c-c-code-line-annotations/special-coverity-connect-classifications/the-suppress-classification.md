---
title: "The SUPPRESS classification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-suppress-classification.html"
content_id: "_6apTZiY7omnnmFws_AE2w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:19.983124+00:00"
---

# The SUPPRESS classification

You can specify that a defect be classified as `SUPPRESS`, so that it
will not be saved.

(Introduced in version 2020.03.)

`SUPPRESS` is a stronger assertion than even `False
Positive`. When you suppress a defect, it is no longer saved by Coverity Connect at all, and it no longer appears in the analysis
summary.

To explicitly suppress a defect report, in the code annotation follow the event tag
with a colon, and then with the keyword `SUPPRESS`.

For example, the following analysis annotation suppresses the report of a
`FORWARD_NULL` event:

```
x = NULL;
...
//coverity[var_deref_op : SUPPRESS]
*x = 0;                              /* bad_deref.c line 20 */
```
