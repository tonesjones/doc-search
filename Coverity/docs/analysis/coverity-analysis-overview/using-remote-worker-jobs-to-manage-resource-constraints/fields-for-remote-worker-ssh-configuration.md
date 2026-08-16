---
title: "Fields for remote worker SSH configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fields-for-remote-worker-ssh-configuration.html"
content_id: "F3BulXXeUBok4LWUbsCObA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:25.840531+00:00"
---

# Fields for remote worker SSH configuration

The top-level JSON fields are as follows:

`ssh-config`
:   Marks a section and informs Coverity Analysis that this cluster
    configuration file is for SSH worker systems. It must always be present when
    configuring remote workers.

`number-of-localworkers`
:   The number of analysis workers that will run on the main analysis host. This
    value can be overridden by the `cov-analyze`
    --jobs option. This field is optional.

`remoteHosts`
:   An object that lists one or more individual remote hosts. This field is
    optional, but omitting it means that no remote hosts will be used, which makes
    the entire configuration file unnecessary.

The following fields describe an individual remote host:

`host`
:   The name or IP address of the remote host. This field is mandatory.

`connect-timeout`
:   The number of seconds in which to attempt an SSH connection before deeming the
    host unreachable.

    This field is optional. If it is absent, Coverity Analysis will wait for the TCP connection to time
    out, which is a function of a platform-dependent value.

`ssh-path`
:   The path name of the SSH binary.

    This field is optional. If it is absent, Coverity Analysis uses the value `ssh`, and
    assumes that `ssh` is defined in the system PATH.

`ssh-options`
:   This field is optional. If it is present, it must be a JSON array of option values.
    The options will be appended to the SSH command in the order in which they appear in the array.
    This field can be used to supply a username, keyfile name, non-standard port
    number, or other SSH options.

    Like other SSH fields, this field must appear only once.

`prevent-path`
:   The installation path of Coverity Analysis on the SSH host.
    The `cov-analyze` binary will be found at
    <prevent-path>/bin/cov-analyze. This field is
    mandatory.

`number-of-workers`
:   The number of worker jobs that should execute on this host. This field is
    mandatory.

    Important:
    Unlike the way it handles the main analysis host, Coverity Analysis does not examine the memory and CPU
    resources of a remote host to make sure that this number is reasonable.
    The SSH worker mode is intended for advanced users who are expected to be able
    to account for these factors.
