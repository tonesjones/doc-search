---
title: "Upgrading to 2025.3"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.3.html"
content_id: "ym2y3BF_ZH_dmPOu502Hsg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:34.752015+00:00"
---

# Upgrading to 2025.3

The 2025.3.0 release introduces the following changes that can impact the upgrade
process:

- The 2025.3.0 release introduces the ability to create read-only PostgreSQL
  database replicas that provide fast read-only storage copies that large numbers
  of iclients can read data from. This removes read overhead from the primary
  database, thereby increasing commit throughput and performance. See Using PostgreSQL read replicas and Pgpool to balance database loads.
- The 2025.3.0 release introduces new Helm keys that enable you to manage security
  for containers within pods in addition to managing security at the pod level.
  This document contains a new chapter that describes pod and container security
  managed through Helm keys. See .Configuring pod and container security
- The 2025.3.0 release introduces the ability to manage the scheduling of scan jobs
  on a single scan job node as well as across multiple scan job nodes. See Creating scan job node pools and scheduling scan jobs.
- The Coverity cloud 2025.3.0 release now supports NGINX 1.27.4, and drops support
  for NGINX 1.24.0.

  Important: If you are using a
  Kubernetes/ingress-nginx controller ([kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)), be aware of the following
  security issue: [CVE-2025-1974: ingress-nginx admission controller RCE
  escalation #131009](https://github.com/kubernetes/kubernetes/issues/131009).

Additionally, you must consider the following if you are upgrading from any release where
you are downloading images from Synopsys SIG repositories.

Important: The repository [sig-repo.synopsys.com](http://sig-repo.synopsys.com/) at IP address 34.110.245.127 is no longer
supported.

- Black Duck Coverity supports a new registry/repository that
  has public and private folders for container images, tool files, Helm chart, and
  other files. See About Black Duck repositories.
- All repository data has been migrated to the new Black Duck repository, [repo.blackduck.com](http://repo.blackduck.com/) at 34.149.5.115. Make sure that you point to and use
  data from the public and private repository folders within this new repository. See
  About Black Duck repositories.
- If you use IP Whitelist to access [repo.blackduck.com](http://repo.blackduck.com/), add the following IP
  address to the IP whitelist: 34.149.5.115. See About Black Duck repositories.
- Change all registry URLs from the Synopsys SIG repositories to Black Duck
  repositories.
- If you use any internal scripts that link to the Synopsys SIG
  registries/repositories, you need to redirect the links to the new Black Duck
  repositories identified in About Black Duck repositories.
- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud. To create
  your own private Coverity cloud repository, see Create your own private Docker registry.
- You must obtain and deploy the new Helm chart for the current release. See Downloading the Helm chart from the Black Duck public Docker registry.

The following table identifies Helm keys where the default value was changed in the
2025.3.0 release.

Table 1. Changed Helm key default values

| Helm key | Old and new default value | Refer to |
| --- | --- | --- |
| ``` cim:   cimweb:     tlsSidecar:       version: ``` | Old: `1.24.0`  New: `1.27.4` | `cnc` chart.  See cim.cimweb.tlsSidecar Helm keys |

The following table identifies Helm keys added in the 2025.3.0 release.

Table 2. Helm keys added in 2025.3.0

| Helm key | Note |
| --- | --- |
| ``` cim:   automountServiceAccountToken:    cimdownloads:     containerSecurityContext: {}    cimtools:     automountServiceAccountToken:     containerSecurityContext: {}    cimweb:     tlsSidecar:       containerSecurityContext: {}    pgpool:     automountServiceAccountToken:     containerSecurityContext: {}    setupJob:     automountServiceAccountToken:     containerSecurityContext: {}  cnc-db-admin:   automountServiceAccountToken:   containerSecurityContext: {} ``` | Container security  `cnc` chart  `automountServiceAccountToken` Helm keys: Refer to:   - Configuring pod and container security - cnc Helm chart: Helm keys   `containerSecurityContext` Helm keys   - Configuring pod and container security - cnc Helm chart: Helm keys |
| ``` cache-service:   automountServiceAccountToken:   containerSecurityContext: {}   podSecurityContext: {}  common-infra:   automountServiceAccountToken:   containerSecurityContext: {}   podSecurityContext: {}  scan-service:   automountServiceAccountToken:   containerSecurityContext: {}   podSecurityContext: {}   migrateJob:     containerSecurityContext: {}  storage-service:   automountServiceAccountToken:   containerSecurityContext: {}   podSecurityContext: {}   migrateJob:     containerSecurityContext: {} ``` | Container security  `scan-services` subchart  `automountServiceAccountToken` Helm keys: Refer to:   - Configuring pod and container security - scan-services Helm subchart: Helm keys   `containerSecurityContext` Helm keys: Refer to:   - Configuring pod and container security - scan-services Helm subchart: Helm keys   `podSecurityContext` Helm keys: Refer to:   - Configuring pod and container security - scan-services Helm subchart: Helm keys |
| ``` cim:   pgpool:     enabled: false     image: "pgpool"     registry: ""     version: "4.6.0"     replicas: 1     annotations: {}     affinity: {}     tolerations: []     containerSecurityContext: {}     automountServiceAccountToken: false     replicadb: []     resources:       limits:         cpu: "2"         memory: 2Gi       requests:         cpu: 250m         memory: 1Gi     maxConnections:     childLifeTime: 300     childMaxConnections: 0     connectionLifeTime: 0     clientIdleLimit: 0     connectionCache: "on" ``` | PostgreSQL DB read replicas - Pgpool-II  `cnc` chart  `pgpool` Helm keys   - Using PostgreSQL read replicas and Pgpool to balance database loads - cnc Helm chart: Helm keys |
| ``` scan-service:   environment:     MULTIPLEJOBSPERNODE_ENABLE ``` | Scheduling multiple analysis jobs on a node.  `scan-services` chart  `pgpool` Helm keys: Refer to:   - Creating scan job node pools and scheduling scan jobs - scan-services Helm subchart: Helm keys |
| ``` cim:   commitrcp4: ``` | `cnc` chart   - Important: Do NOT USE or CHANGE ANY `cnc` Helm chart   `cim.commitrcp4` Helm keys. These   are Black Duck internal use only. |
