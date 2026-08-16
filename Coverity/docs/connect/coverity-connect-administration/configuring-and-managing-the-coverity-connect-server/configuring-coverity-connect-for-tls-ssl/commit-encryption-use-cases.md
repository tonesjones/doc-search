---
title: "Commit encryption use cases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/commit-encryption-use-cases.html"
content_id: "FbbcWVo2_iJcxwlhUyoyrg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:34.595846+00:00"
---

# Commit encryption use cases

Depending on your standards, Coverity Connect and its clients may need to alter their
configurations slightly to allow for committing over TLS/SSL. The typical use-cases for
encrypted commits are as follows:

TLS/SSL is not important for sending or receiving commits
:   Set the value of `commit.encryption` to `none`.
    See Commit encryption use cases.

TLS/SSL is important to Coverity Connect server or administrator
:   Leave `commit.encryption` with its default value of
    "`preferred`", or set the value of `commit.encryption` to
    `required`.
    See Commit encryption use cases.

TLS/SSL is required by the user
:   The Coverity Analysis developer must set the `cov-commit-defects
    --encryption` parameter to `required` for each
    commit.

The following table illustrates the expected outcomes for
`cov-commit-defects` based on the encryption values of the user and
Coverity Connect administrator.

  
 [image: image]
