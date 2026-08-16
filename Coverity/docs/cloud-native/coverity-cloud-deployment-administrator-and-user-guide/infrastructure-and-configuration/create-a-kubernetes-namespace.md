---
title: "Create a Kubernetes namespace"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-kubernetes-namespace.html"
content_id: "g3rq9Teiz2vR9fHIUT3abA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:54.296864+00:00"
---

# Create a Kubernetes namespace

Kubernetes namespaces are needed to isolate the handling of Coverity cloud resources.
Namespaces offer an additional layer of security and isolation from other resources run
in the same Kubernetes cluster. We recommend using distinct namespaces to isolate
application-specific resources.

The command syntax to create a namespace is:

```
kubectl create ns NS_Name
```

Where NS_Name is the name you apply to the namespace.

For example, to assign the name CovConnect1 to the namespace for an instance of Coverity
Connect:

```
kubectl create ns CovConnect1
```
