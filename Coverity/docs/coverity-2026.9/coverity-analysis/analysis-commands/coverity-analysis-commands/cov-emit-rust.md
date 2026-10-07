---
title: "cov-emit-rust"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/cov-emit-rust.html"
content_id: "rkMZnyjF0UaGaM7vr5eXCw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:49.233577+00:00"
---

# cov-emit-rust

Parse Rust source code and emit output to the intermediate directory.

## Synopsis

```
cov-emit-rust 
    --dir <intermediate_directory> 
    [options]
```

## Description

The `cov-emit-rust` command parses source files in a Cargo project in
the current working directory and saves the output to the `emit`
repository within the intermediate directory. `cov-build` invokes
`cov-emit-rust` automatically when Rust (Cargo) build capture is
configured. Users do not typically invoke it directly.

## Options

| Option | Required | Required |
| --- | --- | --- |
| `--dir <intermediate_dir>` | Yes | Specifies the intermediate directory for emitted source files. Returns an error if the directory cannot be created. |
| `--build` | No | Build the cargo project in the current working directory. |
| `<Cargo.toml>` | No | Specifies the intermediate directory for emitted source files. Returns an error if the directory cannot be created. |
| `<path to any rust source file>` | No | Any Rust source files in subdirectories. The current working directory contains a Cargo.toml. |

Note:

- `cov-build` invokes `cov-emit-rust`
  automatically when `cov-configure --cargo` or
  `cov-configure --rustc` has been run. Direct invocation
  is not required.
- `--build`, `Cargo.toml`, or path to Rust
  source file must be specified.

## Exit codes

- 0: Task completed successfully
- 1: Task completed, but no results found
- 2: Task failed (includes error message and remediation advice)
- 4: Unexpected error; task likely incomplete

## Related information

- cov-build- Invokes `cov-emit-rust`
  automatically during Cargo build capture
- cov-configure- Run this command before using
  `cov-build` for Rust projects

**Related information**  

- cov-build
- cov-configure
