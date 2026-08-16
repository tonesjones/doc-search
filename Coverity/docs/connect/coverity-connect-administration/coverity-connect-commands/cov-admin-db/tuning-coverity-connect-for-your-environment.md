---
title: "Tuning Coverity Connect for your environment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tuning-coverity-connect-for-your-environment.html"
content_id: "RvM8na7hdXWNTpEcLYfDDg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:14.084954+00:00"
---

# Tuning Coverity Connect for your environment

The `cov-admin-db tune` command is used by the installer at install time
to adjust your Coverity Connect database and JVM settings for best performance.

After the product is installed, you can use the `cov-admin-db tune`
subcommand to retune Coverity Connect. You might want to retune for reasons like the
following:

- Your environment has changed, and you want to retune the system in response to
  those changes.
- To restrict use of available resources.

Command syntax provides the following options:

```
cov-admin-db tune
    {[--read]|[--show-profile]|[--suggest]|[--write]}
    [--debug]
```

| Option | Use |
| --- | --- |
| `--read` | Reads the current tune settings and displays them. |
| `--show-profile [[<key>=<value>]...]` | Displays the profile that describes the current environment: hardware and OS settings.  Use the `<key=value>` expression to override current profile settings. |
| `--suggest [[<key>=<value>]...]` | Calculates optimal Coverity Connect tuning values based on the current profile and displays what would be written to the settings files with a subsequent `cov-admin-db --write` command.  Use the `<key=value>` expression to provide alternate values for profile settings. |
| `--write [[<key>=<value>]...]` | Calculates optimal Coverity Connect tuning values based on current profile settings and writes them to the settings files.  Use the `<key=value>` expression to provide alternate values for profile settings.  You must restart Coverity Connect for these settings to take effect. |

The subcommand assembles a description of the available resources, called a
*profile*, which is a collection of settings. The profile isn't stored, but it
is used with the `--show-profile`, `--suggest`, and
`--write` options.

Profile settings include the following:

| Setting | Meaning |
| --- | --- |
| `isExternalDb` | Boolean: true if the database disk is external (not embedded). |
| `isSsd` | Boolean: true if the database disk is an SSD. |
| `mode` | Use "default". |
| `os` | "Windows" or "Linux" |
| `physicalMemory` | Physical memory in gigabytes. |
| `processorCount` | Number of cores. |
| `tomcatMemoryFraction` | A number between 0 and 1 that indicates the proportion of memory to allocate to the Coverity Connection Web application. |

Profile settings are derived from three sources (arranged from lowest to highest
precedence):

1. The current environment detected by the application, which is overridden by
2. Values provided on the `cov-admin-db tune` command line using
   `<key=value>`, which are overridden by
3. Values set using environment variables

For example, the following sequence of commands illustrate how profile settings can be
overridden:

```
$ cov-admin-db tune --show-profile
isExternalDb = false
isSsd = false
mode = default
os = Linux
physicalMemory = 16g
processorCount = 12
```

Entering the following command:

```
$ cov-admin-db tune --show-profile processorCount=10
```

Displays the profile as follows:

```
isExternalDb = false
isSsd = false
mode = default
os = Linux
physicalMemory = 16g
processorCount = 10
```

Executing the following commands

```
$export physicalMemory=10g
```

```
$ cov-admin-db tune --show-profile physicalMemory=20g
```

Displays the physical memory of 10g because the environment variable setting overrides
the command line setting.

```
isExternalDb = false
isSsd = false
mode = default
os = Linux
physicalMemory = 10g
processorCount = 10
```

How you use tune options depends on your use case:

- If your environment has changed and you simply want to retune your system for
  these changes, use the `cov-admin-db tune --write` command.
- If you want to retune for testing or to limit the use of available resources, use
  the `cov-admin-db tune --write <key=value>` command.

Note: Remember to restart Coverity Connect after retuning.

## Understanding the Difference Between `--write` and `--suggest`

This section explains how system settings are derived from the system profile, and
how you use the `--suggest` and `--write` options to
display or change these settings.

1. As mentioned before, the system's profile is assembled from three sources:
   current settings, values set on the `cov-admin-db` command
   line, and values set using environment variables.

   To display the profile use the `--show-profile` option.
2. A calculator is chosen based on the profile's `mode` setting.
   (The `default` mode is normally the one used.)
3. The profile is provided as input to the calculator.
4. Based on this input, the calculator outputs a collection of settings for the
   JVM and database.

   - `--suggest` outputs these settings to the console.
   - `--write` writes these settings to their configuration
     files.
