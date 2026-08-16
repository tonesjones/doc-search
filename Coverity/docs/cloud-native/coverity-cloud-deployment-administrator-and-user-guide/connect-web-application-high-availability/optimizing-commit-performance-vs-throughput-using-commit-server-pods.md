---
title: "Optimizing commit performance vs throughput using commit-server pods"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/optimizing-commit-performance-vs-throughput-using-commit-server-pods.html"
content_id: "ko7diGIzhu66nZBYqY29sA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:27.074674+00:00"
---

# Optimizing commit performance vs throughput using commit-server pods

When implementing high availability (HA), you can configure one or more commit-server
pods which manage commits and caching to improve commit performance or commit
throughput. Using commit servers, also called Coverity commit defects (CCD) servers,
directs ingress traffic to the commit servers. Deploying one
`commit-server` pod improves cache performance.

Before you can configure and deploy commit servers, cimweb high availability (HA) must be
configured with at least the following Helm key values:

- `cim.cimweb.enabled: true`
- `cim.cimweb.replicas: 2` or greater

Use the `cim.commit-server.replicas` Helm key to specify the number of
commit server containers to deploy. Deploying one commit server instance improves commit
performance. Deploying two or more commit server instances improves commit throughput.
See the examples that follow. The number of commit server replicas you decide to use can
depend on the size and number of analyses that you run and on your desire to optimize
for commit performance or commit throughput.

For `cim.commit-server.replicas` Helm key information, also see also cim.commit-server Helm keys.

You will also see the `cim.commit-server.logLevel` Helm key. You can leave
this value as is or change if desired.

## Example: commit performance profile

The following figure llustrates a commit performance profile with one
`commit-server` replica.

Figure 1. Commit performance profile
[image: image]

## Example: commit throughput profile

The following figure llustrates a commit throughput profile with two
`commit-server` replicas. Note that you can configure 2 or more
commit seerver replicas as needed.

Figure 2. Commit throughput profile
[image: image]
