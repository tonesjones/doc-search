---
title: "BDIO aggregation"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/bdio-aggregation.html"
content_id: "N8d3uJEYS~VJ~Jttw7CFnw"
version: "12.0.0"
section: "Configuring Detect"
scraped_at: "2026-09-07T21:15:24.996961+00:00"
---

# BDIO aggregation

Detect aggregates all package manager results into a single BDIO file / codelocation.

All dependency graphs produced by any of the following, executed during the Detect run, will be aggregated:

- Detectors
- Docker Inspector
- Bazel

This BDIO takes advantage of Black Duck SCA functionality that enables Black Duck SCA to preserve both source information (indicating, for example, from which
subproject a dependency originated) and match type information (direct vs. transitive dependencies).

Detect now operates in a way that is similar to Detect 7
run with property detect.bom.aggregate.remediation.mode=SUBPROJECT.
The property detect.bom.aggregate.remediation.mode does not exist in Detect 8.

## Related properties

- detect.bdio.output.path
- detect.bdio.file.name
