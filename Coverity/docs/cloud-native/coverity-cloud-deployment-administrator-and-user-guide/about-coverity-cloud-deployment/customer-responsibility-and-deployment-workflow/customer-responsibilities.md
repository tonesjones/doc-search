---
title: "Customer responsibilities"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/customer-responsibilities.html"
content_id: "3iYneFBzYIrIwHerNMy~2g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:22.298733+00:00"
---

# Customer responsibilities

A Cloud Native Coverity application is a set of loosely coupled containerized
microservices, deployed using Kubernetes as the orchestration engine. Cloud Native
Coverity has many requirements, including infrastructure, dependencies, and customer
knowledge and expertise of cloud-native systems and patterns. Many of these requirements
must be provided by the customer.

The following table outlines customer responsibilities.

Table 1. Customer responsibilities

| Category | What | Responsibilities | Required skills |
| --- | --- | --- | --- |
| CNC files | - Container images - Installer files - Helm chart | - Download container images, installer files, and Helm   chart. | - Understand images, Docker, and Helm. - Ability to work with Docker image registries. - Understand image pull secrets. |
| Deploy | - Client-side: kubectl, Helm. - Means of deploying dependencies. - Means of deploying Helm chart. | - Create a process or script for deploying all dependencies and   CNC application | - Understand images, Helm, and Kubernetes. - Understand how to deploy and maintain applications on   Kubernetes. - Understand networking. - Understand curl. |
| Direct dependencies | - cluster: Kubernetes or OpenShift. - PostgreSQL - Scan Services   - object storage   - caching: Redis - Kubernetes namespace (optional) | - Understand, create, maintain, debug, upgrade   dependencies. - Provide connection parameters to CNC Helm chart. | - Understand what dependencies provide and how to work with   them. |
| Indirect dependencies  (application, cluster admin, operations) | - Certificate - Ingress controller - Log aggregator - Metrics aggregator - Private image registry   - CNC images mirrored here   - Image pull secret | - Understand, create, maintain, debug, upgrade - Apply these tools to solve operational problems | - Understand cloud-native tech stacks and how these interact   with applications. For example, telemetry and certificate   managers. |
| Optional dependencies | - Separate analysis node pool. - Custom scheduler (e.g. Volcano). | - Understand, create, and maintain infrastructure   components. |  |
