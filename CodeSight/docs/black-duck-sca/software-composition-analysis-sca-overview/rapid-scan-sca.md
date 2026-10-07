---
title: "Rapid Scan SCA"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/rapid-scan-sca.html"
content_id: "BjWNIkNC9~qvM6jF6g_chA"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.531930+00:00"
---

# Rapid Scan SCA

Rapid Scan SCA performs *software composition analysis* (SCA).
It is the SCA engine that is installed when you set up the
Code Sight Standard Edition (CSSE).

Like Black Duck, Rapid Scan SCA is driven by the Black Duck®
Detect component.
However, Rapid Scan SCA *always* runs standalone, and does not connect to a Black Duck server.
This enables Rapid Scan SCA to take less time than a Black Duck scan might require;
on the other hand, Rapid Scan SCA might not detect all the issues that a full Black Duck scan is
likely to detect, and the details it reports about those issues might not be as complete.

If you have been using the Code Sight Standard Edition with Rapid Scan SCA and then install
Black Duck, from that point Black Duck supplants Rapid Scan Static:
It always runs while connected to the specified Black Duck server, and all the Open Source Analysis
issues that Code Sight displays for a new scan are reported to be “Black Duck (SCA)” issues.
