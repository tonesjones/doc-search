---
title: "Black Duck® Detect's scan target"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/black-duck-detect-s-scan-target.html"
content_id: "kwJnLsAGD7RTMO~LL5reCw"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:57.304514+00:00"
---

# Black Duck® Detect's scan target

When a Docker image is run; for example, using a docker run command, a container is created that has an initial file system. This initial container file system can be determined in advance from the image without running the actual image. Since the target image is not yet trusted, Docker Inspector does not run the image; that is, it does not create a container from the image, but it does construct the initial container file system.

When Detect invokes both Black Duck SCA, and Docker Inspector because detect.docker.image or detect.docker.tar are set, the target of that Black Duck signature scan is the initial container file system constructed by Docker Inspector. The intial container file system is packaged in a way to optimize results from Black Duck SCA's matching algorithms. Rather than directly running the Black Duck Signature Scanner on the initial container file system, Detect runs the Black Duck Signature Scanner on a new image; in other words, the squashed image, constructed using the initial container file system built by Docker Inspector. Packaging the initial container file system in a Docker image triggers matching algorithms within Black Duck SCA that optimize match results for Linux file systems.

By default, Detect also runs Black Duck Binary Analysis on the initial container file system.
If your Black Duck SCA server does not have Black Duck Binary Analysis enabled, you
should disable Black Duck Binary Analysis. For example, you might set: `--detect.tools.excluded=BINARY_SCAN`.
