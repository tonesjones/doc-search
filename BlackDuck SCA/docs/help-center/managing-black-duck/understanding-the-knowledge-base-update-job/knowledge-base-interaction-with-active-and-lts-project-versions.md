---
title: "Knowledge Base Interaction with Active and LTS Project Versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/knowledge-base-interaction-with-active-and-lts-project-versions.html"
content_id: "KaeGqexq2eesBbNAQa4viQ"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:15.581798+00:00"
content_hash: "4ae19f7481eeaf288ec5a72581fb22cc3c087c509ebdde110d30b5f84f105ae7"
---

# Knowledge Base Interaction with Active and LTS Project Versions

Black Duck offers two project version types, each optimized for different stages of your software lifecycle.

## Understanding the KB Update Job Interaction

The Knowledge Base (KB) update job plays a critical role in the functioning of both Active and LTS project versions. In Active projects, the KB update job automatically propagates newly published vulnerabilities, ensuring that your project reflects the most current security landscape. For LTS projects, the centralized architecture allows for efficient updates across multiple versions, enhancing the reliability of vulnerability propagation. Understanding how the KB update job interacts with these project types is essential for maintaining effective vulnerability management and ensuring that your software remains secure.

## Active Project Versions

Active project versions are designed for software under active development and provide the fullest set of capabilities, including:

- **Automatic Vulnerability Propagation:** Newly published vulnerabilities from the Knowledge Base are automatically propagated to ensure your project is up to date.
- **Notifications and Alert Integrations:** Receive timely notifications about vulnerability changes and alerts related to your project.
- **Audit Log Entries:** All changes to vulnerabilities are recorded in the audit log for transparency and tracking.
- **Full Remediation Workflow Support:** Comprehensive support for managing and resolving vulnerabilities.

For best results, we recommend keeping project structures straightforward and re-scanning periodically to ensure your BOM reflects the latest state of your codebase.

## LTS (Long-Term Support) Project Versions

LTS project versions are purpose-built for **released software artifacts** where ongoing monitoring is needed, but re-scanning is not expected. Key features include:

- **Automatic Vulnerability Propagation:** Vulnerabilities are propagated using an enhanced, more resilient architecture, ensuring reliability.
- **Efficient Scalability:** Designed to scale efficiently to accommodate large numbers of project versions.
- **Full Remediation Workflow Support:** Complete support for managing vulnerabilities within LTS versions.
- **Notification and Alert Support:** Coming soon; this is our top priority for expanding LTS capabilities.

LTS versions utilize a **centralized component catalog**, meaning component data is stored once and shared across all projects that reference it. This architecture enables faster and more reliable KB updates at scale.

## Which Should I Use?

| Scenario | Recommended Type |
| --- | --- |
| Software under active development with CI/CD integration | **Active** |
| Released products requiring ongoing vulnerability monitoring | **LTS** |
| Large-scale environments with many monitored versions | **LTS** |

## Best Practices

- **Use Active project versions** for development branches where you need real-time notifications and alert integrations.
- **Use LTS project versions** for released software that requires long-term vulnerability monitoring without re-scanning.
- **Keep project structures simple** — avoid deeply nested sub-project hierarchies for the most reliable update processing.
