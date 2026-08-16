---
title: "Setting up streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-streams.html"
content_id: "awZ7pqBFIODQmtPbk4KyQg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:48.084417+00:00"
---

# Setting up streams

Desktop Analysis relies on a "reference snapshot" to provide analysis summary data.
Reference snapshots should be organized into one or more streams for user convenience.
As a Coverity Connect administrator, you must choose that stream organization.

As a general principle, if you choose to use more streams, developers will be able to
select a reference snapshot that is more similar to the code they are developing, and
hence get more accurate analysis results. However, the cost of more streams is the
necessity to set up and run more central analysis jobs, also requiring more storage
space on the Coverity Connect server.

The following list describes some of the most common stream design options.

One stream (simplest)
:   The simplest solution is to have only one stream enabled for Desktop
    Analysis. In this scenario, each Desktop Analysis user uses the same
    stream for analysis summaries.

Stream per branch (recommended)
:   The recommended organization is to have one stream per branch of your
    code base that is under active development. For example, you may have a
    separate branch for version X, Y, and Z of your code. By setting up a
    stream for each branch, developers working on separate versions will get
    the most accurate summary data for their version of the code.

Stream per branch and platform (most accurate)
:   By setting up one stream per platform, the analysis summary data will be
    specific not only to the version of your project, but also to its
    relative platform. While this configuration offers the most accurate
    summary information, it also requires the most maintenance. Unless your
    project contains significant differences between platforms, it is
    recommended that you use the "stream per branch" configuration.

Make sure that you select Enable Desktop Analysis from the
Desktop Analysis tab for each stream that will used by
Desktop Analysis developers. Any stream that is not meant for use with Desktop Analysis
should leave the Enable Desktop Analysis box unchecked, as
checking this box will cause more storage space to be used.

As a rough guide to space usage, if your code base has 10 million non-blank, non-comment
lines of code, the first snapshot with analysis summary data will require 2 GB of
storage space. Each additional snapshot will require another 100 MB of storage
space.

See Working with projects and streams for additional information on
creating and editing streams.
