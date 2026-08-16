---
title: "Build capture example"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/build-capture-example.html"
content_id: "qp37Sn8gvvS0KbL7cwwktA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:55.939272+00:00"
---

# Build capture example

- For compiled languages (build capture), including Java build capture:

  ```
  > cov-build --dir <intermediate_directory> <BUILD_COMMAND>
  ```

Note:
To capture code that is not compiled, such as scripts and interpreted code, use
the CLI command `coverity capture`.
See the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.
