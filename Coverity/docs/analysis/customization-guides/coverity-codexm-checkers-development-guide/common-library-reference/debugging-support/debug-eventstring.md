---
title: "debug( eventstring )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/debug-eventstring-.html"
content_id: "ALoADJOz2B_omJppAZG02Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:24.813087+00:00"
---

# debug( eventstring )

Prints a message to a standard output stream.

Important:
The `debug()` function does not generate output unless you specify the
`--codexm-print-debug` option when you invoke `cov-analyze`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `eventString` | `eventString` | The string to print |
| ***return value*** | `bool` | Always returns `true`. |

## Example

The following expression prints out the debug log.
This log is located at ./<output_dir>/output/analysis-log.txt.

[image: CXM code follows]

```
    let _ = debug( "custom debug message:" + n ) in // ...
```

Note:
We don't care about the value that `debug()` returns,
so here we use the underscore as a placeholder variable name. We won't reference it elsewhere.
