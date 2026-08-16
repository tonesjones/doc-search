---
title: "Possible loss of triage information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/possible-loss-of-triage-information.html"
content_id: "CxESKbNEo~DO675_EypbXQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:56.700697+00:00"
---

# Possible loss of triage information

Enhancements have been made to Coverity that might result in the loss of triage
information in the following cases:

- An enhancement has been introduced to Rapid Scan Static (Sigma) in order to generate
  more stable defect merge keys (also known as *fingerprints*). This enhancement
  might, however, result in merge keys changing for some existing defects (also known
  as issues), with a resultant loss of triage information for those defects. Such an
  impact is expected to be limited to a small fraction of total defects and will only
  effect Rapid Scan Static (Sigma) defects.
- Loss of triage information is expected for all Terraform checkers. The Terraform
  checker names and defect locations (files and line numbers) will not change, but the
  triage information will be lost. In this release, Coverity has upgraded the
  HashiCorp Configuration Language (HCL) grammar used by the Terraform files to the
  newer, officially supported grammar. (HCL is the language used to create
  configuration files for Terraform.) This upgrade improves defect accuracy,
  performance, and maintainability in the long term. The Abstract Syntax Tree (AST)
  generated using the HCL grammar is used by Coverity to calculate merge keys for
  defects. Therefore, all Terraform merge keys generated in this release will be
  different from previously generated ones, and the data cannot be merged with the
  previous findings. This is a one-time change, and the loss of triage information
  will not repeat after the defects are re-triaged.
