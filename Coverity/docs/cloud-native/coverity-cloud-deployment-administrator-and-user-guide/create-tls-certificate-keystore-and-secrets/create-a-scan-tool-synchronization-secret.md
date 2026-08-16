---
title: "Create a scan tool synchronization secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-scan-tool-synchronization-secret.html"
content_id: "BlJ4yLHCDX_A~TaQuc~5rw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:03.470657+00:00"
---

# Create a scan tool synchronization secret

With scan tool synchronization configured and enabled, when you perform a `helm
install`, the current release version of the Coverity Tools kits (Thin
Client and Analysis kits) is automatically downloaded from the Black Duck registry and uploaded to the cloud storage bucket.
You must create a secret to provide access to the Black Duck registry for the download to succeed.

Create a secret in the Coverity namespace using the `kubectl create secret
generic` command. For example:

```
kubectl create secret generic ${repoKeyName} \
  --namespace ${CNC_NS} \
  --from-literal=username=${username} \
  --from-literal=password=${password} \
  -o yaml
```

where:

| Variable | Meaning | Notes |
| --- | --- | --- |
| `${repoSecretName}` | Assign a unique secret name. | Example: ScanToolsSecret |
| `${CNC_NS}` | Provide the Coverity Kubernetes namespace. | Example: cnc |
| `${username}` | Provide the username to access the repository. | For Black Duck private Docker registry credentials, see Access the Black Duck private Docker registry credentials. |
| `${password}` | Provide the password to access the repository. |

For example, to create a secret named 'blackduck-repo' that contains the username and
password needed to access the Black Duck private Docker
registry, you can create a secret named blackduck-repo that contains the Black Duck registry credentials:

```
kubectl create secret generic blackduck-repo
 --namespace cnc
 --from-literal=username=${REGISTRY_USER}
 --from-literal=password=${REGISTRY_PASSWD}
 -o yaml
```

You must override the `scan-service.tools.sync.existingSecret` Helm key
value with the name of this secret. This Helm key has no default value; it is simply
`""`. To add the secret name to this Helm key, refer to:

- Set Helm keys to enable scan tool synchronization
- scan-service.tools.sync Helm keys
