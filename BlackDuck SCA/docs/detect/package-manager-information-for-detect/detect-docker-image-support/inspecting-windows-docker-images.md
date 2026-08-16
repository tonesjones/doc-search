---
title: "Inspecting Windows Docker images"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/inspecting-windows-docker-images.html"
content_id: "jkYMBl52NfgJd~l~XRiCyg"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:58.552730+00:00"
---

# Inspecting Windows Docker images

Given a Windows Image, Docker Inspector, since it can only discover packages using
a Linux package manager, will not contribute any components to the BOM, but will
return the container filesystem (in the form of a squashed image),
which Detect will scan using the Black Duck Signature Scanner.
