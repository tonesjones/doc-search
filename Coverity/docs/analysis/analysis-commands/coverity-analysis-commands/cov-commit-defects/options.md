---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "637pxh8OuF1NSS4pysc2gg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:13.371059+00:00"
---

# Options

--authenticate-ssl
:   Reject self-signed certificates when doing the TLS/SSL handshake. You cannot use this option
    together with the `--on-new-cert distrust` option.

--auth-key-file <keyfile>
:   Specify the location of a previously created authentication key file, used for connecting to the
    Coverity Connect server. Authentication keys can be registered with a
    Coverity Connect instance and used for authentication in place of the
    `--user` and `--password` options. See
    "Working
    with authentication keys" in Coverity Platform 2026.6.0 User and Administrator Guide.

--certs <filename>
:   In addition to CA certificates obtained from other truststores, use the CA certificates in the
    given `filename`. This file is in PEM format. For information on the TLS/SSL certificate
    management functionality, please see Coverity Platform 2026.6.0 User and Administrator Guide.

--cid-assignment-timeout <timeout-seconds>
:   When committing with `--preview-report`, `--preview-report-v2`, or
    `--preview-report-v3` to an instance of Coverity
    Connect in a clustered environment, assignments of CIDs to issues can
    delay the completion of the preview report. This option specifies the
    number of seconds to wait for this phase of preview report processing to
    complete. If assigning CIDs takes longer than
    `<timeout-seconds>`, Coverity Connect will
    leave some of the CIDs unassigned. They will have null values in the
    preview report. The default CID assignment timeout is 60 seconds.

--comparison-snapshot-id <snapshot-id>
:   This option is used in conjunction with the `--preview-report-v2` option or the
    `--preview-report-v3` option to specify the snapshot
    with which the preview report will compare the commit's defect
    instances. A boolean flag, called
    `presentInComparisonSnapshot`, is included in the
    preview report indicating whether each of this commit's defect
    occurrences is present in the given snapshot. The default value is the
    most recent snapshot ID in the specified stream.

--dataport <port_number>
:   You should use the `--url` option instead of this option. This
    option is deprecated and will be removed in a future release.

    Used with the `--host` option to specify the Commit port on
    Coverity Connect. You can use only one of `--port`,
    `--dataport`, or `--https-port` to specify
    the Commit port.

--description <description>
:   Specify a description for the committed snapshot.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--encryption <requirement_level>
:   This option is deprecated and will be removed in a future release. You
    should use the `--url` option and send analysis data to
    the HTTPS port instead.

    `cov-commit-defects` uses this option to communicate
    with Coverity Connect to determine if the dataport connection will be
    encrypted. By default, the value for `--encryption
    <requirement_level>` is "preferred".

    The available values for <requirement_level> are:

    required
    :   The commit will proceed only if the server requires or
        prefers encryption. The connection will be
        encrypted.

    preferred
    :   The connection will be encrypted if the server requires
        or prefers encryption. Otherwise, the connection will be
        unencrypted

    none
    :   The commit will proceed only if the server prefers
        encryption or has an encryption setting of none (meaning
        it requires no encryption). The connection will be
        unencrypted.

--exclude-files <regex>
:   Omit defects from files that are in paths that match the specified regular
    expression. You cannot use this option multiple times in the same command
    line. You can use it with the `--include-files` option. If
    you use both options together, `--exclude-files` takes
    precedence over `--include-files`. For example, defects from
    a given file are excluded from the output in the case that the regular
    expressions both include and exclude the file.

    Example that excludes paths that contain both `/bar/` and
    `.c`:

    ```
    --exclude-files '/bar/.*\.c$'
    ```

    The example excludes the following file:

    `/foo/bar/test.c`

    The example does not exclude the following files:

    `/foo/test.c`

    `/foo/bar/test.cc`

    Note: The example above uses single quotes around the
    string value. However, your command interpreter might require double quotes
    (for example, `"/bar/.*\.c$"`).

--extra-output <path>

