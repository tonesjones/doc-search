---
title: "Configure"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configure.html"
content_id: "zjaxrW0lorEgDFHFHM1Elw"
version: "2026.9"
section: "Coverity overview"
scraped_at: "2026-10-04T23:32:55.603836+00:00"
---

# Configure

In the *configure* stage, the administrator or Dev/Ops provides information about
configuring the analysis for your project. The required information varies with the type
of analysis you perform:

- **For compiled languages**, specify the settings to be used by the analysis
  engine to emulate your native compiler. Furnish the information needed about the
  build processes, dependencies, and build-related programs used in building the code
  to be analyzed.
- **For scripted languages or buildless capture**, specify the files to be
  analyzed. Typically, you want to analyze source code, configuration files, and any
  library code that your source code needs to compile or run.

You provide configuration information using a JSON configuration file.

**Documentation Resources**

- Guide to the Coverity Point and Scan UI and the Coverity CLI
- Coverity Analysis User and Administrator Guide
