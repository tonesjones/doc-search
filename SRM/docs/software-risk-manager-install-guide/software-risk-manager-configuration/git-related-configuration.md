---
title: "Git Related Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/git-related-configuration.html"
content_id: "kx~dtYLJkF9iwumqdBp5rA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:28.029564+00:00"
content_hash: "adfaaca68188dbf222c236f03bedfe8d1e6bc70f8e4709a1039bb612ecf20993"
---

# Git Related Configuration

Software Risk Manager allows you to configure each project to automatically use source
from a git repository as input for each analysis. When configuring a connection to a git
repository, Software Risk Manager will, by default, disallow the usage of “local” URLs
(i.e., URLs that point to a file in the Software Risk Manager file system). This is
enforced as a security measure to prevent system information exposure via the validation
user interface. Although it is strongly recommended that this setting be left disabled,
in the exceptional cases where it is necessary to use local git repositories, set the
`git.config.allow-local-urls` property to `true`.

When configuring a git repository connection, Software Risk Manager uses a request timeout
of 60 seconds by default. This timeout can be changed by setting a value for the
`git.config.timeout` property. For example, a value of
`2 minutes` changes the timeout to 2 minutes.

By default, Software Risk Manager automatically clones Git submodules during repository
clone operations. In rare cases where you experience "unknown commit" errors with submodules
that have commits not reachable from the default branch, you can disable submodule cloning
by setting the `git.clone.submodules` property to `false`.
**Note:** This is a global setting that applies to all Git repositories. When disabled,
submodules will not be cloned for any repository, which may result in incomplete source
code analysis. This setting should only be used as a temporary workaround while addressing
the underlying repository structure issue. The default value is `true`.