-xo <path>
:   [Deprecated] This option is deprecated as of version 5.5 and subject to
    removal or change in a future release.

    Specify additional output directories from parallel analysis snapshots.
    Use this option for each output directory, in addition to the default
    <intermediate_directory>/output
    directory, that you want to commit into a single snapshot ID in the
    Coverity Connect.

--host <server_hostname>
:   You should the `--url` option instead of this option. This
    option is deprecated and will be removed in a future release.

    Specify the server hostname to which to send the results. The server must
    have a running instance of Coverity Connect.

    If unspecified, the default is the host element from the XML
    configuration file.

    Note:

    - If you're running `cov-commit-defects` on a
      Linux OS, or using `--ssl`, you must enter
      the full host and domain name for the
      `--host` parameter:

      ```
      --host server_hostname.domain.com
      ```
    - The `--host` switch, while still supported,
      now produces a deprecation warning that it may be removed in
      a later release. The `--url` syntax is the
      preferred replacement.

--https-port <port_number>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    If both Coverity Connect and Coverity Analysis are at release 2020.12 or
    later, this option directs commit data to the Coverity Connect server's
    HTTPS port.

    If either Coverity Connect or Coverity Analysis are older than release
    2020.12, this option first retrieves the Coverity Connect server's
    Commit port number from the server's HTTPS port and then directs commit
    data to the Commit port.

    This option requires the `--host` option.

--include-files <regex>
:   Use defects only from files that are in paths that match the specified
    regular expression. You cannot use this option multiple times in the same
    command line. You can use it with the `--exclude-files`
    option. If you use both options together, `--exclude-files`
    takes precedence over `--include-files`. For example, defects
    from a given file are excluded from the output in the case that the regular
    expressions both include and exclude the file.

    Example that includes `/foo/`:

    ```
    --include-files '/foo/'
    ```

    The example includes the following file:

    `/bar/foo/test.c`

    The example excludes the following file:

    `/bar/test.c`

    Note: The example above uses single quotes around the
    string value. However, your command interpreter might require double quotes
    (for example, `"/foo/"`).

--misra-only
:   [Deprecated in 8.0] Using this option will result in an error.

--noxrefs
:   Tells `cov-commit-defects` to skip the phase of
    transferring xrefs (cross-reference data) to Coverity Connect. It is
    useful for debugging and doing commits where the user doesn't mind that,
    when viewed in the Coverity Connect, their code lacks cross-reference
    information. A user might prefer that if they were sensitive to the
    amount of time taken by commit to execute.

--on-new-cert <trust | distrust>
:   Indicates whether to trust (with trust-first-time) self-signed certificates, presented by the
    server, that the application has not seen before. Default is `distrust`. If
    `distrust` and the certificate is self-signed, the connect attempt will fail.
    For information on the new TLS/SSL certificate management functionality, please
    see Coverity Platform 2026.6.0 User and Administrator Guide.

    CAUTION:

    Setting `on-new-cert` to
    `trust` does not currently work with Coverity Analysis and
    Black Duck® Bridge. The workaround is to manually
    add the self-signed certificate to your operating system's
    certificate store. This will tell the operating system that it can
    trust this certificate, and should allow you to continue.

--output-tag <name>
:   Use this option if you used it when generating analysis results. See the
    --output-tag option to
    `cov-analyze`.

--password <password>

-pa <password>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specify the password for either the current user name, or the user
    specified with the `--user` option. For security reasons,
    the password transmitted to Coverity Connect is encrypted. If
    unspecified, the default is (in order of precedence):

    1. The password from the `--url` option.
    2. The password element from the XML configuration file.
    3. The environment variable `COVERITY_PASSPHRASE`.
    4. The password in the file pointed to by the environment variable
       `COVERITY_PASSPHRASE_FILE`.

    Note: The passphrase can be stored in a file without any other
    text, such as a newline character.

    Attention: On multi-user systems, such as Linux, users can see
    the full command line of all commands that all users execute. For
    example, if a user uses the `ps -Awf` command,
    identifying information such as usernames, process identities, dates and
    times, and full command lines display.

    This attribute supports the commit process.

