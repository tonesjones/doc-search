---
title: "Using remote worker jobs to manage resource constraints"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-remote-worker-jobs-to-manage-resource-constraints.html"
content_id: "q7R3hUBcglvtudGk29butQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:25.189284+00:00"
---

# Using remote worker jobs to manage resource constraints

You can set up analysis to be assisted by worker jobs that run remotely, on other hosts, using the
Secure Shell Protocol (SSH).

Using remote workers is entirely optional.

## When are remote worker jobs useful?

Using remote worker jobs with SSH is most useful when you run an initial analysis
(*not* an incremental analysis) on a large C/C++ or CUDA®
project.

Remote worker jobs can also benefit customers whose most powerful analysis host has
fewer than 16 CPU cores. (This estimate might change in future releases.)

## Prerequisites for using remote workers

To set up remote worker jobs, the following conditions must be met:

- A worker host must be reachable from the main analysis host, via SSH.
- The main analysis host must be routable from a worker host (that is, there must
  be no intermediate, masquerading router).
- There must be no firewall rule that prevents the worker host from connecting to
  a TCP/IP socket on the main analysis host.
- The Coverity Analysis binaries must be installed on the worker
  host as well as on the main analysis host.
- On both the main host and the worker host, the Coverity Analysis installation must be the for the same version and platform: You cannot mix
  releases or architectures from one host to another.

A remote configuration can include more than a single worker host.

## Preparation for using remote workers

Make sure you have accomplished the following steps:

- Choose the main analysis host.

  The main analysis host should be one of the
  more powerful machines available, because it has to prepare work units for
  all worker hosts. If the main host falls behind, the worker hosts will have
  to wait.

  Note: The main analysis host is also the system
  that stores the intermediate directory.
- Choose the worker hosts.

  Avoid worker hosts that have a high latency or low
  bandwidth to and from the main analysis host: these will not perform well in
  a remote-hosting configuration.
- Set up the SSH program in advance. In a typical installation, the first time
  SSH connects to a remote host it displays an interactive prompt that asks for
  manual approval of the remote host key. You should perform this step by hand
  before you try to run Coverity Analysis using remote SSH
  workers.

  This interactive step only needs to be done once between any two
  hosts. After that, the connection should succeed on all future attempts.
- (Recommended:) Use an ssh-agent to manage the SSH keys. Connections are never
  made using passwords; authentication is only available with SSH keys.

  An
  alternative to an ssh-agent is to use explicit key files: but if a key file
  is used, it *must not* be passphrase-protected.
- Make a note of the number of CPU cores on *all host machines,* both the
  main host and the workers.

  Note: Simultaneous multithreading (SMT)
  such as the Intel® Hyper-Threading feature does not
  significantly improve the Coverity Analysis workload. In
  such an environment, take into account only the number of physical cores,
  and disregard the contribution of SMT.

## Configuring remote workers

To configure remote worker systems, go through these steps:

1. For each remote host, make a note of the following:
   - The number of physical CPU cores to be used
   - The installation path of Coverity Analysis (every
     directory that appears before bin/cov-analyze)
   - The username of the account that will run on the remote host, if this is
     different from the username on the main analysis host.
2. Verify that you can connect to each remote host. For example, if the remote
   host's IP address is 10.1.1.2, and the username on that host is
   `remote-user`, then the following shell-prompt command should
   return text without any further keyboard interaction (without prompting for host
   key verification, for a password, or for a passphrase):

   ```
   % ssh -l remote-user 10.1.1.2 echo "Success"
   ```

   ...
   If any interactive prompt appears, make the appropriate changes to your SSH
   configuration until this command can be run without human interaction.
3. Using your information about the configuration, including the information you
   noted in step 1, create an SSH configuration file.

   The SSH configuration file uses JSON syntax. Here is an example of such a file:

   ```
   {
       "ssh_config" : {
           "remoteHosts": [
               {
                   "host": "10.0.0.2",
                   "ssh-path": "/usr/bin/ssh",
                   "ssh-options" : [
                                       "-l",
                                       "remote-user"
                                   ],
                   "prevent-path": "/home/remote-user/Coverity",
                   "number-of-workers": 8,
               },
               {
                   "host": "10.0.0.3",
                   "connect-timeout": 10,
                   "ssh-path": "/usr/bin/ssh",
                   "prevent-path": "/usr/local/Coverity",
                   "number-of-workers": 4,
               },
           ],
           "number-of-local-workers": 6,
       }
   }
   ```

   This particular configuration file indicates that Coverity Analysis can be invoked on two remote hosts by running
   the following commands on the main analysis host:

   ```
   % /usr/bin/ssh -l remote-user 10.0.0.2 /home/remote-user/Coverity/bin/cov-analyze
   % /usr/bin/ssh 10.0.0.3 /usr/local/Coverity/bin/cov-analyze
   ```

   ... It also indicates that 10.0.0.2 can support 8 analysis worker jobs,
   while 10.0.0.3 should only run 4 such jobs. The main analysis host itself
   will, by default, run 6 workers.

See the following section, Fields for remote worker SSH configuration, for more
detailed descriptions of the fields that this file uses.

## Invoking remote workers

Once you have created a configuration file, as described in the previous section, you
can use the --cluster-config option to specify it when you invoke
`cov-analyze`. For example:

```
% cov-analyze <OPTIONS> --cluster-config <SSH-worker-config-file>>
```

**Interaction with the --jobs option:**

The `cov-analyze`
--jobs (or -j) option, described more fully in the
Coverity 2026.6.0 Command Reference, can help tune performance. This option has
a <number-of-workers> setting that controls the maximum
number of workers, both remote and local. It is subject to the following
constraints:

- <number-of-workers> cannot be less than the total number
  of remote workers in the configuration file.
- The <number-of-workers> value might be constrained
  because of limits imposed by the site license, or because of the CPU or memory
  resources available on the main analysis host.
- Specifying the <number-of-workers> causes
  --jobs to ignore the
  number-of-local-workers setting in the configuration file
  and to use, instead, a number equal to the total number of jobs requested minus
  the total number of remote worker jobs configured.

For example, using the sample configuration file shown above, if analysis were
invoked with --jobs 30, then there would be 18 local jobs created
along with the 12 remote jobs, for a total of 30 jobs. If analysis were invoked
without the --jobs option, 6 local jobs only would be created. If
it were invoked with --jobs 10 this would be an error, because
`cov-analyze` always attempts to create all the remote jobs
that have been configured.

## What happens when a host is unreachable?

If one or more of the remote hosts is unreachable, or if the settings are incorrect
(such as a bad username or an incorrect `prevent-path`), analysis
will still proceed as long as at least some workers, either remote or local, can be
started. However, performance will suffer.

CAUTION:

License constraints are not adjusted by the failure of some remote hosts to start up, and there is no compensation (for example, by adding local workers)
if remote workers are missing.

In this section:

- Fields for remote worker SSH configuration
