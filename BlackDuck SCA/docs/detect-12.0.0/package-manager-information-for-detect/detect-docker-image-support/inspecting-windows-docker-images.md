---
title: "Inspecting Windows Docker images"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/inspecting-windows-docker-images.html"
content_id: "jkYMBl52NfgJd~l~XRiCyg"
version: "12.0.0"
section: "Package Manager information for Detect"
scraped_at: "2026-09-07T21:16:04.422244+00:00"
---

# Inspecting Windows Docker images

Given a Windows Image, Docker Inspector, since it can only discover packages using
a Linux package manager, will not contribute any components to the BOM, but will
return the container filesystem (in the form of a squashed image),
which Detect will scan using the Black Duck Signature Scanner.
