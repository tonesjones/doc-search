---
title: "BDIO aggregation"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/bdio-aggregation.html"
content_id: "N8d3uJEYS~VJ~Jttw7CFnw"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:25.723437+00:00"
---

# BDIO aggregation

Starting with version 8.0.0, Detect aggregates all package manager results into a single BDIO file / codelocation.

All dependency graphs produced by any of the following, executed during the Detect run, will be aggregated:

- Detectors
- Docker Inspector
- Bazel

This BDIO takes advantage of
functionality added to Black Duck SCA in version 2021.8.0
enabling Black Duck SCA to preserve both source information (indicating, for example, from which
subproject a dependency originated) and match type information (direct vs. transitive dependencies).

Detect now operates in a way that is similar to Detect 7
run with property detect.bom.aggregate.remediation.mode=SUBPROJECT.
The property detect.bom.aggregate.remediation.mode does not exist in Detect 8.

## Related properties

- detect.bdio.output.path
- detect.bdio.file.name
