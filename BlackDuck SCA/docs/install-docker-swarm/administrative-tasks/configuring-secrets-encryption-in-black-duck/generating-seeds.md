---
title: "Generating seeds"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/generating-seeds.html"
content_id: "CcylFeKBXX10jrXGvlb9Ng"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.358461+00:00"
content_hash: "fe4dc1f2b3f2b7c452679243a7f139b97a91804281e1c5cd2c5817638bbd1a00"
---

# Generating seeds

## Generating seeds in OpenSSL

The content of the seeds can be generated using any mechanism that generates secure random contents at least 1024 bytes long. As soon as a seed has been created and saved in a secret, it should be removed from your file system and saved in a private, secure location.

The OpenSSL command is as follows:

```
openssl rand -hex 1024 > root_seed
```

## Generating seeds in Docker Swarm

In Docker Swarm, Black Duck must be stopped in order to create and delete secrets. The Docker Swarm command is as follows:

```
docker secret create crypto-root-seed ./root_seed
```

In Docker Swarm, a secret configured in the orchestration files must exist and it cannot be zero length. To work around this restriction, Black Duck treats "placeholder" encryption seeds of 2 or less bytes as if they do not exist. As such, the previous key secret can be deleted in Docker Swarm with the following command:

```
echo -n "1" | docker secret create crypto-prev-seed –
```

Once cryptography is enabled via the orchestration files, the three seed secrets must be created with commands analogous to those shown here, before enabling Black Duck secrets encryption; see sample scripts.
