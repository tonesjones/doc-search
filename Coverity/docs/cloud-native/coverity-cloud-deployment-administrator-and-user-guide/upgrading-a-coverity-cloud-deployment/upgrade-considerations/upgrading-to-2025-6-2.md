---
title: "Upgrading to 2025.6.2"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.6.2.html"
content_id: "ZgrJy3hY59u~OUsmGSIL8A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:32.689049+00:00"
---

# Upgrading to 2025.6.2

In additions to the features and changes released with 2025.6.0, the 2025.6.2 release
introduces the following changes:

- Version 2025.6.2 of Black Duck container image files and analysis client files is
  supported.

  - For container image file support, see Coverity container images.
  - For analysis client version support, see Supported Coverity Tools (Thin Client) and full analysis client versions and Coverity client installer and documentation files.
- Documentation: Microsoft recently changed Azure Active Directory to Microsoft
  Entra ID. This document version updates the following sections to reflect the
  recent Microsoft product name change. See Configure Storage Service access to the storage blob and storage-service.azure Helm keys.
- Documentation: Created a new chapter, Managing container images,
  that describes two methods of obtaining and deploying container images. We
  recommend that you create your own private registry for Black Duck Coverity
  container images, and describe how to create and use the registry. Although not
  recommended for deployment performance reasons, this document now describes how
  to deploy container images directly from the Black Duck private registry. For
  information, see Managing container images.
- Documentation: Fixed typographical errors where the
  `scan-services` chart and `scan-service` key
  contained a '.' instead of a '-'. Fixed instances in  and in a note in scan-services Helm subchart: Helm keys. The note is especially important since it
  could cause a `scan-services` deployment issue if used with the
  typo.
- Documentation: Reviewed Helm chart and code examples for YAML indentation and
  syntax issues and fixed as needed. Used the YAML 2-space indent standard.
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck
  internal use only.
