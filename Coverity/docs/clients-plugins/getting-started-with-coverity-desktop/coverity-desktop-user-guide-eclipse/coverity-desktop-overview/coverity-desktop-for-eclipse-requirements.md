---
title: "Coverity Desktop for Eclipse requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-desktop-for-eclipse-requirements.html"
content_id: "7BFLb~TpvA9Ctwup03jpTQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:38.175653+00:00"
---

# Coverity Desktop for Eclipse requirements

Note: Refer to "Coverity Desktop" in the Coverity 2026.6.0 Installation and Upgrade Guide for supported IDE and Java version numbers.

Coverity Desktop for Eclipse has the following requirements:

- Coverity Connect 2026.6.0
- Coverity Analysis 2026.6.0 (required for local
  analysis. Typically installed at the same time as the plug-in)
- Java Runtime Environment
- Eclipse or ARM Development Studio 5 (DS-5)
- Eclipse C/C++ Development Tooling (CDT) for the C/C++ analysis only ( 
  http://www.eclipse.org/cdt/  )
- Eclipse Java Development Tools (JDT), only for the Java analysis
- Memory requirements: the minimum is 3 GB of RAM and more if you use parallel analysis. Refer
  to "Minimum
  requirements" and "Memory
  requirements for parallel analysis" in the Coverity 2026.6.0 Installation and Upgrade Guide for more information.

Coverity Desktop for Wind River Workbench has the following
requirements:

- Coverity Connect 2026.6.0
- Coverity Analysis 2026.6.0 (required for local
  analysis. Typically installed at the same time as the plug-in)
- Java Runtime Environment
- Wind River WorkBench

Coverity Desktop for QNX Momentics IDE has the following requirements:

- Coverity Connect 2026.6.0
- Coverity Analysis 2020.12 (required for local analysis. Typically
  installed at the same time as the plug-in)
- Java Runtime Environment
- QNX Momentics

Before getting started with Coverity Desktop, make sure that you also have
the following Coverity Connect access information:

- Host name
- Port number and type (HTTP or HTTPS)
- Authentication key file, or your user name and password for creating a new
  authentication key.
- Stream name

Note: This information is dependent on your Coverity Connect
administrator configuring the server and running an initial analysis and commit. See
the Coverity Platform 2026.6.0 User and Administrator Guide for information on configuring Coverity Connect for use with Desktop Analysis.
