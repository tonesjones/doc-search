---
title: "Models in C# and Visual Basic"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-in-c-and-visual-basic.html"
content_id: "0HCOGbu3hUkWXURGPd4yPg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:43.906883+00:00"
---

# Models in C# and Visual Basic

This section describes how to write custom models for C# and Visual Basic® code, and the available modeling primitives.

To create models for C# or Visual Basic (in other words, .NET) programs, follow the
overall steps in Adding a custom model.

The primitives for C# and Visual Basic are part of the
`Coverity.Primitives` namespace. Coverity Analysis
provides an assembly that contains the primitives in
<install_dir>/library/primitives.dll.

Important: For a .NET model to be applied correctly, the namespace name, class name, number and
names of type parameters, method name, method parameter types, and return type must all
match those of the function being modeled.
