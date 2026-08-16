---
title: "Using a network file system (NFS) with Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-a-network-file-system-nfs-with-coverity-analysis.html"
content_id: "L22SGvVAlR8S5pMhO8ttVA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:26.481357+00:00"
---

# Using a network file system (NFS) with Coverity Analysis

NFS is supported for use with Coverity Analysis in many cases. Support is the same for
all Coverity commands.

For all operating systems:

- Source code, native compilers, and native build system files (for example, Makefiles) may
  reside on NFS.
- User and derived model files may reside on NFS.

  See Customizing Coverity
  for details about models.

For Unix-like operating systems only (not Windows, no Windows clients):

- The Coverity intermediate directory can reside on NFS. However, for performance reasons, the
  local disk is recommended (see The intermediate directory).

  For
  parallel builds, Coverity provides specific recommendations that involve the use
  of NFS (see Running parallel builds). See also the
  `--capture` option to
  `cov-build` in Coverity 2026.6.0 Command Reference for additional guidance.
- The Coverity Client tools (Coverity Analysis and Coverity Desktop) may be installed on
  NFS.
- Compiler configuration files in the <install_dir>/config directory
  (`-c` argument) may reside on NFS.
