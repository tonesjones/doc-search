---
title: "Using Fail Pull Requests With Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-fail-pull-requests-with-coverity.html"
content_id: "27NYrjFir1wLqz7QPEKkEQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:23.221385+00:00"
---

# Using Fail Pull Requests With Coverity

Coverity security scans can be configured to automatically fail Pull Request scans when security issues are detected according to specified levels of impact. Integrating this capability into CI/CD pipelines prevents high-impact security vulnerabilities from entering the production codebase.

## What Are Fail Pull Requests?

Bridge CLI can be configured to fail Coverity Pull Request scans and break the build for new issues detected and filtered according to one or more levels of Impact: [`High`, `Medium`, `Low`, or `Audit`], with a default Impact level of [`High`].

When new issues matching the Impact filter are detected in a Coverity Pull Request scan the following actions occur:

- Review comments are added to the Pull Request.
- Issues are uploaded to the Coverity server (CNC and Connect) as preview commits to enable further decision making based on the scan results, offering the following benefits:
  - Organizations can configure how security findings are communicated during code reviews based on impact levels and organizational preferences.
  - Organizations can address pipeline failures related to newly identified issues in Pull Request scans.
- The Pull Request scan fails and breaks the CI/CD pipeline build.

  Important: The `coverity_policy_view` parameter evaluates static analysis results against predefined security and quality policies to determine whether a build should pass or fail. This parameter is ignored when running Fail Pull Request scans.

Issues marked as ignored/dismissed in the Coverity servers are also excluded from subsequent Coverity Pull Request scans. Subsequently, this also means that Pull Request comments open for an issue that has subsequently been marked as ignored in Coverity will be resolved.

## What Are The Benefits?

Coverity Pull Request scans offer the following benefits:

| Benefit | Description |
| --- | --- |
| **Seamless Issue Management** | Enables bi-directional synchronization between Pull Request scans and Coverity Connect servers, creating a cohesive vulnerability management workflow. |
| **Enforce Security Standards** | Provide configurable build failure mechanisms for Pull Requests containing security vulnerabilities, ensuring security standards are met before code merging. |
| **Risk-Based Security Gates** | Implement Impact based filtering in Coverity server (CNC and Connect) Pull Request comments to allow organizations to establish appropriate security gates based on their risk tolerance. |
| **Improve Developer Experience** | Streamline security feedback in the development process by showing only relevant, actionable security issues during Pull Request reviews. |

## Fail Pull Request Behavior

The table below highlights the behavior of Fail Pull Requests when new issues are detected that **match** a specified filter list of Impact levels, e.g. `[High, Medium, Low, Audit]`. If unspecified, the Impact filter defaults to `[High]`.

| **Pull Request Comments Enabled** | **Pull Request Impact Filter Matched** | **Pull Request Scan Behavior** | |
| --- | --- | --- | --- |
| **Pipeline Build Status** | **Comments Added** |
| ❌ | ✅ | ✅ | ❌ |
| ❌ | ❌ | ✅ | ❌ |
| ✅ | ❌ | ✅ | ❌ |
| ✅ | ✅ | ❌ | ✅ |

## Bridge CLI Example

For an example of using Bridge CLI to create Coverity Fail Pull Requests please refer to Creating Coverity Fail Pull Requests.

## Useful Resources

- [Triaging Issues With Coverity](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/coverity-platform/topics/modern_ui_triaging_issues.html)
- [Coverity Micro Course: Examining and Triaging Issues](https://blackduck.skilljar.com/path/coverity-from-install-to-first-results/coverity-examining-and-triaging-issues)
