---
title: "Customizing and extending static analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/customizing-and-extending-static-analysis.html"
content_id: "ymybEqM_wJ_uDaEYh6w_JA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:23.297872+00:00"
---

# Customizing and extending static analysis

Coverity Analysis can usually scan source code without specific, custom settings, but it
also provides a number of ways to fine-tune the way it runs a scan.

The following list shows some of the possible customization techniques:

- Enabling or disabling particular checkers.
- Setting options to adjust how a checker behaves.
- Writing custom *models* to further specify checker behavior.

  Models are used for interprocedural analysis. Custom models can reduce the
  number of false positives that finds, or increase the number of valid issues
  that are detected.

  Some languages also support in-code *annotations,* whose effect is similar
  to that of models.
- Writing your own custom checkers.

These techniques, along with others are described in Customizing Coverity.
