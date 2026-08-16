---
title: "Managing secret rotation"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-secret-rotation.html"
content_id: "oNMeJ~9G8UATueX1omHG~w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:06.524669+00:00"
---

# Managing secret rotation

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

## Secret rotation in Docker Swarm

For Docker Swarm, Black Duck must be stopped, the three seed operations performed,
and then Black Duck started up again. The root seed extracted from the running Black
Duck instance as the previous seed, `extractRootAsPreviousSeed.sh`.
See the Docker Swarm sample script
`rotateRootSeed.sh`.

After the rotation completes the previous seed secret should be removed; see sample script
`cleanupPreviousSeed.sh`. In Docker Swarm, the system must be brought
down, the previous key removed and then Black Duck started up again.

The state of the rotation can be tracked by looking at crypto diagnostics tab, in the
user interface by going to Admin > System Information > crypto.
