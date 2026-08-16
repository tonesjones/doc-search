---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "PhgT43kMnIlJvmioEko7Ow"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:44.711254+00:00"
---

# Synopsis

```
cov-manage-emit --dir <intermediate_directory> [GENERAL OPTIONS]
          <COMMANDS> <COMMAND OPTIONS> 
          [SHARED_OPTIONS]
```

**GENERAL OPTIONS:**

```
   [ --apex | --cpp | --cs | --cuda | --dart | --fortran | --go | --java | --javascript | --kotlin | --objc |--php |--python2 | --python 3 | --ruby | --rust | --scala | --swift | --text-files | --typescript | --vb]
   [--case-normalized-filename]
   [--preprocess-native]
   [--ticker-mode <mode>]
   [--tu <tu_ids> | --tu-pattern <pattern>] 
   [--tus-per-psf <value>]
```

**COMMANDS and COMMAND OPTIONS:**

```
   [add-other-hosts | check-integrity | delete-source | list-builds | repair | reset-host-name]
   [add <int_dir> | link-file <out_file>] | list | list-capture-invocations | list-json
   [decompile-binary-tus-from-dir <decompile_options>]
   [extract-files --output-dir <dir> [--strip-path <path>]... {--regex <regex> | <filename>...}]
   [{recompile | retranslate | retranslate-or-emit} <recompile_options>]
   [find [OPTIONS]]
   [list-compiled-classes]
   [export-json-build [OPTIONS]]
   [import-json-build [OPTIONS]]
   [list-json-schema-versions]
```

**SHARED
OPTIONS:**

```
   [--config <coverity_config.xml>]
   [--debug]
   [--help]
   [--info]
   [--tmpdir <tmp>]
   [--verbose <level>]
```
