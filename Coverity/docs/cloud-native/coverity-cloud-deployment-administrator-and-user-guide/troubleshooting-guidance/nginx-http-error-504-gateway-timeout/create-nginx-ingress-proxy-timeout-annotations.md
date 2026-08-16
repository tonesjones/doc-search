---
title: "Create NGINX ingress proxy timeout annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-nginx-ingress-proxy-timeout-annotations.html"
content_id: "PE0utS6YPjNLXryiB3Rj6Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:49.391449+00:00"
---

# Create NGINX ingress proxy timeout annotations

To change the value using annotations, create the following annotations in the
`cnc` chart:

If Connect Web clients begin to experince HTTP error 504 issues while trying to access
scan results, you might need to increase the following timeout values to provide the
database adequate time to respond.

```
global:
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/proxy_body_timeout: <override-value>
      nginx.ingress.kubernetes.io/proxy_connect_timeout: <override-value>
      nginx.ingress.kubernetes.io/proxy_read_timeout: <override-value>
      nginx.ingress.kubernetes.io/proxy_send_timeout: <override-value>
```

The default timeout values (in seconds) as set in the NGINX ingress controller are:

```
global:
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/proxy_body_timeout: 60s
      nginx.ingress.kubernetes.io/proxy_connect_timeout: 60s
      nginx.ingress.kubernetes.io/proxy_read_timeout: 60s
      nginx.ingress.kubernetes.io/proxy_send_timeout: 60s
```

How much you increase the timeout value depends on whether the errors follow a period of
gradual performance decline, enabling you to make a small change, or following the
installation of a very large database, where you might want to make a large increase in
timeout value.

Important:

You must follow these conventions when setting NGINX ingress proxy timeout values:

- Valid units of measure are: s (seconds (default)) | m (minutes) | h (hours) | d
  (days)
- You must use a single unit of measure (90s, not 1m30s).
- The value must be a positive integer,
- The unit of measure must immediately follow the value; no space.

For example, the following have the same value:

```
..._timeout: "3600s"
..._timeout: "60m"
..._timeout: "1h"
```

The annotation examples below start with a very high timeout of one hour; you can adjust
the value once you have determined how much time is needed for your database replies.
This example adds the following annotations, using default units of seconds, to the
`cnc` Helm chart:

```
global:
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/proxy_body_timeout: 3600s
      nginx.ingress.kubernetes.io/proxy_connect_timeout: 3600s
      nginx.ingress.kubernetes.io/proxy_read_timeout: 3600s
      nginx.ingress.kubernetes.io/proxy_send_timeout: 3600s
```
