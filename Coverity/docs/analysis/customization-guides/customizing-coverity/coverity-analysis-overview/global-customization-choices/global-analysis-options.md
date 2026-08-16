---
title: "Global analysis options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/global-analysis-options.html"
content_id: "vK1K8FaRK7jn~jxJ7nTpyA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:08.732458+00:00"
---

# Global analysis options

The `cov-analyze` command line gives you coarse-grained, global
control over what code is analyzed, what checkers are run, and analysis
behavior.

**Use case:** Limit analysis to a particular language and set of checker options.

For example, a user wants to save time by rerunning an analysis, but this time testing
only their JavaScript® UI sub-component. This time, the user also wants
to employ a different set of checker options. Users can do both by passing the following
translation unit pattern via the `cov-analyze` command's
`--tu-pattern` option:

```
--tu-pattern="lang('JavaScript') && file('/ui/')"
```

**Use case:** Invoke the STACK_USE checker, which is disabled by default.

For example, the user is testing code meant to be run on an embedded system that has
severe resource constraints. Specifying the option `--enable STACK_USE`
turns on this checker, which now will report large-scale usage of the stack.

**Use case:** In C/C++ source, enable tracing of calls through function pointers, for
interprocedural analysis. (Tracing of calls via function pointers is disabled by
default.)

For example, the source to analyze includes a device driver that makes heavy use of C++
function pointers. Turning on the `cov-analyze` option
`--enable-fnptr` increases the thoroughness of interprocedural
testing, at the cost of some execution time.

**Learn more:** See the `cov-analyze`
section in the Coverity 2026.6.0 Command Reference.
