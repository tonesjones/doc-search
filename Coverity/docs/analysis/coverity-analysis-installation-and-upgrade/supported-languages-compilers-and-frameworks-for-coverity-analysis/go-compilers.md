---
title: "Go compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/go-compilers.html"
content_id: "bYEtyM7YATepx2BXVC47EA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:13.229957+00:00"
---

# Go compilers

Table 1. Supported compilers: Coverity Analysis for Go

| Compiler | Compiler version | Host OS | Notes |
| --- | --- | --- | --- |
| Go | 1.25-1.26 | Linux (64-bit)/Linux ARM64 | Coverity only supports projects that are built with the following commands: `go build`, `go install`, `go run`, and `go test`. Coverity does not support projects that are built by invoking either `go tool compile` or `gccgo` directly.  Coverity does not directly recognize custom flags and arguments of go run or go test. In order for Coverity to recognize these custom flags and arguments, you must modify `config/templates/go/go_switches.dat`.  The `cov-emit-go` command might have dependencies on external tools, depending on the Go code being compiled. Refer to the `cov-emit-go` command in the *Coverity Command Reference* for details.  **Deprecation Notice:** Support for Go 1.25 deprecated as of 2026.6 and will be removed in a future release. |
| macOS |
| Windows (64-bit) |
