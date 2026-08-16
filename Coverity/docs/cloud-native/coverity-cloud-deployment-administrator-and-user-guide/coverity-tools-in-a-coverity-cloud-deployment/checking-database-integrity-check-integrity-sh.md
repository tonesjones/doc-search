---
title: "Checking database integrity: check-integrity.sh"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checking-database-integrity-check-integrity.sh.html"
content_id: "DvWywb7zVdhTMB4y9VKfXg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:09.334321+00:00"
---

# Checking database integrity: check-integrity.sh

The `check-integrity.sh` script checks database integrity for PostgreSQL
databases associated with a Coverity cloud deployment. The script validates tables,
sequences, columns, constraints, and indexes.

When you execute the script, you use the same arguments that are used with the
`cov-admin-db check-integrity` command described in the section
Coverity Connect commands in the Coverity 2026.6.0 Command Reference.

To enable database utilities and run `check-integrity.sh`:

Note: The PostgreSQL service must be running when you perform the
integrity check.

1. Deploy the Helm chart in the Kubernetes namespace `<$NS>`.
2. Scale up the `cim-tools` pod. By default, a pod is scaled to 0
   replicas, and cluster resources are not used.

   ```
   kubectl scale statefulsets <${RELEASE}>-cim-tools -n <$NS> --replicas=1
   ```

   For example, if the namespace `<$NS>` is
   `coverity` and the `<${RELEASE}>` is
   `2026.6.0`:

   ```
   kubectl scale statefulsets 2026.6.0-cim-tools -n coverity --replicas=1
   ```
3. Search for the new pod in the deployed namespace:

   ```
   kubectl get pods -n <$NS>
   ```

   For example:

   ```
   kubectl get pods -n coverity
   ```
4. Open a shell in the new pod:

   ```
   kubectl exec -ti -n <$NS> statefulsets/<${RELEASE}>-cim-tools -- /bin/sh
   ```
5. At the shell prompt, run the `check-integrity.sh` script. Logs and
   reports from the integrity check display in the console.
6. Exit the shell using the `exit` command.
7. Scale down the pod:

   ```
   kubectl scale statefulsets <${RELEASE}>-cim-tools -n <$NS> --replicas=0
   ```

   For example:

   ```
   kubectl scale statefulsets 2026.6.0-cim-tools -n coverity --replicas=0
   ```
