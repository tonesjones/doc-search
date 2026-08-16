---
title: "ReturnConstant"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returnconstant.html"
content_id: "gCpeGvpoWzZc7MymLPxJgQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:37.673814+00:00"
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
