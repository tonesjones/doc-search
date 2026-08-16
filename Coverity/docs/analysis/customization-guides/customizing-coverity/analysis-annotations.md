---
title: "Analysis annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-annotations.html"
content_id: "tfYBK9y0SVG0BWkeE8wzUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:16.723473+00:00"
---

# Analysis annotations

For certain languages, you can affect checker behavior by annotating your source code
with markers known as *analysis annotations*.

Analysis annotations, like models, provide Coverity Analysis with hints
about function behavior. For C/C++, annotations can suppress reports of code patterns
that have an intentional purpose in the source code being analyzed.

Note: The standard Coverity workflow never requires any tool-specific code modifications.
The use of in-code analysis annotations is purely optional.

The Coverity documentation uses *analysis anotation* or simply *annotation* to
refer to the analysis annotations you can add to a source file, regardless of the term
(if any) that is native to the source language.

Analysis annotations are available only for C/C++, C#, Java, and Visual Basic. These are
the specific syntaxes in use:

C/C++
:   In C or C++ source, an analysis annotation is a comment with special
    formatting.

C# and Visual Basic (.NET languages)
:   In C# and Visual Basic source, an analysis annotation uses the native C# or
    Visual Basic *attribute* syntax.

Java
:   In Java source, an analysis annotation uses the native Java *annotation*
    syntax.

CAUTION:

Each language has its own analysis annotation syntax and set of capabilities, and
these are *not the same* as the syntax or capabilities available to the other
languages that can use annotations.

**Suggestion:** The properties that can be described by in-code annotations are
limited and apply only to certain syntax. If analysis annotations are not compatible
with your project source language, or if the situation you want to adjust for is out of
their scope, look at the Coverity 2026.6.0 Security Directives Reference to see if there are
directives that provide the functionality you are looking for.
