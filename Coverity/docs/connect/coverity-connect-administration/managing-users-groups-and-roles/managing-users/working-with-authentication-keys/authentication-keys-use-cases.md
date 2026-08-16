---
title: "Authentication keys use cases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/authentication-keys-use-cases.html"
content_id: "pOu79ryr4_vvHd5OBRvvOg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:39.127839+00:00"
---

# Authentication keys use cases

There are three main scenarios in which a user should consider using an authentication
key:

Desktop Analysis with the `cov-run-desktop` command
:   When performing desktop analysis, `cov-run-desktop`
    needs to communicate with Coverity Connect (unless in disconnected
    mode). Using an authentication key is a secure alternative to typing a
    password on every analysis.

Certain requests when password-based authentication is disabled
:   When RPA is enabled, password-based authentication can be optionally disabled (for details, see
    RPA key concepts). If
    password-based authentication is disabled, you must use authentication
    keys (instead of password-based authentication) for SOAP and REST Web
    services requests and for `cov-commit-defects`
    requests.

Periodic commits of new analysis snapshots with `cov-commit-defects`
:   A user or administrator might use a script to run periodic analyses and
    commits. Using an authentication key is more secure than having the
    Coverity Connect password hard-coded directly in the script.

Authentication keys can be used for all administrative actions that can be
performed by means of a web service. For example, authentication keys can be used for
scripts that create or update projects and streams, or create triage stores.

Note: When an authentication key is created by `cov-manage-im`, its file
permissions will only allow the user who created the key file to read it. If the file
permissions are changed to allow other users to read the file, the
`cov-*` tools will no longer accept the key.
