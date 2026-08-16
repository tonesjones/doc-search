---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "Pg74bR1HfARYAew9iyOmgQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:21.983378+00:00"
---

# Description

Count the number of source code lines in the file(s) specified that are available for
Coverity pricing.

Coverity analyzes the number of lines based on the code collected. This may include some
third-party code, which is included by default in the line count because it is part of
the full code that gets compiled. However, you can exclude third-party code and other
files (specifically, test code and generated code) from the line count and the analysis
with the --third-party-regex option.

When counting lines, Coverity strips away blank lines and comments, but does not strip
away single braces or parentheses (comments and blank lines are not counted as lines).
The command uses the name and contents of the file to identify its language and how it
should be parsed.
