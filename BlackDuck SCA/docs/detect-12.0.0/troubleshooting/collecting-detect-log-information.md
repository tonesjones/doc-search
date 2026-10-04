---
title: "Collecting Detect log information"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/collecting-detect-log-information.html"
content_id: "4eXDN7~NcehC67tunWUNng"
version: "12.0.0"
section: "Troubleshooting"
scraped_at: "2026-10-04T23:33:23.039540+00:00"
content_hash: "e36df0d074f6b1ab07336a9b2129a79630b7915a0fd1ceeb7b6e9791af9d0dbb"
---

# Collecting Detect log information

## Simple issues

- Run Detect with `--logging.level.detect=DEBUG` (the default logging level, INFO, is insufficient for troubleshooting) and read through the entire log for clues.
- For additional detail, run with `--logging.level.detect=TRACE`.
- Detect typically runs package manager commands or build tool commands similar to commands used in your build.
  When run by Detect, those commands (as well as the environment
  in which they run) need to be consistent with your build, and it's important to verify that they are.
  For example, the Gradle detector defaults to running *./gradlew dependencies* if it finds the file ./gradlew.
  If your build runs a different Gradle command or wrapper such as /usr/local/bin/gradle, use property
  *detect.gradle.path* to tell Detect to run the same Gradle command that your build runs.
  Check the DEBUG log for the package manager commands that Detect is running, and compare
  them to the commands your build runs.

## More complex issues

For more complex issues, including any issue that requires help from Black Duck Support, refer to Diagnostic mode.
