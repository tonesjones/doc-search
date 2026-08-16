---
title: "Coverity Analysis hardware"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-hardware.html"
content_id: "lMiIYyJt5FPJ0kanMHc5og"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:46.331738+00:00"
---

# Coverity Analysis hardware

Coverity Analysis has certain minimum requirements for memory size. Though the speed of
the analysis can increase many times through the use of CPU parallelism and extra
memory, it is important to note the following constraints:

- The speed of the analysis depends on the analysis configuration including which
  checkers are enabled, and which languages are being analyzed.
- There are points of rapidly diminishing return beyond which neither additional CPU
  parallelism nor additional memory will increase the speed significantly.
