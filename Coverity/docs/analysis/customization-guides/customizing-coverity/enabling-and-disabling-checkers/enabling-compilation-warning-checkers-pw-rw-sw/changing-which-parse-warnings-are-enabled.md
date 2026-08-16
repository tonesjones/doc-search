---
title: "Changing which parse warnings are enabled"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-which-parse-warnings-are-enabled.html"
content_id: "knxEJxH5cT~gDI1s1UNfsQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:18.505463+00:00"
---

# Changing which parse warnings are enabled

Use these steps to manage enablement of C/C++ parse warning checkers.

1. Copy the parse_warnings.conf.sample file and save it with a new name.
2. Edit the copy of the configuration file.

   - Remove comment characters before the default directives that you want to use.
   - Add directives for checkers that you want enable or disable.
3. Run the `cov-analyze` command, specifying both the `--enable-parse-warnings`
   and the `--parse-warnings-config <config_file>` options.

   Here, `<config_file>` is the name of your own, customized configuration file,
   including a full or a relative path.

   To enable the parse warning checkers using a configuration file named
   my_parse_warnings.conf, use the following command
   line:

   ```
   cov-analyze --enable-parse-warnings --parse-warnings-config my_parse_warnings.conf
   ```
