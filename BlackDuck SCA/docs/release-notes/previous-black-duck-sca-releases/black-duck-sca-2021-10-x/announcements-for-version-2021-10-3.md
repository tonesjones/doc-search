---
title: "Announcements for Version 2021.10.3"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2021.10.3.html"
content_id: "2EbRPRIOx0UdFjhFWBpRGQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:48.230553+00:00"
---

# Announcements for Version 2021.10.3

## Security Advisory for Apache Log4J2 (CVE-2021-45046 and CVE-2021-45105)

The Apache Organization released a new version (2.17.0) of the Log4j2 component,
which addresses an additional vulnerability not fixed in versions 2.15.0 and
2.16.0.

[CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046) allows attackers with control over
Thread Context Map (MDC) input data when the logging configuration uses a
non-default Pattern Layout with either a Context Lookup or a Thread Context Map
pattern to craft malicious input data using a JNDI Lookup pattern resulting in a
denial of service (DOS) attack.

[CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105) allows attackers with control over
Thread Context Map (MDC) input data to craft malicious input data that contains
a recursive lookup, resulting in a StackOverflowError that will terminate the
process resulting in a denial of service (DOS) attack.

For more information, see [Apache's Log4j Security Vulnerabilities page](https://logging.apache.org/log4j/2.x/security.html).

As stated with the Black Duck 2021.10.2 version, we believe that there is limited
exposure to Black Duck’ products, services and systems. To the extent we have had
exposure, we have remediated or are in the process of remediating the situation.
Please continue monitoring our [community page](https://community.blackduck.com/s/article/Critical-Severity-Vulnerability-Notice-CVE-2021-44228) for further updates.
