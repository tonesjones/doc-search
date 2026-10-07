---
title: "ReturnConstant"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/returnconstant.html"
content_id: "gCpeGvpoWzZc7MymLPxJgQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:01.806886+00:00"
---

# ReturnConstant

**Used by these directives:**
`method_returns_constant`

A `ReturnConstant` value is a JSON object that describes the constant
value returned by a method.

bool ReturnConstant value

- A JSON object describing a Boolean constant returned by a method.
- It has a field `bool`, taking a JSON Boolean value corresponding
  to the returned constant.
