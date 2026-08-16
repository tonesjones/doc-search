---
title: "Introduction to CodeXM"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-codexm.html"
content_id: "E1WfUytn_1pcSjd6djsDtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:31.957405+00:00"
---

# Introduction to CodeXM

The name *CodeXM* is short for *Code eXaMination*.

CodeXM is a specialized language used to write customized checkers that run using the Coverity engine.
It allows you to concisely define problematic patterns that you want to find in your source code.

CodeXM checkers are written in the CodeXM (CXM) language, which is easy to learn and allows you to write meaningful checkers quickly.
The CodeXM checker definition involves three elements:

- The checker name
- What pattern the checker should look for
- What message the checker should display when it finds that pattern

CodeXM checkers are seamlessly integrated with the typical Coverity workflow.
After writing your checker definitions in a text file, you simply pass the name of that file to the `cov-analyze` command.
The checkers defined in that file are executed along with Coverity's built-in checkers, and results are reported in the same way.

## Getting Help

If you need assistance, please open a Support case by logging in to the Black Duck Community
site (<https://community.blackduck.com/s/contactsupport>).
