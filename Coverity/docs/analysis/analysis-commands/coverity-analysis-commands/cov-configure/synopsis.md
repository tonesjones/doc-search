---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "mU_XogVTidM0EzBygd_Xwg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:15.945563+00:00"
---

# Synopsis

**Apex:**

```
cov-configure 
   [--config <cov_config_file>] 
   --apex
   [SHARED_OPTIONS]
```

**CUDA (nvcc):**

```
cov-configure 
   [--config <cov_config_file>] 
   --cuda
   [SHARED_OPTIONS]
```

**Clang:**

```
cov-configure 
   [--config <cov_config_file>] 
   --clang
   [SHARED_OPTIONS]
```

**Dart:**

```
cov-configure
   [--config <cov_config_file>] 
   --dart
   [--no-capture-config-files]
   [SHARED_OPTIONS]
```

**Go:**

```
cov-configure 
   [--config <cov_config_file>] 
   --go
   [SHARED_OPTIONS]
```

**GNU C/C++ compiler (gcc/g++):**

```
cov-configure 
   [--config <cov_config_file>] 
   --gcc
   [SHARED_OPTIONS]
```

**Java buildless capture:**

```
cov-configure 
   [--config <cov_config_file>] 
   --java-buildless 
   [--no-capture-config-files] 
   [--no-android] 
   [--no-jsp]
   [SHARED_OPTIONS]
```

**JavaScript:**

```
cov-configure 
   [--config <cov_config_file>] 
   --javascript 
   [--no-html] 
   [--no-jsx] 
   [--no-typescript] 
   [--no-vue] 
   [--no-capture-config-files]
   [--fs-library-path path1 [--fs-library-path path2 ...]]
   [SHARED_OPTIONS]
```

**Kotlin:**

```
cov-configure 
   [--config <cov_config_file>] 
   --kotlin 
   [--no-capture-config-files]
   [SHARED_OPTIONS]
```

**Microsoft C/C++ compiler (cl):**

```
cov-configure 
   [--config <cov_config_file>] 
   --msvc
   [SHARED_OPTIONS]
```

**Microsoft C# compiler (csc):**

```
cov-configure 
   [--config <cov_config_file>] 
   --cs
   [SHARED_OPTIONS]
```

Note: If your system uses .NET to compile C#,
`cov-configure` correctly sets up that environment.

**Microsoft Visual Basic compiler (vbc):**

```
cov-configure 
   [--config <cov_config_file>] 
   --vb
   [SHARED_OPTIONS]
```

Note: If your system uses .NET to compile Visual Basic,
`cov-configure` correctly sets up that environment.

**Oracle Java compiler (javac):**

```
cov-configure 
   [--config <cov_config_file>] 
   --java 
   [--no-capture-config-files] 
   [--no-android] 
   [--no-jsp]
   [SHARED_OPTIONS]
```

**PHP:**

```
cov-configure 
   [--config <cov_config_file>] 
   --php 
   [--no-capture-config-files]
   [SHARED_OPTIONS]
```

**Python:**

```
cov-configure 
   [--config <cov_config_file>] 
   --python 
   [--no-capture-config-files] 
   [--version 3]
   [SHARED_OPTIONS]
```

**Ruby:**

```
cov-configure 
   [--config <cov_config_file>] 
   --ruby
   [SHARED_OPTIONS]
```

**Rust:**

```
cov-configure 
   [--config <cov_config_file>] 
   --rust
   [SHARED_OPTIONS]
```

**Scala:**

```
cov-configure 
   [--config <cov_config_file>] 
   --scala 
   [--no-capture-config-files]
   [SHARED_OPTIONS]
```

**TypeScript:**

```
cov-configure 
   [--config <cov_config_file>] 
   --typescript 
   [--no-html] 
   [--no-jsx] 
   [--no-javascript] 
   [--no-vue] 
   [--no-capture-config-files] 
   [--fs-library-path path1 [--fs-library-path path2 ...]]
   [SHARED_OPTIONS]
```

**Other compiler:**

```
cov-configure 
   [--config <cov_config_file>] 
   [--template]
   --compiler <name> 
   --comptype <type> 
   [--version <comp_version>]
   [--cygpath <path>] 
   [--cygwin] 
   [--force]
   [--xml-option=[tag][@<language>]]
   [SHARED_OPTIONS]
```

**Buildless capture with custom file pattern:**

```
cov-configure 
   [--config <cov_config_file>] 
   --comptype <type>
   (--file-glob <glob>|--file-regex <regex>)
   [--xml-option=[tag][@<language>]]
   [SHARED_OPTIONS]
```

**[SHARED_OPTIONS]**:

```
    [--debug]
    [--ident]
    [--info]
    [--redirect stdout|stderr,<filename>]
    [--tmpdir <tmp>]
    [--verbose <level>]
```
