---
title: "Scan job node pool sizing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-job-node-pool-sizing.html"
content_id: "2lSg2F~quIznX071F9NBeg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:08.954317+00:00"
---

# Scan job node pool sizing

The following table identifies the number of CPUs and the amount of memory required per
scan job for predefined and custom scan job node pool sizes. Once you have determined
the scan job requirements, you need to create a node pool that supports these
requirements as well as any supporting software running on the nodes. This table should
help you when sizing and creating your scan job node pool. Infrastructure requirements
to size a node pool are determined by your infrastructure provider's virtual machine
families and machine types. Refer to your cloud provider documentation for information
to size and create a node pool.

You can create as many as five scan job node pools; one for each node pool type: small,
medium, large, extra large, and custom.

For information on the Helm keys to define scan job node pools, refer to the
`scan-service.environment` Helm keys in scan-service.environment Helm keys.

Note: For optimal scan performance, a node pool should support nodes
with a minimum of 8 CPUs and 32 GB of RAM.

Table 1. Scan job node pool sizing

| Node pool type | Taints | CPUs required | Memory required | Description |
| --- | --- | --- | --- | --- |
| Small size | NodeType​=​​ScannerNode | 6.5 core vCPUs | 26 GB | Each node deployed in the node pool requires 6.5 vCPUs and 26 GB RAM for the scan job.  Example: To support this node requirement, you might create a node pool in your infrastructure that supports 8 vCPU, 32 GB RAM nodes.  The Helm key to enable or disable this node pool is:   ``` scan-service:     ​environment:         ​SMALLNODEPOOL_ENABLE: true|false ``` |
| Medium size | 14.5 core vCPUs | 56 GB | Each node deployed in the node pool requires 14.5 vCPUs and 56 GB RAM for the scan job.  Example: To support this node requirement, you might create a node pool in your infrastructure that supports 16 vCPU, 64 GB RAM nodes.  The Helm key to enable or disable this node pool is:   ``` scan-service:     ​environment:         ​MEDIUMNODEPOOL_ENABLE: true|false ``` |
| Large size | 28.5 core vCPUs | 108 GB | Each node deployed in the node pool requires 28.5 vCPUs and 108 GB RAM for the scan job.  Example: To support this node requirement, you might create a node pool in your infrastructure that supports 32 vCPU, 128 GB RAM nodes.  The Helm key to enable or disable this node pool is:   ``` scan-service:     ​environment:         ​LARGENODEPOOL_ENABLE: true|false ``` |
| Extra large size | 58.5 core vCPUs | 222 GB | Each node deployed in the node pool requires 58.5 vCPUs and 222 GB RAM for the scan job.  Example: To support this node requirement, you might create a node pool in your infrastructure that supports 64 vCPU, 256 GB RAM nodes.  The Helm key to enable or disable this node pool is:   ``` scan-service:     ​environment:         ​EXTRALARGENODEPOOL_ENABLE: true|false ``` |
| Custom size | Custom CPUs | Custom memory | You can create and deploy a custom node pool. You must specify the custom node pool label and sizing using the following Helm keys.   ``` scan-service:   environment:     CUSTOMNODEPOOL_LABEL: "<label>"     CUSTOMNODEPOOL_CPU:  <CPU> in cores     CUSTOMNODEPOOL_MEM: <Memory> in MB     COVANALYSIS_DEFAULTPOOLTYPE: "<label>" ```   Refer to the `scan-service.environment` Helm keys in scan-services Helm subchart: Helm keys.  In your infrastructure, you must size and create a node pool that supports your custom node pool requirement. For example, to deploy scans in a custom node pool where each node requires 3 vCPUs and 14 GB RAM for the scan job, you might create a node pool in your infrastructure that supports 4 vCPU, 16 GB RAM nodes. |
