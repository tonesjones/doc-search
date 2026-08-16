---
title: "covanalyzeandcommit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/covanalyzeandcommit.html"
content_id: "9qPiLA6GKZf6Bsnm_wH9Pw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:54.613491+00:00"
---

# covanalyzeandcommit

Analyze Java source code and class files, and then commit the results to
Coverity Connect.

## Synopsis

```
<covanalyzeandcommit 
  dir="int_dir"
  [OPTIONAL_ATTRIBUTES]>
    <[OPTIONAL_ELEMENTS]/>
</covanalyzeandcommit>
```

## Description

The `covanalyzeandcommit` analyzes Java source code and class files
that have been previously stored in an intermediate directory by capturing a build
with the `cov-build` command and/or by adding them manually using
the `cov-emit-java` command. Then it commits the results to
Coverity Connect. The commit process occurs if the analysis had either no errors or
only recoverable errors. Otherwise, the commit process is skipped.

## Attributes

additionalanalysisoptions="options"
:   Most users are unlikely to use this attribute, which provides a string of
    additional, space-separated options to pass to the analysis command. You
    might use it to pass options that are not available as analysis-related
    attributes to this Ant task.

    This attribute should not be used with any options that contain spaces,
    such as filenames with spaces.

    Example:

    ```
    <covanalyzeandcommit additionalanalysisoptions="--append false --max-mem 8000"/>
    ```

    See 
    `cov-analyze`
     for a complete list of options.

additionalcommitoptions="options"
:   Most users are unlikely to use this attribute, which provides a string of
    additional, space-separated options to pass to
    `cov-commit-defects`. You might use it to pass
    options that are not available as commit-related attributes to this Ant
    task.

    This attribute should not be used with any options that contain spaces,
    such as filenames with spaces.

    Example:

    ```
    <covanalyzeandcommit additionalcommitoptions="--debug false --ticker-mode none"/>
    ```

    See 
    `cov-commit-defects`
     for a complete list of options.

all="true"
:   Enables Coverity Analysis for Java checkers that are disabled by
    default.

    Exception: Web application security checkers (such as XSS) are not
    affected by this option. To enable them, see
    `--webapp-security`.

analysis="false"
:   Allows you to turn off the analysis process, which normally takes place
    prior to the commit process. In this way, you can commit the results of
    a prior analysis to Coverity Connect without running another analysis
    first. Defaults to true.

binpath="<install_dir>/bin"
:   Specifies the directory containing `cov-analyze` and
    `cov-commit-defects`. Use this attribute if the Ant
    task fails to find these commands. Without this attribute, the Ant task
    searches for these based on the PATH environment variable and/or the
    location of coverity-anttask.jar.

commit="false"
:   Allows you to turn off the commit process. In this way, you can perform
    an analysis without committing results to Coverity Connect afterward.
    Defaults to true.

config="coverity_config.xml"
:   Uses the specified configuration file instead of the default
    configuration file located at
    <install_dir>/config/coverity_config.xml.
    This file applies to both the analysis and the commit processes.

dataport="cim_commit_port"
:   Specifies the commit port of the Coverity Connect server.

dir="int_dir"
:   Pathname to an intermediate directory that is used to store the emit
    repository and output directory.

    If you specify ".", it uses the current directory as the intermediate
    directory.

disabledefault="true"
:   Disables default checkers. This option is useful if you want to disable
    all default checkers and then enable only a few with the --enable
    option.

    For a list of checkers that are disabled through this option, see the
    --enable option documentation for the
    `cov-analyze` command.

failonerror="true|false"
:   If true, the build process will succeed only if both
    `cov-analyze` and
    `cov-commit-defects` exit without return codes that
    indicate failure. Otherwise, the Ant task will always succeed. Defaults
    to `true`.

host="server_hostname"
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

