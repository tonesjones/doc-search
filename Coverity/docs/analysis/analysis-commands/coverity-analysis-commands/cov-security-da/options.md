---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "vB_fqY5O4otsmZtFEQTisg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:24.420809+00:00"
---

# Options

--bytecode-da-timeout
:   [C# and Visual Basic Security Analysis option] Specify the maximum amount of
    time (in ms) that the C#/VB Dynamic Analysis engine will spend analyzing a
    single method. The default is 10000 (10s).

--bytecode-da-global-timeout
:   [C# and Visual Basic Security Analysis option] Specify the maximum amount of
    time (in ms) that the C#/VB Dynamic Analysis engine will spend analyzing the
    entire application. The default is 1800000 (30 minutes).

--da-max-mem
:   [Java Web application security option] Sets the JVM heap size of the VM that
    is running the dynamic analyzer, a component of the Java Web application
    security analysis. The option accepts an integer that specifies a number of
    megabytes (MB). The default value is 1024.

--dir <intermediate directory>
:   Specifies the intermediate directory to emit to. This option is required: You
    must specify a directory.

--no-bytecode-da
:   Disables all bytecode analysis for Java, C#, and Visual Basic.

--run-template-da-on-emit
:   Specify to have `cov-security-da` attempt to re-run the
    template-DA on an existing intermediate directory that contains one or more
    captured JavaScript projects.

--template-da-timeout
:   Specify the maximum amount of time to take (in ms) when analyzing a single
    JavaScript template file. Defaults to 1 minute.

--tu <id>, --tu-pattern <translation_unit_pattern>
:   Restricts the dynamic analysis to specific translation units, identified
    either by numeric ID (`--tu`) or by pattern
    (`--tu-pattern`).

    The `--tu-pattern` option can be specified multiple times.
    Both `--tu` and `--tu-pattern` can be
    specified on a single command line. The tool runs on the union of the
    translation units indicated by all such options.

    It is an error if at least one `--tu-pattern` argument is
    specified but no translation unit matches any of the specified patterns.

    For more information, see Translation unit pattern matching.
