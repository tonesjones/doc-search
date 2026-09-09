---
title: "Project Management Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/project-management-overview.html"
content_id: "mfRkBddAo8FN6E7cYCXGZQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:05.000566+00:00"
content_hash: "7618ff53df6142c20f3653a82e80a53104f621a4afe20cc35b1fcad202331e13"
---

# Project Management Overview

Before you can run an analysis on a file, you need to create a project. Once projects are
configured, which includes policy associations, tool configurations, analysis settings,
and so on, you can add files for analysis. SRM analyzes the files in that project and
creates findings that can be viewed on the Findings page.

When working with projects, it's important to understand the following terms:

- **Project.** A collection of branches for a target software.
- **Branch.** A unique line of development containing a collection of scans
  over time. A project contains at least one branch, and each branch may contain
  any number of findings.
- **Analysis.** An individual scan, in which any number of tool results are
  taken into account in order to create or update findings.
- **Finding.** Information about some part of an application, generally a flaw
  or vulnerability. Findings are generated from an analysis, but can also be
  entered manually.
- **Tool Result.** Information about an application, as reported by a tool;
  tool results are correlated during analysis, becoming associated with
  findings.
- **Manual Result.** Information about an application which is entered into the
  system manually.
- **Result.** A generic term that includes both tool and manual results.

## Project Management Tasks

For more information on Project Management tasks, see the following topics:

- Working with Projects
- Using Filters to Find
  Projects
- Adding a Project
- Working with Nested Projects
- Configuring a Project
  Analysis
- Configuring Tools for a
  Project
- Configuring Tool Connectors for a
  Project
- Analyzing Code in a Git
  Repository
- Issue Tracker
  Configuration
- Configuring Project
  Metadata
- Tool Service
  Configuration
- Orchestrated Analysis
- Working with Project
  Branches
- Intelligent
  Orchestration
