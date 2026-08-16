---
title: "About security risk"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-security-risk.html"
content_id: "dYsokFeNvudnq6CJJz2zdg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:18.963890+00:00"
---

# About security risk

Black Duck helps security and development teams identify security
risks across their applications.

By mapping vulnerabilities to your open source software, Black Duck
can provide you with high-level overview information on security risk of your projects,
along with detailed information on security vulnerabilities which you can use to
investigate and remediate your security vulnerabilities.

Vulnerabilities are linked to the open source components by the Common Vulnerabilities
and Exposures numbers (CVEs), as reported in the National Vulnerabilities Database (NVD)
maintained by the National Institutes of Standards and Technology (NIST) and/or by
(BDSA) numbers If you have licensed Black Duck Security Advisories.
Note that Black Duck displays the numbers together in reports and
in the UI because they represent the same vulnerability from different sources.

## Security risk levels

NVD and BDSA use the Common Vulnerability Scoring System (CVSS) which provides a
numerical score reflecting the severity of a vulnerability. The numerical score is
then translated into a risk level to help you assess and prioritize security
vulnerabilities.

Black Duck provides you with the option of viewing CVSS versions
2, 3.x, and 4.x scores. By default, Black Duck displays CVSS
v4.x scores.

CVSS scores have the following values:

- None: 0.0
- Low risk: 0.1 - 3.9
- Medium risk: 4.0 - 6.9
- High risk: 7.0 - 8.9
- Critical risk: 9.0 - 10.0

For more information on the Common Vulnerability Scoring System, see the CVSS [3.x](https://www.first.org/cvss/v3.1/specification-document) and [4.x](https://www.first.org/cvss/v4.0/specification-document) specification documents.

Note: CVSS v2 will no longer be supported as the highest-priority CVSS ranking. However,
it will still be displayed if no CVSS v3.x or CVSS v4.x score exists for a
vulnerability.

## Estimated Security Risk

This estimated risk statistic is used when a component in the BOM has an unknown
version. Such components are marked with a [image: Unknown version] icon next to the component name.

[image: BOM containing a component with an unknown version]

Estimated security risk is formulated by looking at all the versions of a component
sorted by security vulnerability severity category and calculating the maximum
vulnerability count for each severity category for each component version. The
maximum vulnerability count for each severity category of the component with no
version specified is shown in the components's **Security Risk** column.

Clicking the security risk icons for a component with an unknown version displays a
popup which provides more information on which component versions are known to fall
into each specified risk category.

[image: Estimated Security Risk popup]

The highest severity category counts may reference different component versions. For
example:

- Component version 1.1 has 2 Critical, 3 High, 15 Medium, 4 Low
- Component version 1.2 has 2 Critical, 4 High, 12 Medium, 1 Low

The estimated security risk by severity category for this component with unknown
versions would return as 2 Critical, 4 High, 15 Medium, 4 Low on the BOM.

Users should choose the exact version used in the application to view the accurate
risk instead of the estimated risk. This estimated risk information is provided to
help prioritize what components to review first. Users are encouraged to use
estimated risk information in conjunction with BD Policy Management to further
prioritize what components to triage first based on their company’s security
policies.

Note: The information presented is only a statistical data estimation. As a result, the
estimated security risks will not have CVE data.

## Suggested workflow

To manage security risk using Black Duck:

1. With the assistance of your security team, determine your security risk
   policies.
2. If necessary, users with the system administrator role can define the default security ranking.

   Note that the security ranking also defines how vulnerabilities appear in
   reports. Depending on the data available, the vulnerability will be
   presented as either: BDSA (NVD) or NVD (BDSA).
3. Create policies that
   trigger violations when components do not comply with your security
   policies.
4. Depending on your interests:

   - Use the Summary Dashboard to view
     the overall health of your projects and identify areas of concern.
     Use this page to quickly assess areas where you need to focus your
     attention.
   - Use these Dashboard pages for a high-level overview of risk:

     - Use the Watched or My Project
       dashboards to view the security risk across all
       your projects.
     - Create saved
       searches to customize the information shown on
       the Dashboard page to view the projects, components, and
       vulnerabilities that interest you.
   - Use these pages for project version-level information:

     - project version
       page/**Components** tab, also known as the
       project version BOM, to view the components specific to that
       project version, that have security risk.
     - project version page/**Vulnerabilities** tab
       to view the security vulnerabilities of each severity
       associated with the components used in a project
       version.
5. Investigate vulnerabilities and policy violations. For detailed information
   on security vulnerabilities, view the:

   - CVE page
   - BDSA page if you have
     licensed Black Duck Security Advisories
     (BDSA)
6. After reviewing the severity of the vulnerability, users with the appropriate
   role can
   change the remediation status of the security vulnerability.
7. Monitor notifications for any new security vulnerabilities.

   You will receive notification alerts if security vulnerabilities are
   published or updated against components that are included in one or more of
   your projects.
