---
title: "Scanning Your Code"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scanning-your-code.html"
content_id: "o~qzUSe2nnTOV7qSFISrXw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:26.078646+00:00"
---

# Scanning Your Code

Scanning is the core way Black Duck SCA identifies open source components,
licenses, and known vulnerabilities in your codebase. When you run a scan, Black Duck SCA analyzes your project files and generates a comprehensive
Bill of Materials (BOM), helping you stay compliant, secure, and informed.

## What does a Black Duck SCA scan do?

Black Duck scans your codebase to:

- Identify open source components and their versions
- Detect known security vulnerabilities using sources like the National
  Vulnerability Database (NVD) and Black Duck Security
  Advisories (BDSA)
- Evaluate license risk and compliance
- Generate a BOM for auditing and reporting
- Enforce custom policies based on your organization's risk tolerance

Scans can be triggered during development, in CI/CD pipelines, or manually—depending on how
you choose to integrate Black Duck SCA.

## Available scanning tools

Black Duck offers a variety of tools to suit different environments and
workflows:

- **SCM Onboarding UI**

  Use the [SCM Onboarding UI](https://integrations.blackduck.com/onboard) for a streamlined setup
  process, currently supporting GitHub.com only. This interface simplifies
  integration and helps you quickly onboard projects. For detailed
  instructions, see the [GitHub Black Duck Integration
  documentation](https://docs.blackduck.com/access?ft:originId=58f48ad4c89c53317cf57f364d022fb8/c6dc98c86dc2c606ffc19b23cb23fe0b.topic).
- **Action Integrations**

  For other SCM platforms, the action integrations provide flexible options to incorporate
  Black Duck into your existing workflows. Quickstart guides, such as the
  [GitLab SCA Quickstart Guide](https://docs.blackduck.com/access?ft:originId=58f48ad4c89c53317cf57f364d022fb8/b06c8446fc50dd217491f2c661e3baf3.topic),
  assist in setting up scanning seamlessly.
- **Detect CLI**

  The [Black Duck Detect CLI](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/5cab2bc9716c11432d8032762489aa98.topic) offers
  advanced users a powerful and customizable scanning tool for source code,
  binaries, and containers. It supports integration into CI/CD pipelines with
  commands available for Windows and Linux environments ([Bash/PowerShell guides](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/46c830e6fbe085f3c5ce5e0a053a0a81.topic)).
- **Detect Desktop**

  The [Detect Desktop](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/58f3c57501f1732b2cf746c9e6d839ea.topic) provides a
  user-friendly desktop application, making it easy to scan projects without
  command-line interaction.
- **Code Sight IDE**

  [Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/bbda872c8a804e4ceeee1be00dec643d.topic) integrates directly
  into your development environment to deliver real-time scanning and
  vulnerability insights, helping developers identify and address issues as
  they code.

Note: Some features may require a specific license or configuration. Contact your administrator
if you are unsure which scanning tools are available in your environment.
