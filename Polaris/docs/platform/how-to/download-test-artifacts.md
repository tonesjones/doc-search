---
title: "Download test artifacts"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/download-test-artifacts.html"
content_id: "axklN1DzHqS4bHdqtPsgyQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:18.846078+00:00"
content_hash: "a7418efb81b91a59971acaa7f13989a4fe728feb83c5093e296545aad841816d"
---

# Download test artifacts

How to download test artifacts and find a test's UID in the Polaris user interface.

## Artifact availability

Not all tests generate artifacts that can be downloaded from the Polaris user interface. Test artifacts are available for download in the following scenarios:

| Test types | Created when | Artifacts may include |
| --- | --- | --- |
| SAST tests (full or rapid) run via File Upload, SCM integrations, or CI using the file upload option (`polaris.test.sca.location` and `polaris.test.sast.location` are set to `remote`) | Tests fail | Execution logs, analysis output, and test results |
| SCA tests (Package Manager or Signature Analysis) run via File Upload, SCM integrations, or CI using the file upload option (`polaris.test.sca.location` and `polaris.test.sast.location` are set to `remote`) | Tests fail | error-details.json and a BDIO file |
| All DAST tests | Tests succeed or fail | Execution logs and screenshots. If automated BOLA scanning is enabled, an extra file containing related annotations is also included (`postprocessed_spec.json`) |

Note: You cannot download test artifacts from the Polaris user interface for:

- External analysis tests
- Tests run with Code Sight
- SAST and SCA tests run with Bridge using the default or local analysis options (`polaris.test.sca.location` and `polaris.test.sast.location` are set to `hybrid` (default) or `local`)

## Download test artifacts

To download test artifacts, follow these steps:

1. Go to Tests and select a Test ID.

   Note: Alternatively, you can go to Portfolio, select an application, select a project, open the Tests tab, and select a Test ID.
2. Open the Debugging tab.

   [image: test artifacts debugging]
3. Under Test Artifacts, select Download.

   Note: Test artifacts are not available for all tests, and are only available for 30 days.