--port <port_number>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    If both Coverity Connect and Coverity Analysis are at release 2020.12 or
    later, this option directs commit data to the Coverity Connect server's
    HTTP port.

    If either Coverity Connect or Coverity Analysis are older than release
    2020.12, this option first retrieves the Coverity Connect server's
    Commit port number from the server's HTTP port and then directs commit
    data to the Commit port.

    This option requires the `--host` option.

--ssl
:   Specifies that TLS/SSL is to be used for both HTTPS port and dataport connections. For the
    negotiation with the server on whether to use TLS/SSL on the dataport, this
    is the equivalent of `--encryption required`. This option
    is deprecated. Instead, using the --url option with the
    `https:` scheme is recommended.

--preview-report <filename>
:   Instead of sending files, cross-references, and other assets to the
    server, this option sends only the defect occurrences. The server
    returns a commit preview report, which is written in JSON format, to
    <filename>.

    The commit preview report uses the structure defined in the following
    table. Note that the order of items contained within objects or arrays
    is arbitrary.

    There is a second version of the preview report, used by Coverity Desktop Analysis, which
    contains additional details for each CID. See
    `--preview-report-v2 <filename>` for more information.

    Table 1. Report v1 element syntax

    | Report element | Comments |
    | --- | --- |
    | ``` report  <- {     "header" : header,     "analysisInfo" : analysisInfo,     "issueInfo" : issueInfo, } ``` |  |
    | ``` header  <- {     "format" : "commit preview report",     "version" : 1, } ``` |  |
    | ``` analysisInfo <- {      "command" : string,     "reportTimestamp" : string,     "user" : string, } ``` | ReportTimestamp has format `yyyy-mm-ddThh:mm:ss.mmmZ`. The T separates the date from the time. The Z indicates that the timestamp is in UTC. |
    | ``` issueInfo <- [   {      "cid" : number or null,      "mergeKey" : string,      "occurrences" : occurrences,      "triage" : triage,   }, ... ] ``` | Each distinct issue has a unique identifier, the mergeKey. The CID may sometimes be null in clustered installations. |
    | ``` occurrences  <- [   {      "checker" : string,      "file" : string,      "function" : string,      "extra" : string,      "subcategory" : string,      "mainEvenLineNumber" : integer,      "mainEventDescription" : string,   }, ... ] ``` | Each issueInfo has one or more occurrences, all with the same mergeKey. |
    | ``` triage <- {      "classification" : string,      "action" : string,      "fixTarget" : string,      "severity" : string,      "owner" : string, } ```   (one additional item for each custom attribute. Value is *`string`* or null.) |  |

--preview-report-v2 <filename>
:   Similar to `--preview-report`, this option sends only
    defect occurrences to the server, which then returns a commit preview
    report, written in JSON format, to
    <filename>. Version 2 of the preview report
    contains all of the information present in version 1, with several
    additional fields.

    The commit preview report (v2) uses the structure defined in the
    following table. Note that the order of items contained within objects
    or arrays is arbitrary.

    Table 2. Report v2 element syntax

    | Report element | Comments |
    | --- | --- |
    | ``` report  <- {     "header" : header,     "analysisInfo" : analysisInfo,     "issueInfo" : issueInfo, } ``` |  |
    | ``` header  <- {     "format" : "commit preview report",     "version" : 2, } ``` |  |
    | ``` analysisInfo <- {     "command" : string,     "reportTimestamp" : string,     "user" : string,     "comparisonSnapshotId" : string,     "ownerAssignmentRule" : string,     "ownerLdapServerName" : string,  } ``` | ReportTimestamp has format `yyyy-mm-ddThh:mm:ss.mmmZ`. The T separates the date from the time. The Z indicates that the timestamp is in UTC. The `comparisonSnapshotId` is the snapshot identifier given by the `--comparison-snapshot-id` command line parameter. If not specified by `--comparison-snapshot-id`, this will be the ID of the most recent snapshot. |
    | ``` issueInfo <- [   {      "cid" : number or null,      "mergeKey" : string,      "occurrences" : occurrences,      "triage" : triage,      "customTriage" : customTriage,      "presentInComparisonSnapshot" : boolean,      "firstDetectedDateTime" : string,      "ownerLdapServerName" : string,   }, ... ] ``` | Each distinct issue has a unique identifier, the mergeKey. The CID may sometimes be null in clustered installations. The `presentInComparisonSnapshot` flag is true if this issue occurs in the comparison snapshot identified by the `comparisonSnapshotId` (listed in the `analysisInfo` element). |
    | ``` occurrences  <- [   {      "checker" : string,      "file" : string,      "function" : string,      "extra" : string,      "subcategory" : string,      "mainEvenLineNumber" : integer,      "mainEventDescription" : string,      "componentName" : string,      "componentDefaultOwner" : string,      "componentDefaultOwner " string   }, ... ] ``` | Each issueInfo has one or more occurrences, all with the same mergeKey. |
    | ``` triage <- {      "classification" : string,      "action" : string,      "fixTarget" : string,      "severity" : string,      "owner" : string,      "legacy" : string,      "externalReference" : string, } ``` |  |
    | ``` customTriage <- {      "quotedString" : string } ``` | The custom triage attributes, if any, are listed here. |

