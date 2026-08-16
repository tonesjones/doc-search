---
title: "Recompiling"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/recompiling.html"
content_id: "P5GcOY~1eo7ff9KpvVHzmQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:50.150690+00:00"
---

# Recompiling

The recompile sub-commands repeat a `cov-emit` compilation. You can use
this option, for example, with updated `cov-emit` binary or compiler
configuration settings to attempt to compile inputs that have previously failed. This is
similar to `cov-build --replay`.

You can modify the translation units that are recompiled with the `--tu`
and/or `--tu-pattern` options.

The recompile sub-commands are:

parse-source-only-tus [OPTIONS]
:   Recompiles source-only TUs from the intermediate directory (those that were
    added through 
    `cov-build --record-with-source`
     and that have not been recompiled already).

    This subcommand works only for C/C++ source code.

recompile [OPTIONS]
:   Recompile the set of TUs specified by the filter. For each TU to be
    recompiled, invoke `cov-emit` with the command line,
    environment settings, and current directory recorded in the emit repository.
    Source files are re-read from the file system.

    Note: This subcommand will not correctly recompile your selected TUs if the intermediate
    directory has been moved since running `cov-emit`. If you
    have moved your intermediate directory to a new location or separate
    machine, use `recompile-from-dir` and specify the new
    `--dir` location.

recompile-from-dir [OPTIONS]
:   Recompiles translation units from source contained within the emit directory.
    Replaying from the emit will have the same results, regardless of changes to
    the files in the filesystem (including deletion).

    This option is similar to `cov-build --replay-from-emit`,
    but it allows you to perform finer-grained filtering of the TUs being
    replayed. For example:

    ```
    cov-manage-emit --dir idir --tu 10 recompile-from-dir
    ```

    This subcommand works only for C/C++ source code.

replay-from-script -if json_file [OPTIONS]
:   Reads a JSON script produced by IncrediBuild
    or in the LLVM [Compilation Database format](https://clang.llvm.org/docs/JSONCompilationDatabase.html),
    builds a list of compile commands, and executes each of the compile commands against
    `cov-translate` for accelerating Windows code builds.

    The -if json_file option points to the JSON script file
    that is described in the `replay_from_script` command.

    For more information, see "Using IncrediBuild"
    in the Coverity Analysis 2026.6.0 User and Administrator Guide.

    Note: `--record-only` works the same as `cov-build
    --record-only`, recording the build to be replayed later.

retranslate [OPTIONS]
:   Run `cov-translate` on the set of TUs specified by the
    filter.

    For each TU to be recompiled, invoke `cov-translate` using
    the command line, environment settings, and current directory recorded in
    the emit repository. Does not work with a TU complied directly by
    `cov-emit`.

    Invocation of `cov-translate` requires a Coverity
    configuration. By default, the configuration that was used during the
    initial compilation will be used, but this can be overridden by specifying a
    configuration on the `cov-manage-emit` command line.

    This subcommand works only for C/C++ source code.

    Note: Note that this subcommand will not correctly retranslate your selected TUs
    if the intermediate directory has been moved since running
    `cov-emit`.

retranslate-or-emit [OPTIONS]
:   Run `cov-translate` on the set of TUs specified by the
    filter.

    Similar to the retranslate option, except that in the case of a TU where
    `cov-emit` was invoked directly without
    `cov-translate`, invokes `cov-emit`
    instead of using `cov-translate`.

    This subcommand works only for C/C++ source code.

    Note: Note that this subcommand will not work correctly if the intermediate
    directory has been moved since running `cov-emit`.

The recompile sub-command [OPTIONS] are as follows:

--compilation-log log_file
:   Saves diagnostic messages from `cov-translate` and
    `cov-emit` to log_file (instead of
    the default of standard output and standard error). Also displays a progress
    ticker bar.

--desktop
:   Used in conjunction with Desktop Analysis to perform recompilation faster by
    disabling bytecode decompilation in Java, C#, and Visual Basic builds.

--do-decomp
:   Used in conjunction with Desktop Analysis to perform recompilation in Java
    builds where bytecode decompilation is enabled.

--emit-complementary-info
:   Enables emitting of complementary information for compliance checkers such as
    MISRA checkers. Selecting this option results in a slower build capture but
    a faster analysis, and it should be applied when using compliance checkers.
    The default value is `--no-emit-complementary-info`

    Note: Enabling the --emit-complementary-info option prior
    to running an analysis is likely to turn up additional
    defects.

    Any analysis involving `--coding-standard-config` requires the
    information generated during `cov-build` when including the
    `--emit-complementary-info` option. The
    `cov-build` command will take longer, so this option
    should only be used when `cov-analyze` is used with
    `--coding-standard-config`.

    If `cov-build` did not include the
    `--emit-complementary-info` option and
    `cov-analyze` does include
    `--coding-standard-config`,
    `cov-analyze` automatically re-runs every
    `cov-emit` command (for the Translation Units to be
    analyzed). This excludes the native build and the
    `cov-translate` overhead, but it will add significant
    overhead to `cov-analyze`. Note that analysis will fail if
    the emit database does not include source; that is re-emit is not
    possible.

--name name
:   Associates any new TUs created with a build named name.
    New TUs are not created by `parse-source-only-tus` or
    `recompile-from-dir`. These commands will reuse the
    existing TUs, so this option will have no effect. TUs will also not be
    created if the TUs are already up to date.

--parallel number_of_processes

-j number_of_processes
:   Spawn up to number_of_processes processes to run the
    recompilations. This option accepts the number of processes, or
    `auto` which sets the number of replay processes to the
    number of logical processors in the machine (`-j 0` is also
    accepted and is the same as `auto`).