httpport="port_number"
:   Used with the `--host` option to specify the HTTP port on
    the Coverity Connect host. This port is used to connect to the
    `--dataport` commit port.

    The Commit port is determined using one of the following methods, listed
    in order of priority (the first applicable item will be used):

    1. The Commit port specified with
       `--dataport`.
    2. The HTTP port specified with `--port`.
       `cov-commit-defects` connects to this
       port to retrieve the dataport using HTTP if
       `--ssl` is absent or HTTPS if
       `--ssl` is present.
    3. The HTTPS port specified with `--https-port`.
       `cov-commit-defects` connects to this
       port using HTTPS to retrieve the dataport.
    4. The Commit port, specified with the
       `cim`/`commit`/`port`
       element from the XML configuration file.
    5. The HTTP or HTTPS port specified with the
       `cim`/`port` or
       `cim`/`https_port`
       element, respectively, from the XML configuration file.
    6. HTTP port 8080 without `--ssl` or 8443 with
       `--ssl` is used to retrieve the dataport
       from Coverity Connect.

    Note: If you are committing to an TLS/SSL-enabled instance of Coverity Connect,
    you might encounter an error message when you define the
    `--port` option (for example, `--port
    8443`. Use the `--https-port` option
    instead.

parallelthreads="N"
:   Allows you to control the number of analysis workers that run in
    parallel. This number is limited by the terms of your license. The
    default value for the `-j` option is 1.

    This attribute supports the analysis process.

password="password"
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specify the password for either the current user name, or the user
    specified with the `--user` option. For security reasons,
    the password transmitted to the Coverity Connect is encrypted. If
    unspecified, the default is (in order of precedence):

    1. The password from the `--url` option.
    2. The password element from the XML configuration file.
    3. The environment variable `COVERITY_PASSPHRASE`.
    4. The password in the file pointed to by the environment
       variable `COVERITY_PASSPHRASE_FILE`.

    Note: The passphrase can be stored in a file without any other text,
    such as a newline character.

    Attention: On multi-user systems, such as Linux, users can see
    the full command line of all commands that all users execute. For
    example, if a user uses the `ps -Awf` command,
    identifying information such as usernames, process identities, dates and
    times, and full command lines display.

    This attribute supports the commit process.

resultproperty="property_name"
:   The name of a property to store the return code of the command. It
    provides the maximum value of the `cov-analyze` and
    `cov-commit-defects` return code. Only used if
    `failonerror=false`.

    This attribute supports the analysis process.

stream="stream_name"
:   Specifies a stream name to which to commit these defects.

    If the stream option is not specified, the stream element from the XML
    configuration file is used.

    If the stream is associated with a specific language and you attempt to
    commit results from other languages to that stream, the commit will
    fail. However, in Coverity Connect, it is possible to associate a stream
    with multiple languages even if the stream was previously associated
    with a single programming language.

strippath
:   Strip the prefix from all file names in error messages and file
    references committed. This might make commits from multiple users match,
    even if the code is located in a different location.

    strippath is a nested element which expects one attribute,
    `prefix`. The value of the prefix attribute is the
    prefix that will be stripped from file names. This is an example of the
    `strippath` element: `<strippath
    prefix="/path/to/project/root">`

    If specified multiple times, strips all of the prefixes from each
    filename, in the order the strippath elements are supplied.

    This nested element supports the analysis process.

target="target_name"
:   Target platform for this project (for example, i386).

user="user_name"
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specifies the user name that is shown in Coverity Connect as having
    committed this snapshot. If unspecified, the default is:

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

version="version"
:   This snapshot's project version.

Elements

The following elements must be enclosed by the `covanalyzejava`
element.

checkeroption checker="checker_name" option="option_name" val="value"/
:   Pass option option_name (with optional value `value`) to a specific checker
    checker_name.

    For example:

    ```
    <checkeroption checker="NULL_RETURNS" option="check-bias" value="5"/>
    ```

disable checker="checker_name"/
:   Disable checker_name. This can be specified multiple times. See also
    `--list-checkers` and
    `--disable-default`. For example, to disable
    cross-references in defects in the code browser, specify disable
    checker="XREFS"/.

    ```
    [<disable checker="checker_name"/>
    ```

enable checker="checker_name"/
:   Enable checker_name. The checker name is case insensitive. This can be
    specified multiple times. See also the disable checker="checker_name"
    element and the disabledefault="true" attribute.

    ```
    [<enable checker="checker_name"/>
    ```

## Examples

Analyzing and committing results.

```
<target name="loadtask" description="Load the covanalyzejava task">
    <taskdef resource="com/coverity/anttask.xml" classpath="${anttask.jar}"/>
</target>

<target name="build.analyzeandcommit" description="Analyze and commit results" depends="loadtask">
  <covanalyzeandcommit
    dataport="${env.CIM_COMMIT_PORT}"
    dir="${env.PREVENTINTDIR}"
    host="${env.CIM_SERVER}"
    password="coverity"
    stream="${env.SA_TEST_PROJECT}"
    user="admin"
    version="1.2 rc 7"/>
</target>
```

Enabling all but one of the default checkers for the analysis.

```
<target name="analyzeandcommit.no.forwardnull" depends="loadtask">
  <property environment="env1"/>
  <echo message="Current PATH = ${env1.PATH}"/>
  <covanalyzeandcommit
    dataport="${env.CIM_COMMIT_PORT}"
    dir="${env.SA_INT_DIR}"
    disabledefault="true"
    host="${env.CIM_SERVER}"
    password="coverity"
    stream="${env.SA_TEST_PROJECT}"
    user="admin"
    version="1.2">
    <enable checker="FORWARD_NULL"/>
  </covanalyzeandcommit>
</target>
```

## See Also

cov-analyze

covbuild
