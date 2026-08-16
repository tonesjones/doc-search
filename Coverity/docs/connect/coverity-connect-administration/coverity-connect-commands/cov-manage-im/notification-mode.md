---
title: "Notification mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/notification-mode.html"
content_id: "sSQ1NZVz7Z4DXZgNaxXpcg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:36.650591+00:00"
---

# Notification mode

Manually triggers a notification on a specific Coverity Connect view.

## Synopsis

```
--mode notification --execute --view viewName
```

For shared views, only the user who shared the view can trigger the notification. An
error will occur if the user with whom the view is shared attempts to trigger the
notification through this command option.

For help configuring notification settings for a view in Coverity Connect, see Coverity Platform 2026.6.0 User and Administrator Guide.

## Notification mode options

In general, you can specify options in any order.

The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option in commit mode.

    --execute
    :   Triggers the firing of the notification email.
        `--execute` requires the inclusion of
        the `--view` filter.

FILTER options
:   FILTER options focus the set of defects that are operated on.

    --view viewName
    :   Specifies the Coverity Connect view for which the
        notification will be sent.

## Notification mode example

This example shows the command to trigger a notification on the Coverity Connect
view, myView.

```
> cov-manage-im --mode notification --execute --view myView
```
