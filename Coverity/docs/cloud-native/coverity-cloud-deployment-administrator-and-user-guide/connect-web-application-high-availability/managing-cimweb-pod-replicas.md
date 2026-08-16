---
title: "Managing cimweb pod replicas"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-cimweb-pod-replicas.html"
content_id: "xaIdjOARK8HVdG42zxHHbQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:26.169510+00:00"
---

# Managing cimweb pod replicas

You can scale the number of `cimweb` pod replicas as follows:

- Change the `cim.cimweb.replicas` Helm key from the default value
  of `1` which deploys one cimweb pod, to `2` or
  greater to deploy multiple pods. For example, to scale up to 2
  `cimweb` pod replicas, set the Helm key as follows:

  ```
  cim: 
    cimweb: 
      replicas: 2
  ```

  `cim.cimweb.replicas` is located within the `cnc`
  chart `values.yaml` file or your custom `.yaml`
  file.

  For further information on the `cim.cimweb.replicas` Helm key,
  refer to cim.cimweb Helm keys.
