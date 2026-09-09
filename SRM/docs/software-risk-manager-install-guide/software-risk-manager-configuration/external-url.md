---
title: "External URL"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/external-url.html"
content_id: "zixIHJGyjQoXdIjVsH0vVg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:20.930869+00:00"
content_hash: "ca853155ff1b6fcf43fbc3c380ce8a2eef884d70d6abe61afd8e743c646ec184"
---

# External URL

In most cases, Software Risk Manager can infer its own external URL based on the requests
sent to it from users. For example, you might access Software Risk Manager from
`https://localhost/codedx` or
`https://codedx.mycompany.com`. This information is necessary for
some subprocesses of Software Risk Manager that need to communicate back to Software
Risk Manager over HTTP, or to provide accurate links back to Software Risk Manager when
generating content—Issue Trackers, for example.

In some cases, the accurate "external URL" may not be available through inspection of
user requests. When this happens, the value must be provided from your
*codedx.props* file via the `codedx.external-url` property.

```
codedx.external-url = https://codedx.mycompany.com
```

Additionally, there are some cases where you may want internal services (running on the
same machine as Software Risk Manager) to access Software Risk Manager from a different
URL compared to the external URL. By default, the external URL will be used in this
scenario (unless overridden by setting `codedx.internal-url`):

```
codedx.internal-url = https://localhost:8443/codedx/
```
