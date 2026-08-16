---
title: "Rust compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/rust-compilers.html"
content_id: "6VjDTGUfKYorSOa2g4dZog"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:15.188728+00:00"
---

# Rust compilers

Note: Rust language support is a beta feature in the 2026.6 release.
Do not use it in production. Coverity Analysis for Rust supports projects built with
the Cargo build system.

Table 1. Supported compilers: Coverity Analysis for Rust

| Compiler | Compiler version | Host OS | Notes |
| --- | --- | --- | --- |
| Cargo (Rust stable toolchain) | 1.92.0 | Linux (64-bit)/Linux ARM64 | - Only projects built using `cargo` are captured.   Projects that invoke `rustc` without cargo are   not supported. - This feature supports Rust Edition 2021 and 2024. |
| macOS |
| Windows (64-bit) |
