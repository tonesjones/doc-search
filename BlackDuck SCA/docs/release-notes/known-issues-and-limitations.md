---
title: "Known Issues and Limitations"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/known-issues-and-limitations.html"
content_id: "amc8YKd7sXs0AyCS7uM~xw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:27.993581+00:00"
---

# Known Issues and Limitations

The following is a list of known issues and limitations in Black Duck:

## New Known Issues and Limitations

- With the recent updates, Bitbucket Data Center (BBDC) now aligns with the
  workflow of other SCM providers, such as GitHub and GitLab, in terms of
  creating SCM projects. However, our QA team has identified a bug that users
  should be aware of:

  **Issue:** A limitation exists when two repositories with the same name
  are displayed on the same page in the UI. If one of these repositories is
  selected, both will be selected, resulting in both being scanned.

  **Next Steps:** This is a known bug, and we are actively working on a
  solution that will be included in the next release.

  **Workaround:** To avoid this issue, users can search for the exact
  project or repository they wish to scan and conduct the scan
  individually.

## Current Known Issues and Limitations

- Simultaneously creating or updating serveral age-based policies may cause the BOM Engine
  container to run out of memory and restart, depending on system resources.
  If this occurs, contact Customer Support for assistance.
- Due to updates to the security ranking algorithm, searching for
  vulnerabilities on the Find → Vulnerabilities page may display results
  different from previous versions.
- When transitioning active project versions to LTS, additional vulnerabilities might the
  discovered in the LTS project if the active project included components
  identified through snippet scanning. In future updates, components matched
  via snippet scanning will no longer be carried over to LTS projects.
- Users of the Bitbucket Cloud SCM provider must use the same workspace name and workspace ID
  in Bitbucket in order to clone repositories from that workspace.
- When searching for CISA Known Exploited Vulnerabilities on the Find page, you must also
  check the Affecting Projects checkbox to get results. Checking only the CISA
  Known Exploited Vulnerability checkbox will not yield any search
  results.
- The Scan Heatmap found under Admin > Diagnostics > Heatmaps displays results
  in UTC time instead of local time. Please be aware of this when using this
  new feature.
- Components marked for deletion based on Match Score threshold setting are not being removed
  when re-uploading BDIO through UI.
- The **Purge ONLY Archived Project Version Unmatched Scan File Data** and **Purge All
  Unmatched File Data** links do not work at both the project
  (*project* > Settings tab) and global (Admin > System Settings >
  Data Retention) levels.
- The Component Management > Component Versions tab > Add (KB) Component modal > Save does not display newly added component versions until the
  page is refreshed.
- Customers currently using Blackduck 2021.8.0 or later might experience
  timeout issues when Detect is invoked with the following parameters in a
  request:

  - ```
    --detect.wait.for.results=true
    ```
  - `--min-scan-interval=` (a non-zero, positive
    value)

  This issue will be resolved in an upcoming Detect and Blackduck release.

  [Hub-22657When scanning
  with Signature Scanner CLI, Black Duck Detect Desktop, or Black Duck Detect, you may see error
  messages that starts with the following:

  ```
  ERROR StatusLogger Unrecognized
  ```

  You can ignore these messages. These errors do not impact the scans and will
  not cause the scan to fail.
- [Hub-20216The
  **Overview** tab for the *Component Name* page shows CVSS 2.0
  data, even if you selected to view CVSS 3.0 (NVD or BDSA) data.
- If you are using an LDAP directory server to authenticate users, consider the following:
  - Black Duck supports a single LDAP server.
    Multiple servers are not supported.
  - If a user is removed from the directory server, Black Duck user account continues to appear as
    active. However, the credentials are no longer valid and cannot be
    used to log in.
  - If a group is removed from the directory server, Black Duck group is not removed. Delete the group
    manually.
- Tagging only supports letters, numbers, and the plus (+) and underscore (_)
  characters.
- If Black Duck is authenticating users, user names are not
  case sensitive during login. If LDAP user authentication is enabled, user
  names are case sensitive.
- If a code location has a large bill of materials, deleting a code location
  may fail with a user interface timeout error.
