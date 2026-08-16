---
title: "Copying and deleting projects and streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/copying-and-deleting-projects-and-streams.html"
content_id: "wztNnBGtKPHTl9rH5nh9rA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:01.454157+00:00"
---

# Copying and deleting projects and streams

Projects and streams have the same mechanism for copying and deleting:

- You can create a copy of a project or stream that will contain its original
  configuration settings. Copying is useful to preserve complex stream and
  component configuration that you might update in the original stream or project
  later.

  To create a copy, select a project or stream and click Duplicate. You
  can then edit the copied project or stream. Click Create
  to save your changes.
- To delete a project or stream, select it, and click
  Delete. When the delete prompt appears, click
  Delete to continue with the deletion, or
  Cancel to exit without deleting the project.

The data belonging to a stream is deleted in the background while Coverity Connect is
running. Some parts of this background activity conflict with other activities: for
example ETL, garbage collection, commit actions, intra-cluster synchronization. The
property cim.cleanup.stream.delay.min defines a delay that Coverity
Connect introduces between deleting separate streams to give an opportunity for other
conflicting activities to start. Before version 2020.03, the default value of this
property was 30 (minutes), and starting with 2020.03 the default value is 2 (minutes).
While it is possible to set the value of the property to 0, we do not recommend doing
so. It might be worth doing temporarily to delete a large number of streams as fast as
Coverity Connect can do it provided that starving all the conflicting activities is not
considered to be a problem.

The property cim.cleanup.stream.delay.min also affects auto-deletion of
expired streams. See Designating a stream for auto-deletion of expired streams for more
information.
