---
title: "Evidence"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/evidence.html"
content_id: "MPOSfe7PtiS7qtqKDIgD~A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:25.009289+00:00"
content_hash: "0d25865db046598fa3617b40aa3bc74f9478c9477bbe4f47a15e57e9fd2367a9"
---

# Evidence

The *Evidence* section of the Finding Details page shows the raw results that make
up a finding—regardless of whether the finding originated from an analysis tool or a
manual entry. Each result in the Evidence section will be displayed in its own
subsection, with the result's "type" as the header.

[image: image]

Each result in the evidence section includes the following fields:

- **Detection Method.** Describes how the result was discovered (e.g., what type of
  analysis was performed), typically either "Static Analysis" or "Dynamic Analysis."
- **First Seen On.** For supported tools, reflects the date that the result was observed by
  that tool.
- **Location.** Describes exactly where the result was reported, i.e. a file, line
  number, and column number, or a URL. Note that because Software Risk Manager
  attempts to normalize locations, a result's location may differ slightly from the
  location of the finding it belongs to.
- **Tool.** The name of the tool that reported the result.
- **Tool Code.** The raw "code" that describes the type of the result (for example,
  "SQL Injection").
- **Tool Category.** The raw "category" (depending on the tool, the terminology may
  differ, e.g., "group") to which the tool code belongs.
- **CWE.** The Common Weakness Enumeration item reported by the tool, if available.
  Note that because Software Risk Manager uses *Rule Sets* to determine how
  results are combined into findings, a result's CWE may differ from its finding's
  CWE. To control this behavior, create or choose a different Rule Set to use in your
  project's *Analysis
  Configuration*.
- **CVE.** The Common Vulnerabilities and Exposures identifier reported by the
  tool, if available.
- **Severity.** The Software Risk Manager equivalent of the tool's reported
  severity. Note that some tools use different terminology for this, such as
  "priority," or different scales, like "1 through 10." Also note that when multiple
  results of different severities are combined, the finding will either take the
  severity of the rule that joined them or the highest severity from among the
  combined results.
- **Related Findings.** Lists any other findings that share the result, when
  applicable. This is more common when dealing with DAST and Hybrid results, as
  correlation between DAST results is less strict than with SAST.
- **Tool Rule Description.** The tool's unique description of the *type* of
  result being reported. For example, with a SQL Injection result, this is where you
  could find the tools' description of *what SQL Injection is*. Click the "show
  more" and "show less" links to expand and collapse the description.
- **Contextual Description.** The tool's description of the specific result. For
  example, with a SQL Injection result, this is where you could find out how this
  particular part of your codebase is vulnerable to SQL Injection. Click the "show
  more" and "show less" links to expand and collapse the description.
- **Host Info.** Shows the raw host data of the result being reported for
  Network Analysis results as well as certain DAST results. The host data is displayed as a
  table, with the left column indicating the host "field" (e.g., *Fully Qualified
  Domain Name (FQDN)*, *Hostname*, *IP Address*, etc.), and the right
  column containing the values for that field. The *Also include values from host
  normalization* checkbox will cause the page to include any values from the
  "normalized" version of this host to also be displayed. The "normalized" host is
  what is shown on the *Hosts* page. Values present on the normalized host and
  not present on the raw host will be rendered in green.
- **HTTP Activity.** This is shown for DAST results, and it will expand to its own
  subsection, which is described
  here.

Some tools report additional information that may appear in this section, such as
Veracode's *Flaw ID*. When these additional fields are present in a project, some
of them may become available as a finding search option on the Findings page.
