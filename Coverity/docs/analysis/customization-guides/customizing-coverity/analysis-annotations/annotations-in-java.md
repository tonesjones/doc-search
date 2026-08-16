---
title: "Annotations in Java"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/annotations-in-java.html"
content_id: "xAHNWUXWMdp7zEA7NSFBfg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:27.846032+00:00"
---

# Annotations in Java

This section describes Coverity Analysis annotations for Java
code.

Adding annotations to source files that are analyzed by Coverity Analysis allows you to obtain more accurate results from certain checkers. Instead of letting
the checker infer information, you can explicitly tag classes and methods with the
appropriate behavior. The analysis reads these annotations as it runs.

Coverity Analysis annotations use the native Java *annotation*
syntax.

In this section:

- Adding annotations to Java source
- The '@Tainted' and '@NotTainted' attributes for Java code
- The '@SensitiveData' attribute for Java code
