---
title: "Tools"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/tools.html"
content_id: "CzfTZRGmNQASgyITof92tQ"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:12.641157+00:00"
---

# Tools

Black Duck® Detect tools are components that enable the scanning of your source code. Detect uses several underlying tools to perform scanning including:

- Detector (for inspecting package manager dependencies)
- Signature Scanner (for inspecting the file system)
- Docker Inspector (for inspecting Docker container content)
- Bazel detector ( to discover dependencies in Bazel projects)
- Binary Analysis (used to determine components within binary files)
- Vulnerability Impact Analysis Tool (generates a Vulnerability Impact Analysis Report)
- IaC Scanner (supports infrastructure as code scanning)
- Container Scanning (scanning container images to provide component risk details)

Optional properties can be specified to explicitly enable or disable these underlying tools, but by default, Detect will run both the Detector and Signature Scanner on the code being analyzed when a valid path with analyzable content is provided.

The default tools that are run by Detect:

- Detector (--detect.tools=DETECTOR).
  The detector tool runs the appropriate detectors that are used to find and extract dependencies by using package manager inspection.
- Black Duck Signature Scanner (--detect.tools=SIGNATURE_SCAN).
  The Black Duck Signature Scanner tool runs by default when Black Duck SCA connection details are provided. A file/folder (Signature) scan is performed on the built project to examine all project files for open-source software.

Other Detect tools such as Docker Inspector or Black Duck - Binary Analysis are not run by default in most scenarios but can be added to a run by specifying their properties on the command line.
