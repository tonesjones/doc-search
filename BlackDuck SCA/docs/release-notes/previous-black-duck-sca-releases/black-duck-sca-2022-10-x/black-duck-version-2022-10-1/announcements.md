---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "DRAT24bt8SHb8Un6hq_l6A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:20.674399+00:00"
---

# Announcements

## Security Advisory for OpenSSL versions 3.0.0 to 3.0.6

On November 1, 2022, the OpenSSL Project disclosed the following high severity
vulnerabilities present in OpenSSL 3.0.x.

The nature of both vulnerabilities allows a buffer overrun which can be triggered in
X.509 certificate verification, specifically in name constraint checking. Note that
this occurs after certificate chain signature verification and requires either a CA
to have signed the malicious certificate or for the application to continue
certificate verification despite failure to construct a path to a trusted issuer.

[CVE-2022-3602](https://nvd.nist.gov/vuln/detail/CVE-2022-3602): An attacker can craft a malicious email
address to overflow four attacker-controlled bytes on the stack. This buffer
overflow could result in a crash (causing a denial of service) or potentially remote
code execution.

[CVE-2022-3786](https://nvd.nist.gov/vuln/detail/CVE-2022-3786): An attacker can craft a malicious email
address in a certificate to overflow an arbitrary number of bytes containing the `.'
character (decimal 46) on the stack. This buffer overflow could result in a crash
(causing a denial of service).

Currently, Black Duck believes there is limited exposure to Black Duck SIG products,
services, and systems. To the extent we have had exposure, we have applied
mitigations that prevent attempted exploitation.

The binary scanner (BDBA) has been updated to version 2022.9.2 which includes an
upgrade to OpenSSL 3.0.7 in response to the high severity vulnerabilities. Customers
running 2022.10.0 without BDBA do not need to upgrade.

Please continue monitoring our [Community page](https://community.blackduck.com/s/article/SIG-Security-Advisory-for-OpenSSL-Vulnerability-CVE-2022-3786-BDSA-2022-3107-CVE-2022-3602-BDSA-2022-3108) for further updates.
