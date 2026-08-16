---
title: "Options: Brakeman checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-brakeman-checkers.html"
content_id: "ZEo9g374HBEx6HvBlAUZRQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:35.097761+00:00"
---

# Options: Brakeman checkers

--brakeman-aggressiveness-level <low|medium|high>
:   Tune the aggressiveness of Brakeman Pro to only report defects that are above
    a certain confidence level. A higher setting reports more defects and
    increases the likelihood that any given defect is a false positive. Accepted
    values for this option are `low`, `medium`, or
    `high`. Default is `high`.

--disable-brakeman
:   Disables Brakeman Pro checkers. Use the `--enable-brakeman`
    option to re-enable these checkers.

--enable-brakeman
:   Enables Brakeman Pro checkers (default). Use
    `--disable-brakeman` to disable these checkers.
