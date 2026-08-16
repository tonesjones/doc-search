---
title: "The program analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-program-analysis.html"
content_id: "oHYHW3RLYSZ4r0J_CJtGmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:50.435972+00:00"
---

# The program analysis

Analyzing the program as a whole is a key functionality of Coverity Fortran Syntax
Anal­ysis. All references of external procedures are verified. Undefined actual
arguments are flagged. When the complete option `-ancmpl` is specified,
unreferenced and undefined global entities over the program as a whole are flagged. In
that case unreferenced procedures, unreferenced common blocks, unreferenced and
undefined common-block objects, unreferenced modules, unreferenced and undefined public
module procedures, operators and data are flagged. See also Verification of common blocks and Verification of modules.

If not all procedures are available you can make the interface available; see Specification of procedure interfaces.