--preview-report-v3 <filename>
:   Similar to `--preview-report-v2`, this option sends only
    defect occurrences to the server, which then returns a commit preview
    report, written in JSON format, to
    <filename>. Version 3 of the preview report
    contains all of the information present in version 2, with one additional field, `lastTriageComment`.

    The commit preview report (v3) uses the structure defined in the
    following table. Note that the order of items contained within objects
    or arrays is arbitrary.

    Table 3. Report v3 element syntax

    | Report element | Comments |
    | --- | --- |
    | ``` report  <- { 	"header" : header, 	"analysisInfo" : analysisInfo, 	"issueInfo" : issueInfo, } ``` |  |
    | ``` header  <- { 	"format" : "commit preview report", 	"version" : 2, } ``` |  |
    | ``` analysisInfo <- { 	"command" : string, 	"reportTimestamp" : string, 	"user" : string, 	"comparisonSnapshotId" : string, 	"ownerAssignmentRule" : string, 	"ownerLdapServerName" : string,  } ``` | ReportTimestamp has format `yyyy-mm-ddThh:mm:ss.mmmZ`. The T separates the date from the time. The Z indicates that the timestamp is in UTC. The `comparisonSnapshotId` is the snapshot identifier given by the `--comparison-snapshot-id` command line parameter. If not specified by `--comparison-snapshot-id`, this will be the ID of the most recent snapshot. |
    | ``` issueInfo <- [ 	{ 		"cid" : number or null, 		"mergeKey" : string, 		"occurrences" : occurrences, 		"triage" : triage, 		"customTriage" : customTriage, 		"presentInComparisonSnapshot" : boolean, 		"firstDetectedDateTime" : string, 		"ownerLdapServerName" : string, 	}, ... ] ``` | Each distinct issue has a unique identifier, the mergeKey. The CID may sometimes be null in clustered installations. The `presentInComparisonSnapshot` flag is true if this issue occurs in the comparison snapshot identified by the `comparisonSnapshotId` (listed in the `analysisInfo` element). |
    | ``` occurrences  <- [ 	{ 		"checker" : string, 		"file" : string, 		"function" : string, 		"extra" : string, 		"subcategory" : string, 		"mainEvenLineNumber" : integer, 		"mainEventDescription" : string, 		"componentName" : string, 		"componentDefaultOwner" : string, 		"componentDefaultOwner " string 	}, ... ] ``` | Each issueInfo has one or more occurrences, all with the same mergeKey. |
    | ``` triage <- { 	"classification" : string, 	"action" : string, 	"fixTarget" : string, 	"severity" : string, 	"owner" : string, 	"legacy" : string, 	"externalReference" : string, 	"lastTriageComment" : string } ``` | The `lastTriageComment` field contains the last non-empty comment that was added to the corresponding defect. |
    | ``` customTriage <- { 	"quotedString" : string } ``` | The custom triage attributes, if any, are listed here. |

--product <product_name>
:   Deprecated. See `--stream`.

