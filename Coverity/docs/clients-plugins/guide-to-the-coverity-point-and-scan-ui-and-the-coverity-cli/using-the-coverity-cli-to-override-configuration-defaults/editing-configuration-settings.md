---
title: "Editing configuration settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/editing-configuration-settings.html"
content_id: "fBUxjOCPCB509bm_kmdF8Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:26.381159+00:00"
---

# Editing configuration settings

You can use the `-o` or `--config-override` options to access any
configuration setting in the configuration file from the command line.
You can also use the --setup-override option to the `setup` subcommand.

This interface does not support removing values from the configuration file; only adding or overriding
values is supported.

If the configuration setting specified on the command-line does not exist in the
configuration file, the setting specified on the command-line is created in the
configuration such that the effective configuration is as if the setting had been
specified in the configuration file. If the configuration setting specified on the
command-line exists in the configuration file, the setting in the configuration file is
overridden by the one specified on the command-line.

Note:
Any value specified on the command-line must refer to a scalar value in the
configuration: it is not possible to specify the value for a complex data structure such
as an object, map, or list on the command-line.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

**Syntax**

```
-o key-path=value
```

```
--config-override key-path=value
```

```
--setup-override key-path=value
```

These options can be used with all Coverity CLI subcommands except the `help` options
aside from `coverity help config`.

The key-path specifies the path to the setting in the configuration
file and the `value` specifies the value for the configuration setting.
For example, the following argument would set the value for capture encoding:

```
coverity scan -o capture.encoding=UTF-8
```

**Handling lists**

To override a specific setting in a list, use array index notation to specify the element
of the list to override:

```
coverity scan -o "capture.build.cov-build-args[1]=--no-parallel-translate"
```

It is an error to specify an array index for a list element that doesn't exist.

Some lists are actually a list of other complex data-structures such as other objects in
which case the path to the target setting must be specified after the array index:

```
coverity scan -o "capture.files.webapp-archives[0].path=target/custom-output/my-webapp.war"
```

To add new settings to the end of an existing list, simply specify the values to be added
without an array index:

```
coverity scan -o capture.build.cov-build-args=--no-parallel-translate
```

The above would simply add `--no-parallel-translate` to the end of the
list of `cov-build-args`.

If the configuration file did not have any existing "cov-build-args" configured then a
new list would be created in the effective configuration with "--no-parallel-translate"
as the only entry. Of course, if additional values were specified then they would be
used to form the complete list:

```
coverity scan -o capture.build.cov-build-args=--instrument -o capture.build.cov-build-args=--no-parallel-translate
```

In the example above, the `cov-build-args` would be passed to
`cov-build` in the order they appear on the command-line.

To create or append to a list of complex types on the command-line, the values for each
element must be specified consecutively before values for the next element are
specified:

```
coverity scan -o capture.files.webapp-archives.path=target/custom-output/my-webapp.war \
              -o capture.files.webapp-archives.validate-webapp=false\
              -o capture.files.webapp-archives.path=target/custom-output/my-other-webapp.war \
              -o capture.files.webapp-archives.validate-webapp=true
```

In the example above, two Web apps should be captured: `my-webapp.war` and
`my-other-webapp.war`. The first archive will be captured without
doing a validity check.

Of course if the configuration file already specified Webapp archives to capture then values on
the command line would add to the list.

**Map and object type handling**

Map values will be handled the same way that objects are; the path will include the map
key:

```
coverity scan -o analyze.checkers.checker-config.NULL_RETURNS.enabled=true
```

If the configuration does not have a value for the map entry, the value specified on the
command-line is added to the map; otherwise the existing value is overridden. If the map
value is a complex type, only the setting specified on the command-line is overridden.
In the example above, only the `enabled` setting would be overridden;
the checker options settings would be left unchanged.

Some map keys might contain special characters; for example, dots ("."). Notably, checker names can
contain dots. To handle keys with special characters, the key must be specified with
square brackets and enclosed in single quotes, as in the following example:

```
coverity scan -o "analyze.checkers.checker-config.['CONFIG.HARDCODED_TOKEN'].enabled=true"
```

Remember:
Square brackets might have special meaning to the shell you are using, which is
why this example shows the -o string enclosed in double quotes.
