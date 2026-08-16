---
title: "Specifying the target language"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-the-target-language.html"
content_id: "fqx_1Z3iOdX1TnaAitG2bQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:10.138907+00:00"
---

# Specifying the target language

In your CodeXM source, begin with an `include` declaration that names the target;
for example, `` include `C/C++`; ``.

Specifying the target language includes the library for that language. This makes language-specific patterns and functions available within
the CodeXM file.

The language specification also causes the checkers defined in your CodeXM file to be applied only to appropriate target source code in your code base.
