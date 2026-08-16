---
title: "The intermediate directory"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-intermediate-directory.html"
content_id: "GhBus18d0st1wnyD1IMAYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:58.324701+00:00"
---

# The intermediate directory

The intermediate directory stores data produced by the Coverity compiler, before the data
is committed to a Coverity Connect database.

CAUTION:

The intermediate directory might use a significant amount of space for large
code bases.

On Windows, the intermediate directory cannot be on a network drive,
neither as a mapped drive nor as a UNC path.

The intermediate directory is
intended to be modified only by Coverity programs. Unless directed by
Coverity support, do not create or remove files anywhere in the
intermediate directory.

You cannot use a VMware shared folder as a location to store the intermediate
directory.
