---
title: "Using Coverity Analysis configuration files in the analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-coverity-analysis-configuration-files-in-the-analysis.html"
content_id: "3CTMdQ91JEEvcH~~5QtyvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:58.767759+00:00"
---

# Using Coverity Analysis configuration files in the analysis

As discussed in The configuration, the `cov-configure`
command generates a compiler configuration file. Though not typically recommended
without the help of Coverity Support (open a Support case by logging in to the [Black Duck Community site](https://community.blackduck.com/s/contactsupport)),
you can modify the file in following ways to support your analyses:

**Using the `<include>` tag set to include additional configuration
files**

- You might do so to partition your configuration by organization, project,
  individual, or other classification. For information about this tag set, see
  The configuration.

**Specifying command-line options**

- You can specify Coverity Analysis command-line options explicitly on the command
  line or through one or more XML-based configuration files. See Specifying command-line options in the configuration file.
  Coverity Analysis searches for coverity_config.xml in all
  configuration directories that are specified in the include tags. See Using the <prevent> tag to specify directories and emit options.

**Specifying Coverity Analysis directories and emit options**

- You can specify the temporary and intermediate directory and emit options (for
  example, to `cov-emit` and `cov-emit-java`) )
  within the prevent tag set. For details, see Using the <prevent> tag to specify directories and emit options.

**Specifying options used to commit analysis results to Coverity Connect**

- You can specify options to `cov-commit-defects` within the
  commit tag set. The tags go in the master configuration file. For details, see
  Using the <cim> tag to specify commit options.

**Changing the name and/or location of coverity_config.xml**

- By default, Coverity Analysis creates coverity_config.xml
  file in the following location: <install_dir>/config.
  If you need to change the file name or location, see Using alternative configuration file names and directories.

Note that if you modify configuration files in ways that violate the DTD description
(found in coverity_config.dtd), most Coverity Analysis commands
will issue a warning.

Also note that **COVLKTMPDIR** and environment variable names
starting with **COV_** or **COVERITY** are
reserved. Users should not set them unless directed to do so by Coverity support
staff.

In this section:

- Using alternative configuration file names and directories
- Specifying command-line options in the configuration file
