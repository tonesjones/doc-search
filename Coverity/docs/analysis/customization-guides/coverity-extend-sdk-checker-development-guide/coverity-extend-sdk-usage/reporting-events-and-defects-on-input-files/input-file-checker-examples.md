---
title: "Input file checker examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/input-file-checker-examples.html"
content_id: "VZp_0Vv6w1dD5M9XzZ4vJA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:01.743188+00:00"
---

# Input file checker examples

The sample checkers iterate over input files, querying encoding and parent archives,
loading the contents to the emit (part of the intermediate directory), and reporting
defects in both simple and stateful checkers.

Location: <intermediate_directory>
sdk/samples

- `java_input_file_simple.cpp`
- `java_input_file_stateful.cpp`
