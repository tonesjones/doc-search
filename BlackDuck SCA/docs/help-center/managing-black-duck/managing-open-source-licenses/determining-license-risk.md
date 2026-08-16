---
title: "Determining license risk"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/determining-license-risk.html"
content_id: "2T32GO2TQB0tGQZPDjzRBQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:35.444397+00:00"
---

# Determining license risk

License Risk is determined by the license risk of the components and subprojects in the project
version's BOM.

There are four levels of overall license risk (high, medium, low, and none), based on the license family declared by the
component, the type of distribution for the project (external, internal, SaaS, or open
source) and the usage (statically linked, dynamically linked, source code, dev.
tool/excluded, implementation of standard, merely aggregated, prerequisite, separate
work, and unspecified).

Note: Other licenses include "Unknown" which indicates that the OSS component version's license is
not known; "License Not Found" which indicates that although researched by Black Duck, no
declared license was found for the component; and "No License" which indicates that
Black Duck found a declaration of 'No License' for the component.

These licenses are
included in the Unknown license family in the tables below.

For components with multiple licenses:

- "AND" licenses: license risk is determined by the license with the highest
  risk.
- "OR" licenses: license risk is determined by the license with the lowest
  risk.

Risk calculations assume that your project is being distributed under a proprietary
license.

## Subproject license risk

If your project contains subprojects, the license risk is determined the subproject's license
risk. A subproject's license is determined when it is added to the
project.

Notice: Black Duck 2023.10.0 introduces Enhanced license risk aggregation as a
Limited Customer Availability Feature which improves the way subproject risk is
determined. When enabled, the License Risk displayed for a subproject in your
project's BOM will be determined by the subproject's license risk and the highest
license risk of its components which reduces the possibility that license risk could
be missed when using subproject hierarchies.

Important: When modifying a subproject's distribution type after it has been added to a project, the license risk
of the parent project may not necessarily change to reflect the modification. The
parent project's distribution takes precedence when calculating license risk.

## Estimated licenses

A default license may be assigned to components with an unknown version found during
a scan. This is an estimated license based on greatest number of times it shows up
across the top 1,000 versions of the component.

When viewing the BOM for a project, components with unknown versions will have a
question mark next to the component name.

  
 [image: image]   

Clicking the license in the License column will open the Modify License
window which will display the following warning banner:

  
 [image: image]   

It is recommended that you review these components and manually specify a version for
more accurate results.

## Default license risk

The following tables show the license risk for the default (KnowledgeBase) license
families. Users with the License Manager role
can create
custom license families and define the license risk by usage and
distribution for those custom license families.

Note: If your License Manager created a custom license family labeled "Restrictive Third Party
Proprietary" or "Internal Proprietary" before the 2019.10.0 release, the number
"(1)" is appended to those custom license family names.

## License risk - by usage

### Statically linked

The following table lists the license risk when the component's usage is
**Statically Linked**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | High | High | None | None |
| Reciprocal | High | Low | None | None |
| Weak Reciprocal | High | Low | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | High | High | High | High |

### Dynamically linked

The following table lists the license risk when the component's usage is
**Dynamically Linked**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | High | High | None | None |
| Reciprocal | High | Low | None | None |
| Weak Reciprocal | Medium | Low | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | High | High | High | High |

### Source code

The following table lists the license risk when the component's usage is
**Source Code**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | High | High | None | None |
| Reciprocal | High | Low | None | None |
| Weak Reciprocal | High | Low | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | High | High | High | High |

### Dev. tool / excluded

The following table lists the license risk when the component is not distributed
with your product. (Usage value is **Dev. Tool / Excluded**).

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | None | None | None | None |
| Reciprocal | None | None | None | None |
| Weak Reciprocal | None | None | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Low | Low | Low | Low |
| Internal Proprietary | None | None | None | None |
| Unknown | None | None | None | None |

### Implementation of Standard

The following table lists the license risk when the component usage is
**Implementation of Standard**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | None | None | None | None |
| Reciprocal | None | None | None | None |
| Weak Reciprocal | None | None | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Low | Low | Low | Low |
| Internal Proprietary | None | None | None | None |
| Unknown | None | None | None | None |

