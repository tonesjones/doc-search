---
title: "Sharing a common intermediate directory on an NFS partition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sharing-a-common-intermediate-directory-on-an-nfs-partition.html"
content_id: "~~GsfTahVUANLVt1JUKYuQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:16.514067+00:00"
---

# Sharing a common intermediate directory on an NFS partition

To distribute a build:

1. Run `cov-build` once without a build command to initialize the intermediate
   directory:

   ```
   cov-build --dir <intermediate_directory> --initialize
   ```
2. Run one or more `cov-build`, `make`, or equivalent command
   per host
   machine:

   ```
   cov-build --dir <intermediate_directory> --capture make [-j N]
   make [-j N] CC="cov-translate ..."
   ```

   The `--capture`
   option ensures that `cov-build` log and metric files are merged
   and not replaced.
3. Combine the log and metrics files from all contributing hosts, and identify any commands that
   need to be run on the machine that is used for subsequent
   analyses:

   ```
   cov-build --dir <intermediate_directory> --finalize
   cov-manage-emit --dir <intermediate_directory> add-other-hosts
   ```

   After
   the build is finalized, and the indicated commands run, the
   <intermediate_directory> is ready for analysis.
   The `cov-manage-emit` command must run after a distributed
   build to aggregate the data captured on other hosts, and on the host machine
   that will run the `cov-analyze` command.
