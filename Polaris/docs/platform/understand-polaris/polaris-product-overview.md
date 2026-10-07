---
title: "Polaris product overview"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-product-overview.html"
content_id: "M2~OGTkBhzfyApNKaB~Kqg"
product_key: "polaris-platform-latest"
section: "Understand Polaris"
scraped_at: "2026-10-04T23:29:17.132877+00:00"
content_hash: "019278e99a9c2b96bec43955fa9eba7abdba3f5df1abc686e3bdd40a8547bb38"
---

# Polaris product overview

The Black Duck Polaris® Platform delivers highly scalable Static Application Security Testing (SAST), Software Composition Analysis (SCA), Dynamic Application Security Testing (DAST), and Container Analysis for your Enterprise.

## What Polaris does

- **Testing**: Scan applications in the cloud using static analysis (SAST - Full or Rapid) and software composition analysis (SCA - Package Manager, Signature Analysis, or Binary Analysis). Run dynamic tests (DAST) against your organization's web applications and APIs. Scan container images for open source risk using Container Analysis.
- **Issue Lifecycle Management**: Review, triage (either manually or with AI), dismiss, and close issues discovered during security scans. Actions can be taken manually or programmatically.
- **Build a software bill of materials (SBOM)**: Generate the industry's most complete SBOM using package manager, signature analysis, binary analysis, and container analysis. Evaluate the supply chain of each open source component, license and copyright used to create the application and/or project.
- **Consolidate SAST and SCA findings from other tools**: Import SAST and SCA issues from third-party security tools to view all an application's vulnerabilities in one place.
- **Analytics**: Review the overall risk posture of a project, application, or organization.
- **Automation**: Use SCM repository integrations, a command-line client, or REST APIs to integrate security testing into your DevOps pipeline. Test and monitor branches to ensure your applications stay secure.
- **Dashboards**: Offers high-level snapshots of test results, components or licenses with filters to customize your view.
- **Reporting**: Create customized reports of your test results, SBOM, or notices file.
- **Policy management**: Establish guidelines and use Polaris to automatically execute specific actions like scheduling tests, breaking builds, notifying users of test findings, and setting fix-by dates.
- **Expert triage assistance**: For Static scans of a project's default branch, human assessors are available to review findings and reduce false positives, helping developers to focus on meaningful results. You can also use AI to triage up to 20 SAST issues at a time, and if you choose to accept the automated suggestions, they'll be submitted for approval using your standard workflow.

## What teams do with Polaris

- Move security testing to the cloud.
- Enable developers by building security testing into CI/CD pipelines.
- Schedule regular scans of repos.
- Set scan policies that can fail a build and prevent code from merging when pre-defined events are detected.
- Use the web UI to triage issues found in the code and dismiss them or assign owners to them.
- Use dashboards to monitor the security stance of applications and their constituent projects.

## Components of Polaris

- **Polaris Web UI**: Manage subscriptions, schedule testing, review, and triage issues, and monitor your security stance on dashboards.
- **Bridge command line interface**: Use a simple scripting language to automate tests. Scan information is uploaded to the Polaris UI, and you can see all the information from your tests in the web UI.
- **Integrations**: Polaris can:
  - Interact with SCM repositories, including GitHub, GitLab, Bitbucket, and Azure DevOps.
    - Event-Based Test Automation.
    - Synchronization.
    - PR comments, Fix and Fail PRs.
  - Create tickets in Azure DevOps, Jira, ServiceNow, GitHub Issues, and GitLab Issues for issues captured in tests.
  - Include links to Secure Code Warrior training resources with issues captured in tests.
- **Polaris API**: Robust APIs make it possible to quickly retrieve and filter issue data after running tests.
- **Issue Management MCP server**: Query your organization's security findings using natural language through AI assistants.