### Separate Work

The following table lists the license risk when the component usage is
**Separate Work**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | None | None | None | None |
| Reciprocal | None | None | None | None |
| Weak Reciprocal | None | None | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | None | None | None | None |

### Merely aggregated

The following table lists the license risk when the component's usage is
**Merely aggregated**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | None | None | None | None |
| Reciprocal | None | None | None | None |
| Weak Reciprocal | None | None | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | Medium | Medium | Low | Low |

### Prerequisite

The following table lists the license risk when the component's usage is
**Prerequisite**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | Medium | None | None | None |
| Reciprocal | Medium | None | None | None |
| Weak Reciprocal | Low | None | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | Medium | Medium | Low | Low |

### Unspecified

The following table lists the license risk when the component's usage is
**Unspecified**.

| License Family | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Affero General Public License (AGPL) | High | High | None | None |
| Reciprocal | High | Low | None | None |
| Weak Reciprocal | High | Low | None | None |
| Permissive | None | None | None | None |
| Restrictive Third Party Proprietary | Medium | Medium | Medium | High |
| Internal Proprietary | None | None | None | Medium |
| Unknown | High | High | High | High |

## License risk by license family

### Affero General Public License (AGPL)

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | High | High | None | None |
| Statically Linked | High | High | None | None |
| Dynamically Linked | High | High | None | None |
| Separate Work | None | None | None | None |
| Merely Aggregated | None | None | None | None |
| Implementation of Standard | None | None | None | None |
| Prerequisite | Medium | None | None | None |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | High | High | None | None |

### Reciprocal

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | High | Low | None | None |
| Statically Linked | High | Low | None | None |
| Dynamically Linked | High | Low | None | None |
| Separate Work | None | None | None | None |
| Merely Aggregated | None | None | None | None |
| Implementation of Standard | None | None | None | None |
| Prerequisite | Medium | None | None | None |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | High | Low | None | None |

### Weak Reciprocal

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | High | Low | None | None |
| Statically Linked | High | Low | None | None |
| Dynamically Linked | Medium | Low | None | None |
| Separate Work | None | None | None | None |
| Merely Aggregated | None | None | None | None |
| Implementation of Standard | None | None | None | None |
| Prerequisite | Low | None | None | None |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | High | Low | None | None |

### Permissive

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | None | None | None | None |
| Statically Linked | None | None | None | None |
| Dynamically Linked | None | None | None | None |
| Separate Work | None | None | None | None |
| Merely Aggregated | None | None | None | None |
| Implementation of Standard | None | None | None | None |
| Prerequisite | None | None | None | None |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | None | None | None | None |

### Restrictive Third Party Proprietary

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | Medium | Medium | Medium | High |
| Statically Linked | Medium | Medium | Medium | High |
| Dynamically Linked | Medium | Medium | Medium | High |
| Separate Work | Medium | Medium | Medium | High |
| Merely Aggregated | Medium | Medium | Medium | High |
| Implementation of Standard | Low | Low | Low | Low |
| Prerequisite | Medium | Medium | Medium | High |
| Dev. Tool/Excluded | Low | Low | Low | Low |
| Unspecified | Medium | Medium | Medium | High |

### Internal Proprietary

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | None | None | None | Medium |
| Statically Linked | None | None | None | Medium |
| Dynamically Linked | None | None | None | Medium |
| Separate Work | None | None | None | Medium |
| Merely Aggregated | None | None | None | Medium |
| Implementation of Standard | None | None | None | None |
| Prerequisite | None | None | None | Medium |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | None | None | None | Medium |

### Unknown

| Usage | External Projects | SaaS Projects | Internal Projects | Open Source Projects |
| --- | --- | --- | --- | --- |
| Source Code | High | High | High | High |
| Statically Linked | High | High | High | High |
| Dynamically Linked | High | High | High | High |
| Separate Work | None | None | None | None |
| Merely Aggregated | Medium | Medium | Low | Low |
| Implementation of Standard | None | None | None | None |
| Prerequisite | Medium | Medium | Low | Low |
| Dev. Tool/Excluded | None | None | None | None |
| Unspecified | High | High | High | High |
