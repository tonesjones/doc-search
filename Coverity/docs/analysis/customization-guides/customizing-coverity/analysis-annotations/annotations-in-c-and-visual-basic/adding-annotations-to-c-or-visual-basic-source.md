---
title: "Adding annotations to C# or Visual Basic source"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-annotations-to-c-or-visual-basic-source.html"
content_id: "pET3VvquyuCIN8MuVG8txw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:25.883985+00:00"
---

# Adding annotations to C# or Visual Basic source

These are steps to add annotations to C# or Visual Basic (.NET) source
code.

1. Import the relevant attribute classes.

   The Coverity attributes are part of the
   `Coverity.Attributes` namespace, and a DLL file that
   contains the attribute classes (as well as other modeling primitives) is
   located in Coverity Analysis installation directory at
   <install_dir>/library/primitives.dll.
2. In the project source, annotate methods or classes with the relevant
   attributes.

   These are checkers that support C# or Visual Basic attributes, and the
   particular attributes they support (remember that the set of checkers can
   change with each release of Coverity):

   - SENSITIVE_DATA_LEAK

     `SensitiveData`
   - WEAK_PASSWORD_HASH

     `SensitiveData`
   - TAINT_ASSERT

     `NotTainted`
   - Tainted dataflow checkers (various, including OS_CMD_INJECTION, SQLI,
     and XSS)

     `Tainted`,
     `NotTainted`
3. Run `cov-analyze` to scan the annotated code.
