---
title: "Descriptions"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/descriptions.html"
content_id: "yuABpsuiq9gbx_xeAGSzFA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:22.477639+00:00"
content_hash: "b97021643eb2170cf5add4dc4b41aeed03f2a9c486817789e0e6542d052929f7"
---

# Descriptions

The description information shown by Software Risk Manager can come from a variety of
sources, with varying levels of detail. At a high level, descriptions are divided into
"general" and "contextual."

- "General" descriptions explain the *type* of finding, e.g. answering the
  question "What is SQL Injection?"
- "Contextual" descriptions explain a particular *instance* of the finding,
  e.g. answering the question "Why is this particular code a SQL Injection
  risk?"

The main "Description" section of the details page is a "general" description. Most of
the time, the main description comes from a Rule Set. When a finding matches up to a rule,
the main description section will use that rule's description. For findings created by
*observed* tool results (i.e. types of findings that Software Risk Manager
doesn't already know about - see the Tool Configurationsection), if the tool result
does not match a rule, the general description may be created from that tool result, as
long as the tool result provides one. This will often be the case with tools such as
Fortify and Veracode.

[image: image]

The finding itself will not have a "contextual" description. This will instead be found
on the individual results shown in the *Evidence* section. The "general" and
"contextual" descriptions for results will be shown in the *Tool Rule Description*
and *Contextual Description* sections of their display area, respectively (see
below).
