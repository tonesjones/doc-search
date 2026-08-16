---
title: "The FALSE classification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-false-classification.html"
content_id: "tBBHI8vT2OnUls8foqtjeg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:19.330296+00:00"
---

# The FALSE classification

You can specify that a defect be classified as `FALSE`, for *False
Positive*.

`FALSE` is a stronger assertion than `Intentional`. A
False Positive asserts that developers are satisfied the code is not a bug under any
circumstances.

To explicitly classify a defect report as False Positive, in the analysis annotation
follow the event tag with a colon, and then with the keyword
`FALSE`.

For example, the following code annotation assigns the Coverity Connect
classification of `FALSE` to a `FORWARD_NULL`
event:

```
x = NULL;
...
//coverity[var_deref_op : FALSE]
*x = 0;                             /* bad_deref.c line 20 */
```
