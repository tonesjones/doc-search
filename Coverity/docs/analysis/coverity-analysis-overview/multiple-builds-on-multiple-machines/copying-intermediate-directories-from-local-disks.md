---
title: "Copying intermediate directories from local disks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/copying-intermediate-directories-from-local-disks.html"
content_id: "g5MQ~9GKTBYhsbU_kFKuQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:17.163318+00:00"
---

# Copying intermediate directories from local disks

To distribute a build:

1. Run `cov-build` once on each server to initialize an intermediate directory
   on a local disk used only by that build
   server:

   ```
   cov-build --dir <intermediate_directory> --initialize
   ```
2. Run one or more `cov-build`, `make`, or equivalent command
   per build
   server:

   ```
   cov-build --dir <intermediate_directory> --capture make [-j N]
   make [-j N] CC="cov-translate ..."
   ```

   The `--capture`
   option ensures that `cov-build` log and metric files are merged
   and not replaced.
3. Complete the build(s) on each build
   server:

   ```
   cov-build --dir <intermediate_directory> --finalize
   ```
4. Copy the complete intermediate directory tree from each build server to a local disk on the
   machine on which you will run `cov-analyze`.

   For example:

   - Use a remote-copy utility such as `scp -r`.
   - Use an NFS partition or network file share.
5. Merge the intermediate directory that was copied from each build server with the intermediate
   directory that you want to
   analyze:

   ```
   cov-manage-emit --dir <copied_directory> reset-host-name
   ```

   ```
   cov-manage-emit --dir <intermediate_directory> add <copied-directory>
   ```

   After
   the build finalizes, and the indicated commands run, the
   <intermediate_directory> is ready for
   analysis.
