---
title: "Selecting an installer mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/selecting-an-installer-mode.html"
content_id: "YTqcd6Vaj0Sw6BMcfYdDVg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:55.450724+00:00"
---

# Selecting an installer mode

On Linux-based systems, the console mode (with text-based prompts) is the default, and on
Windows systems graphical mode is the default. For both the Coverity Platform installer
and Coverity Analysis installer, you can use the options described below to select the
mode.

To specify an installer mode:

- Console mode: Use the command-line option `-c` for console mode.
- Graphical mode: Use the `-g` option for graphical mode.
- Silent mode: Use the `-q` option to run the silent (quiet)
  installer.

For example, to start the graphical installer on Linux:

```
> cov-platform-linux64-2026.6.0.sh -g
```

On
Windows, when using the command prompt, you must precede the command with a
`start /wait` command. Additionally, if the executable filename
contains spaces, you must include empty, double quotes even if the filename is
double-quoted:

```
> start /wait "" "<executable name>" -c
```

You can use the empty quotes even when the executable name does not contain spaces. For
example:

```
> start /wait "" cov-platform-win64-2026.6.0.exe -c
```
