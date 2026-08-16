---
title: "Basic workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-workflow.html"
content_id: "B3_axeJJMyXeEk9M_vtFoQ"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:19.048330+00:00"
---

# Basic workflow

The basic workflow varies with your deployment, and depends on whether the build is done
using the GUI or using commands or scripts. In this section, we will assume a Command
Line Interface (CLI) based approach to better explain each step. With respect to the
roles we just described, the steps are discharged as follows:

1. **Setup**: The administrator installs Coverity and configures
   maintenance tasks.
2. **Configure**: The administrator or Dev/Ops provides information about
   the language of the source files to capture and analyze, and for build capture,
   provides settings that are used to emulate your native compiler, its options,
   definitions and version.
3. **Analysis**: Involves the following sub-steps. Whether these are
   implicit or explicit depends on whether you use the GUI or the CLI and on the
   degree of control you want over the analysis.
   - **Capture**: The developer or Dev/Ops creates the intermediate
     directory for the source code to be analyzed.
   - **Analyze**: The developer or Dev/Ops directs Coverity to scan the
     code using currently enabled checkers.
   - **Commit**: The developer or Dev/Ops commits the defect database
     and summary to the Coverity Connect server.
4. **Organize**: The developer or
   Dev/Ops filters and inventories issues and related data.
5. **Triage**: The developer or
   Manager triages issues. These are fixed, dismissed, or archived.
6. **Resolve**: The developer
   updates code to resolve the issues identified during analysis.
7. **Report**: The manager or Dev/Ops monitors dashboards, evaluates
   trends, and generates reports.

These steps are described in the following sections. Of course, in many deployments, some
of these steps would be automated.
