---
title: "Enabling collection of scan transparency data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-collection-of-scan-transparency-data.html"
content_id: "5mzpzsjw_tk8Tbk09w6iBA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:12.893795+00:00"
---

# Enabling collection of scan transparency data

To enable the storing of scan transparency data in the Coverity Connect database during a
commit, edit your `cim.properties` file to include the following property
setting:

```
scan.transparency.enabled=true
```

You can find `cim.properties` in the
`<coverityConnectInstallDir>/config/` directory.

You must restart the Coverity Connect server for this change to take effect.

Note: The Coverity Analysis `cov-build` and `cov-analyze`
commands generate scan transparency data by default. However, they can be configured
through options to not generate this data. See the commands descriptions in the Coverity 2026.6.0 Command Reference
for details.

After setting this property and restarting the server, the Coverity Connect GUI displays
values in these fields:

- **Source Files Captured**

  This field is displayed on a snapshot's **Build
  Details** panel.
- **Functions Analyzed (with Models)**

  **Number of Annotations**

  **Number of Custom Models**

  These fields are displayed on a snapshot's **Analysis Details** panel.
- **Scan Transparency Data**

  This field provides a link to a ZIP file of JSON-formatted scan transparency data
  associated with the stream's most recent snapshot.

  To locate this field, click **Configuration** > **Projects & Streams**.

  Open the project and select the stream.

  Select the snapshot and click the **Details** button.
