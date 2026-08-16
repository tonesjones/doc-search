---
title: "Auto-configuring compilers for the QNX and WindRiver toolchains"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/auto-configuring-compilers-for-the-qnx-and-windriver-toolchains.html"
content_id: "XwLsY_oSZiYURopxA9RESw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:54.667871+00:00"
---

# Auto-configuring compilers for the QNX and WindRiver toolchains

For the QNX and WindRiver toolchains, it is convenient to automatically configure the
compilers by using coverity.conf.

In coverity.conf, you can add a
`add_compiler_configurations` element to the
`settings` section.

For more information, see the Coverity
Desktop Analysis
2026.6.0 User Guide.

**For QNX:**

```
"add_compiler_configurations": [
  { "cov_configure_args": ["--template", "--compiler", "qcc", "--comptype", "qnxcc"] }
]
```

**For WindRiver:**

```
"add_compiler_configurations": [
  { "cov_configure_args": ["--template", "--compiler", "ccmips", "--comptype", "gcc"]},
  { "cov_configure_args": ["--template", "--compiler", "ccpentium", "--comptype", "gcc"]},
  { "cov_configure_args": ["--template", "--compiler", "ccppc", "--comptype", "gcc"]},
  { "cov_configure_args": ["--template", "--compiler", "c++arm", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "cpparm", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "g++arm", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "c++mips", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "cppmips", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "g++mips", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "c++pentium", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "cpppentium", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "g++pentium", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "c++ppc", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "cppppc", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "g++ppc", "--comptype", "g++"]},
  { "cov_configure_args": ["--template", "--compiler", "dcc", "--comptype", "dcc"]}
]
```

Note: If the user has a data-coverity folder in their workspace, the
`"add_compiler_configurations"` setting will not take effect. To
correct this issue, delete the data-coverity folder.
