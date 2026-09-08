---
title: "Visual Log Filters"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/visual-log-filters.html"
content_id: "LH5aL~_kUm7ahDqSV1LUYg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:43.887797+00:00"
content_hash: "08281ef2c4055f1a1460b4737457ad4f806130622148ca04edafb78364316755"
---

# Visual Log Filters

The *Visual Log Page* offers a filtering capability that allows users to easily
select a subset of the log.

[image: image]

By default, the *Log Filter* section will contain a single blank filter block. Each
filter block contains three optional criteria:

- View only those log entries whose *User* is one of the users selected in the
  filter block.
- View only those log entries whose *Project* is one of the projects selected in
  the filter block.
- View only those log entries whose *Type* is one of the types selected in the
  filter block.

For example, you could set a filter in order to only view `failed-login`
events where someone attempted to log in as the "admin" user.

[image: image]

Clicking the *Or...* button below the filter will add an extra filter block,
allowing you to set alternate criteria. In the example below, the filter will select
`failed-login` events related to the "admin" user, **OR** any
event related to "Project A" and the "John Doe" user.

[image: image]

Note: Although all log types will be available for selection in the filter, those types may
not always be present in the log. For example, non-admin users will only be allowed to
view log events that are directly related to a project they manage, so they inherently
won't be able to see `failed-login` events, for example, because those
events are never associated with projects. Also, the `successful-login`
event is not recorded by default. See the Visual Log Configuration section in the install guide to enable recording of
that event type.
