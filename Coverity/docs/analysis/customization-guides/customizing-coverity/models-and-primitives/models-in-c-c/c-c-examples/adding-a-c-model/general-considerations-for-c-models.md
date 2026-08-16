---
title: "General considerations for C++ models"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/general-considerations-for-c-models.html"
content_id: "drFNAGmDVt6f_ML55Ot8fQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:37.092334+00:00"
---

# General considerations for C++ models

These are some considerations that apply to building new models.

- A .c file will create models that use C linkage. A .cpp file will create models that use C++ linkage.
- Make sure to use `extern "C"` when appropriate; for example, when you want to reference an existing built-in model.
- Match the prototypes properly. Namespaces and class names must be identical. When you use a `typedef`,
  what matters is the final target of the `typedef`, *not* the name of the `typedef`.

  If the target of a `typedef` can vary, you might need to write multiple models, each of which uses a possible target for the `typedef`.
- Do not use these instructions to model a template. Instead, see Models for templates (C++).
