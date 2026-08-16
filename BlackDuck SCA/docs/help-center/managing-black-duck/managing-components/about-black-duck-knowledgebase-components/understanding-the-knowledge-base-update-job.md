---
title: "Understanding the Knowledge Base Update Job"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-the-knowledge-base-update-job.html"
content_id: "mcyVoJSBKdwgsiFGyxznQA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:20.224179+00:00"
---

# Understanding the Knowledge Base Update Job

An overview of the Knowledge Base update job in Black Duck SCA,
explaining how vulnerability data is propagated, notifications are generated, and the
limitations users should be aware of.

The Knowledge Base (KB) update job plays a crucial role in maintaining the accuracy and
currency of vulnerability information within the system. Its primary functions include
propagating newly published vulnerabilities, such as CVEs (Common Vulnerabilities and
Exposures) and BDSAs (Black Duck Security Advisories), to
Active project versions without requiring a rescan, provided that the Bill of Materials
(BOM) remains unchanged.

**Key Functions of the KB Update Job:**

- **Propagation of Vulnerabilities:** Newly added or deleted
  vulnerabilities are automatically reflected in the project BOMs.
- **Notifications and Audit Logs:** Notifications are generated
  for newly added or deleted vulnerabilities, ensuring users are informed of
  important changes. Audit log entries are created to maintain a record of these
  updates.
- **Interaction with
  Active and LTS Projects:** The Knowledge Base (KB) update job
  plays a critical role in the functioning of both Active and LTS project
  versions.

**Limitations:**

- The KB update job does not generate notifications for score-only updates or
  severity changes; these updates are applied silently.
- In cases where vulnerabilities transition between identifiers (e.g., from BDSA to
  CVE), they are treated as new entries, which can reset remediation statuses and
  comments.
- The propagation of vulnerabilities may not be immediately observable if the KB
  update job has not yet processed a specific project version, or if the job fails
  or becomes stuck.

Understanding the behavior of the KB update job is critical for effectively managing
vulnerabilities and ensuring that your projects are always up-to-date with the latest
security information.

## What's Coming Next

We are continuously improving the KB update experience. Key areas of investment
include:

- **LTS notification support** — enabling notifications and alert integrations
  for LTS project versions.
- **Improved remediation continuity** — preserving remediation status across
  vulnerability identifier transitions.
- **Next-generation notification system** — a more flexible and reliable
  notification framework that will support additional change types.

For the latest on these and other improvements, visit the [Black Duck
Ideas Portal](https://bdsi-sca.ideas.aha.io/) or speak with your Black Duck account team.
