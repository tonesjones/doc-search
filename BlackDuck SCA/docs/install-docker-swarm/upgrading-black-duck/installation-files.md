---
title: "Installation files"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/installation-files.html"
content_id: "2vCdIjISnG7JEOCPtup2wg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.755323+00:00"
content_hash: "e94af1a381cb85408f069e30b2184a1e646098daf5782bbf5f64282a8b3ba4da"
---

# Installation files

The installation files are available on GitHub.

Download the orchestration files. As part of the install/upgrade process, these orchestration files pull down the necessary Docker images.

Note that although the filename of the `tar.gz` file differs depending on how you access the file, the content is the same.

## [HUB-13466]Download from the GitHub page

1. Select the link to download the `.tar.gz` file from the GitHub page: <https://github.com/blackducksoftware/hub>.
2. Uncompress the Black Duck`.gz` file:

   ```
   gunzip hub-2026.7.1.tar.gz
   ```
3. Unpack the Black Duck`.tar` file:

   ```
   tar xvf hub-2026.7.1.tar
   ```

## Download using the wget command

1. Run the following command:

   ```
   wget https://github.com/blackducksoftware/hub/archive/v2026.7.1.tar.gz
   ```
2. Uncompress the Black Duck`.gz` file:

   ```
   gunzip v2026.7.1.tar.gz
   ```
3. Unpack the Black Duck`.tar` file:

   ```
   tar xvf v2026.7.1.tar
   ```
