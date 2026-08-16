---
title: "Coverity product overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-product-overview.html"
content_id: "9zHlvaRq1FStYIjlxgA0uw"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:30.104209+00:00"
---

# Coverity product overview

There are two installer applications that Coverity provides, the Coverity Analysis installer
and the Coverity Platform installer.

## Coverity Analysis Installation

The Coverity Analysis component and its extensions are built on top of a set of foundational
technologies that support the use of Coverity checkers to detect quality defects
(quality issues), and potential security vulnerabilities (security issues). The
Coverity Analysis extensions are listed below:

- Third Party Integration Toolkit supports the addition of issues found by
  third-party products to the Coverity Connect database.
- Compiler Integration Toolkit (CIT) allows you to extend the set of compilers
  that can be used to build source code for Coverity code analysis.
- CodeXM supports the development of custom checkers.

## Coverity Platform Installation

Coverity Platform components support Web-based management of issues found by Coverity
Analysis and third-party tools.

- **Coverity Connect** is a Web-based application that helps
  software developers and team leaders manage and fix issues found using Coverity
  Analysis and third party tools. The Coverity Connect interface
  provides descriptions of the issues found by Coverity Analysis and shows where
  the issues exist in the source code. Coverity Connect also
  facilitates code governance by enabling software development organizations to
  set policies for code quality and security, and then manage, monitor, and report
  on these policies as code is tested. This policy management capability provides
  managers and leaders who have cross-organizational responsibilities with the
  insight needed to better align quality goals with business objectives, to
  enforce standards across the development organization, and to manage third-party
  code dependencies.
  - **Downloads**: Coverity Connect provides access to
    downloads for the Coverity Desktop plug-ins and the
    Coverity Reports installer. Coverity Desktop plug-ins
    support IDE-based analysis, management, and remediation of issues. Coverity Desktop relies on Coverity Analysis to
    support local code analysis. For more information about installing Coverity Desktop, see Installing Coverity Desktop components. For more
    information about installing report generators, see Installing Coverity Reports.
  - **Extensions**: Coverity Connect provides access to the
    Coverity Platform REST Web Services API and the Coverity Platform SOAP
    Web Services API.
