---
title: "About Custom Components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-custom-components.html"
content_id: "PqcDcvyPRvvB7yZK4Tbi0Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:12.435731+00:00"
---

# About Custom Components

Custom components enable you to represent software components in your BOM that are
not available from the KnowledgeBase, such as proprietary, commercial, internal, or
otherwise untracked components. Users with the Component Manager role can create and
manage custom components and add them to project BOMs.

Users with the **Component Manager** role can create and manage custom components and
their versions, and then add them to project BOMs.This helps ensure that your BOM
accurately reflects all software used by your project.

Custom components can contain information such as version details, licensing information,
and descriptive metadata. Depending on how a custom component version is configured, it
can also be associated with known security vulnerabilities. Custom component
vulnerabilities are included in BOM risk calculations, policy evaluation, notifications,
and reports when vulnerability data is available for that component version.

If you require a version of an open source component that is not available in the
KnowledgeBase, contact Customer Support.

## Managing custom components

Component Managers can use the following pages to manage custom components and custom
component versions.

| Page | Description |
| --- | --- |
| **Custom Component Overview** | View information about a custom component, including approval status, description, tags, custom fields, and component versions. Create additional versions for the component. |
| **Custom Component Settings** | View and update component details, manage custom fields and SBOM metadata, and delete a custom component. |
| **Custom Component Version Overview** | View information about a custom component version, including project usage, vulnerability counts, licensing information, approval status, and additional metadata. |
| **Custom Component Version Vulnerabilities** | View vulnerabilities associated with a custom component version. Vulnerabilities are determined by the CPE assigned to the component version. |
| **Custom Component Version Origin IDs** | View and manage origin identifiers associated with a custom component version. Origin IDs can be used to automatically match scan results to the component version. |
| **Custom Component Version Settings** | View and update component version details, manage licenses, custom fields, SBOM metadata, origin identifiers, and CPE values, and delete a custom component version. |

Note: Component Managers must have permission to view projects before they appear on the
Custom Component Version Overview page.

## Understanding risk for custom components

Black Duck SCA evaluates custom components differently from KnowledgeBase
components.

**License risk**

Custom components display license risk based on the license assigned to the component version.

**Security risk**

Custom component versions can display security risk when vulnerabilities are
associated with the version. Associated vulnerabilities can be viewed from the
custom component version's Vulnerabilities page.

**Operational risk**

Operational risk is not calculated for custom components.

## Custom components in the BOM

When a custom component is added to a BOM:

- The match type is **Manually Added**.
- Policy Managers can create policy rules that apply to custom components.
- You can search for custom components by using the **Component Source** filter
  and selecting **Custom Component**.
- Project Version reports identify custom components separately from
  KnowledgeBase-managed components.
- Custom components do not have origins.

Project Version reports include a **Source/Type** field that identifies whether a
component is a custom component or a KnowledgeBase-managed component.

## Related tasks

- Create a custom component or custom component
  versions
- Managing custom components
- Manage custom component
  versions
