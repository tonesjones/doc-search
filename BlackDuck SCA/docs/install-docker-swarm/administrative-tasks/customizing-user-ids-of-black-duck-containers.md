---
title: "Customizing user IDs of Black Duck containers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/customizing-user-ids-of-black-duck-containers.html"
content_id: "6OxSPVDgQJ0UGUQVp3bTIg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:01.446450+00:00"
---

# Customizing user IDs of Black Duck containers

You may need to change the user ID (UID) under which a container runs.

The current UID for each container is:

- Authentication (blackduck-authentication): 100
- Binaryscanner (bdba-worker): 0
- CA (blackduck-cfssl): 100
- DB (blackduck-postgres): 1001
- Documentation (blackduck-documentation): 8080
- Job Runner (blackduck-jobrunner): 100
- Logstash (blackduck-logstash): 100
- RabbitMQ (rabbitmq): 100
- Registration (blackduck-registration): 8080
- Scan (blackduck-scan): 8080
- Web App (blackduck-webapp): 8080
- Webserver (blackduck-nginx): 100
- Redis (blackduck-redis): run as any user/group
- Bomengine (blackduck-bomengine): 100
- Matchengine (blackduck-matchengine: 100

Changing the UID consists of adding the new value for a container to the
`docker-compose.local-overrides.yml` located in the
`docker-swarm` directory. Add the

`user:UID_NewValue:root` line in the container's section.

The following example changes the UID for the webapp container to 1001:

webapp:

user: 1001:root

Note the following:

- The UID for the postgres container and binaryscanner *cannot* be changed.
  - The UID for the postgres container must equal 1001.
  - The UID for the binaryscanner container must equal 0 (root).
- Although some containers have the same UID value (for example, the Documentation,
  Registration, Scan, and Web App container each has a UID of 8080), changing the
  UID value of one container does *not* change the UID value for the
  containers that have the same UID value. For example, changing the value of the
  Web App container from 8080 to 1001 does not change the value of the
  Documentation, Scan, or Registration containers – the UID value for these
  containers remains 8080.
- The containers expect that whichever user the container runs as, the user must
  still be specified as being in the root group.

To customize the UID:

1. Bring down
   Black Duck.
2. Edit the value as described above.
3. Bring up
   Black Duck.
