---
title: "Compiler configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-configuration.html"
content_id: "NOWuUk50hIv0y69jJuIN0A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:27.021402+00:00"
---

# Compiler configuration

Use the --compiler-config-file option to specify a custom compiler configuration to use.

You can use this option with the `capture`, `list`, and
`scan` subcommands. The option works with the
`list` subcommand because compiler configurations can be used to
change the way that source files are identified.

For C/C++ source, the Coverity CLI automatically configures for the following compilers: gcc, MSVC, Clang.
If your project uses a different compiler, or invokes one of these compilers using a non-standard name, then a custom configuration is needed.
Otherwise, the automatic configuration is sufficient and you don't need to use --compiler-config-file.

**Syntax**

```
--compiler-config-file file
```

The file argument contains the desired compiler configuration.
