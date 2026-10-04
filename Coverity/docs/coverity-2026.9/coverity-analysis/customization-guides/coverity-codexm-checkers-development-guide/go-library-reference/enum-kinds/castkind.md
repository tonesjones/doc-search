---
title: "castKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/castkind.html"
content_id: "QepIvKs2_o9pwlqcl~6MCw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:32.675505+00:00"
---

# castKind

Represents the various kinds of type casts in Go.

The following values are defined:

| Name | Description |
| --- | --- |
| `` `dynamic` `` | A dynamic cast |
| `` `explicit` `` | An explicit cast |
| `` `implicit` `` | An implicit cast |

## Example

In Go an explicit type cast, or *conversion,* appears similar to a function call.
For example, consider the following declarations:

  
 [image: Go code follows]   

```
    var sum int = 17
    var count int = 5
    var mean float32
```

... then to obtain a value for `mean` based on `sum` and
`count`, the Go code would first have to convert the integers to 32-bit floating-point
values, as follows:

  
 [image: Go code follows]   

```
    mean = float32(sum) / float32(count)
```

## See also

castOperator
