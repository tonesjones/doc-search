---
title: "Operation: notify"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-notify.html"
content_id: "u8rn13hcA_L7UZJEy5J1Xg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:04.937904+00:00"
---

# Operation: notify

## Name

notify

## Description

Send an email notification to a specified user.

## Parameters

usernames
:   **Type:** string

    One or more usernames.

subject
:   **Type:** string

    Subject-line text for the email.

message
:   **Type:** string

    Body text for the email.

## Output (Literal)

The output of this operation is the argument notifyResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | string |

## Remarks

Precondition to using this operation: Coverity Connect must be properly configured to
send email.
