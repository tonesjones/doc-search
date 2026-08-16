---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "z9Wn6FTonIUJ447~vRZJHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:42.025491+00:00"
---

# Options

--addmodule <file>
:   Identifies a module that is referenced by the compilation but not added to the emit repository.
    The location of the module can be absolute or relative. For rules on
    specifying the location, see `--reference`.

    It is an error if the referenced module is not found. To change this
    behavior, see `--allow-missing-refs`.

    You must specify this option separately for each module.

--allow-missing-refs
:   Issues a warning if any referenced assemblies are missing. If you do not set this option, missing
    assemblies result in an error that stops the process. This error applies to
    explicitly referenced assemblies (see `--reference` and
    `--addmodule`) that are absolute or not found in the
    Common Language Runtime (CLR) system directory. The error also applies to
    mscorlib.dll (see `--nostdlib`).
    Note that missing vbc.rsp assemblies (see
    `--noconfig`) always result in a warning.

--codepage <codepage>
:   Identifies the numeric codepage corresponding to codepages that are supported
    by VBC with the `/codepage` option. Source file encodings are
    determined in the following manner:

    If a byte order mark (BOM) is present in the source file, the command uses
    the BOM-related encoding. If a BOM is *not* present, encoding is
    determined in the following manner:

    - The character encoding of the specified codepage is used. If a
      codepage is not specified, the command attempts to detect and use
      UTF-8. If neither of the preceding alternatives is possible, the
      command uses the system default codepage.

--compiler-dir <directory>
:   Identifies the CLR system directory. It is an error to specify a directory
    that does not exist. The CLR system directory is used as a search path for
    referenced assemblies (see `--reference`) and to locate the
    vbc.rsp file (see `--noconfig`). If
    `--compiler-dir` is not specified, the command defaults
    to
    $SYSTEM_ROOT/Microsoft.NET/Framework/<version>,
    where <version> is the latest supported framework version (for
    details, see the Coverity 2026.6.0 Installation and Upgrade Guide). It is an error if
    no suitable CLR system directory is found.

--define <define>
:   Corresponds to the VBC preprocessor directive and `/define`
    option. Note that it is necessary to specify a separate
    `--define` option for each directive.

--dir <intermediate_dir>
:   Identifies the intermediate directory into which this command emits source
    files and referenced assemblies. An error occurs if the specified
    intermediate directory exists but is not valid, or if the directory does not
    exist and cannot be created.

    This option is required.

--disable-ref-assembly-replacement
:   By default, the `cov-emit-vb` command attempts to replace
    each reference assembly it encounters with a version of the assembly that
    includes an implementation. Use this switch to disable this default
    behaviour. The recommended use of this switch is as an xml-option option to
    a `cov-configure` command.

    Example of adding this switch to a Visual Basic configuration:

    ```
    cov-configure --cs -c config/config.xml --xml-option=:"<append_arg>--disable-ref-assembly-replacement</append_arg>"
    ```

--enable-cs-parse-error-recovery
:   Makes `cov-emit-vb` fall back to error recovery mode when
    compilation errors are encountered during the processing of source
    files.

    This option is disabled by default.

--force
:   Disables incremental compilation by forcing the command
    to compile and generate output for all source files, including files that have
    already been compiled and are present in the Intermediate Directory and whose
    timestamps has not changed.

--imports <namespace name>
:   Imports a namespace from an assembly. Corresponds to the VBC option
    `/imports`.

--langversion <Visual Basic language version>
:   Specifies the Visual Basic Language version to use. Corresponds to the VBC
    option `/langversion`.

--lib <directory>, -L <directory>
:   Identifies a library directory to use when searching for referenced
    assemblies (see `--reference`). A warning (not an error)
    occurs if you specify a directory that does not exist. This option
    corresponds to the VBC `/lib` option.

    You must specify this option separately for each library directory.

--link <[alias=]filename> | -l <[alias=]filename>
:   Supercedes `--use-link-semantics`. Effectively the same as
    `--reference`, but changes how the compiler treats
    certain COM interop types. Corresponds to the VBC option
    `/link`.

--no-banner
:   Suppresses the `cov-emit-vb` application name and version
    banner.

--noconfig
:   Ignores the vbc.rsp file under the CLR system directory
    (see `--compiler-dir`). If this option is not set, the
    references `/r` or `/reference` within
    vbc.rsp are added to the list of referenced
    assemblies. Any vbc.rsp references that are not
    absolute filenames are subject to the search directory rules (for details,
    see `--reference`). Corresponds to the VBC option
    `/noconfig`.

