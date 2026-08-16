---
title: "Tasks to complete after an upgrade"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tasks-to-complete-after-an-upgrade.html"
content_id: "xSTbbur30taXRdvzafvAFA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:26.601386+00:00"
---

# Tasks to complete after an upgrade

## Scale up the Coverity Connect web application

After completing the upgrade, scale up the Coverity Connect web application,
`cim-webapp`. For example:

```
kubectl scale deployment/${RELEASE}-cim-webapp -n ${NS} --replicas=1
```

For example, for the 2026.6.0 release in the cnc namespace:

```
kubectl scale deployment/2026.6.0-cim-webapp -n cnc --replicas=1
```

## Verify functionality

Verify that the upgrade was successful and that Coverity is working.

1. Another way is to use the `kubectl get pods --namespace ${NS}`
   command and verify that the Coverity Connect pod is running. For example,
   `kubectl get pods --namespace cnc`.
2. Verify that all jobs completed successfully.
3. Using the `$ helm status --namespace "${NS}
   "${CNC_APP_NAME}"` command, verify that the Connect
   instance is in the correct namespace and deployed. For
   example:

   ```
   $ helm status -n cnc connect
   NAME: connect
   LAST DEPLOYED: Fri Jan 6 08:16:19 2023
   NAMESPACE: cnc
   STATUS: deployed
   REVISION: 3
   TEST SUITE: None
   ```
4. In a web browser, log into the Coverity Connect web application and verify that
   it is running.
