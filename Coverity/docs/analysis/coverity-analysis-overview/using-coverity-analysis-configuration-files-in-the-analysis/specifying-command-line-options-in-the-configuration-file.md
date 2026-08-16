---
title: "Specifying command-line options in the configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-command-line-options-in-the-configuration-file.html"
content_id: "Fdv0QBOqckvnhrw7YRC31A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:00.052166+00:00"
---

# Specifying command-line options in the configuration file

Instead of passing command-line options to Coverity Analysis on the
command line, it is possible to pass command-line options to Coverity Analysis through a Coverity Analysis
configuration file. However, note that the options that you specify on the command line
take precedence over those that you specify in a configuration file.

Coverity Analysis commands point to a Coverity Analysis
configuration file by using the following command line option:

```
--config path/to/XML/config/file
```

A number of Coverity Analysis commands (including `cov-configure`, `cov-build`, `cov-analyze`, `cov-commit-defects`,
and `cov-make-library`) support this option. For others, check
Coverity 2026.6.0 Command Reference.

To construct the option tags in the configuration file, refer to the following general
rules:

- **Options without arguments**

  A command instruction, such as the
  `--return-emit-failures` option. The XML configuration tag
  for such an option replaces each inter-word dash (-) with an underscore (_), for
  example, `<return_emit_failures>`. In the XML file, you set
  this tag's value to `true` to enable it. You delete the tag from
  the XML file to remove the option.
- **Single-specified options with arguments**

  An option that you can submit only once on
  the command line or in a single configuration file. For example, the
  `--dir` option specifies the intermediate directory location.
  On the command line, you can specify this option as `--dir
  <intermediate_directory>`. In XML, it is specified as
  `<dir>intermediate_directory</dir>`. If multiple
  configuration files contain a `dir` entity, Coverity Analysis uses the value from the first-specified
  file.
- **Multiple-specified options with arguments**

  Options that can be submitted
  more than once on the command line or in a configuration file. The only
  difference from single-specified options is that when multiple options appear
  across multiple configuration files, Coverity Analysis uses all
  the values. For example, the `--disable checker` option instructs
  `cov-analyze` to turn off one or more checkers.

In this section:

- Using the <cim> tag to specify commit options
- Using the <prevent> tag to specify directories and emit options
