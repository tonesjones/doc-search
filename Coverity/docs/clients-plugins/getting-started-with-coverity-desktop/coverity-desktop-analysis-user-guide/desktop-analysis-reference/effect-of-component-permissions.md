---
title: "Effect of component permissions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/effect-of-component-permissions.html"
content_id: "xHwql7mAUIh8U6buyNNJ6Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:02.953883+00:00"
---

# Effect of component permissions

Desktop Analysis does not respect user permissions for components in Coverity Connect.
This means that when a user does not have access to a particular component, Desktop
Analysis will still be aware of any defects associated with that component. This could
cause some confusion, as the "present in reference" attribute, along with all other
triage information, is displayed correctly in the output. For example, if the issue was
found centrally, "present in reference" will be set to "true" even if the issue is in an
inaccessible component.

A common cause of this issue may be if an organization wants to suppress all issues from
third party code. In this case, the system administrator could place all third party
code into a private component, so that other Coverity Connect users would not see third
party issues. However, in this scenario, those issues would still be present in the
Desktop Analysis output. One way to ensure that this behavior does not occur is for the
Coverity Connect administrator to set the "Action" attribute for all third party issues
to "Ignore". This will cause Desktop Analysis to filter out those defects by default.
