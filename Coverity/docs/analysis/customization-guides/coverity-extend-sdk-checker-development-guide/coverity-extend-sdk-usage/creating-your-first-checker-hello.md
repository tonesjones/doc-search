---
title: "Creating your first checker: hello"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-your-first-checker-hello.html"
content_id: "QwRly0tVaVI14VvJ6_cvYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:22.364378+00:00"
---

# Creating your first checker: hello

In this section, you will build and run the Hello checker, then commit issues it finds to
a stream in Coverity Connect. In addition to using Coverity Connect
and the Coverity Extend SDK, you will also need to run Coverity
Analysis commands on sample code and use Coverity Analysis to run your
Hello checker.

Important:

- You must have an installation of Coverity with a valid license. The
  Coverity Analysis installer can install Coverity
  Analysis along with the Coverity Extend SDK component and
  other Coverity products.

  For an introduction to Coverity products, see Coverity Analysis 2026.6.0 User and Administrator Guide.
- You must have access to an installation of Coverity Connect. As a
  best practice, you should use a test instance of Coverity Connect,
  rather than using a production instance. At minimum, you (or a Coverity
  Connect administrator) should set up a separate project in
  Coverity Connect with a test stream into which you can commit
  issues found by the Hello checker. You will need the stream name and a
  Coverity Connect role that gives you permission to commit
  issues to that stream and to view issues in that stream.

  For Coverity Connect installation and configuration details, see Coverity 2026.6.0 Installation and Upgrade Guide and Coverity Platform 2026.6.0 User and Administrator Guide.
