---
title: "CPAN Support"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/cpan-support.html"
content_id: "ZAXidkE_o4XQuBzXK85iLw"
version: "12.0.0"
section: "Package Manager information for Detect"
scraped_at: "2026-10-04T23:33:20.477564+00:00"
content_hash: "35ee8b0dd4db7c3d7d42f5b47de4dddcd0b27d73224c09f53c90a9cd044067df"
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
