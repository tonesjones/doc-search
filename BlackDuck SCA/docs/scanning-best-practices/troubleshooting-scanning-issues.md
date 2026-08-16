---
title: "Troubleshooting scanning issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/troubleshooting-scanning-issues.html"
content_id: "RwFpxhTmn7HU6zRRLzgINA"
version: "2026.7"
section: "Scanning Best Practices"
scraped_at: "2026-08-08T15:34:30.264065+00:00"
---

# Troubleshooting scanning issues

This chapter describes some scanning problems and provides solutions.

## Accidental full scan proliferation by folder paths which include build or commit ID

Suppose your build server performs a full scan of the same project repeatedly and the
full scan is mapped to the same project version each time. The build server creates
a workspace folder which includes a build or commit ID in the path. If a scan name
was not provided, Black Duck Detect creates a scan name which is derived
from the full folder path. Because that path includes an element that changes with
each build, the result is a growing list of scans that all are mapped to the same
project version. The resulting BOM for the project version will be the sum of all
components identified in all the scans, that is, across all the builds.

### Solution

1. If the goal is to provide quick feedback to developers and the results do
   not need to be persisted, switch to a rapid scan by using the following
   property:, **--detect.blackduck.scan.mode=RAPID**. Doing this will
   eliminate the problem because rapid scans only show the results for the
   code scanned, and it is not possible to integrate results from previous
   scans.
2. If the results should be persisted, supply a scan name using the
   **--detect.code.location.name** property so that each build
   over-writes the prior scan results. By over-writing the previous scans,
   the issue is eliminated, and we can ensure that the BOM is accurate.
   This also avoids accumulating lots of old scan data.

Click [here](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/a70278796354c7ed0ab8107252357c78.topic) for more information on Black Duck Detect
properties.

## Accidental full scan proliferation by a build server farm

If you have a build server farm creating your builds, then each time a build occurs
there is potentially a new host (up to the number of hosts in the farm). If you do
not supply your own scan name, Black Duck Detect derives one that includes
the hostname and therefore, you will get a different scan for each host. All full
scans will be mapped to the same project version in Black Duck and the result is
multiple redundant full scans mapping to the same project version.

### Solution

1. If the goal is to provide quick feedback to developers and the results do
   not need to be persisted, switch to a rapid scan by using the following
   property: **--detect.blackduck.scan.mode=RAPID**. Doing this will
   eliminate the problem because rapid scans only show the results for the
   code scanned, and it is not possible to integrate results from previous
   scans.
2. If the results should be persisted, supply a scan name using the
   **--detect.code.location.name** property so that each build
   over-writes the prior scan results. By over-writing the previous scans,
   we eliminate the issue and ensure that the BOM is accurate. This also
   avoids accumulating lots of old scan data.

Click [here](https://documentation.blackduck.com/bundle/detect/page/properties/all-properties.html) for more information on Black Duck Detect
properties.
