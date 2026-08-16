---
title: "Annotations in C# and Visual Basic"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/annotations-in-c-and-visual-basic.html"
content_id: "XosbkR0CtQ6U4~M3kHtjhw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:25.236565+00:00"
---

# Annotations in C# and Visual Basic

This section describes Coverity Analysis annotations for C# and
Visual Basic code.

Adding annotations to source files that are analyzed by Coverity Analysis allows you to obtain more accurate results. Instead of letting the checker infer
information, you can explicitly tag program data as having certain properties or
behavior. The analysis reads these annotations as it runs. Coverity Analysis annotations use the standard *attribute* syntax
for C# or Visual Basic.

In this section:

- Adding annotations to C# or Visual Basic source
- The 'Tainted' and 'NotTainted' attributes for .NET code
- The 'SensitiveData' attribute for .NET code
