---
title: "Customizing Software Risk Manager"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/customizing-software-risk-manager.html"
content_id: "va7NXx0u3f1_Y5qyxZMhDw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:08.664929+00:00"
content_hash: "97f624bb0e59f8a60f9f9a053d0d373e661c945e5ab3c81cf052d7d2649ae298"
---

# Customizing Software Risk Manager

You can customize Software Risk Manager's behavior by specifying certain configuration
properties.

## Custom Props

Software Risk Manager features can be customized through the configuration file
`codedx.props` which, by default, is located in your Tomcat container at
`/opt/codedx`. (A full list of configuration parameters and how to change
them can be found in the section on using the native installer.)

For example, to automatically sign a user out after 15 minutes of inactivity (20 minutes by
default), set `session.lifetime` to `15 minutes`.

**To set the sign-out property in a Docker Compose install:**

1. With Software Risk Manager up and running, copy its `codedx.props` file
   to your current working directory using the following `docker cp`
   command, replacing the `srm-docker-codedx-tomcat-1` Docker container name
   as necessary (you can list running Docker containers with `docker ps`):

   ```
   docker cp srm-docker-codedx-tomcat-1:/opt/codedx/codedx.props .
   ```
2. Edit your local `codedx.props` file by appending the following line:

   ```
   session.lifetime = 15 minutes
   ```
3. Copy `codedx.props` back to its original location, replacing the
   `srm-docker-codedx-tomcat-1` Docker container name as necessary:

   ```
   docker cp codedx.props srm-docker-codedx-tomcat-1:/opt/codedx/codedx.props
   ```
4. Restart the SRM web container by running the Docker Compose `down` and
   `up` commands that you use for your deployment.

## Custom Context Path

By default, Software Risk Manager is accessible at `/srm`. For backward
compatibility, requests to `/codedx/api` and `/codedx/x` will
be rewritten to `/srm/api` and `/srm/x` respectively, and
requests to `/codedx` will be redirected to `/srm`.

You can change the Software Risk Manager context path by setting the SRM_WEBAPP_NAME
environment variable in your Docker Compose file. The following example changes the default
context path from `/srm` to `/mysrm`:

```
    codedx-tomcat:
        image: ...
        environment:
            DB_URL: ...
            SRM_WEBAPP_NAME: "mysrm"
```

With this configuration, you can access Software Risk Manager at
`hostname/mysrm` after restarting Software Risk Manager. URL rewrites and
redirects from `/codedx` become disabled when using a custom context
path.
