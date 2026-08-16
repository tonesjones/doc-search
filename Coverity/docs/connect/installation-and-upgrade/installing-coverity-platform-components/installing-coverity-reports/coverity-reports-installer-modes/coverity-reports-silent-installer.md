---
title: "Coverity Reports silent installer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-reports-silent-installer.html"
content_id: "DCqibGHlKYgTjZJyNP1x6g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:07.621322+00:00"
---

# Coverity Reports silent installer

The Coverity Reports silent installer allows you to specify all of the installation
configuration details on the command line so you do not need to run the "step-through"
process either through the command line (`-c`) or the graphical
(`-g`) installer modes.

To run the silent installer, specify the installation utility with the
`-q` option, followed by the installation parameters. The
`-q` option and the installation parameters must all be on the same
command line. The following example installs Coverity Report version 2026.6.0 to the home/cov-reports-linux64-2026.6.0 directory.

```
./cov-reports-linux64-2026.6.0.sh --installation.dir=~/cov-reports-linux64-2026.6.0 -q
```

If you are installing on Windows, use the `-q -console` options preceded
by a `start /wait` command. If the executable filename contains spaces,
precede it with empty double quotes, even if the filename itself is double-quoted, for
example:

```
> start /wait "" "<my executable name>" -q -console
```

Note: You can include the empty double quotes whether or not the executable name contains
spaces.

The silent installer accepts the following options. Note that not all of the options are
required. If you use any of the following parameters, you should provide specifically
assigned values. Some values, if left blank, will accept the default value, but this is
not a recommended practice.

## Installer command line options

Note: Do not use the `-V` prefix with these options:

| Option | Description |
| --- | --- |
| `-q` | **Required.** Enables the silent installer. |
| `-console` | **Required on Windows.** Displays status messages in the console from which you invoked the silent installer. |
| -`-installation.dir= directory-path` | **Required.** This option sets the location to which the Coverity Reports product is installed. The default value is `cwd/Coverity/Coverity Reports/`. |
