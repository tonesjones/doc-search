---
title: "Java side-effect primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-side-effect-primitives.html"
content_id: "2bANaWRr1dXstB2lBYrRcA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:04.240480+00:00"
---

# Java side-effect primitives

Primitives for establishing intended presence of side effects.

## `void sideEffectFree()`

Any method that calls this primitive is assumed to have no useful side effects outside of the method's return value.

## `void nsideEffectOnlyThis()`

Any method that calls this primitive is assumed to have no useful side effects outside of modifying its receiver ('this') and possibly returning a value.

## `void sideEffects()`

Any method that calls this primitive is assumed to have potential side effects outside of its return value.
