---
title: "General considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/general-considerations.html"
content_id: "GPRMBremG3l_bGpb3Ohh0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:55.054801+00:00"
---

# General considerations

The configuration file uses standard .yaml syntax as described in <https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html>. In addition, please observe the following:

- All configuration settings for various reports can be included in one
  `.yaml` file per project.
- Each Coverity project requires its own `.yaml` configuration file
  with a unique filename. For example:

  `coverityprojectconfig1.yaml`,
  `coverityprojectconfig2.yaml`,
  `coverityprojectconfig3.yaml`
- Configuration settings (or customized schema elements) that stand alone in the
  `.yaml` configuration file can be expressed outside of a
  nested block.
- Some elements that are required for a particular report are not present in the
  schemas because they must be provided via command line. For example, the
  password must be entered via command line.
- Some fields are file pathnames. A relative pathname is interpreted relative to
  the directory containing the configuration file. If the configuration did not
  come from a file, the pathname would be relative to the Report Generators'
  working directory.

  Pathnames may use a slash or backslash as a separator, whichever is more
  appropriate for their platform.
