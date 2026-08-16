---
title: "The capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-capture.html"
content_id: "4g7EoYMyuo9C_s5mZ5j5uA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:45.747167+00:00"
---

# The capture

After optionally generating a configuration, you need to capture a binary representation of your
source code to a directory (the *intermediate directory)* where it can be analyzed.
You have two main options: the Coverity CLI (with or without a build command), or build capture.

- Use the Coverity CLI for both compiled and non-compiled (interpreted) languages.
- Use `cov-build` for compiled languages.

Generally speaking, using the Coverity CLI without providing a build command requires no setup, no knowledge about
how to build your projects, no third-party tools installed, and gives you satisfactory results quickly.

After you test analysis using the Coverity CLI without providing a build command, if it makes sense for you to invest more time
to get more accurate results, you can specify a build command when you invoke `coverity capture`.
Alternatively, you can also use the `cov-build` command directly.

**In this section:**

- Build capture (for compiled languages)
- .NET build capture

**See also:**

- The capture: Examples
- The capture: Further notes on build capture
