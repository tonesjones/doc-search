---
title: "Managing secret rotation in Kubernetes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-secret-rotation-in-kubernetes.html"
content_id: "32FoENxW5KoccN9QMIbKmw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:18.661884+00:00"
---

# Managing secret rotation in Kubernetes

It is good practice to rotate the root seed in use on a periodic basis according to
your organization’s security policy. In order to do this, an additional secret is
necessary to perform the rotation. To rotate the root seed, the current root seed is
configured as the “previous root seed”, and a newly generated root seed is generated
and configured as the root seed. Once the system processes this configuration
(specifics below), the secrets will have been rotated.

At that point in time both the old and the new seeds are able to unlock the system
contents. By default, the new root seed will be used, allowing you to test and make
sure the system is working as intended. Once everything has been verified, you
complete the rotation by removing the “previous root seed”.

Once the previous root seed is removed from the system it can no longer be used to
unlock the contents of the system and can be discarded. The new root seed is now the
proper root seed which should be backed up and secured appropriately.

The root key is used to wrap the low-level TDEKs (tenant decrypt, encrypt key) that
actually encrypt and decrypt Black Duck secrets. Periodically, at times convenient
for Black Duck administrators and conforming to user organization rules, the root
key should be rotated.

The procedure to rotate the root key would be create a previous seed secret with the
contents of current root seed. Then a new root seed should be created and stored in the
root seed secret.

## Secret rotation in Kubernetes

For Kubernetes the three operations can be done with the Black Duck running. The
Kubernetes sample script `rotateRootSeed.sh` will extract the root
seed into `prev_root`, create a new root seed and then recreate the
previous and root seeds.

After the rotation completes the previous seed secret should be removed; see sample script
`cleanupPreviousSeed.sh`. Again, this cleanup can be performed on a
running Kubernetes Black Duck instance.

The state of the rotation can be tracked by looking at crypto diagnostics tab, in the
user interface by going to Admin > System Information > crypto.
