---
title: "Coverity Analysis deployment models"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-deployment-models.html"
content_id: "CMMmzbceDKJhT5otYJ3iaQ"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:39.009473+00:00"
---

# Coverity Analysis deployment models

The Coverity analysis tools are installed as part of the Coverity®
Analysis installation package and the goal of these tools is to find issues in your
code:

[image: image]

Software organizations generally produce several products, and each product tends to
consist of a number of related code branches and targets. These branches and targets
might be for the various supported platforms, product versions, trunk and development
branches. Coverity Analysis runs over each code base to produce a snapshot of each code
base. A snapshot consists of the results of running Coverity Analysis once over a code
base. The snapshot includes both the issue information and the version of the source
code in which the defects were found and is committed to Coverity Connect after the
analysis process is completed.

As your developers continue to modify their code bases, it is useful to provide them with
on-going data about the creation of new issues and the elimination of existing ones.
Administrators can define streams for each specific code base that they wish to analyze.
A stream is a sequence of snapshots over a specified code base. Each time Coverity
Analysis runs, the analysis results are grouped with previous results that are made up
of the same code base and configuration. Streams capture issue information and trends
over time. For more information, see the Coverity Platform 2026.6.0 User and Administrator Guide).

For specific implementation details (including how to configure compilers, integrate with
the build, enable checkers and so forth), see the Coverity Analysis 2026.6.0 User and Administrator Guide.

Note: Hardware considerations for the analysis tools are generally established by the needs
of your organization's build server (performance, size, and so forth.) However, there
are some sizing options to consider. For more information, see Coverity Analysis hardware.
