---
title: "Specifying the target language"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-the-target-language.html"
content_id: "JOYCn0rlmPxIyFfSk2PhPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:46.139477+00:00"
---

# Specifying the target language

In your CodeXM source, begin with an include declaration that names the library target language:
`` include `Go` ``.

Specifying the target language makes the library's special patterns and functions available within this CodeXM file.
These patterns and functions are the subject of this reference.

The language specification also causes the checkers defined in your CodeXM file to be applied only to the target
source code in your code base.
