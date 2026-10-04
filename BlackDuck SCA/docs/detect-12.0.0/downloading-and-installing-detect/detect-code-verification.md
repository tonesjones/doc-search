---
title: "Detect Code Verification"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-code-verification.html"
content_id: "Hov7oWB9PuIyKGencjI9fA"
version: "12.0.0"
section: "Downloading and Installing Detect"
scraped_at: "2026-10-04T23:33:18.625445+00:00"
content_hash: "124aaeb534fb99b7819c5f09d9dfa3177b3f3c4745a01bb8fbc08890ba029641"
---

# Detect Code Verification

Two methods are available to verify that the Detect code you run has not been tampered with since it was built:
code signature verification and checksum verification.
Both methods apply to the Detect .jar file, and only offer protection when you run
Detect by invoking the Detect .jar file directly (as opposed to invoking detect12.sh or detect12.ps1).

## Code signature verification

Code signature verification is the most secure method available for verifying Detect code. This method relies on Java tools.

It involves verifying the Detect .jar file that you download from the location specified in download locations,
using the Java *jarsigner* tool. In the event that the .jar has been tampered with, verification will fail.

To verify the Detect .jar:

jarsigner -verify -strict {your Detect .jar file}

The output should be `jar verified.`.

## Checksum verification

Checksum verification provides less protection against tampering than code signature verification provices because
in the unlikely scenario the Artifactory server has been compromised, an attacker could alter
both the .jar and the checksum. But checksum verification does provide some degree of protection
against other attack scenarios.

The binary repository provides SHA-256, SHA-1, and MD5 checksums for each Detect .jar
file. To find it, navigate to the .jar file in the Artifactory server specified in download locations,
and scroll to the bottom of the page. Various tools (such as md5sum, sha1sum, and sha256sum on Linux, and certutil and Get-FileHash on Windows) are available for
calculating checksums of files on your computer. Use one of those tools to get a checksum for your copy of the Detect .jar, and compare it
to the corresponding checksum on the binary repository page to make sure they match.
