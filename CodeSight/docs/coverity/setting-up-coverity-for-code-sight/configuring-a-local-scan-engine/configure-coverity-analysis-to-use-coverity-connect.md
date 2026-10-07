---
title: "Configure Coverity Analysis to use Coverity Connect"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/configure-coverity-analysis-to-use-coverity-connect.html"
content_id: "O4P6OrwlOU4sQLeGg6cSqA"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.564345+00:00"
---

# Configure Coverity Analysis to use Coverity Connect

To connect to a particular Coverity Connect server, a client system needs to locally specify
some setup information.
In addition, before a client can connect to it, the Coverity Connect server must be set up
to support Code Sight clients.

This section and the one that follows explain the setup steps for both client systems and the server that they use.

## Client-side configuration for Coverity Connect

To configure a client system so that Code Sight can connect to a particular Coverity Connect server,
you need to specify that server on the local client systems. There are two ways to do so.

## 1. Use Coverity CLI configuration options (recommended)

1. When you create a new Coverity scan configuration, choose the Coverity (.yaml, .json) option.
2. Create a configuration file for Coverity scans.
   This file can be in either YAML or JSON format.
3. Save the configuration file to your working directory.
4. In the configuration file, specify the server and the stream to use.

   For example, if the file is in JSON format, it might specify:

   ```
       "settings": {
           "server": {
               "url": "https://coverity-server.example.com:443",
               "ssl": true,
               "on_new_cert": "trust"
           },
           "stream": "myProjectsStreamName"
       }
   ```

For more information, see Coverity scan configurations and custom scan settings

## 2. Use a coverity.conf file

While we recommend using Coverity CLI settings, Code Sight continues to support coverity.conf,
and if your configuration has already been set up this way, it makes sense to continue doing so.

The coverity.conf file is in JSON format.

**Best Practice:**
A development team should share common settings, so create a project-specific
coverity.conf file.
Then check it in to your code repository so each developer can download the same configuration.

1. The coverity.conf file should contain the following object:

   ```
   {
       "type": "Coverity configuration",
       "format_version": 1,
       "format_minor_version": 7,
       "settings": {
           "server": {
               "url": "https://coverity-server.example.com:443",
               "ssl": true,
               "on_new_cert": "trust"
           },
           "stream": "myProjectsStreamName"
       }
   }
   ```
2. Change the value of the `"url"` field in the `"server"`
   object to point to your Coverity Connect server.
   The `"url"` string must include the protocol, `http://` or `https://`,
   and the port.

   The port value defaults to 80 for a nonsecure server (`http`)
   or 443 for a secure server (`https`).
3. Change the value of the `stream` field to the name of the Coverity Connect stream that
   your project is using.
4. Save the file to the root directory of your project’s code repository.
5. Commit the edited coverity.conf file to your code repository so that
   all users will share the same settings automatically.
