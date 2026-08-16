---
title: "Provisioning JWT public/private key pairs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/provisioning-jwt-public/private-key-pairs.html"
content_id: "_WThSBohZP5CjqCUJWZipQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:22.683718+00:00"
---

# Provisioning JWT public/private key pairs

To enhance the security and flexibility of JWT management, our system now supports the
optional provisioning of public/private key pairs. This allows you to securely provide
and manage these keys, ensuring they are only used by the appropriate services, such as
the Authentication service for private keys and public API services for public keys.

Currently, only RSA keys (PEM encoded) are supported. Specifically, public keys must be
in X.509 format, and private keys must be in PKCS#8 format.

## Creating Kubernetes secrets

1. Create Kubernetes secret (template command). Exact files must be provided for the
   public and private key options.

   ```
   kubectl create secret generic -n <namespace> <name>-blackduck-jwt-keypair --from-file=JWT_PUBLIC_KEY=public_key_file --from-file=JWT_PRIVATE_KEY=private_key_file
   ```

   Here is an sample command if `namespace` = `bd`
   and `name` = `hub`:

   ```
   kubectl create secret generic -n bd hub-blackduck-jwt-keypair --from-file=JWT_PUBLIC_KEY=public-key.pem --from-file=JWT_PRIVATE_KEY=private-key.pem
   ```
2. Confirm secret created in `namespace`:

   ```
   kubectl get secrets -n <namespace>
   ```

   The expected output would be what follows, if `namespace` =
   `bd` and the secret name =
   `hub-blackduck-jwt-keypair`:

   ```
   kubectl get secrets -n bd
   NAME                        TYPE     DATA   AGE
   hub-blackduck-jwt-keypair   Opaque   2      7s
   ```
3. Uncomment the following line in `values.yaml` and edit
   `name` accordingly with the secret name:

   ```
   jwtKeyPairSecretName: <name>-blackduck-jwt-keypair
   ```
4. Deploy Black Duck in the same
   `namespace`. For example:

   ```
   helm install bd . --namespace bd -f values.yaml -f sizes-gen04/10sph.yaml --set exposedNodePort=30000 --set environs.PUBLIC_HUB_WEBSERVER_PORT=30000
   ```
