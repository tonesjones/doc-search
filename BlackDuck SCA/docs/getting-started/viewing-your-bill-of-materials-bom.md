---
title: "Viewing your Bill of Materials (BOM)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-your-bill-of-materials-bom-.html"
content_id: "4YSuFYgOW~AUASIY6NYYwg"
version: "2026.7"
section: "Getting Started with Black Duck"
scraped_at: "2026-08-08T15:32:36.946809+00:00"
---

# Viewing your Bill of Materials (BOM)

Once you have scanned your codebase and mapped the results to a project version, Black Duck automatically generates a Bill of Materials (BOM). The
BOM lists all the open source components detected in that project version, along with
associated data like licenses, vulnerabilities, and policy status.

The BOM is your central view for understanding what's in your software and whether any
risks or compliance issues need to be addressed.

## How to view a BOM

1. Log in to Black Duck SCA.
2. On the **Dashboard**, select the project using either the **Watching** or My Projects
   tab.
3. On the **Project** page, choose the version you want to view. This will take you to the
   **Components** tab, which displays the BOM.  
    [image: BOM page]

## Understanding the BOM view

- The BOM shows all open source components found in the selected project version.
- By default, it dispalys a flat view, meaning all components appear in a single list,
  regardless of how they were introduced into the codebase.
- Each component entry includes important details such as the component's name and version,
  match type, license(s), and security and operational risks. Click here for more
  information on these component characteristics.

You can sort, filter, and search within the BOM to focus on components that are high-risk or
policy-violating.

## What you can do from the BOM

- Click a component to open a slide-out panel with more detailed information, including:

  - Vulnerabilities
  - Licenses
  - Origin IDs (e.g., PURL, CPE)
  - Other details, such as description and approval status
- Apply policy overrides or
  remediation actions
  directly from the BOM if you have the appropriate permissions.
- Generate an
  SBOM report using supported formats such as SPDX or CycloneDX.

## Deeper dive

- To explore what you can do with the BOM, see Project Version BOMs in the Black Duck
  documentation.
- For help interpreting vulnerabilities, see Managing Security Risk.
- To learn about setting policies, see Managing
  Policies.
