---
title: "Create a container image pull secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-container-image-pull-secret.html"
content_id: "padfd90zxoEkSo_HQqeIMQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:39.880151+00:00"
---

# Create a container image pull secret

Coverity cloud container images must be kept in a private Docker registry that requires
secure credentials to access. This registry can be the Black Duck private Docker registry or a private Docker registry
that you have created. See also Obtaining Black Duck Community access, Coverity licenses, registry credentials, Helm chart, and client software. You need to
create a secret that contains credentials needed for the Kubernetes cluster to access
the registry. You can create a secret using the `kubectl create secret
docker-registry` command. The secret must exist in the Coverity namespace.

Command syntax to create a secret to pull Docker images:

```
kubectl create secret docker-registry ${RegistrySecretName} \
--docker-server=<docker-registry(gcr.io|repo.blackduck.com)> \
--docker-username=${username} \
--docker-password=${password} \
--namespace ${namespace}
```

| Variable | Meaning | Notes |
| --- | --- | --- |
| `${RegistrySecretName}` | Assign a unique name for this secret. | Example: ContainerImagesSecret |
| ${docker-registry(gcr.io|repo.blackduck.com)} | Black Duck registry. | Example: gcr.io|repo.blackduck.com |
| `${namespace}` | Provide the Coverity namespace. | Example: cnc |
| `${registryUsername}` | Provide the username to access the registry. | For Black Duck private Docker registry credentials, see Access the Black Duck private Docker registry credentials. |
| `${registryPassword}` | Provide the password to access the repository. |

For further information on creating a Docker image pull secrets and private Docker
registry, refer to the Kubernetes page <https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod>.

You must override the `imagePullSecret` Helm key value with the name of
this secret. This Helm key has no default value; it is simply `""`. To
add the secret name to this Helm key, refer to:

- imagePullSecret keys
