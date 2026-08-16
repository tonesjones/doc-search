---
title: "Changing a configuration for a compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-a-configuration-for-a-compiler.html"
content_id: "ped8v7GJwcPe86umW0FDww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:02.005588+00:00"
---

# Changing a configuration for a compiler

If you have already configured a particular compiler, you cannot create a new
configuration for that compiler by re-invoking `cov-configure`. When
you invoke `cov-configure`, Coverity Analysis simply inserts the
include directive that references a new compiler configuration
file below any other include directives that are already in the file.
When you invoke `cov-build`, Coverity Analysis uses the first
configuration it finds that matches the compiler you specify. So the existing
configuration (which precedes the new configuration) always takes precedence over the
new configuration of the same compiler.

The following example shows a master configuration file. The file includes other
coverity_config.xml files that are configured for the compilers
that belong to the gcc and g++ compiler types:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>
<!-- Coverity Version Information -->
<cit_version>1</cit_version>
<config>
<include>$CONFIGDIR$/template-gcc-config-0/coverity_config.xml</include>
<include>$CONFIGDIR$/template-g++-config-0/coverity_config.xml</include>
</config>
</coverity>
```

In the example, the configuration file references compiler-specific configuration files
through relative paths of the following form:
$CONFIGDIR$/comptype-config-number/coverity_config.xml, where
$CONFIGDIR$ is expanded to the absolute path name of the
directory that contains the top-level configuration file, comptype is the compiler type
specified by `cov-configure`, and number is a numerical designation
used to separate multiple compilers of the same type.

If you need to change an existing compiler configuration (for example, because the
current one does not work), you can delete it. For example, if you ran
`cov-configure --compiler cl --comptype gcc` and wanted to remove
the erroneous `cl as GCC` configuration, you could run one of the
following to remove those configurations:

```
cov-configure --delete-compiler-config gcc-config-0
```

```
cov-configure --delete-compiler-config g++-config-0
```

Once the configuration works correctly in a local directory, you can run `cov-configure` once more without `--config` to create the
configuration. Be sure to save the exact `cov-configure` command that
worked and any additional customization, just as you would save any essential source
code.

Sample commands using a test configuration file:

```
> cov-configure --config cfg/test-cfg.xml --gcc
```

```
> cov-build --config cfg/test-cfg.xml --dir intdir gcc hello.c
```
