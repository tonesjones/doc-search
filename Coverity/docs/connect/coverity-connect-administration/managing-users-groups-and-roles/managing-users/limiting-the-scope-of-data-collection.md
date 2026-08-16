---
title: "Limiting the scope of data collection"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/limiting-the-scope-of-data-collection.html"
content_id: "E8n3vKa7lRGkssx5_8dQgA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:35.978240+00:00"
---

# Limiting the scope of data collection

You can change the scope of the data that the reporter
 collects by disabling its access to that data for any of the following
items:

- Project
- Stream
- Component

For example, you might want to omit data collection from certain streams so that the
issue data contained in those streams are not added to the overall issue trend data.

**To limit the scope of data collection on a project or stream:**

1. Navigate to the Configuration > Projects & Streams menu.
2. Select the appropriate project or stream from the file tree on the left.
3. Select the reporter user from the
   Roles tab and click Edit. If
   reporter isn't listed, click
   Add and type it in the
   Group/User field.
4. Assign the No Access permission to the user.

   Note: The No Access permission will only be assigned to the
   reporter in the context of this specific project or
   stream.

**To limit the scope of data collection on a component:**

1. Navigate to the Configuration > Component Maps menu.
2. Select the appropriate component under Component
   Maps.
3. On the Components tab, under
   Group/User, select the
   reporter user and click Edit.
   If reporter isn't listed, click
   Add and type it in the
   Group/User field.
4. Assign the No Access permission to the user. This
   permission will only be assigned to the reporter in the
   context of this specific component.

Note: Streams created through the Coverity Desktop plug-in automatically have the
User Group - No Access permission assigned to them by
default. This will cause data collection from these streams to be omitted. To enable
data collection for a stream created by the Coverity Desktop plug-in, remove the User
Group from the stream. Note that doing so effectively makes the stream visible to
others.
