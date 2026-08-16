---
title: "Incorporating SCM data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incorporating-scm-data.html"
content_id: "SaNx9Wc24H4msbriI0WLrA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:32.289063+00:00"
---

# Incorporating SCM data

Adding SCM change data provides important information about the authors and change dates
of your code. This information can be utilized for automatic owner assignment and is
displayed in Coverity Connect. SCM change data includes the following for each line of
the source code:

- date - The date that the changed code was checked into the SCM system.
- revision - The revision number corresponding the check-in of the changed code. See SCM revision format for more information.
- author - The username of the user who checked the code in. Author is limited to a maximum of
  1024 characters.

Coverity provides several tools that enable you to extract and import accurate and
effective change data from your SCM. SCM change data is only maintained for files that
appear in the emit as a result of being used in the build. If a file is no longer used,
the SCM change data is discarded and will not be retained in the event that a new build
starts to reference the file.
