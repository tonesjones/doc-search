---
title: "Running cov-install-updates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-cov-install-updates.html"
content_id: "69u87263AZG7QIvdzcJ6sw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:23.154168+00:00"
---

# Running cov-install-updates

This section provides an overview of the `cov-install-updates` command.
For full details, see the `cov-install-updates` entry in the Coverity 2026.6.0 Command Reference.

The `cov-install-updates` utility is used to list and install
incremental updates. It can also be used to check if updates are available and to roll
back an undesired update.

To list the updates that are available for a given Coverity Analysis client, use the
`cov-install-updates list` command on that client and specify the
options necessary to connect to a Coverity Connect instance. Minimally, it is necessary
to provide hostname and port information (using the `--host` and
`--port` options) and login credentials. It is recommended to obtain
an access token from the Coverity Connect instance, and use that
(`--auth-key-file`) with your user name (`--user`), in
preference to a plaintext password (`--password`).

To install the available updates, use the `cov-install-updates install`
command, and again specify the required connection options.
