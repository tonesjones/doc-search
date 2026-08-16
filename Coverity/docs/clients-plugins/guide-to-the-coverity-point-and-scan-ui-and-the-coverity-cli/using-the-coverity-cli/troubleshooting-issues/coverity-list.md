---
title: "coverity list"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-list.html"
content_id: "oMCjemJBbmNPqyuprA0_qw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:21.765575+00:00"
---

# coverity list

The `coverity list` command is most useful for troubleshooting issues where an
expected defect is not found, or to confirm that the expected set of files actually were captured for analysis.

If a file was not captured then it will not be analyzed. The `coverity list` command displays the set of files
that are present in the project directory and labels each one with a capture status.
The capture status can be `"Succeeded”`, `"Incomplete"`, `"Failed"`, or `"Ignored"`.

- If a file has a capture status of `"Incomplete"`, this means that Coverity understood only some of the content in the file.
  This can occur when the Coverity compiler for the corresponding language skips over parts of the source file it doesn't understand.
- If a file has a capture status of `"Failed"`, this means that the Coverity compiler didn't understand the content of the file at all.
- If a file has a capture status of `"Ignored"`, this means that Coverity did not attempt to capture the file at all,
  either because the file type is not supported or because the file was excluded from capture by the current configuration.
