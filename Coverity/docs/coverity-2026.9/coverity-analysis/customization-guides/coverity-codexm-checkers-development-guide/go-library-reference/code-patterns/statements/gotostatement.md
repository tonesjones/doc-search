---
title: "gotoStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/gotostatement.html"
content_id: "6wTTcW4CnlQZGWLgd~7~YQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:33.911336+00:00"
---

# gotoStatement

Matches `goto` statements.

This pattern only matches nodes of type `statement`.

## Properties

`goToStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `labelStatement` | `statement` | The statement to go to |

**Inherits properties from:**

- astnode
- statement
