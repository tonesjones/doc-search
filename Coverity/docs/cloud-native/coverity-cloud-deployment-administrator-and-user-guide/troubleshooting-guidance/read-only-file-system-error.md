---
title: "Read-only file system error"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read-only-file-system-error.html"
content_id: "M17W7hrwpq4qEtaUcz_~gw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:54.854924+00:00"
---

# Read-only file system error

This section describes an issue where you execute a script or command such as
`db-tuning`, `cov-archive`,
`db-restore`, or try to write a file to either the
`cim-tools` pod or the `cnc-db-admin` pod, and a
Read-Only error is returned. Some volumes/paths are readOnly, therefore unable to
process write operations.

To solve this issue:

The 2025.6.0 release contains mounted data volumes, `/data` and
`/workdir`, that can be written by either Connect tools
(`/data`) or by a user (`/workdir`). The following
bullets provide information on these volumes:

- If you need to write files to a persistent volume in either the
  `cim-tools` pod or the `cnc-db-admin` pod, use
  `/workdir`:
  - The new `/workdir` volume mounted to the
    `cim-tools` pod and the `cnc-db-admin`
    pod, is a writable volume in which you can write and store files.
    Whenever you need to write any files into either
    `cim-tools` or `cnc-db-admin`, you
    must write the files to `/workdir`.
  - To perform a write operation in either a `cim-tools` pod or a
    `cnc-db-admin` pod, use the `/workdir`
    path.
- The `/data` volume is a persistent data volume, mounted to the
  `cim-tools` pod, that enables Connect tools software to write and
  read logs and other data. For a tool/script to write to a persistent volume in the
  `cim-tools` pod, use `/data`:
  - To mount `/data`, the
    `cim.cimtools.volume.enabled` Helm key must be
    `true`:

    ```
    cim:
      cimtools:
        volume:
          enabled: true
    ```
  - In the Helm chart, the persistent `/data` volume must be
    `readOnly: false`, For
    example:

    ```
    cim:
      containers:
        - name: cim-tools
          image: "cim-tools"  
          ...
          volumeMounts:
            - name: cimtools-data
              mountPath: /data/
              readOnly: false
    ```

    For further information about the
    persistent `/data` volume and Helm keys, see Create and mount a /data persistent volume and cim.cimtools.volume Helm keys: create and mount a /data volume.
