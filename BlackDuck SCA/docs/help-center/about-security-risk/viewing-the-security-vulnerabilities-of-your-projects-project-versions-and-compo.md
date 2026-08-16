---
title: "Viewing the security vulnerabilities of your projects, project versions, and component versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-the-security-vulnerabilities-of-your-projects-project-versions-and-component-versions.html"
content_id: "NkjDha8uA8RGSVGXoBe~CA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:19.572373+00:00"
---

# Viewing the security vulnerabilities of your projects, project versions, and component versions

Use your dashboards to view the types and
severity of risk that are associated with the components that are in one or more
versions of your projects. Dashboards provide an overall view of risk across the
components in your projects and project versions. Use the project version
**Vulnerabilities** tab to view a list of vulnerabilities for each component
version origin.

Note that the security risk values shown use CVSS v3.x or CVSS
v4.x scores, depending on which security risk
calculation you selected; by default, CVSS v3 scores are shown.

## Related vulnerabilities

Note that BDSA-1234-6789 or CVE-1234-5678 is the ID for a single vulnerability from
BDSA or NVD: there is one vulnerability, but there are two databases and each has
its own set of IDs to distinguish the same vulnerability.

There can be instances when the Black Duck UI shows vulnerabilities as related and in
other instances (for example a different component version origin) when the same
vulnerabilities are not shown as related. This may occur as sometimes NVD or BDSA
does not evaluate certain origins, components, or component versions.

For example, suppose vulnerability X is found; NVD identifies it as CVE1 and BDSA identifies
it as BDSA1. NVD has also found vulnerability X in component version origin A and
component version origin B but BDSA has only found it in component version origin B
(BDSA has either decided NVD is incorrect or not evaluated it). If your BOM has
component version origin A, the project version's **Vulnerabilities** tab
displays just the NVD identifier (CVE1) for that component version origin. BDSA does
not apply in this context because it is not linked to this component version origin.
If your BOM has component version origin B, both NVD and BDSA have found that
Vulnerability X applies. You will see either BDSA 1 (CVE 1) or CVE 1 (BDSA 1)
depending on your security priority system settings.

If NVD does not find the exploit at all then Black Duck only lists the BDSA ID,
whether it be for specific component version origins or just generally looking up
the BDSA identifier in the Black Duck application.
