---
title: "Coverity container images"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-container-images.html"
content_id: "GRirjsJKh3~5E6eXFPJkag"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:38.566392+00:00"
---

# Coverity container images

You need to pull all of the Coverity container images required for your deployment from
the Black Duck private Docker registry and push these files to your own private Docker
registry. To deploy only Connect in the cloud, you need only the Connect and ingress
containers. To deploy Scan Service and run scans in the cloud, you need all of the
container images: Connect, Scan Service, and ingress in the tables below.

For instructions to `login` | `pull` | `tag`
| `push` these images using `docker` commands, see the
sections that follow the container image tables.

The following table identifies Coverity cloud container images that you use to deploy
Coverity in Kubernetes containers in infrastructure platforms except OpenShift. These
platforms include AWS, GCP and Azure. Pull these images from the Black Duck private Docker registry:

- `repo.blackduck.com`

  Note: In
  `docker` commands, do not include
  `https://`.

Note: The container images in the tables below work with both ARM64 and
Intel/AMD. When deployed, the images are used to create containers within Kubernetes
nodes; the images and resulting containers are isolated from underlying hardware.

Table 1. Container images for all deployment platforms except OpenShift

| Category | Black Duck® Coverity® container image | Description |
| --- | --- | --- |
| Connect | `cim-downloads:2026.6.0` | This container image contains static files for downloads from the Connect UI. It is implemented via init containers in the cim-webapp pod and includes client-side binaries and documentation. |
| `cim-tools:2026.6.0` | This container image creates a container that provides administrator functionality: cov-archive and reset-admin-password (cov-admin-db). The statefulset is initially set to replica count 0; it must first be scaled up to create a pod before use. |
| `cim-web:2026.6.0` | This container image creates a group of containers that run the Connect webapp. They include:   - an init container to set up configuration. - an init container to set up documentation. - an init container to set up downloads of client-side   utilities. - (optional) an nginx reverse proxy as a sidecar to provide TLS   termination. |
| `cov-manage-im:2026.6.0` | This container image creates a container for the cov-manage-im tool which is used to manage and query defects, projects, and streams in Coverity Connect. See Managing Coverity Connect: cov-manage-im. |
| Scan Services | `cache-service:2026.6.0` | This container image creates a container that provides analysis caching capabilities |
| `common-infra:2026.6.0` | This container image creates a container that performs setup tasks related to certificates and configuration. |
| `job-runner:2026.6.0` | This container image is needed to run analysis jobs in Kubernetes containers.  See Managing supported Coverity Tools and Thin Client versions in the Connect UI. |
| `scan-service-migration:2026.6.0` | This container image creates a container that controls a job which upgrades the scan database schema to the latest; it is idempotent and may safely be run multiple times, even if not necessary. |
| `scan-service:2026.6.0` | This container image creates a container that configures Scan Service resource allocation and other parameters. |
| `storage-service-migration:2026.6.0` | This container image creates a container that controls a job which upgrades the storage database schema to the latest version. |
| `storage-service:2026.6.0` | This container image creates a container that manages the storage of uploaded intermediate directories (idirs), and provides idir access for analysis jobs. |
| AI-Assisted Triage Service | `triage-suggestion-service-api:2026.6.0` | This container image creates a triage-suggestion-service API container. |
| `triage-suggestion-service-worker:2026.6.0` | This container image creates a triage-suggestion-service worker container. |

The following table identifies Coverity Cloud UBI images needed to deploy containers in
OpenShift. Pull these images from the Black Duck private
Docker registry.

Table 2. UBI container images for OpenShift deployments

| Category | Black Duck® Coverity® container image |
| --- | --- |
| Connect | `cim-downloads:2026.6.0-ubi`  `cim-tools:2026.6.0-ubi`  `cim-web:2026.6.0-ubi` |
| Scan services | `cache-service:2026.6.0-ubi`  `common-infra:2026.6.0-ubi`  `job-runner:2026.6.0-ubi`  `scan-service-migration:2026.6.0-ubi`  `scan-service:2026.6.0-ubi`  `storage-service-migration:2026.6.0-ubi`  `storage-service:2026.6.0-ubi` |
| AI-Assisted Triage Service | `triage-suggestion-service-api:2026.6.0-ubi`  `triage-suggestion-service-worker:2026.6.0-ubi` |

Note: For information on the function of each -ubi image, refer to the
Description column in the Container images for all deployment platforms except
OpenShift table above.
