---
title: "Configuration file syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuration-file-syntax.html"
content_id: "UjNYnnazoQV47Ov0VbEFlQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:29.162164+00:00"
---

# Configuration file syntax

A security directives configuration file uses a variant of the JSON format. Overall, the
file consists of two parts:

1. Three initial fields. These identify the file as a security directives file,
   specify the directives format version it uses, and then the language to which
   the directives apply.
2. A `directives` object. The `directives` contains
   the directive sub-objects that specify what this configuration file
   accomplishes. It can also contain sub-objects whose specifications support the
   behavior of the directives themselves.
