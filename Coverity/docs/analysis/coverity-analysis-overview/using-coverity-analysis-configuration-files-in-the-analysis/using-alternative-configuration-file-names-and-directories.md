---
title: "Using alternative configuration file names and directories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-alternative-configuration-file-names-and-directories.html"
content_id: "ytdHgok2R0C4gbTzXur7jw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:59.411491+00:00"
---

# Using alternative configuration file names and directories

If you install Coverity Analysis in a read-only location, Coverity Analysis will not be
able to use the <install_dir>/config directory. To specify an
alternative configuration file directory (or configuration file name), you can use the
`--config` option to the `cov-configure` command.
For example:

```
> cov-configure --config /var/coverity/config/coverity_config.xml \
   --comptype gcc --compiler gcc
```

You need to be able to create sub-directories relative to the directory that contains
coverity_config.xml.

To use an alternative name for the configuration file (for example,
coverity_foobar.xml) and then use that file name for each step
in the analysis, you need to complete *one* of the following tasks:

- Use the `--config` option when running Coverity Analysis
  commands.
- If recommended by Coverity support, set the COVERITY_CONFIG environment variable
  to point to the directory that contains the configuration file.
- Move coverity_config.xml and any other directories generated
  by the configuration to ~/.coverity. (Note that this is a
  local configuration that applies only to you.)

Note: If you need to move the configuration after it is generated, you must move the entire
configuration file directory and all of its sub-directories.
