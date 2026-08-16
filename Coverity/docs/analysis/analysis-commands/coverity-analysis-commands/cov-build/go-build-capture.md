---
title: "Go build capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/go-build-capture.html"
content_id: "AvjwbH6KZJgxSXpydAj9cA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:53.982903+00:00"
---

# Go build capture

Go source files are emitted by performing a native build and intercepting calls to the Go
command line tool (that is, `go <command> [arguments]`) when the
command is `test` or `build`.

Note: If the Go command line tool is invoked by way of some other Go application, the
invocation of the Go command line tool is not captured.
