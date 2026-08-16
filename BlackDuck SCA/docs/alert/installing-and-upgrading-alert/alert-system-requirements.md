---
title: "Alert System Requirements"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-system-requirements.html"
content_id: "GOTmZXzaYfCJA4ctlOJq3Q"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:18.561793+00:00"
---

# Alert System Requirements

## Prerequisites to install and run Alert

- A compatible Black Duck SCA instance (Refer to Black Duck SCA [Release Compatibility](https://documentation.blackduck.com/bundle/blackduck-compatibility/page/topics/Black-Duck-Release-Compatibility.html) to view the
  supported versions of Black Duck SCA)
- A Black Duck SCA API token for Alert to receive notifications from Black Duck SCA; see
  below for more information.
- Docker Swarm with administrative access to the docker host machine or Kubernetes
  (HELM) Kubernetes 1.9+ with Helm2 or Helm3.
- Docker `v20.10` or later
- Java version `17`
- PostgreSQL major version support for bundled database as of Alert 8.2.0:
  `16`
- When deploying with an external database, you will also need to meet the
  prerequisites as per installing with an external database.
  - External PostgreSQL major version support: `15` and
    `16`
- When deploying Alert with a Black Duck SCA instance in the same environment,
  specific configuration changes will be required. Consult the deploying with Docker swarm or deploying with
  Helm sections for further guidance.

## Supported Channel application versions

- Jira Server/Data Center version `9` or `10`
- Jira Cloud (Version agnostic)
- Slack (Version agnostic)
- MS Teams (Version agnostic)
- Azure Boards (Version agnostic)
- Email (Version Agnostic)

## Recommended overall system specifications

- 5 CPU Cores or greater (**Note:** The unit suffix "m" in the table below
  stands for thousandth of a core. 1000m or 1000 millicore is equal to 1
  core.)
- Minimum of 12GB free disk space plus blackduck-cfssl container disk space.
  (Review Black Duck requirements to determine the value appropriate for your
  environment.)
- 5GB RAM or greater

## Recommended container specifications

| Container | CPU Core | Memory | Disk Space |
| --- | --- | --- | --- |
| Alert Server | 2000m | 2560MB | 5GB |
| RabbitMQ | 1000m | 1024MB | 2GB |
| PostgreSQL | 1000m | 1024MB | 5GB |
| CFSSL (For BD) | 100m | 640MB | As per BD |

Note: There may be other pods in the cluster using memory and CPU cycles.
You may need to modify the allocations for your cluster if other applications
are running.

Additional Kubernetes container information: [Resource Management for Pods and
Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## Minimum overall system specifications

- 4 CPU Cores (**Note:** The unit suffix "m" in the table below stands for
  thousandth of a core. 1000m or 1000 millicore is equal to 1 core.)
- Minimum of 12GB free disk space plus blackduck-cfssl container disk space.
  (Review Black Duck requirements to determine the value appropriate for your
  environment.)
- 4.5GB RAM

## Minimum container specifications

| Container | CPU Core | Memory | Disk Space |
| --- | --- | --- | --- |
| Alert Server | 1000m | 2560MB | 5GB |
| RabbitMQ | 1000m | 1024MB | 2GB |
| PostgreSQL | 1000m | 1024MB | 5GB |
| CFSSL (For BD) | 100m | 640MB | As per BD |

## Black Duck SCA API token

Logging in to Black Duck SCA is not required for using Alert; its user management is
separate from Black Duck SCA. However, an API token is required to enable the Black Duck SCA
provider to receive notifications from Black Duck SCA.

Use the Black Duck SCA user profile to generate an API token from Black Duck. This API
token is plugged into the Alert Black Duck SCA Providers configuration page or during
Alert installation by using an environment variable. See Configuring
Black Duck SCA Providers and Alert Environment Variables
