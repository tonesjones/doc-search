---
title: "Visual Log Messages"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/visual-log-messages.html"
content_id: "DBRgxnUPJ~wcIA45iQ9IGw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:43.059843+00:00"
content_hash: "df614e0a2c93df931f8edae3d9d71e834f57f9a9a62cfbbd9b02142d0ddacbfb"
---

# Visual Log Messages

An entry in the visual log contains several useful parts:

[image: image]

- **Type** is an identifier for the type of event that the entry describes. The
  entry's type can be used as a filter criteria (explained below).
- **Title** is a brief description of the event.
- **Timestamp** indicates when the event happened. The default display mode for
  this is " ago", but hovering the mouse over the timestamp will reveal the precise
  date and time of the event.
- **Expand/Collapse** can be clicked to expand or collapse the log entry. By
  default, all log entries are collapsed. You can actually click anywhere in the
  colored title area to expand or collapse the log entry.
- **Body** a longer-form description of the event. In some cases, it may be the
  same as the title.
- **Identifying Info** points out the Project and User associated with the event,
  if applicable. For example, a login attempt for a Software Risk Manager user would
  be associated with that user. An analysis failure event would be associated with the
  Project for which the analysis failed.
- **Metadata** is unstructured information related to the event. In the example
  shown above, the *IP Address*, *Login Method*, and *Reason* are all
  metadata specific to the `failed-login`event type. Other event types
  can (and typically will) have different metadata fields.
- **Actions** refer to the bar at the bottom of an expanded event, containing one
  or more buttons.
  - The *Dismiss* button will cause the entry to become "dismissed," which
    will hide the event from view by default when visiting the page later.
  - The *Retry* button will be available for some error-type events,
    allowing users to retry whatever process whose failure generated the log
    entry.

As noted in reference to the *Timestamp*, the visual log is ordered in
reverse-chronological order, so that the newest events will be at the top. As you scroll
through the log, you'll eventually encounter a Load More button that will load the next
portion of the log. You can keep scrolling and clicking Load More until you reach the
end of the log (the earliest event). While you are on the Visual Log page, if new events
happen, rather than interrupting your view of the log by immediately appearing and
altering the UI, a notification will appear at the top of the page, prompting you to
reload the log.

## Dismissed Entries

Clicking Dismiss on a visual log entry will "dismiss" it, sending it into a
semi-ignored state.

Once a reload is triggered (e.g., by refreshing the page, clicking the "click to
reload" prompt, changing filter states, or changing view menu settings), dismissed
entries will be hidden from view (assuming the *Include dismissed log entries*
setting in the *View* menu is switched off). The *Include dismissed log
entries* setting in the *View* menu can be toggled to show or hide
dismissed log entries, causing them to appear with the checkered background
style.
