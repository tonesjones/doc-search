---
title: "Getting remediation guidance for components with security vulnerabilities"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/getting-remediation-guidance-for-components-with-security-vulnerabilities.html"
content_id: "p8pxNsEU42Qd85wGWQB1ew"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:28.729224+00:00"
---

# Getting remediation guidance for components with security vulnerabilities

When Black Duck identifies a component version with known security
vulnerabilties, it attempts to find safer alternative versions of that component. These
are presented as a **Upgrade Recommendation** within the component
slide-out panel on the project version's BOM.

After reviewing this information, you may want to explore whether alternative component
versions are available—particularly ones that resolves the security vulnerability
affecting the version used in your BOM.

## Upgrade recommendations

The simplest way to minimize or resolve security risk is to upgrade the version of
the used component with fewer vulnerabilities.

[image: Upgrade recommendation]

If your project version contains any component versions which have known
vulnerabilities or are simply out of date, the Upgrade Recommendation section will
display options you can explore to mitigate risk:

- **Short-Term** recommendations provides a short-term upgrade path as it is
  typically the same major version as the version currently used in your
  BOM.
- Unlike the short term upgrade recommendation, **Long-Term**
  recommendations usually requires a major version upgrade. This may require
  more planning and/or engineering work to implement.

If the component is a transitive dependency, you will see two additional options, **Direct
Dependency** and **Component Version**:

  
 [image: Upgrade recommendation for transitive dependency]   

- **Direct Dependency**: Provides a short- and long-term upgrade recommendation for the
  root node of a transitive dependency.
- **Component Version**: Short-term typically reflects upgrading a component's minor or
  patch version. Long-term will focus on upgrading a component's major
  version.
