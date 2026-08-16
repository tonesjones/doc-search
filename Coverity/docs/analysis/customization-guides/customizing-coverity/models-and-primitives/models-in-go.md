---
title: "Models in Go"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-in-go.html"
content_id: "pN0OdNZvILxy5iHUIPFDRw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:49.997983+00:00"
---

# Models in Go

This section describes how to write custom models for Go code, and the available
modeling primitives.

Note: User written models for Go are deprecated as of 2026.3.0.

To create models for Go programs, follow the overall steps in Adding a custom model.

The primitives for Go are part of the `blackduck.com/coverity-primitives`
namespace. Coverity Analysis provides an assembly that contains the
primitives in <install_dir>/library/go/src/blackduck.com/coverity-primitives/primitives.go.

Important: For the Go model to be applied correctly, the namespace name, class name, number and
names of type parameters, method name, method parameter types, and return type must all
match those of the function being modeled.
