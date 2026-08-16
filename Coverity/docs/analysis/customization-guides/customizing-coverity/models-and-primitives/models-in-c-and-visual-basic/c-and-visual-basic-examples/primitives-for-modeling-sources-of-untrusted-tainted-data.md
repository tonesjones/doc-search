---
title: "Primitives for modeling sources of untrusted (tainted) data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/primitives-for-modeling-sources-of-untrusted-tainted-data.html"
content_id: "2FUU9gjjHTKmA_qst7gpWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:45.214241+00:00"
---

# Primitives for modeling sources of untrusted (tainted) data

The following C# and Visual Basic security primitives model untrusted
data sources:

| No parameter | Parameter |
| --- | --- |
| `Security.HttpSource()` | `Security.HttpSource(Object)` |
| `Security.HttpMapValuesSource()` | `Security.HttpMapValuesSource(Object)` |
| `Security.NetworkSource()` | `Security.NetworkSource(Object)` |
| `Security.DatabaseSource()` | `Security.DatabaseSource(Object)` |
| `Security.FileSystemSource()` | `Security.FileSystemSource(Object)` |
| `Security.ConsoleSource()` | `Security.ConsoleSource(Object)` |
| `Security.EnvironmentSource()` | `Security.EnvironmentSource(Object)` |
| `Security.SystemPropertiesSource()` | `Security.SystemPropertiesSource(Object)` |
| `Security.RpcSource()` | `Security.RpcSource(Object)` |
| `Security.CookieSource()` | `Security.CookieSource(Object)` |

As the table shows, each primitive is one of a pair. The primitives that do not take an
argument model a method that returns a string-like or simple collection object: analysis
treats this object as tainted data. The primitives that take an `Object`
argument model a method that taints a string-like or simple collection parameter,
presumably by inserting a tainted string or sequence of characters into it. The
primitive argument must be one of the modelled method's parameters.

Each variant corresponds to a particular taint type that can be trusted or distrusted
using the `cov-analyze`
command's `trust` or `distrust` command-line options;
for example, `--trust-http` and `--distrust-http`. These options
are described in the Coverity 2026.6.0 Command Reference.
