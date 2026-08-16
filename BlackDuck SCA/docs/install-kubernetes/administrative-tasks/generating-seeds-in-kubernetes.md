---
title: "Generating seeds in Kubernetes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/generating-seeds-in-kubernetes.html"
content_id: "xsQ37IIlMMgO98wIw8Yk5g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:17.508286+00:00"
---

# Generating seeds in Kubernetes

## Generating seeds in OpenSSL

The content of the seeds can be generated using any mechanism that generates secure
random contents at least 1024 bytes long. As soon as a seed has been created and
saved in a secret, it should be removed from your file system and saved in a
private, secure location.

The OpenSSL command is as follows:

```
openssl rand -hex 1024 > root_seed
```

## Generating seeds in Kubernetes

There are many Kubernetes command lines that will create a secret. The
command listed below allows better tracking of the secret and whether it changes or not, and
ensures compatibility with being able to manipulate secrets with an online system.
Secrets can be created and deleted in Kubernetes with Black Duck actively running.

```
kubectl create secret generic crypto-root-seed -n $NAMESPACE --save-config --dry-run=client --from-file=crypto-root-seed=./root_seed -o yaml | kubectl apply -f -
```

In order to delete the prev key secret in Kubernetes:

```
kubectl delete secret crypto-prev-seed -n $NAMESPACE
```
