---
title: "Conditionals"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditionals.html"
content_id: "Ck5wlgIkcwM~IJlnlyyEkA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:42.785044+00:00"
---

# Conditionals

A checker has two fundamental sources of information about a path: assignments and
conditionals. Assignments are handled by computing an abstraction of the right-hand
side, and storing that abstraction in the left-hand side. That is, they simply
correspond to updating the store.

Conditionals, on the other hand, act as *constraints*: the current abstract state
(the store) must be refined in such a way as to be consistent with the branch of the
conditional being taken. The refinement algorithm is dependent on the abstraction being
used by the checker.
