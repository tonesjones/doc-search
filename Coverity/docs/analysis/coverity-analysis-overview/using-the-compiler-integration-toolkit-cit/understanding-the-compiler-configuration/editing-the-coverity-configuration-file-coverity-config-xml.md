---
title: "Editing the Coverity configuration file—'coverity_config.xml'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/editing-the-coverity-configuration-file-coverity_config.xml-.html"
content_id: "s6ux6YJf1VtW1FYtcyDUeQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:09.083191+00:00"
---

# Editing the Coverity configuration file—'coverity_config.xml'

If a compiler cannot be successfully configured and the issues cannot be fixed in the
Compiler Integration Toolkit (CIT) configuration, you can modify the Coverity
configuration file, coverity_config.xml. Use the
`cov-configure --xml-option` option and add any of the  transformation
options. For more information about `cov-configure
--xml-option`, see `cov-configure` in the Coverity 2026.6.0 Command Reference.

For the most part, if they are correct, you do not need to edit the
`cov-configure` generated files. If there is an incompatibility
between your compiler and `cov-emit`, editing the configuration file
can be a short-term fix while Coverity improves compiler support in subsequent
releases.

All command-line manipulations in the generated configuration are defined with an
`<option>` tag. Each `<option>` tag lists
all of the automatically generated options, followed by an empty tag of the following
form:

```
<begin_command_line_config></begin_command_line_config>
```

You can add all additional command-line manipulations to the
`<option>` tag on the lines after the
`begin_command_line_config` entity. Do not put modifications inside
of the `begin_command_line_config` entity.