--no-friends
:   Prevents the compilation from accessing internal types or members. This
    option works by disabling the processing of compiler output retrieved
    through the `--out` option. This behavior corresponds to VBC
    behavior in the case where `/out` is not specified and a
    default name is used.

--no-out, -n
:   Indicates that there is no compiler output.

    It is necessary to specify `--out` or
    `--no-out` (or the alternative, `-n`), else an error
    will occur.

--nostdlib
:   Disables the default behavior of searching for
    mscorlib.dll in the CLR system directory and adding
    the file to the list of referenced assemblies. If that file is not found,
    the next search in this directory is for a
    vbc.exe.config file that specifies a
    requiredRuntime version. If a version is found, the
    search continues to the corresponding directory (the parent directory of the
    CLR system directory).

    This option corresponds to the VBC `/nostdlib` option.

--optioncompare
:   Controls whether string comparisons should be binary or use locale-specific
    text semantics. Corresponds to the VBC option
    `/optioncompare`.

--optionexplicit
:   Controls whether the compiler enforces explicit declaration of variables.
    Corresponds to the VBC option `/optionexplicit`.

--optioninfer
:   Controls whether the compiler allows use of local type inference in variable
    declarations. Corresponds to the VBC option
    `/optioninfer`.

--optionstrict
:   Controls whether the compiler uses strict language semantics. Corresponds to
    the VBC option `/optionstrict`.

--out <file>
:   Specifies the compiler output file, which is then used by the command to
    access internal types or members in referenced assemblies.

    Subsequent calls to `cov-emit-vb` will not re-emit the
    output file if a referenced assembly is found.

    It is necessary to specify `--out` or
    `--no-out` (or the alternative, `-n`), else an error
    will occur.

--ref-assembly-replacement-search-path <path>
:   Adds a search path to assist `cov-emit-vb` in finding
    implementation versions of reference assemblies. You can specify this option
    multiple times. This option is useful for pointing
    `cov-emit-vb` at the correct .NET Core framework
    directory in cases where `cov-emit-vb` fails to find the
    correct version. The recommended use of this switch is as an xml-option
    option to a `cov-configure` command.

    Example of adding this switch to a Visual Basic configuration:

    ```
    cov-configure --vb -c config/config.xml --xml-option=:"<append_arg>--ref-assembly-replacement-search-path=D:\utilities\dotnet-core\dotnet-sdk-2.1.403-win-x64\shared\Microsoft.NETCore.App\2.1.5\</append_arg>"
    ```

--reference <[alias=]filename> | -r <[alias=]filename>
:   Identifies an assembly to provide for compilation and addition to the emit
    repository, unless this setting is overridden by other options. The location
    of the assembly can be absolute or relative. If relative, the command
    searches the following paths in the following order:

    1. Current working directory.
    2. CLR system directory.
    3. Each directory specified by the `--lib` option, in
       the order specified.

    By default, it is an error if a referenced file cannot be found on disk. See
    `--allow-missing-refs` for complete rules.

    Note that `[alias=]` identifies an external alias directive,
    just as it does for VBC.

    Example with an alias:

    ```
    --reference v1=my.dll
    ```

--removeintchecks
:   Disables integer overflow checking by the compiler. Corresponds to the VBC
    option `/removeintchecks`.

--rootnamespace <namespace name>
:   Specifies a namespace for all type declarations. Corresponds to the VBC
    option `/rootnamespace`.

--sdkpath <directory>
:   Specifies where to search for mscorlib.dll and
    Microsoft.VisualBasic.dll. Corresponds to the VBC
    option `/sdkpath`.

--target
:   Specifies the type of assembly that was created. Corresponds to the VBC
    option `/target`.

--vbruntime -|+|*
:   Specifies whether the compiler should compile with a reference to
    Microsoft.VisualBasic.dll (`+`),
    without a reference to it (`-`), or to embed it within the
    assembly (`*`). Corresponds to the VBC option
    `/vbruntime[+|-|*]`.

--vbruntime-path <filename>
:   Specifies the exact file the compiler should use for
    Microsoft.VisualBasic.dll. Corresponds to the VBC
    option `/vbruntime:<filename>`.

Any unrecognized options result in an error, which causes an immediate exit with an
appropriate error message.
