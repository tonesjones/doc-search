---
title: "coverity help"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-help.html"
content_id: "hxWF2MHVGZfJv~XDLQa_xg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:33.635413+00:00"
---

# coverity help

Display version or help information, or displays configuration
schema.

## Synopsis

```
coverity (-h | --help)
coverity (-v | --version | --ident)
coverity [options] <command> [<args>...]
```

## Description

Depending on the syntax variant used, the coverity help command displays
version information, adds debug messages, modifies output to desired format,
displays help for a particular command, or displays the configuration schema.

## Options

-h, --help
:   Displays the information in this section.

-q, --quiet
:   Display only error messages.

--machine-readable-output <style>
:   Set the output to be machine-readable.
    Style must be `"json"`.
    Use machine-readable output, useful for CICD.

--ticker-mode <style>
:   Sets the style of the ticker displayed during processing.
    Must be one of `"none"`, `"no-spin"`, or `"spin"`.
    Default: `"spin"`.

-v, --version, --ident
:   Display version.

-V, --verbose
:   Add debug messages to provide the highest level of detail possible.

## Commands

You can specify one of the following commands using the syntax variant that allows you to
specify a command:

| Command Type | Command Name | Description |
| --- | --- | --- |
| **Basic** | scan | Capture, analyze, and get a link to the analysis results. See coverity scan for arguments. |
|  | help | Display help for the specified command, or for configuration (`help config`), or display the information in this section if no command is specified. |
| **Advanced** | setup | Set up a new project. See coverity setup for arguments. |
|  | capture | Capture source files for analysis. See coverity capture for arguments. |
|  | analyze | Analyze captured source files. See coverity analyze for arguments. |
|  | commit | Send analysis results to the Connect server or to a local directory. See coverity commit for arguments. |
|  | list | List files that have been captured. See coverity list for arguments. |
|  | help config --schema | Display the file <*install-dir>/*`doc/configuration-schema.json`. |
|  | help config --syntax | Display the file <*install-dir>/*`doc/configuration-syntax.txt`. See Configuration syntax help. |
|  | help config [args] | You can specify the following arguments  - `-c, --config`   *file* Specify the configuration file whose contents   should be included in the example output. - `-o, --config-override`   *key=val* Key and value to override for inclusion in   the example output.  You can specify this option   multiple times. - `--format`   *format* Display configuration examples in the   specified format: `yaml`,   `yml`,   `json`.  Default:   `yaml`. - `--setting` *setting* Display an   example configuration file that includes the specified   setting.  You can specify this option multiple   times. - `--show-all` Display an example   configuration file that includes all possible   settings. |

## Example 1

The following command:

```
coverity help config --setting url -o commit.connect.stream=test1
```

would produce output like the following:

```
# Coverity configuration file.
# The schema is available here: <install-dir>/doc/configuration-schema.json
 
# Specifies where the analysis results should be sent.
commit:
 
  # Coverity Connect configuration to use when committing defects to Coverity
  # Connect.
  connect:
 
    # The name of the stream to commit the results to.
    stream: test1
 
    # Absolute URL of where to commit the Coverity Connect results.
    ##url: <value>
```

- Comments begin with a single "`#`" character followed by a
  space.
- Commented-out configuration settings begin with "`##`" and no
  following space.

Here is the equivalent JSON output:

```
{
  "_comment_configuration": "Coverity configuration file. The schema is available here: <install-dir>/doc/configuration-schema.json",
  "_comment_commit": "Specifies where the analysis results should be sent.",
  "commit": {
    "_comment_connect": "Coverity Connect configuration to use when committing defects to Coverity Connect.",
    "connect": {
      "_comment_stream": "The name of the stream to commit the results to.",
      "stream": "test1",
      "_comment_url": "Absolute URL of where to commit the Coverity Connect results.",
      "__url": "<value>"
    }
  }
}
```

JSON does not directly support comments, so for JSON output, comments consist of the
prefix`_comment_` followed by the name of the setting to which
the comment refers. Commented-out configuration settings begin with
`__`.

- If a setting is requested that occurs at more than one location within the
  schema (such as `file`), then all such locations are
  included.
- A non-leaf-level setting includes everything under that setting. For example,
  `--setting commit` would show the entire
  `commit` section of the configuration.
- If any item under a specified non-leaf-level setting is a map (such as
  `checker-config` whose keys are checker names, or
  `trust` whose keys are trust properties), then every
  setting below that level is commented out and `<name>` is
  used as the (commented-out) key.

## Example 2

The following command:

```
coverity help config --setting checker-config
```

would produce output like the following:

```
# Coverity configuration file.
# The schema is available here: <install-dir>/doc/configuration-schema.json
 
# Specifies how the project should be analyzed.
analyze:
 
  # If no checker configuration is specified, the CLI will enable a set of
  # checkers based on the files that were captured.
  checkers:
 
    # Map from checker name to configuration for the checker. The
    # configuration indicates whether the checker should be enabled or not and
    # allow users to set options used to configure the checker.
    checker-config:
      ##<name>:
 
        # Indicates whether this checker should be enabled or not.
        ##enabled: true
 
        # Options to set for each checker. The map key is the name of the
        # checker option and the string value is the setting to use for the
        # option.
        ##options:
          ##<name>: <value>
```

Leaf-level settings are shown with their default value, if there is one. If there is
no default but the valid values are defined by an enumerated list, then the first
item in the list is used. Otherwise, "`<value>`" is used.

Settings whose valid values are defined by an enumerated list are included in the
comment preceding the setting. The following example shows an instance of this:

```
# Coverity configuration file.
# The schema is available here: <install-dir>/doc/configuration-schema.json
 
# Specifies where the analysis results should be sent.
commit:
 
  # Coverity Connect configuration to use when committing defects to Coverity
  # Connect.
  connect:
 
    # Indicates whether to trust self-signed certificates presented by Coverity
    # Connect that are not currently trusted.
    # Valid values:
    #   trust
    #   distrust
    ##on-new-cert: trust
```

Configuration files generated by `coverity setup` include the same
comments as are included by `coverity help config`.
