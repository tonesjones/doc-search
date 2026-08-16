---
title: "Name mangling"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/name-mangling.html"
content_id: "kBwQb9rlHXjAX2ooENQHTw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:03.061175+00:00"
---

# Name mangling

Name mangling is a technique used by compilers to encode the type of an entity in its
linker symbol name. This is necessary because of function
overloading:`f(int)` and `f(int,int)` are distinct
entities, so their linker symbol names must be distinct.
