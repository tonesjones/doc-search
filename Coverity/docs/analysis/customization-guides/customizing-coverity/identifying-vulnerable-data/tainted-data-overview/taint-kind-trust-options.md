---
title: "Taint kind trust options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taint-kind-trust-options.html"
content_id: "6ruzj~fgjEPdecf4DVa2VQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:21.749485+00:00"
---

# Taint kind trust options

For the `cov-analyze` and
`cov-run-desktop` commands, several options let you customize the
trust settings for a particular scan.

For example, using the HEADER_INJECTION checker, the following settings affect the
`cookie` taint kind (and in some cases, other taint kinds as
well):

`--trust-all` or `--distrust-all`
:   Trusts or distrusts *all* taint kinds, including `cookie`,
    for all the checkers being run.

`--trust-cookie` or `--distrust-cookie`
:   Trusts or distrusts only the `cookie` taint kind, for all the
    checkers being run.

`--checker-option HEADER_INJECTION:trust_cookie:true`
:   Trusts the `cookie` taint kind for the HEADER_INJECTION checker.

    This option overrides the `--distrust-cookie` or the
    `--distrust-all` options, if those are also
    specified.

`--checker-option HEADER_INJECTION:trust_cookie:false`
:   Distrusts the `cookie` taint kind for the HEADER_INJECTION
    checker.

    This option overrides the `--trust-cookie` or the
    `--trust-all` options, if those are also
    specified.

## Benchmark scanning:

Security analysis tool benchmarks often take the point of view that *every* kind
of tainted data should be distrusted. When you run a benchmark scan, use the
`--distrust-all` option, with no checker-specific trust settings,
to distrust all taint kinds.

Remember: Setting `--webapp-security--agressiveness-level` to
`high` includes the effect of setting
`--distrust-all`.
