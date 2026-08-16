---
title: "Manage SAST tool versions"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/manage-sast-tool-versions.html"
content_id: "kM8rJBypJZnxyeM83MeVAQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:11.566599+00:00"
content_hash: "6c89ced8690b506071dd6e8e9ce068e58bc4dce8c0ee263136148a6055868b76"
---

# Manage SAST tool versions

Learn how to change the version of Coverity used for SAST tests on Polaris.

After Black Duck Support enables this feature for your organization, you can customize the version of Coverity (and Rapid Scan Static) used for static analysis. This allows you to change your organization's default Coverity version, or override the default version for specific applications, projects, or branches in your portfolio.

Important: Support for multiple SAST tool versions is generally available, but the feature is disabled and hidden by default. To enable this feature, create a support case in Black Duck Community. See [Enable SAST tool version customization](manage-sast-tool-versions/enable-sast-tool-version-customization.md) for more information.

Each version of Coverity (used for full SAST tests) is keyed to a corresponding version of Rapid Scan Static (Sigma). The latest supported version of Coverity is keyed to the latest supported version of Sigma.

When you choose to use a specific Coverity version (including the recommended version), the corresponding version of Rapid Scan Static (Sigma) is locked, and won't change when newer Sigma versions are available. Find available versions of Coverity and Sigma here: Supported tools.

## SAST tool version inheritance

The version of Coverity you enable at the organization-level serves as the default for all the applications, projects, and branches in your portfolio. However, the version assigned to an application, project, or branch takes precedence:

- The version of Coverity enabled for an application overrides the organization-level version.
- The version of Coverity enabled for a project overrides both application and organization-level versions.
- The version of Coverity enabled for a branch overrides project, application, and organization-level versions.

To check the active Coverity version for an application or project, open the Analysis tab.

- For an application, go to Portfolio > select an application > Settings > Analysis.
- For a project, go to Portfolio > select an application > select a project > Settings > Analysis.

When Inherited appears at the top of the SAST Analysis panel, the versions of Coverity and Sigma the application (example below) or project use are inherited.

[image: Screenshot of the SAST Analysis panel for an application.]

To check the active Coverity version for a branch, go to Portfolio > select an application > select a project > Branches. Then, select the options [image: icon polaris options] icon at the end of the branch's row and select Edit. When Inherited appears near SAST Analysis, the version of Coverity the branch uses is inherited.

## Coverity upgrades on Polaris

Polaris can support several versions of Coverity at a time.

### Deprecated versions of Coverity

Versions of Coverity will be flagged as deprecated 90 days before they're removed. When a version of Coverity is deprecated, you can continue running SAST tests with the deprecated version.

Note: Typically, a Coverity version upgrade occurs every quarter. When the version of Coverity you use is deprecated, we recommend you upgrade to the latest supported version within 60 days.

### Unsupported version of Coverity

When support for a version of Coverity ends, SAST tests that attempt to use the unsupported version will not run. To resume testing, you must activate a supported version of Coverity.

## Version changes

Changing the version of Coverity at the organization, application, project, or branch level won't interrupt tests that are already in progress. However, after you make the change, you must run a full SAST test on at least one branch in affected projects before rapid SAST tests can run.

When you choose to use a specific Coverity version (including the recommended version), the corresponding version of Rapid Scan Static (Sigma) is locked, and won't change when newer Sigma versions are available.

### Issues captured with different versions of Coverity and Rapid Scan Static

The issues captured by different versions of Coverity may differ. If you scan a project with a newer version and then switch to an older version, some issues detected by the newer version might not be captured by the older version. When this occurs, issues that are no longer detected by the active version of Coverity are marked as absent and removed from the main Issues view.

Note: You can get a list of absent issues on the Absent issues tab (Tests > select a completed SAST Test ID > Absent Issues).

## Test Summary Report

The versions of Coverity (and Rapid Scan Static) used in the latest SAST tests are listed in the Test Summary Report. See [Create a report](create-a-report.md) for more information.
