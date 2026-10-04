---
title: "Analysis location"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/analysis-location.html"
content_id: "1NZNE2VAoTJnsICZ413qgQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:22.381080+00:00"
---

# Analysis location

If you installed the Thin Client, the generated configuration file contains
`analyze: location: connect` which directs an analysis to be
performed in the cloud. For example:

```
analyze:
  location: connect
 
commit:
  connect:
    auth-key-file: /Users/jbloggs/.coverity/authkeys/ak-connect.example.com-8443
    stream: my-stream
    url: https://connect.example.com:8443
```

If you installed the full CLI client, the generated configuration file does NOT contain
`analyze: location: connect`, as shown below. Scans automatically
default to a local analysis performed by the CLI on the local client.

```
commit:
  connect:
    auth-key-file: /Users/jbloggs/.coverity/authkeys/ak-connect.example.com-8443
    stream: my-stream
    url: https://connect.example.com:8443
```
