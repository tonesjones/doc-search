---
title: "Upgrade considerations for 2024.12"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2024.12.html"
content_id: "qSkeoPc7_7Zq94NsqARYpw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:50.204351+00:00"
---

# Upgrade considerations for 2024.12

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see "Coverity 2024.12.0 Release Notes" (and the sections for associated hot
fixes) in the Coverity 2026.6.0 Release Notes Archive.

For the list of Sigma checkers disabled by default when running Coverity Analysis
2024.12, see ["Checkers disabled in Sigma when running Coverity
Analysis"](https://documentation.blackduck.com/bundle/coverity-docs-2024.12/page/checker-ref/checkers/S/sigma._checkers.html#d100634e144) in the [*Coverity 2024.12.0 Checker
Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2024.12/page/webhelp-files/checkerref_start.html).

CAUTION:

When you upgrade Coverity Analysis, all previous
settings are overwritten. All checkers listed in the [" Sigma checks disabled by default in Coverity
2024.12"](https://documentation.blackduck.com/bundle/coverity-docs-2024.12/page/checker-ref/checkers/S/sigma._checkers.html#SIGMA_checkers__section_disabled_sigma_checkers) table in the [*Coverity 2024.12.0 Checker Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2024.12/page/webhelp-files/checkerref_start.html)
will be disabled by default in Coverity Analysis 2024.12, regardless of their enablement
status in previous installations.

## Change in registry/repository

Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the
new URL, <https://repo.blackduck.com/>.

Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor
of <https://updates.lic.blackduck.com>.

Customers should also add the new URL, <https://repo.blackduck.com/> and IP address
(34.110.245.127) to the allowed list.

Support for the deprecated URLs will be removed on March 1st, 2025.
