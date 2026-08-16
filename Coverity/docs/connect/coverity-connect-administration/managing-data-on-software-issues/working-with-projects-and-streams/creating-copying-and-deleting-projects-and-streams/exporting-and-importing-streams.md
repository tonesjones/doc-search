---
title: "Exporting and importing streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exporting-and-importing-streams.html"
content_id: "BbAOphwnCM9xDWIbADzzug"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:02.088653+00:00"
---

# Exporting and importing streams

A system administrator can use the cov-archive command to export a set
of streams into an archive file (and optionally delete the exported streams), import
streams from an archive, or get information about an archive file (its version, the date
and time of creation, the streams contained, and so on). You, the system administrator,
can *export* one or more streams to an archive file that contains those streams and
some associated entities. You may specify the streams to export either by name or by the
project to which they belong.

Exporting and importing streams can be useful in situations like the following:

- You need to save one or more streams offline and to restore these to online
  status in future.
- You need to transfer a stream to another Coverity Connect instance for
  coarse-grained load balancing or for some other administrative purpose.
- You need to remove streams from Coverity Connect as part of an offlining or
  moving operation, or simply to reclaim resources.

Export and import actions are logged in the file
<CC_install_dir>/logs/cov-archive.log. For more information
and for examples, please see the `cov-archive`
command in the Coverity 2026.6.0 Command Reference.

Note: You may import an archive into a Coverity Connect instance that has the same or a
newer version as the Coverity Connect instance used to create the archive. You can check
the Coverity Connect version used to create the archive using the cov-archive
list command.
