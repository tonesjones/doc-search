---
title: "Cloud Vendor Specific Database Considerations"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/cloud-vendor-specific-database-considerations.html"
content_id: "JRXn_MF_1POMu21vXfRAMQ"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:30.818287+00:00"
---

# Cloud Vendor Specific Database Considerations

## Microsoft Azure

With Microsoft Azure deployments, there are several considerations in terms of
storage classes:

- Azure Disk is node bound. This means that in instances where the database pod
  terminates, the pod may be scheduled on a different node. This may lead to
  data loss.
- Azure File does not support hard links by default and the pod may fail to
  start. A NFS based azurefile storage class can be created in this instance
  [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/aks/azure-files-csi#nfs-file-shares).

## Amazon Web Services

Amazon Elastic Block Store (EBS) is node bound. This means that in instances where
the database pod terminates, the pod may be scheduled on a different node. This may
lead to data loss.

In general, it is recommended to use an externally managed database in production
deployments.
