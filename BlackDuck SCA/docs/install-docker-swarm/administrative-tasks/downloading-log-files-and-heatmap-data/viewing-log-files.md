---
title: "Viewing log files"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-log-files.html"
content_id: "ik1bXrTEwmzvxv3ysDRL5w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.618990+00:00"
content_hash: "2643e6b3cfbfcbec53206fd829a293078dc9d07fe21080c83836a8b80717d836"
---

# Viewing log files

## Obtaining logs

To obtain logs from the containers:

```
docker cp <logstash container ID>:/var/lib/logstash/data logs/
```

where '`logs/`' is a local directory where the logs will be copied into.

## Viewing log files for a container

Use the docker-compose `logs` command to view all logs:

```
docker-compose logs
```

For more information on Docker commands, visit the Docker documentation website: <https://docs.docker.com/>

## Purging logs

Be default, log files are automatically purged after 14 days. To modify this value:

1. Stop the containers.
2. Edit the `docker-compose.local-overrides.yml`file located in the `docker-swarm` directory:
   1. Add the logstash service.
   2. Add the DAYS_TO_KEEP_LOGS environment variable with the new value. This example purges log files after 10 days:

      ```
      logstash: environment: {DAYS_TO_KEEP_LOGS: 10}
      ```
3. Restart the containers.
