---
title: "Options: Sigma"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-sigma.html"
content_id: "r8fkgwiNaMgJVrcktOJ1wA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:43.917255+00:00"
---

# Options: Sigma

Note: There is also a --sigma-enable-check-set option that
can enable or disable particular sets of Sigma checkers.
See Options: Checkers.

--disable-sigma
:   Disables Sigma analysis.

    When Sigma analysis is enabled (the default), you can disable it by using
    the --disable-sigma or you can disable it along with all other
    checker defaults by using the --disable-default option, as described in
    Options: Checkers.

--enable-sigma
:   Enables Sigma analysis.

    As of 2023.9.0, Coverity Sigma analysis is enabled by default.
    The --enable-sigma option has been deprecated, and will be discontinued
    in a future release.

--sigma-config-file
:   Specify a configuration file for Sigma, either in JSON or YAML format. See ["Creating a Default Configuration"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/creating-a-default-configuration.html) in
    the Sigma online documentation for information on creating a configuration file
    for Sigma.

    Note: This option will only have an effect when Sigma is enabled.

--sigma-malicious-url-patterns-file <list of files>
:   The --sigma-malicious-url-patterns-file option is used to
    enable and customize the behaviour of the
    `SIGMA.malicious_url` checker, which is used to detect
    malicious URLs in source code.

    This option expects arguments as a comma separated list of files. A file
    given as parameter to the
    --sigma-malicious-url-patterns-file option should
    contain a list of URLs that need to be reported, with one URL per line.

--update-sigma-binary <path_to_binary>
:   Permanently update the Sigma binary used by Coverity so that any succeeding
    calls to cov-analyze will use the newer Sigma binary. All
    other options are ignored. The newer binary will be copied into the Coverity
    installation and you can safely remove the provided binary after the upgrade
    completes successfully. You may use this option to revert to the Sigma
    version bundled with Coverity.

    <path_to_binary> must point to an executable Sigma binary
    with a version no earlier than the one bundled with Coverity. If any issues
    are encountered with the binary, the analysis will halt with an error
    message.

    Coverity CLI users must use this option to use new versions of Sigma.
    Performing a single analysis run with a newer Sigma binary is not
    supported.

    Note: This option is not supported for Polaris.

--use-sigma-binary <path_to_binary>
:   Perform a single analysis run using the Sigma binary at the specified path.
    Any succeeding calls to cov-analyze without this option
    will continue to use the Sigma binary bundled with Coverity. This option
    allows you to evaluate the results of a newer Sigma binary before
    permanently upgrading to it. You can safely use this option with other
    cov-analyze options.

    <path_to_binary> must point to an executable Sigma binary
    with a version no earlier than the one bundled with Coverity. If any issues
    are encountered with the binary, the analysis will halt with an error
    message.

    Note: This option is not supported for Polaris.
