---
title: "Analyzing non-primary source files (C/C++)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-non-primary-source-files-c/c-.html"
content_id: "uJXDlCz7OChgATimxVhQ2g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:58.374953+00:00"
---

# Analyzing non-primary source files (C/C++)

During the build capture step of Desktop Analysis, the `cov-run-desktop
--build` command records only primary source
files (PSF) and corresponding command lines, ignoring headers and other
supporting files (non-primary source files).

If you would like to run Desktop Analysis on a header file, or other non-PSF, there are
two ways to do so:

Analyze the non-PSF along with a PSF that includes it
:   Since the non-PSFs in your project are not recorded during the build,
    `cov-run-desktop` will not have the necessary context
    to analyze them when specified. To fix this, you can specify the non-PSF,
    along with a PSF which includes it, to the
    `cov-run-desktop` command.

    For example, if you want
    to analyze a header file (header.h) which is
    included by the PSF file1.c, you would specify both
    files in the command:

    ```
    > cov-run-desktop [OPTIONS] file1.c header.h
    ```

Recapture the build with --record-with-source
:   If you plan to analyze non-PSFs frequently, it may be beneficial to repeat the build
    capture step, using `cov-run-desktop --build
    --record-with-source`. This will record all of the source files
    in your project, including non-PSFs. Thus, each non-PSF in your project will
    be directly available to `cov-run-desktop`, as long as it
    is included by a primary source file.

    When a header file (or other
    non-PSF) is specified, `cov-run-desktop` will search
    for a PSF that includes the header. If one is found, it will analyze the
    header as it was compiled in the context of the selected PSF (if more
    than one PSF includes the header, the one with the alphabetically first
    file name is selected). If no PSF is found to include the specified
    header, `cov-run-desktop` halts with an error.

    Note that the `--record-with-source` option will
    slow down the build capture by 10-50%. This should be used only if you
    intend to regularly run analysis on non-PSFs.
