---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "XRlJeA9Rm1oQaPFhLogEdw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:26.618906+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-44558). Resolved a bug that resulted in a 412 error when attempting to add a
  different version of a project to the Bill of Materials (BOM) of another version
  of the same project. This issue blocked valid use cases, particularly for
  customers who utilize multiple versions of the same project in their BOMs, such
  as in microservices architectures. The problem originated from a fix designed to
  prevent projects without versions from being added to BOMs; however, it
  unintentionally restricted the addition of different versions of the same
  project. The team has decided to remove this restrictive check, allowing for the
  addition of different project versions without causing unnecessary upgrade
  friction. Cyclic dependency detection will continue to be enforced to prevent
  recursive references, ensuring a balance between functionality and safety.
- (HUB-46221, HUB-46224). Custom field options created prior to version 2025.7.0
  were not properly migrated to match the format required by the 2025.7.0
  codebase. A new migration script has been implemented to automatically upgrade
  these entries to the correct format. This ensures that all custom field options
  display and function correctly after upgrading to version 2025.7.0.

  If you
  have made changes to the custom field values that were not functioning correctly
  after the 2025.7.0 upgrade, please reach out to Support before applying the 2025.7.1
  upgrade. It is necessary to clean up the values in the database prior to the upgrade
  to prevent any potential failures during the process. Your prompt attention to this
  matter will help ensure a smooth upgrade experience.
