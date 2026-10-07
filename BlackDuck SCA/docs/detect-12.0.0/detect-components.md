---
title: "Detect Components"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-components.html"
content_id: "J7hHBARvgOFyNAAVKT5P5g"
version: "12.0.0"
section: "Detect Components"
scraped_at: "2026-10-04T23:33:20.138232+00:00"
content_hash: "4b624da5bd045b1140f28b9e7f57bb6e9eec7375bef4e44aec84ebd67475448f"
---

# Detect Components

This topic introduces the components in Detect that are used to examine your code and produce analyzable output.

The components comprise the following:

## Tools

Each Detect run consists of running any applicable Detect tools used in the analysis of code.

## Detectors

Detect uses detectors, appropriate to your package manager ecosystem, to find and extract dependencies from all supported package managers.

For a quick tutorial on detectors, see: [Detectors Introduction](https://community.blackduck.com/s/article/Black-Duck-Detectors-Introduction).

## Inspectors

An inspector is typically a plugin that Detect uses to access the internal resources of a package manager through its API.
