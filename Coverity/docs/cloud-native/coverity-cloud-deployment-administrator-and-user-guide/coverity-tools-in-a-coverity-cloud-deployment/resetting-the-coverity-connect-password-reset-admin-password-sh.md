---
title: "Resetting the Coverity Connect password: reset-admin-password.sh"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/resetting-the-coverity-connect-password-reset-admin-password.sh.html"
content_id: "xXN~bzr_6tq1WUDyo~dsgg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:09.975023+00:00"
---

# Resetting the Coverity Connect password: reset-admin-password.sh

This procedure describes how to reset the password for a Coverity Connect instance in a
Coverity cloud deployment. It finds the pod that contains the Connect instance, opens a
shell prompt, and runs a script to change the password.

When you execute the script, you use the same arguments that are used with the
`cov-admin-db reset-admin-password` command described in the section
Coverity Connect commands in the Coverity 2026.6.0 Command Reference.

To reset the Coverity Connect password for a Connect instance:

1. Deploy the Helm chart in the Kubernetes namespace <$NS>.
2. By default, the `cim-tools` pod is scaled to 0 replicas, and cluster
   resources are not used. Scale up the `cim-tools`
   pod:

   ```
   kubectl scale statefulsets <${RELEASE}>-cim-tools -n <$NS> --replicas=1
   ```

   For
   example, if namespace <$NS> is coverity and <${RELEASE}> is 2026.6.0:

   ```
   kubectl scale statefulsets 2026.6.0-cim-tools -n coverity --replicas=1
   ```
3. List all pods in the namespace and find the Connect
   pod:

   ```
   kubectl get pods -n <$NS>
   ```

   For
   example, for a namespace named
   coverity:

   ```
   kubectl get pods -n coverity
   ```
4. Open a shell in the `cim-tools`
   pod:

   ```
   kubectl exec -ti -n <$NS> statefulsets/<${RELEASE}>-cim-tools -- /bin/sh
   ```
5. At the shell prompt, run the `reset-admin-password.sh` script and
   provide the password.
6. When finished, exit the shell using the `exit` command.
7. Scale down the `cim-tools`
   pod:

   ```
   kubectl scale statefulsets <${RELEASE}>-cim-tools -n <$NS> --replicas=0
   ```

   For
   example:

   ```
   kubectl scale statefulsets 2026.6.0-cim-tools -n coverity --replicas=0
   ```
