---
title: "CPAN Support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/cpan-support.html"
content_id: "ZAXidkE_o4XQuBzXK85iLw"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:52.666737+00:00"
---

# CPAN Support

## Related properties

Detector properties

## Overview

The CPAN detector will run if it finds a Makefile.PL file.

The detector requires the following executables:

- cpan - used to determine the list of direct dependencies required by the project.
- cpanm - used to assign versions to the dependencies found by cpan by determining the list of Perl modules installed on the system.

When executing the cpan command, Detect will set the PERL_MM_USE_DEFAULT environment variable to true. This ensures that if cpan has not been configured on the system before, default configuration settings will be accepted.

The CPAN detector reports only direct dependencies and not transitive ones.
