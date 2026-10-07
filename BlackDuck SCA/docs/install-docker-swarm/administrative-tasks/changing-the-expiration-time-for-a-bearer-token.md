---
title: "Changing the expiration time for a bearer token"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-the-expiration-time-for-a-bearer-token.html"
content_id: "0~Ua6OH6RCNdR~VYGepQYg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.319180+00:00"
content_hash: "dd35c6fe61cd229168e01202667b59c51c55dfece5affb948fb050736d9c6970"
---

# Changing the expiration time for a bearer token

To extend the expiration time of a bearer token used in REST API, use the `docker-compose.local-overrides.yml` file to override the default setting by configuring the `HUB_AUTHENTICATION_ACCESS_TOKEN_EXPIRE` environment variable with the new expiration value in seconds.

The `HUB_AUTHENTICATION_ACCESS_TOKEN_EXPIRE` property is the number of seconds that the access tokens take to expire.

Note: The expiration configuration change only works for API tokens that are created after you change the setting in the `docker-compose.local-overrides.yml` file. The expiration time that you configure isn't updated for existing database records/API tokens when the setting is changed and the service is restarted.
