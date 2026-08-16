---
title: "Windows systems"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/windows-systems.html"
content_id: "owa_7dPoQbNt9SCgRkxZCg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:30.320047+00:00"
---

# Windows systems

You might encounter the following issues if you use Coverity Analysis on Windows
systems.

When using the `cov-build` command with Cygwin `make`, I get an error about not being able to load `cygwin.dll`.
:   Run the `cov-build` command in a Bourne or Bash shell. For
    example:

    ```
    > <install_dir>/bin/cov-build.exe --dir <intermediate_directory> bash make
    ```

    The
    problem is that `cov-build` executes `make`
    as if it were a native Windows program, but `make` is usually
    invoked from the Cygwin `bash` shell, which invokes it
    differently. Having `cov-build` use a Bourne or Bash shell
    lets the shell invoke `make` in the correct manner.

When using the `cov-build` with Cygwin and a shell script that invokes a build, I get a `CreateProcess` error.
:   Execute the build script in a Bourne or Bash shell using the format `sh|bash
    <script_name>`, where
    `<script_name>` is the script that executes the
    build.

    For
    example:

    ```
    > <install_dir>/bin/cov-build.exe --dir <intermediate_directory> \
      sh build.sh
    ```

    The problem is that Windows does not know how to
    associate a Cygwin shell script with the Cygwin shell that processes it.
    Therefore, you need to explicitly reference the shell when using the script.

The `cov-commit-defects.exe` command hangs when an invalid port is used for the remote host. When the host running the Coverity Connect uses Windows firewall and an invalid port is used with `cov-commit-defects.exe --host`, the command fails without an immediate error message. Eventually, a timeout error is returned.
:   Make sure to use the correct port. Also, check that the Windows firewall is configured to
    unblock the necessary port, or allow the Coverity commands to run as exceptions.
    See also the previous two questions.

The `cov-analyze` command returns error: `boost::filesystem::path: invalid name`
:   For `cov-analyze`, the `--dir` option does not support a
    path name with just the root of a drive, such as `d:\`.

    For
    `cov-analyze`, the `--dir` option does
    not support a path name with just the relative directory of a drive, such as
    `d:foo`. Valid values for path names with drives use the
    full directory name in addition to the drive letter (for example,
    d:\cov_apache_analysis), or a relative directory
    path name without a drive letter.

The `cov-analyze` command returns error: `[FATAL] No license file (license.dat) or license configuration file (license.config) found`
:   If you get a fatal `No license
    found` error when you attempt to run this command, you need to make sure
    that license.dat was copied correctly to <install_dir>/bin.

    On some Windows platforms, you might need to use
    administrative privileges when you copy the Coverity license to
    <install_dir>/bin. Due to file
    virtualization in some versions of Windows, it might look like
    license.dat is in <install_dir>/bin when it is not.

    Typically, you can set the administrative permission
    through an option in the right-click menu of the executable for the command interpreter
    (for example, Cmd.exe or Cygwin) or Windows Explorer.

The `cov-configure` returns error: `access denied`
:   On some Windows platforms, you might need to use
    Windows administrative privileges when you run `cov-configure`.

    Typically, you can set the administrative permission
    through an option in the right-click menu of the executable for the command interpreter
    (for example, Cmd.exe or Cygwin) or Windows Explorer.
