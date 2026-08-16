---
title: "Roles and responsibilities"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/roles-and-responsibilities.html"
content_id: "bWBwcIICKgjDXZ5ZBDQBXQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:23.096411+00:00"
---

# Roles and responsibilities

Coverity Analysis tasks and responsibilities vary based on the role you play in your
organization:

Coverity Analysis Administrators
:   Coverity Analysis administrators install, provision, configure, and integrate Coverity
    Analysis into the software build cycle. The Coverity Analysis administrator
    role has the following sub-roles:

    - IT engineers ensure that Coverity Analysis has the hardware and
      software resources required to run optimally. They add machines and
      other hardware, back up data, and install software.
    - Build engineers automate and integrate Coverity Analysis into
      existing build processes. They set up the system to automatically
      run Coverity Analysis over source code, generate defect reports, and
      make reports available to the Coverity Analysis consumers. In some
      organizations, they might also help developers to run Coverity
      Analysis on their local repositories.

Coverity Analysis Consumers
:   Coverity Analysis consumers use Coverity Analysis results to assess and improve software.
    The Coverity Analysis consumer role has the following sub-roles:

    - Developers and team leads are the primary consumers of Coverity Analysis
      analysis results. Both examine and prioritize software issues in
      Coverity Connect or Coverity
      Desktop. Developers also fix the issues by using the information
      that Coverity Connect provides about them. Sometimes
      these consumers work with the Coverity Analysis
      administrator to optimize the effectiveness of Coverity Analysis analyses, for example, by
      changing the set of checkers that is enabled.

      Coverity Connect is a web-based application for
      examining and handling defect data. Coverity
      Desktop is a plug-in to the Eclipse, IntelliJ IDEA, or Visual
      Studio Integrated Development Environment (IDE). Coverity Desktop provides most of the same management
      capabilities as Coverity Connect and allows you to
      modify source code to fix defects. A developer can examine,
      prioritize, triage, and fix defects across related code bases,
      such as multiple development branches or different target
      platforms.
    - Managers monitor defect reports and trends, to determine the overall
      software quality and trends. They might also monitor and manage the
      personnel responsible for fixing defects.

Coverity Analysis Power Users
:   Coverity Analysis power users are typically developers who understand both your software
    development environment and Coverity Analysis. These power users help
    communicate needs and requirements to consumers and administrators. Common
    tasks for this role include assessing the need for custom models (see Using custom models to improve analysis results) and
    determining what checkers to enable (see Enabling or disabling checkers). Development tasks that pertain to extending the functionality of
    Coverity Analysis in other ways also fit into this role.
