---
title: "Software Risk Manager Install and Deployment Options"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/software-risk-manager-install-and-deployment-options.html"
content_id: "utOgXkgASNhkOCjO7VuCwQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:45.734559+00:00"
content_hash: "2a83ca1d741362a22284d723231bfdefecc28d8464b1b2acfdb3a520be2ad1b3"
---

# Software Risk Manager Install and Deployment Options

The full range of Software Risk Manager functionality is based on how it is deployed.
This section provides an overview of what each deployment provides.

Software Risk Manager has four deployment options, which are described below.

## Native Installer

The native installer (also referred to as the "stand alone" deployment) is available
for both Windows and Linux. It provides an easy way to install the entire technology
stack on a single server with an easy-to-use UI and command line wizard. This
deployment is recommended for users who want to get up and running quickly and for
simple maintenance and upgrades.

With the native installer, both the web application and database are running on the
same system, which can cause contention. For high availability, the Kubernetes
deployment is recommended. In addition, the native installer does not support
running an external database, nor does it support horizontally scaling the running
of tools. For more information, see Running the Native Installer.

Note: Tool
Orchestration and Scan Farm modules are not supported with this deployment
option.

## Docker Compose Deployment

This deployment is recommended for users who want to leverage containers while having
everything on a single server. (Note that the database can also be deployed on a
seperate server). This deployment option allows for using a bundled database or an
external one. For more information, see Installation Using Docker Compose.

Note: Tool Orchestration and Scan Farm
modules are not supported with this deployment option.

## Kubernetes Deployment

This deployment option is recommended for high availability and scalability.
Kubernetes also supports Tool Orchestration and Scan Farm modules. For more
information, see Installation Using
Kubernetes.

## Manual Installation

This deployment is reserved for advanced administrators who want total control of the deployment.
It allows the user to install the web server and database and manage that
infrastructure independently. The database can be deployed on the same machine or a
separate one from the web application. This deployment method is not recommended due
to its complexity and being prone to error.

Note: Tool Orchestration and Scan Farm
modules are not supported with this deployment option.
