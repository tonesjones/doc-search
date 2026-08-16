---
title: "Configuring a backup seed"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-a-backup-seed.html"
content_id: "hEBl7zF_eQZBG434C31qOw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:05.955175+00:00"
---

# Configuring a backup seed

Having a backup root seed is recommended to ensure the system can be recovered in a
disaster recovery scenario. The backup root seed is an alternative root seed that can be
put in place in order to recover a system. Consequently, it must be stored securely in
the same way as a root seed.

The backup root seed has some special features in that once it is associated with the
system, it remains viable even across root seed rotations. Once a backup seed is
processed by the system, it should be removed from the secrets to limit its exposure
to attacks and leakage. The backup root seed may have a different (less often)
rotation schedule as the secret should not be “active” in the system at any point in
time.

When you need or want to rotate a root seed, you first need to define the current root
seed as the previous root seed. You can then generate a new root seed and put that in
place.

When the system processes these seeds, the previous root key will be used to rotate
resources to use the new root seed. After this processing, the previous root seed should
be removed from the secrets to complete the rotation and clean up the old resources.

## Creating a backup root seed

Once created initially, the backup seed/key wraps the TDEK (tenant decrypt, encrypt key)
low-level key. The sample script `createInitialSeeds.sh` will create both
a root and a backup seed. Once Black Duck is running, it uses both keys to wrap the
TDEK.

After that operation is complete and both the root and backup seeds are securely
stored elsewhere, the backup seed secret should be deleted; see sample script
`cleanupBackupSeed.sh`.

If the root key is lost or leaked, the backup key can be used to replace the root
key; see sample script
`useRootSeed.sh`.

## Rotating the backup seed

Similarly to the root key, the backup seed should be rotated periodically. Unlike for
the root seed, where the old root seed is stored as a previous seed secret and a new
root seed secret presented to the system, the backup seed is rotated just by
creating a new backup seed. See the sample script
`rotateBackupSeed.sh`.

After the rotation is complete, the new backup seed should be stored securely and removed
from the Black Duck host file system.
