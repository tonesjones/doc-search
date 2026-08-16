---
title: "stripImplicitCasts( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripimplicitcasts-e-.html"
content_id: "F1VVAMcMUmwcoTAvtvf6mg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:10.124901+00:00"
---

# stripImplicitCasts( e )

This function strips implicit casts from an expression.

In some circumstances, such as loop conditions, JavaScript wraps expressions with implicit casts.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to be stripped |
| ***return value*** | `expression` | The resulting expression that is not an implicit cast |
