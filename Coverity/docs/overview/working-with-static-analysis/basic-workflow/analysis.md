---
title: "Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis.html"
content_id: "jmCi3mQOlKoa_M7v8o_RVw"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:20.950229+00:00"
---

# Analysis

The work of analysis is done in three stages: *capture*, *analyze*, and
*commit*. The stages are usually performed sequentially on the same machine.
Here we describe each of these component steps, which you might want to configure
independently to assist debugging and to support advanced use cases.

- **Capture**

  In this stage, Coverity captures a representation of your source code (whether
  compiled or file-based) and stores it in a known location, separate from the
  build artifacts. Coverity analysis does not modify source code or compiled
  binaries.
- **Analyze**

  During this stage, the developer or Dev/Ops uses the GUI, the CLI, or a script to
  scan binary representation of the code from the capture stage for issues or rule
  violations.
- **Commit**

  In this stage, analysis results are committed to the database (a collection of
  analysis instances corresponding to a release branch). The command or script
  that initiates the commit specifies the data-storage location, the connection
  information for the Connect server, and the user credentials.

Note: The Third-Party Integration Toolkit is available to combine third-party issues with
the Coverity Connect database.

**Documentation Resources**

- Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI
- Coverity Analysis 2026.6.0 User and Administrator Guide
