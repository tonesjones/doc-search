---
title: "Enabling MISRA compliance testing"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/enabling-misra-compliance-testing.html"
content_id: "rCGIyT4dWBRTyBPw6gesIA"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.140019+00:00"
---

# Enabling MISRA compliance testing

Within the Eclipse and Visual Studio environments, Code Sight can run the Coverity
MISRA compliance tests.

To enable MISRA testing, add the following entry to the `"settings"` section of your
current configuration file.
Here is an example in JSON format:

```
"cov_run_desktop": {
    "coding_standard_configs": [
        "$(code_base_dir)/MISRA_c2012_7.config"
    ]
}
```
