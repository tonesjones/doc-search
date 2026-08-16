---
title: "Options: Checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-checkers.html"
content_id: "b5WsY0QAGNQHwywzx9dZuA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:37.264146+00:00"
---

# Options: Checkers

--all
:   Enables almost all checkers that are disabled by default (exceptions are
    noted below). Using this option is equivalent to using all of the following
    options:

    - `--concurrency`
    - `--enable-parse-warnings`
    - `--enable PARSE_ERROR`
    - `--enable STACK_USE`
    - `--security`

    To find out whether a checker can be enabled with this option, see
    the --list-checkers option.

    Exceptions
    :   The following checkers are disabled by default, and the
        `--all` option *does not* turn them
        on:

        - Android security checkers (which are enabled with the
          `--android-security` option).
        - DC.STRING_BUFFER
        - ENUM_AS_BOOLEAN
        - HARDCODED_CREDENTIALS
        - HFA
        - INTEGER_OVERFLOW
        - LOCK_INVERSION (for C#)
        - MISRA_CAST
        - ODR_VIOLATION for C++
        - ORM_LOST_UPDATE
        - Rule checkers (which are enabled with the
          `--rule` option).
        - SECURE_CODING (Deprecated)
        - SIZECHECK (Deprecated)
        - UNENCRYPTED_SENSITIVE_DATA
        - USER_POINTER
        - WEAK_GUARD
        - WEAK_PASSWORD_HASH
        - Web application security checkers (such as XSS) are
          not affected by this option. To enable them, see
          `--webapp-security`.
        - XML_INJECTION

    Default checkers are enabled by default and are therefore unaffected by this
    option.

    For information about enabling individual checkers, see the `--enable`
    option.

--all-security
:   Enables all security checkers. This includes the Security, Android Security, and Web App
    Security categories, and other security checkers that require explicit
    enablement. It also includes the default set of Sigma checks. It *does not
    include* audit security checkers (which are enabled by
    --enable-audit-checkers).

    You can view the list of
    checkers that the --all-security option has enabled by
    invoking `cov-analyze` with the
    --list-checkers option.

--checker-option <checker_name>:<option>[:<option_value>]

-co <checker_name>:<option>[:<option_value>]
:   Passes a checker option. Checker options and their default values are
    documented in the Coverity 2026.6.0 Checker Reference.

    Example:

    ```
    INFINITE_LOOP:report_no_escape:true
    ```

    Starting in version 7.0, when you specify the
    value of a checker option for a checker that supports the analysis of
    multiple languages, the value that you specify will apply to all languages
    to which that checker option applies. For example, if you set the
    stat_threshold to NULL_RETURNS, and you run an analysis on C/C++, C#, and
    Visual Basic code bases, the value you set for that option will apply to
    both languages. If you do not set the value, the checker will use the
    default values for those options, which in a very limited number of cases
    can vary by language.

    Some checker options are language-specific, such as
    FORWARD_NULL:dynamic_cast. This option is only available for (and can only
    apply to) C/C++ even though the FORWARD_NULL checker supports multiple
    languages.

--dc-config <file.json>
:   Identifies a JSON file for one or more DC.*CUSTOM_** (custom Don't Call)
    checkers that you intend to run in the analysis (see
    "DC.*CUSTOM_CHECKER"*
    in the Coverity 2026.6.0 Checker Reference).

    Note that use of this option enables all the DC.*CUSTOM_** checkers that are configured
    in the JSON file. You can disable them individually with `--disable
    <checker-name>`. The `--disable-default`
    option will disable all of them.

    Note: CodeXM is a language specifically designed for writing new checkers. If
    you have not already invested in custom DC checker configuration, we
    recommend you use CodeXM rather than the JSON configuration. See
    "Writing your own *Don't Call* checker"
    in the Coverity
    CodeXM Checkers Development Guide.

--disable <checker_name>

-n <checker>
:   Disables a checker. This option can be specified multiple times. See also
    --list-checkers and
    `--disable-default`.

    To find out whether a checker is enabled or disabled by default, see the
    --list-checkers option.

    To disable Sigma checkers, you need to add the SIGMA prefix to the checker name. For
    example:

    ```
    --disable SIGMA.access_to_secret
    ```

--disable-android-security
:   Disables the Android application security checkers. Note that these checkers
    are disabled by default.

    See also, --android-security.

--disable-default
:   Disables default checkers. This option is useful if you want to disable all default checkers,
    including Sigma checkers, and then enable only a few with the
    `--enable` option.

    For a list of checkers that are disabled through this option, see the
    `--enable` option documentation for the
    `cov-analyze` command.

--enable <checker_name>

-en <checker>
:   Enables a checker that is not otherwise enabled by default. The checker name is case
    insensitive. This option will enable a checker for all languages supported
    by the checker. Note that default enablement of a given checker can vary by
    language.

    Checkers are enabled by name, so related checkers such as
    MISSING_LOCK and
    GUARDED_BY_VIOLATION are enabled independently. You
    can specify this option multiple times. See also --list-checkers and `--disable-default`.

    To
    enable Sigma checkers, you need to add the SIGMA prefix to the checker name. For
    example:

    ```
    --enable SIGMA.access_to_secret
    ```

--enable-check-set <coverity-check-set(s)>
:   Bulk-enables a set of Coverity checkers that report defects for a specific
    vulnerability list. Multiple sets can be specified as a comma-separated
    list. When this option is used, the check sets are also enabled on the Sigma
    engine (unless Sigma analysis is explicitly disabled).

    The available sets are the following:

    - `cwe-top-25-2023` - Enables checkers reporting
      vulnerabilities from CWE Top 25 2023
    - `cwe-top-25-2024` - Enables checkers reporting
      vulnerabilities from CWE Top 25 2024
    - `owasp-mobile-top-10-2016` - Enables checkers
      reporting vulnerabilities from OWASP Mobile Top 10 2016
    - `owasp-mobile-top-10-2024` - Enables checkers
      reporting vulnerabilities from OWASP Mobile Top 10 2024
    - `owasp-web-top-10-2021` - Enables checkers reporting
      vulnerabilities from OWASP Web Top 10 2021
    - `owasp-web-top-10-2025` - Enables checkers reporting
      vulnerabilities from OWASP Web Top 10 2025

--enable-default
:   Enables all default checkers. This option takes precedence over the
    `--disable-default` option. That is, if this option is
    specified, then all default checkers are enabled regardless of the use of
    those options. However, individual checkers can still be disabled using the
    `--disable` option.

--list-checkers
:   Displays a list of checkers that are available in the current release. Each
    entry indicates whether the checker is enabled by default, and if not, how
    you can enable it. Some require the use of`--enable`, while others can be enabled with
    other options (for example, `--concurrency` or
    `--security`), as well. For detailed information about
    checkers, see the Coverity 2026.6.0 Checker Reference.

--list-check-sets
:   Displays the list of check sets supported by the `--enable-check-set` option in
    the current release.

--list-check-set-checkers <coverity-check-set>
:   Displays the list of Coverity checkers that are enabled by a particular check set supported by
    the `--enable-check-set` option in the current release. For
    detailed information about checkers, see the Coverity 2026.6.0 Checker Reference.

--sigma-base-check-set <sigma-check-set>
:   Bulk-enables a base set of Sigma checks. Only one of the
    following values can be used:

    - `all` - Enables all Sigma
      checks, including checks disabled by default.

      For a list of Sigma checks disabled by default, see the
      section "Checkers disabled in Sigma when running Coverity Analysis"
      on the SIGMA.*
      page of the Coverity 2026.6.0 Checker Reference.
    - `default` - Enables all Sigma checks, except for the disabled checks
      (those either disabled by default, or explicitly disabled by using the
      `--disable` option).
    - `empty` - Disables all Sigma checks, except for those checks that
      are explicitly enabled by using the `--enable` option.
    - `cis` - Enables the CIS (Center for Internet Security)
      benchmark checks.

    Note: If this option is not set, the default set of checks is enabled.
    This is equivalent to setting `--sigma-base-check-set
    default`.

--sigma-enable-check-set <sigma-check-set(s)>
:   Bulk-enables an additional set of Sigma checks. Multiple sets can be specified as a
    comma-separated list.

    - `all` - this will enable all Sigma checks, including checks disabled by
      default. For a list of Sigma checks disabled by default, see "Sigma
      checks disabled by default in Coverity 2026.6.0" in the Coverity 2026.6.0 Checker Reference.
    - `default` - this will enable all Sigma checks, except for the disabled
      checks (either disabled by default, or explicitly disabled with the
      `--disable` option).
    - `empty` - this will disable all Sigma checks, except for the checks which
      are explicitly enabled using the `--enable` option.
    - `cis` - this will enable the CIS (Center for Internet Security) benchmark
      checks.

    Note: If you wish to run the default Sigma checks, while
    excluding all non-Sigma checkers, use the following
    command:

    ```
    cov-analyze --disable-default --sigma-enable-check-set default
    ```
