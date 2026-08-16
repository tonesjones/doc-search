---
title: "Increasing the size of the binary scan file"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/increasing-the-size-of-the-binary-scan-file.html"
content_id: "~6wKSKs5aDZY14O9gN9HdQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:42.562077+00:00"
---

# Increasing the size of the binary scan file

When using Black Duck Binary Analysis, the maximum size of the binary that can be scanned
is 100 GB. You can increase this limit by adding the environment variable
`BINARY_UPLOAD_MAX_SIZE` to the
`docker-compose.local-overrides.yml` file or by setting this globally
in `blackduck-config.env` and specifying a value in megabytes.

For example, to increase the maximum binary scan to 10 GB, add the following:

```
webserver:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240m
storage:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240m
scan:
    environment:
        BINARY_UPLOAD_MAX_SIZE: 10240m
```

After updating the file when deploying the stack, ensure that the
`docker-compose.local-overrides.yml` file is included as a command
line parameter in the deploy command:

```
docker stack deploy -c docker-compose.yaml -c ... -c docker-compose.local-overrides.yml
```
