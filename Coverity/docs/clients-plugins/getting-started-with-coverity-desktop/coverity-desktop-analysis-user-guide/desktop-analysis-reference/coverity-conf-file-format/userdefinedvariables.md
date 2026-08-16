---
title: "UserDefinedVariables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/userdefinedvariables.html"
content_id: "jbIzWOqYHMgZaYHESaEv2Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:14.566163+00:00"
---

# UserDefinedVariables

`UserDefinedVariables` contains user defined variable names that can be
defined to specific values. These defined variable names are expanded in strings (See
Table 1 for details).

The `variables` property is a top-level property in the configuration
file, and is unconditionally evaluated. Variables may be referenced in the expression
associated with `a regex_matches_string` condition for a conditional
settings block.

If a variable is defined in both a
project-specific coverity.conf file as well as
the coverity.conf file in the user's home directory, the
value in the user-specific file takes precedence. In addition, this process is applied
on a per-variable basis, so a user only needs to define values in the user-specific file
which they intend to override.
