---
title: "Manage copyright format"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/manage-copyright-format.html"
content_id: "GYjS9vDHTuHNcRb6Pz8Hpw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:28.167644+00:00"
content_hash: "f98c033975ef9865e36d59866fff8fb0ebd15e6aa26fb867da30515af54e04fc"
---

# Manage copyright format

Organization Admins now have the ability to select how the copyright information is displayed in dashboards, reports, etc. By default, Polaris normalizes copyright entries to follow a standard format. This includes:

- Merging identical copyrights with different date ranges. If a component has multiple copyright entries for different years, they will be combined into one entry displaying the range of years. For example, if there were three copyrights:
  - Copyright 2021 Component Corporation
  - Copyright 2022 Component Corporation
  - Copyright 2023 Component Corporation

  The copyright would be displayed as "Copyright 2021-2023 Component Corporation."
- Removing copyrights without dates.
- Truncating long copyrights to the first 200 characters.

To enable or disable normalized copyright entries, follow these steps:

1. Go to My Organization > Licenses.
2. Select Edit (near Copyright Information).
3. Enable or disable the Normalize copyright entries to follow a standardized format setting, as required.
4. Select Save.

## Get copyright information

View open source and third-party copyright information:

- **Dashboards** > **Table - License Search** > License Information > Description.
- **Reporting** - Both SBOM and Notices File Reports (if included).
- **Portfolio** > select an application > select a project > **Components** tab > select a component > **Copyrights** tab in bottom pane. View copyright text for selected component.
