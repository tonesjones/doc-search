---
title: "Line or statement numbering"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/line-or-statement-numbering.html"
content_id: "WvXp8sXwvDcVTeslSPLjiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:32.198456+00:00"
---

# Line or statement numbering

By default Coverity Fortran Syntax Analysis numbers each source input line sequentially.
Lines in include files are numbered in an hierarchical way. Line numbering starts anew
for each source input file. In this way you can use your editor to locate the lines of
interest in the easiest way.

However, you can instruct Coverity Fortran Syntax Analysis to number lines or statements
in a different way. To do so, you can place `count mode` option lines in
the [VARI­OUS] section of the configuration file. The lines to be added have the form
`count mode = ’mode’`, in which mode can be:

| line | number source input lines |
| statement | number statements |
| new_in_sub | start numbering anew for each subprogram |
| new_in_file | start numbering anew for each source input file |
| new_in_include | apply hierarchical numbering for included lines c.q. statements |
| continue_in_include | proceed numbering sequentially for included lines c.q. statements |

For example, if you want statement numbering, beginning from 1 in each subprogram and
proceed statement numbering sequentially in included lines, you specify the following
lines in the [VARIOUS] section of the configuration file:

`count mode = ’statement’`

`count mode = ’new in sub’`

`count mode = ’continue in include’`

Note that the mode keyword has to be placed within apostrophes. You can concatenate a
supplied configuration file with a private configuration file as described in Redefinition and suppression of messages.
