---
title: "Configuring the keepalive setting"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-the-keepalive-setting.html"
content_id: "HcHZtTQCN741kXq_OlUGzg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:34.599786+00:00"
---

# Configuring the keepalive setting

The `net.ipv4.tcp_keepalive_time` parameter controls how long an
application will let an open TCP connection remain idle. By default, this value is 7200
seconds (2 hours).

For optimal Black Duck performance, this parameter should have a value
between 600 and 800 seconds.

This setting can be configured before or after Black Duck is
installed.

To edit the value:

1. Edit the `/etc/sysctl.conf` file. For example:

   ```
   vi /etc/sysctl.conf
   ```

   You can also use the `sysctl` command to modify this file.
2. Add the `net.ipv4.tcp_keepalive_time` (if the parameter is not in
   the file) or edit the existing value (if the parameter is in the file).

   ```
   net.ipv4.tcp_keepalive_time = <value>
   ```
3. Save and exit the file.
4. Enter the following command to load the new setting:

   ```
   sysctl -p
   ```
5. If Black Duck is installed, restart it.
