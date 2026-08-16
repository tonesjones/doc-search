---
title: "Crossworks MSP430 support change"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/crossworks-msp430-support-change.html"
content_id: "PgVWwxQPNBahFuLInWz9Dg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:34.578011+00:00"
---

# Crossworks MSP430 support change

**Affects:** Customers who use Crossworks MSP430 compilers.

**Changes:**

- The compiler type `crossworks:430` has been converted to
  `crossworks:cc` for compiler driver cc.
- The compiler type `crossworks:hcc` has been added for compiler
  driver hcc.
- The compiler type `crossworks:hcl` has been added for compiler
  driver hcl.

**Impact:** Users must regenerate compiler configurations because of significant
restructuring of how these compilers are handled.

**Upgrade procedure:**

Run `cov-configure` with the compiler type (option
`--comptype`) set to one of:

- `crossworks:cc` for compiler driver cc
- `crossworks:hcc` for compiler driver hcc
- `crossworks:hcl` for compiler driver hcl

As always, a configuration template is recommended.
