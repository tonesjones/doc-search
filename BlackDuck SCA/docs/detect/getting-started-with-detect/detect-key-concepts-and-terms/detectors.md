---
title: "Detectors"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detectors.html"
content_id: "IZJzyBESfi___olLm~_Zew"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:07.097389+00:00"
---

# Detectors

The Black Duck® Detect Detector tool runs one or more detectors to find and extract dependencies from all supported package managers.

Each package manager ecosystem is assigned a detector type. Each detector type may use multiple methods (detectors) to extract dependencies.

Which detector(s) will run against your project is determined by the detector search process.

For example, the Maven detector, which is run by default, executes an mvn dependency:tree command against a Maven project and derives dependency information, which can be sent to Black Duck SCA

By default, all detectors are eligible to run. The set of detectors that actually run depends on the files that exist in your project directory and whether all detector requirements have been met.
