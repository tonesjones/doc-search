---
title: "Coverity cloud quick-start chart and scripts - simplified version"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-cloud-quick-start-chart-and-scripts-simplified-version.html"
content_id: "lipQLGRrIVW~7tLPGi~KKQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:24.254857+00:00"
---

# Coverity cloud quick-start chart and scripts - simplified version

In the 2026.3.0, release, Black Duck is providing Helm chart files and scripts designed
to simplify Coverity cloud deployments for a number of deployment environments and
scenarios. These charts are intended to be used for initial basic Coverity Kubernetes
deployment test and learning. They are not intended to be used for more complex
production deployments.

Attention:

Beginning with the 2026.3.0 release of Coverity cloud, Black Duck is providing and
maintaining a public repository that contains the Helm charts and scripts
specifically designed for you to perform basic Coverity cloud deployments.

## Standalone vs distributed Kubernetes deployment

A **standalone** Kubernetes deployment runs the entire cluster, including control
plane and worker components, on a single node (virtual machine, physical server,
laptop, etc.). In a standalone deployment, a single node handles all containers,
including: API server, etcd. scheduler, controller manager, kubelet, container
runtime, and application pods. Standalone is much simpler to deploy, however it is
not intended for complex production environments such as Coverity. You can use a
standalone deployment for quickly deploy for testing, learning, and simple
demonstration. Typical examples of a standalone environment include minikube, kind,
k3s, and a manually installed Kubernetes node where control plane and workloads
coexist

A **distributed** Kubernetes deployment consists of two broad categories of
multiple nodes each: control plane nodes, and worker nodes. This is the standard
production architecture for Kubernetes.

A distributed Kubernetes deployment makes the following possible:

- High availability (HA)
- Fault tolerance (node failures don’t take down the cluster)
- Horizontal scaling (nodes and pods)
- Separation of concerns (control plane vs workloads)
- Production‑ready reliability
- Supports advanced features:
  - Pod anti‑affinity
  - Rolling upgrades
  - Auto‑scaling
  - Multi‑zone / multi‑region designs

Cons

- More complex to set up and operate
- Higher infrastructure cost
- Requires careful networking, security, and monitoring
- More components to maintain (etcd quorum, load balancers, certs

## About the Coverity cloud quick-start repository

The Coverity cloud quickstart public repository is located here:

- [cnc-quickstart](https://github.com/blackduck-inc/cnc-quickstart)

For the repository layout and contents, see the following file in the top-level
repository folder: `STRUCTURE.md`.

Using the `quickstart` scripts and Helm chart files, you can create
simple deployments in the following platforms:

- AWS
- Azure
- GCP
- Kind

These folders contain subfolders for specific deployments such as:

- Connect-only
- Connect and scan service
- others

For instructions, in the `/docs` directory, see the file
`QUICKSTART.md` which has the title, "CNC Quickstart Guide".
