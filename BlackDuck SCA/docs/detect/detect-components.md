---
title: "Detect Components"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-components.html"
content_id: "J7hHBARvgOFyNAAVKT5P5g"
version: "11.5.1"
section: "Detect Components"
scraped_at: "2026-08-08T23:44:44.900890+00:00"
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
