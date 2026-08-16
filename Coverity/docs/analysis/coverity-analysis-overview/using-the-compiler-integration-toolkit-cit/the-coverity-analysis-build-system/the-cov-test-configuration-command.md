---
title: "The 'cov-test-configuration' command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-test-configuration-command.html"
content_id: "Kc85F_7e3FoXeCS0PEjL8w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:00.488596+00:00"
---

# The 'cov-test-configuration' command

The `cov-test-configuration` command is used to test command-line
translations of a configuration by making assertions about the translations. It parses
an input script and confirms that the commands are true or false.

**Example:**

```
cov-configure --config myTest/coverity_config.xml --msvc
cov-test-configuration --config myTest/coverity_config.xml MyTests.json
```

Output of the cov-test-configuration example:

```
Section [0] My Section Label
Tests run: 1, Failures: 0, Errors: 0
Sections run: 1, Tests run: 1, Failures: 0, Errors: 0
```

Examples of the format to use are found at
<install_dir>/config/templates/*/test-configuration.*.json
for the supported compilers.