--scm <scm_type>
:   Specifies the name of the source control management system. For this option to
    function correctly, your source files must remain in their usual locations in the
    checked-out source tree. If the files are copied to a different location after
    checkout, the SCM query will not work.

    Possible `scm_type` values:

    - GIT: `git`
    - Perforce: `perforce`
    - Plastic: `<plastic|plastic-distributed>`.

      Use `plastic` when working in a non- or partially-distributed Plastic
      configuration. Use `plastic-distributed` when working in
      a fully-distributed Plastic configuration.
    - SVN: `svn`

    For usage
    information for the `--scm` option, run `cov-extract-scm
    --help`.

    Note: The following commands or setup utilities must be run beforehand in order to
    successfully communicate with the SCM server:

    - `perforce`

      The environment variable `P4PORT` should be set to the
      value expected by the p4 tool.

--scm-command-arg <command_arg>
:   This option has been deprecated. Instead of
    using `--scm-command-arg arg1`, use `--scm-param
    annotate_arg=arg1`. Specifies additional arguments that are
    passed to the command that retrieves the last modified dates. The arguments
    are placed after the command and before the target file. This option can be
    specified multiple times.

    For usage information, see `cov-extract-scm`.

--scm-param
:   Specifies additional arguments that are passed to the SCM tool in a
    context-aware manner.

    For usage information, see `cov-extract-scm`.

--scm-project-root <root_path>
:   Specifies a path that represents the root of the source control repository.
    When this is used, all file paths that are used to gather information are
    interpreted as relative to this project-root path.

    For usage information, see `cov-extract-scm`.

--snapshot-id-file <filename>
:   If the commit succeeds, write the snapshot ID for this commit to the
    specified file, and make this file writable.

--scm-tool <tool_path>
:   Specifies the path to an executable that interacts with the source control
    repository. If the executable name is given, it is assumed that it can be
    found in the path environment variable. If not provided, the command uses
    the default tool for the specified `--scm` system.

    For usage information, see `cov-extract-scm`.

--scm-tool-arg <tool_args>
:   This option has been deprecated. Instead of using `--scm-tool-arg
    arg1`, use `--scm-param tool_arg=arg1`. Specifies
    additional arguments that are passed to the SCM tool, specified in the
    `--scm-tool` option, that gathers the last modified
    dates. The arguments are placed before the command and after the tool. This
    option can be specified multiple times.

    For usage information, see `cov-extract-scm`.

--security-file <license file>

-sf <license file>
:   Path to a valid Coverity Analysis license file. If not specified, this path is given by the
    `security_file` tag in the Coverity configuration or by
    license.dat (located in the Coverity Analysis
    <install_dir>/bin directory). A valid license
    file is required to run the analysis.

--stream <stream_name>
:   Specifies a stream name to which to commit these defects.

    If the stream option is not specified, the stream element from the XML
    configuration file is used.

    If the stream is associated with a specific language and you attempt to
    commit results from other languages to that stream, the commit will
    fail. However, in Coverity Connect, it is possible to associate a stream
    with multiple languages even if the stream was previously associated
    with a single programming language.

--strip-path <path>

-s <path>
:   Strips leading directory names from file paths that
    appear in error messages and in references to your source files.

    The leading portion of the path is omitted if it matches a value
    specified by this option. For example, if the actual full path name of a
    file is /test/me/sourceFile.c, and
    `--strip-path /test` is specified, then the name
    attribute for the file becomes
    /me/sourceFile.c.

    The `--strip-path string` can include more than one
    directory name. Also, you can specify the `--strip-path`
    option multiple times. If more than one `--strip-path` is
    present, Coverity uses the longest of these. (Coverity does not attempt
    to use more than one of the specified path prefixes.)

    For example, suppose that you specify the following:

    ```
    --strip-path /a --strip-path /b --strip-path /b/c
    ```

    ... then `--strip-path` would condense paths in the
    following way:

    Table 4. Results of using `--strip-path`

    | Original path | Stripped path | Notes |
    | --- | --- | --- |
    | a/fname | /fname |  |
    | a/b/fname | /b/fname | In this case, /b was not a leading directory name in the path. |
    | b/fname | /fname |  |
    | b/c/fname | /fname |  |

    Important: We recommend using this option for a number of
    reasons:

    - Failure to use this option can result in poor Coverity Connect
      performance, triage issues related to component maps, an
      unnecessary increase the size of the Coverity Connect database,
      and even incorrect LOC counts.
    - This option shortens paths that Coverity Connect displays. It
      also allows your deployment to be more portable if you need to
      move it to a new machine in the future.
    - In addition, using this option during the analysis, rather than
      when committing the analysis results to Coverity Connect, can
      enhance end-to-end performance of the path stripping process
      itself.

    The `--strip-path` is available for several commands.\

    Note that instead of using this option when committing issues to Coverity
    Connect through `cov-commit-defects`, you can enhance
    end-to-end performance by using this option with
    `cov-analyze` when analyzing code, or with
    `cov-import-results` when importing third-party
    issues.

