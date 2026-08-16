---
title: "Changing the default server port"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/changing-the-default-server-port.html"
content_id: "nFcKxoM~XWY3hBZhAtosgw"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:30.201551+00:00"
---

# Changing the default server port

This section describes what you must change to use a different port if Alert will not be
running on the default port of 8443.

## Docker Swarm

For docker swarm, we need to make several changes to the local
`overrides` file controlling your Alert deployment:

- Define the new ports for the Alert service. Add 'ports' to the service
  description.

  ```
      alert: 
          ports: ['<NEW_PORT>:<NEW_PORT>']
  ```
- Configure the environment variables (`ALERT_HOSTNAME` and
  `ALERT_SERVER_PORT`).

  ```
      alert: 
          environment:
              - ALERT_HOSTNAME=localhost
              - ALERT_SERVER_PORT=<NEW_PORT>
  ```
- Change the health check to reference the new port. Add 'healthcheck' to the
  service
  description.

  ```
      alert:
          healthcheck:
                test: [CMD, /usr/local/bin/docker-healthcheck.sh, 'https://localhost:<NEW_PORT>/alert/api/about',
                       /opt/blackduck/alert/security/root.crt, /opt/blackduck/alert/security/blackduck_system.crt,
                       /opt/blackduck/alert/security/blackduck_system.key]
                interval: 30s
                timeout: 60s
                retries: 15
  ```

Below is a sample of what your `overrides` file should resemble.
**Note** that the service is exposed on port `9090` and the
`healthcheck` references the same port.

```
    alert:
        ports: ['9090:9090']
        environment:
            - ALERT_HOSTNAME=localhost
            - ALERT_SERVER_PORT=9090
        secrets:
            - ALERT_ENCRYPTION_PASSWORD
            - ALERT_ENCRYPTION_GLOBAL_SALT
        healthcheck:
            test: [CMD, /usr/local/bin/docker-healthcheck.sh, 'https://localhost:9090/alert/api/about',
                 /opt/blackduck/alert/security/root.crt, /opt/blackduck/alert/security/blackduck_system.crt,
                /opt/blackduck/alert/security/blackduck_system.key]
            interval: 30s
            timeout: 60s
            retries: 15
    secrets:
        ALERT_ENCRYPTION_PASSWORD:
            external: true
            name: "blackduck_ALERT_ENCRYPTION_PASSWORD"
        ALERT_ENCRYPTION_GLOBAL_SALT:
            external: true
            name: "blackduck_ALERT_ENCRYPTION_GLOBAL_SALT"
```

## Helm

For Helm installs, changing the server port is straightforward.

- Set the properties via the `values.yaml` file, change the value
  of the following properties followed by a `helm upgrade`
  command.

```
alert:
  hostname: localhost
  port: 8443
```

- Alternatively, the environs `ALERT_HOSTNAME` and
  `ALERT_SERVER_PORT` can be set via a `helm
  install` command.

```
--set environs.ALERT_HOSTNAME=localhost
```

- You must also change the healthcheck found under
  `/templates/alert.yaml` to point to the port you have
  specified otherwise the pod will exit due to the failed probe call to the now
  incorrect port.

```
        livenessProbe:
          exec:
            command:
              - /usr/local/bin/docker-healthcheck.sh
              - https://localhost:8443/alert/api/about
```

Tip: Work with your IT staff if necessary to verify the configured port
is accessible through the network.
