---
title: "Upgrading"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/upgrading.html"
content_id: "7mr6BBdOGdMA5Kr56oSAIw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:58.340043+00:00"
content_hash: "ecf74e0df73b0bb4294c9eff9d4778b4353076ff15b30ae1bcab5eb9a4c2f84c"
---

# Upgrading

During the upgrade process, the installer may present you with a list of issues. These
issues must be resolved to complete the process.

If you are performing an upgrade using the installer over SSH, it is recommended to use
`screen`, `tmux`, or similar to ensure the upgrade process
will continue if the SSH session is disconnected.

## Clean File System

The upgrade process expects only certain files and folders to exist in the
installation location. If you are presented with a list of files, do the
following:

- Open the installation directory (e.g., `C:\Program Files\Software Risk
  Manager` or `/opt/srm/`).
- Remove the specified files or folders but leave the backup folder
  (`backup-<timestamp>`), the
  `upgrade.ini` file, and the
  `properties.ini` file.

## Remove Services

On Windows, the upgrade process requires specific Software Risk Manager services.
Other Software Risk Manager services should be removed. If you are presented with a
list of services, you can remove them by doing the following:

- Open the “Command Prompt” application as an administrator.
- Remove the presented service:

```
> sc delete CodeDxMariaDB
[SC] DeleteService SUCCESS
```

Note: Replace CodeDxMariaDB with the service name that the installer
displays.

## Free Ports

The upgrade process requires certain ports to be available. If you are presented with
a list of ports, you can free them using the procedures shown below.

### Windows

1. Open the “Resource Monitor” application as an administrator.
2. Click the “Network” tab.
3. Click the “TCP Connections” bar to see a list of TCP connections
   established.
4. Look for one of the ports in the presented list.

To continue with the upgrade process, you have to make sure that the presented
ports are available. If the process using the required ports is a version of
Software Risk Manager, please follow the instructions in the "Remove Services"
section. If it is not related to Software Risk Manager, make sure to find the
conflicting program and ensure that the problem will not occur after
installation.

### Linux and OS X

List the processes listening to a TCP connection using terminal:

```
sudo lsof -iTCP:8009 -sTCP:LISTEN
COMMAND   PID    USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
java    81106  codedx   50u  IPv4 40576813      0t0  TCP *:8009 (LISTEN)
```

Note: Only use sudo if installed as root.

To continue with the upgrade process, you have to make sure that the presented
ports are available. You should stop the process that spawned the service and
ensure that the conflict will not occur after installation.