--target <target_name>
:   Target platform for this project (for example, i386).

--ticker-mode <mode>
:   Set the mode of the progress bar ticker. The available modes are:

    none
    :   No progress bar is displayed.

    no-spin
    :   Only the print stars are displayed; the spinning bar is
        not.

    spin
    :   This is the default mode. Stars with a spinning bar at the
        end are displayed. Each file, function, or defect committed
        corresponds to steps of spin.

--url <path>
:   Use this option to specify the information needed to connect to a
    Coverity Connect server. You should use this option instead of the
    `--dataport`, `--host`,
    `--https-port`, `--port`, and
    `--user` options (these options are deprecated and
    will be removed in a future release).

    - The `--url` switch now allows a username and
      password to be supplied, as an alternative to
      `--user` and `--password`.
      The syntax used to supply those credentials in the URL is
      https://[<USERNAME>[:<PASSWORD>]@]<HOSTNAME>[:<PORT>][/<CONTEXT_ROOT>],
      where the brackets show which parts are optional.
    - The parallel construct also exists for
      http:// and
      commit://.
    - The `--host` switch, while still supported,
      now produces a deprecation warning that it may be removed in
      a later release. The `--url` syntax is the
      preferred replacement.

    The value you specify for this option can have one of two forms: one used
    with HTTPS or HTTP, or one used with the commit scheme. Examples are
    provided in the following table:

    | Scheme | Meaning | Example |
    | --- | --- | --- |
    | https or http | Use HTTPS or HTTP to connect to the Coverity Connect HTTPS or HTTP port. HTTPS is the preferred scheme. For `http`, the default port is 80; for `https`, the default port is 443. | ``` https://example.com/coverity ```  ``` https://cimpop:8008 ```  ``` http://cim.example.com:8080 ``` |
    | commit | Connect to the data port specified by the URL. This scheme is deprecated and will be removed in a future release. | ``` commit://cim.example.com:9999 ```  ``` commit://cim.example.com ``` |

    Refer to the following table as an aid in updating existing command lines
    that use the `--host`, `--port`,
    `--https-port`, and `--dataport`
    options:

    | Existing command form | New command form |
    | --- | --- |
    | ``` cov-commit-defects --host <hostname> --port <http-port> --encryption <level> … ``` | ``` cov-commit-defects --url https://<hostname>:<https-port> … ```  For example:  ``` cov-commit-defects --url https://admin:1256@coverity_server1 --stream xalan --dir xalan_int_dir ``` |
    | ``` cov-commit-defects --url http://<hostname>:<http-port> --encryption <level> … ``` |
    | ``` cov-commit-defects --url commit://<hostname>:<commit-port> --encryption <level> … ``` |

--user <user_name>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specifies the Coverity Connect user name. If unspecified, the default is:

    1. The username specified by the `--url` option, if
       any.
    2. The user element from the XML configuration file.
    3. The environment variable `COV_USER`.
    4. The environment variable `USER`.
    5. The name of the operating system user invoking the command (where
       supported).
    6. The UID of the operating system user invoking the command (where
       supported).
    7. `admin`.

--version <version>
:   This snapshot's project version.

## Shared options

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
