---
title: "Downloading the Helm chart from the Black Duck public Docker registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-the-helm-chart-from-the-black-duck-public-docker-registry.html"
content_id: "l~U1~DNFxJrCMV16ZPMlfA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:33.128298+00:00"
---

# Downloading the Helm chart from the Black Duck public Docker registry

This section describes how to download the default Helm chart from the Black Duck
public Docker registry using either the `curl` command.or a web
browser.

## What file do you download?

From the Black Duck public Docker registry, you will download the following file
for your release:

```
cnc-<version>.tgz
```

where `<version>` is `<year.major.minor>`

For example, for 2026.6.0:

```
cnc-2026.6.0.tgz
```

Important:

Do NOT download files with -x (for example, -0 or -1) appended to the
filename.

## Download using `curl`

To download the default Helm chart from the Black Duck public Docker registry using
the `curl` command at a Linux prompt:

```
curl https://repo.blackduck.com/cloudnative/cnc-2026.6.0.tgz -o cnc-2026.6.0.tgz
```

## Download using a Web browser

To download the default Helm chart from the Black Duck public Docker registry using
a Web browser:

1. In a browser, open the Black Duck public Docker registry at <https://repo.blackduck.com>>.
2. Navigate to cloudnative.
3. Click on the `cnc-<version>.tgz` link to download the
   `.tgz` file.

## Extract the `.tgz` file

Extract the `.tgz` file. The file extracts to a `cnc`
directory that contains

- a `values.yaml` file
- `Chart.yaml` file
- a `/templates` directory that contains many
  `cim-`,
- `cnc-`
- other `.yaml` files
- scan-services subchart

These files make up the Helm chart.
