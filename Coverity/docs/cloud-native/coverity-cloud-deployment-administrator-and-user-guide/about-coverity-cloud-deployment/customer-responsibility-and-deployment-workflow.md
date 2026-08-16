---
title: "Customer responsibility and deployment workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/customer-responsibility-and-deployment-workflow.html"
content_id: "su4N3FmBo3kR3W5WzAd3Lg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:21.574061+00:00"
---

# Customer responsibility and deployment workflow

Kubernetes is a complex environment that places significant responsibility on you for
installing, maintaining, and upgrading the infrastructure required to deploy Coverity in
a Kubernetes environment in the cloud. This includes:

- Installing Kubernetes, Docker, and Helm. The administrator must know Kubernetes,
  Docker, and Helm.
- Creating a Kubernetes cluster.
- Creating a private Docker registry.
- Creating and managing an external PostgreSQL database.
- Installing and managing an ingress controller.
- Configuring networks.
- Configuring authentication and authorization, including secrets and
  certificates.
- If deploying Scan Service, create a storage bucket and cache bucket for Scan
  Service.
- Install configure, and manage Redis.
- Address any platform-specific dependencies.
- If needed, create and maintain deployment scripts.

How you set up Kubernetes containers in the cloud depends on whether you are setting up a
new Coverity installation/deployment or migrating an existing deployment to Kubernetes
in the cloud. Coverity deployment scenarios provides high-level procedures for
several deployment scenarios to provide guidance.
