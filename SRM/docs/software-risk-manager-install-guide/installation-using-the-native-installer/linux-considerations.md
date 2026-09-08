---
title: "Linux Considerations"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/linux-considerations.html"
content_id: "BjEGTG5rOPkzcBDA8iN61g"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:47.922138+00:00"
content_hash: "1b6a3a7ddc30b4d0414809967a371c4ecb8f4de4cff8ad7487e6c89d239c11ba"
---

# Linux Considerations

For headless Linux environments, the installer comes with an option to interact from the
command line. To do so, run the installer with the `--mode text`
option.

For example:

```
./srm-<version>-linux-x64-installer.run --mode text
```

where you substitute the installer version number for "version."

The installer behaves differently depending on whether it is executed by the root user
(or with sudo privileges) or by a standard user. The default directories will change and
the port numbers used for the installation will also be different (port 80 for HTTP
access for instance when using the root user vs. port 8080 for non-root users). For
production installations, we strongly recommend triggering the installer with root/sudo
privileges.

By default, Software Risk Manager does not automatically start up on Linux systems. In
order to have Software Risk Manager start and stop cleanly when the system boots and
shuts down, several commands need to be executed depending on distribution.

Note: Running on start up is only supported for root installations and assumes
commands are run with root privileges.

## Run on Start Up for Debian-based Distributions

Copy `ctlscript.sh` to the `/etc/init.d` directory and
name it `codedx`. `ctlscript.sh` can be found in the
Software Risk Manager installation folder. By default this will be in
`/opt/srm`.

```
cp installdir/ctlscript.sh /etc/init.d/codedx
```

Then make the script executable.

```
chmod +x /etc/init.d/codedx
```

Add the following to the top of the codedx file below `#!/bin/bash` to
ensure that the script is compatible with systemd.

```
### BEGIN INIT INFO
# Provides:          codedx
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start SRM services at boot time
# Description:       Enable services required by SRM at startup.
### END INIT INFO
```

Enable the service to run by default

```
systemctl enable codedx
```

Following a reboot, Software Risk Manager should start automatically. To revert these
changes, SRM can be removed from the startup services with the following
commands:

```
cd /etc/init.d
systemctl disable codedx
```

## Run on Start Up for RedHat-based Distributions

Copy `ctlscript.sh` to the `/etc/init.d` directory and
name it `codedx`. `ctlscript.sh` can be found in the
Software Risk Manager installation folder. By default this will be in
`/opt/srm`.

```
cp installdir/ctlscript.sh /etc/init.d/codedx
```

Replace the `#!/bin/bash` at the top of the file with the
following:

```
#!/bin/bash
#
# chkconfig: 2345 80 30
# description: SRM services
```

Then install the script as a service.

```
chkconfig --add codedx
```

After a reboot, Software Risk Manager will start up automatically. To revert these
changes, Software Risk Manager may be removed from the startup services with the
following command:

```
chkconfig --del codedx
```
