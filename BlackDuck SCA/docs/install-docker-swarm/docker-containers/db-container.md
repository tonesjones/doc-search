---
title: "DB container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/db-container.html"
content_id: "Tsl8TvresxOOr_PWpu6I_w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:20.989812+00:00"
---

# DB container

Note: This container is not included in the Black Duck application if you use an
external Postgres instance.

| Container Name: blackduck-postgres | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-postgres:9.6-1.1 |
| Description | The DB container holds the PostgreSQL database which is an open source object-relational database system. The application uses the PostgreSQL database to store data.  There is a single instance of this container. This is where all of the application's data is stored. There are two sets of ports for Postgres. One port will be exposed to containers within the Docker network. This is the connection that the application will use. This port is secured via certificate authentication. A second port is exposed outside of the Docker network. This allows a read-only user to connect via a password set using the `hub_reportdb_changepassword.sh` script. This port and user can be used for reporting and data extraction.  Refer to the *Report Database* guide for more information on the report database. |
| Scalability | There should only be a single instance of this container. It should not be scaled. |
| Links/Ports | The DB container needs to connect to these containers/services:   - logstash - cfssl   The container needs to expose port 5432 to other containers that will link to it within the Docker network.  This container exposes port 55436 outside of the Docker network for database reporting. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resource/Constraints | - Default max Java heap size: N/A - Container memory: 3GB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 1001. If the container is started as UID 0 (root) then the user will be switched to UID 1001:root before executing its main process.  This container is not able to start with any other user id. |
| Environment File | N/A |
