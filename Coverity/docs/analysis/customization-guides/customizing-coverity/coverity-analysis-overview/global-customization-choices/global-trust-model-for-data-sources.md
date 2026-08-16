---
title: "Global trust model for data sources"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/global-trust-model-for-data-sources.html"
content_id: "ZurgECya9GTSCyK4BBryKA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:09.389512+00:00"
---

# Global trust model for data sources

The application-wide trust model can classify various kinds of data sources as either
trusted, or mistrusted and potentially malicious.

The kinds of data sources you can specify include HTTP requests, filesystems, remote
procedure calls, databases, HTTP headers, and more.

**Use case:** Specify a publicly accessible disk as a mistrusted source of data.

The application to analyze reads arbitrary data from a network disk that untrusted users
also share. Use the `cov-analyze` option
`--distrust-filesystem` to specify that the network disk is not
trusted.

Important:
In general, specifying trust at the global level is something that should be done only
*once,* when a project is first deployed.

**Limitations and alternatives:** The global trust options turn entire categories of
data sources on or off. There are ways to refine the granularity of the classification,
as shown in the following list:

- Many of the built-in dataflow checkers have checker-specific trust models (most
  these have names that begin with TAINT_ or
  TAINTED_; also see the SQLI and XSS checkers). These
  inherit from the global trust model but allow it to be overridden in individual
  cases. These overrides are exposed as checker options. See individual checker
  descriptions for details.
- To change the trust setting of individual data sources when a checker-specific
  alternative is not available, use API models or security analysis directives,
  instead. See Choices that depend on the
  checker, the language, or other contexts.

**Learn more:**
See Identifying Vulnerable Data.
Also, in the `cov-analyze`
section of the Coverity 2026.6.0 Command Reference,
there are descriptions of a whole family of complementary options whose name begins with
either `--distrust-` or `--trust-`, followed by the name
of the data source category to globally mistrust or trust.
