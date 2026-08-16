---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "EkBelFoASf5hrrSX9irIsA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:17.901023+00:00"
---

# Options

-acqintf
:   (analysis, global and local) During the local analysis phase, use the
    interfaces of previously--analyzed subprograms to validate calls and
    function invocations whose interfaces are not explicitly provided. If
    negated, the actual argument lists of subprogram invocations will only be
    verified during the global analysis phase.

    This option should be specified when analyzing an unrelated set of program
    units, and when interfaces have been updated but the a library file
    presenting these interfaces has not yet been updated.

    Default: `-nacqintf`

-allc
:   (analysis, global and local) Analyze all columns of each input record. If
    negated and the `-ff` option is not in effect, only columns 1
    to 72 (after expansion of any tabs) will be analyzed.

    Default: `-nallc`

-ancmpl
:   (analysis, global only) The complete program is analyzed. Unreferenced
    procedures, unreferenced and undefined common blocks, unreferenced and
    undefined common block objects, unreferenced modules, unreferenced and
    undefined public module variables, unreferenced public module constants and
    unreferenced public module derived types are flagged. If the
    `-anref` and `-rigorous` options are also
    in effect, the call tree will be traversed to detect unsaved common blocks
    and modules with unsaved public data which are not saved in the root of
    referencing program units.

    Default: `-nancmpl`

-anprg
:   (analysis, global only) Verify the consistency of the whole program.

    Default: `-anprg`

-anref
:   (analysis, global only) Analyze the reference structure.

    Default: `-anref`

--append
:   (control) Append defects from this analysis run to the defects from the last
    analysis run.

    This option is intended for combining the Coverity Fortran Syntax Analysis
    outpus from different code sets into a single emit. No attempt is made to
    cull duplicate file or defect entries.

-cntl <c>
:   (analysis, global and local) Allow a maximum of `c`
    continuation lines in a statement. The value of `c` must be
    999 or less.

    Default: depends on the selected compiler emulation

-cond
:   (analysis, global and local) Process debug lines (lines with a
    `D` in the first column). If this option is negated,
    debug lines are treated as comments.

    Default: `-ncond`

--config-path
:   (control) Specifies an alternate path where Coverity Fortran Syntax Analysis
    should look for its configuration files. By default, these are in
    `fortran/share/` relative to the
    `cov-analysis` installation directory.

--configuration
:   (control) The configuration option can be used to directly specify the name
    of the configuration file to be used by Coverity Fortran Syntax Analysis.

    For a list of the available configurations, use `cov-run-fortran
    --list-configs`. For a list of supported compiler emulations and
    their corresponding configuration filenames, consult Appendix A.1 in the Coverity Fortran Syntax Analysis User Guide.

-cpp
:   (analysis, global and local) Interpret C-style preprocessor directives as if
    the Fortran sources are first run through the C preprocessor
    `cpp`.

    Default: `-cpp` for files whose filename extension begins with
    `.F`; `-ncpp` otherwise.

-create
:   (analyis, global) Create a new library file. If more than one library file is
    specified, the library file to be created must be the first in the list.

    Default: `-ncreate`

-declare
:   (analysis, global and local) Generate a warning for all variables that have
    not been explicitly declared in a type statement.

    Default: `-ndeclare`

-define <symbols>
:   (analysis, global) Define metasymbols for conditional compilation. The list
    of `<symbols>` must be comma-, semicolon- or
    colon-separated.

    Default: `-ndefine`

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

-dp
:   (analysis, global and local) Map all real objects to double precision and all
    double precision objects to REAL(16). Map all complex objects to double
    complex and all double complex to COMPLEX(16).

    Default: `-ndp`

-externals
:   (analysis, global and local) Flag referenced external procedures which have
    not been deiclared `external`.

    Default: `-nexternals`

-f77
:   (analysis, global and local) Validate the syntax for conformance to the
    FORTRAN 77 standard. All nonstandard syntax will be flagged. Note that this
    option by itself does not enable FORTRAN 77 syntax validation. It is also
    necessary to select a configuration that supports FORTRAN 77 syntax. Both of
    these steps are taken if the configuration control options include the
    `--level` option.

    Default: `-nf77`

-f90
:   (analysis, global and local) Validate the syntax for conformance to the
    Fortran 90 standard. All nonstandard syntax will be flagged. Note that this
    option by itself does not enable Fortran 90 syntax validation. It is also
    necessary to select a configuration that supports Fortran syntax. Both of
    these steps are taken if the configuration control options include the
    `--level` option.

    Default: `-nf90`

-f95
:   (analysis, global and local) Validate the syntax for conformance to the
    Fortran 95 standard. All nonstandard syntax will be flagged. Note that this
    option by itself does not enable Fortran 95 syntax validation. It is also
    necessary to select a configuration that supports Fortran syntax. Both of
    these steps are taken if the configuration control options include the
    `--level` option.

    Default: `-nf95`

-f03
:   (analysis, global and local) Validate the syntax for conformance to the
    Fortran 2003 standard. All nonstandard syntax will be flagged. Note that
    this option by itself does not enable Fortran 2003 syntax validation. It is
    also necessary to select a configuration that supports Fortran 2003 syntax.
    Both of these steps are taken if the configuration control options include
    the `--level` option.

    Default: `-nf03`

-f08
:   (analysis, global and local) Validate the syntax for conformance to the
    Fortran 2008 standard. All nonstandard syntax will be flagged. Note that
    this option by itself does not enable Fortran 2008 syntax validation. It is
    also necessary to select a configuration that supports Fortran 2008 syntax.
    Both of these steps are taken if the configuration control options include
    the `--level` option.

    Default: `-nf08`

-f18
:   (analysis, global and local) Validate the syntax for conformance to the
    Fortran 2018 standard. All nonstandard syntax will be flagged. Note that
    this option by itself does not enable Fortran 2018 syntax validation. It is
    also necessary to select a configuration that supports Fortran 2018 syntax.
    Both of these steps are taken if the configuration control options include
    the `--level` option.

    Default: `-nf18`

-ff
:   (analysis, global and local) Specifies that source code is in the free source
    form. The exact interpretation depends on the compiler configuration and
    language level options selected.

    For files with the filename extension `f90`,
    `f95`, `f03`, `f2003`,
    `f03`, `F2008`, `F90`,
    `F95`, `F03`, `F2003`,
    `F03`, or `F2008` the default is
    `-ff`. For all other files, the default is
    `-nff`.

-I <paths>
:   (analysis, global) Set directories of include files. Path names must be
    separated by commas or colons with no embedded spaces.

    Default: `-nI`

-i2
:   (analysis, global and local) Default integers occupy 2 bytes.

-i4
:   (analysis, global and local) Default integers occupy 4 bytes.

-i8
:   (analysis, global and local) Default integers occupy 8 bytes.

-idep <d>
:   (analysis, global) Generate a file listing all referenced include files.

    Default: `-ndep`

--impact <impact>
:   (control) Selects the impact level of the issues formatted for input into
    Coverity Connect. Valid values are Audit, Low, Medium and High. A lower
    impact level selects all higher impact levels as well. Default: High

-include, -include -, -include <sub_list>
:   (analysis, global) From the library file, include the subroutines named in
    `<sub_list>` in the analysis. The
    `<sub_list>` must be a comma-, semicolon- or
    colon-separated list that does not contain any spaces. If
    `<sub_list>`is omitted, then all subroutines are
    included.

    Default: `-ninclude`

-informative
:   (analysis, global) Show informative messages.

    Default: `-ninformative`

-intent
:   (analysis, global and local) Flag parameters for which no INTENT attribute
    has been specified.

    Default: `-nintent`

-intrinsic
:   (analysis, global and local) Flag referenced intrinsic procedures which have
    not been declared intrinsic.

    Default: `-nintrinsic`

-l, -l <list-file>
:   (analysis, global only) Specified that a merged list file is desired and
    optionally supplies the list file name.

    In the first form, the file name is omitted. The listing is written to a file
    whose base name is the same as that of the first source file and has the
    filename extension `.lst`.

    In the second form, the file name is a single hyphen. The listing file is
    written to the standard output.

    In the third form, the listing filename is supplied. The listing is written
    to the specified file.

--level <level>
:   (control) Specifies the language level (standard) used to select a Coverity
    Fortran Syntax Analysis configuation file. Available values are:
    **`f77`****`f90`****`f95`****`f03`****`f08`****`f18`**

    The `--level` option selects the minimum language level that
    must be supported by the selected compiler configuration. We assume that a
    compiler supporting a given language level also supports all prior levels.
    Thus, for example, a compiler supporting Fortran 95 will also be selected if
    `--level f90` is specified.

    When this configuration control option is provided, the corresponding
    language level option (`-f77`, `-f90`,
    `-f95`, etc.) is also supplied to Coverity
    Fortran Syntax Analysis.

-library <filename>
:   (global) The filename specificed is a \FCK\ library file.

    Default: `-nlibrary`

-log
:   (global) Show defines and undefines of metavariables.

    Default: `-nlog`

--list-configs
:   (control) The `--list-configs` option reads all of the
    available configurations from the Coverity Fortran Syntax Analysis
    installation and prints out summary information in tabular form. Each entry
    contains the name of the configuration followed by a tuple containing its
    platform, vendor, version and language level. Any of these that are
    unspecified are omitted from the tuple.

-moddep, -moddep <file>
:   (analysis, global only) Generate a file containing the module dependency
    structure in XML format. If no filename is specified,
    `fckmd.xml` is used.

-obsolescent
:   (analysis, global and local) Flag all syntax elements marked as obsolescent
    in the Fortran standard that is in effect.

    Default: `-nobsolescent`

--platform <platform>
:   (control) Specifies the target architecture or operating system used to
    select a Coverity Fortran Syntax Analysis configuration file. This option
    can be used to narrow the configuration selection when a compiler has
    different features that depend on the platform. Usually, the
    `--vendor` and `--version` options are
    sufficient to select the desired compiler emulation. Platform values
    include: **`convex cray dec fujitsu hp9000 hpvms hp ibm rs6000
    unisys vax vms`**.

-plen <lines>
:   (analysis, global only) Specifies the page length of the output listing.
    Default:62

-pwid <columns>
:   (analysis, global only) Specifies the page with of the output listing.
    Default:100

-r8
:   (analysis, global and local) Map all default reals to double precision. Map
    all default complex objects to double complex.

-refstruct, -refstruct <file>
:   (analysis, global only) Generate a file containing the reference structure of
    the program. The output is stored in XML format. If no filename is
    specified, `fckrs.xml` is used.

-relax
:   (analysis, global and local) Relax type checking on integers, logicals and
    Holleriths. No messages will be produced for type conflicts between logicals
    and integers, for the use of relational operators on logicals, and for the
    use of logical operators on integers. Hollerith (character) constants can be
    used in expressions and mixed with logicals, integers and reals.

    Default: `-nrelax`

-report <filename>
:   (analysis, global) Generate a report file with the given name. The default
    filename extension is `.rpt`. If the filename is omitted,
    `fck.rpt` is used.

    Default: `-nrpt`

-rigorous
:   (analysis, global) Flag less robust and less portable code at the expense of
    more informative messages. This option removes the limit on the number of
    messages displayed per line, so should be used with caution.

    Default: `-nrigorous`

-save
:   (analysis, global and local) Assume that all variables are saved by
    default.

    Default: `-nsave`

--security-file <license file>

-sf <license file>
:   Path to a valid Coverity Analysis license file. If not specified, this path is given by the
    `security_file` tag in the Coverity configuration or by
    license.dat (located in the Coverity Analysis
    <install_dir>/bin directory). A valid license
    file is required to run the analysis.

-shcom, -shcom <com_list>
:   (analysis, global and local) In the listing file, show cross-references of
    common-block objects. The **`com_list`** names the common
    blocks to be displayed. If omitted, all common blocks are displayed.

    Default: `-nshcom`

-shinc
:   (analysis, global and local) In the listing file, show included source as
    well.

    Default: `-shinc`

-shmoddep, -shmoddep <mod_list>
:   (analysis, global only) Show module dependencies. If the
    **`mod_list`** is supplied, dependencies of the
    named modules are shown. Otherwise, dependencies are shown for all
    modules.

    Default: `-nshmoddep`

-shmodtyp, -shmodtyp <mod_list>
:   (analysis, global only) Show cross-reference listings of public module
    derived types. If the **`mod_list`** is supplied,
    cross-references for the named modules are shown. Otherwise,
    cross-references are shown for all modules.

    Default: `-nshmodtyp`

-shmodvar, -shmodvar <mod_list>
:   (analysis, global only) Show cross-reference listings of public module data.
    If the **`mod_list`** is supplied, cross-references for
    the named modules are shown. Otherwise, cross-references are shown for all
    modules.

    Default: `-nshmodvar`

-shprg
:   (analysis, global only) Show cross-reference listings for the program.

    Default: `-shprg`

-shref, -shref <root-list>
:   (analysis, global only) Show the complete reference structure of the
    referenced procedures. If supplied, the **`root-list`**
    provides the roots for the reference structure. If omitted, the main program
    is used as the root.

    Default: `-shref`

-shsngl
:   (analysis, global and local) In the program unit cross-references, show
    unreferenced constants, namelist groups and procedures that are declared in
    include files or modules. Also, show unreferenced common-block objects and
    unreferenced imported module variables.

    Default: `-shsngl`

-shsrc
:   (analysis, global and local) In the listing file, show the source code. To
    list source code, the `-shsub` option must also be in
    effect.

    Default: `-shsrc`

-shsub
:   (analysis, global and local) In the listing file, show the code and
    cross-references of program units and subprograms. The listing of source
    code lines can be suppressed using the `-nshsrc` option.

    Default: `-shsub`

-specific
:   (analysis, global and local) Flag all referenced procedures that are invoked
    using type-specific (i.e. non-generic) names.

    Default: `-nspecific`

-standard
:   (analysis, global and local) Validate all syntax for conformance to the
    selected language level (standard).

    Default: `-nstandard`

--strip-path <path>, -s <path>
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

    Table 1. Results of using `--strip-path`

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

    The `--strip-path` is available for several commands.

-truncate
:   (analysis, global) Truncate names to 6 significant characters.

    Default: `-ntruncate`

-update
:   (analysis, global) Update the library file. If the library file does not
    exist, it will be created.

    Default: `-nupdate`

--vendor
:   Specifies the compiler vendor to be used in selecting a Coverity
    Fortran Syntax Analysis configuration file. Vendor values include: **`absoft
    cd control convex cray cv compaq cyber dec digital equip res digres
    apollo domain ftn salford fujitsu gnu hp hewlett ibm intel lahey ms
    microsoft nag ndp ps pathscale pdp pgi princeton prime prospero rm
    ryan sgi silicon sun solaris oracle unisys watcom`**

--version <ver>
:   Specifies the compiler version to be used in selecting a Coverity
    Fortran Syntax Analysis configuration file. Valid values for the
    `--version` option are vendor-specific.

    This option should be specified only when emulation of a particular compiler
    version is desired. Moreover, not all configuration files provide version
    information, so specifying a particular version might select the empty
    set.

-warnings
:   (analysis, global) Show warnings.

    Default: `-warnings`

## Example 1

```
> cov-run-fortran --dir idir -- file1.f file2.f
```

This will use Coverity Fortran Syntax Analysis to analyze
file1.f and file2.f using the default
configuration file. Coverity Fortran Syntax Analysis defects will be written into
the output/ subdirectory of the emit directory
idir in a file called FC.errors.xml.
This file is suitable for upload to Coverity Connect using
`cov-commit-defects`.

## Example 2

```
> cov-run-fortran --dir idir --vendor intel --version 14.1 -- file1.f
```

This will use Coverity Fortran Syntax Analysis to analyze
file1.f, selecting the configuration file that will emulate
the Intel Fortran compiler version 14.1. Coverity Fortran Syntax Analysis will
accept all of the standard langauge constructs and extensions normally accepted by
the Intel Fortran compiler of that version. It will report incompatibilities with
the language recognized that compiler, including obsolescent and deleted features
and features supported by other compilers but not by that version of the Intel
Fortran compiler.

## Example 3

```
> cov-run-fortran --dir idir --vendor intel --version 14.1 --level f95 -- file1.f
```

This will use Coverity Fortran Syntax Analysis to analyze
file1.f, selecting the configuration file that will emulate
the Intel Fortran compiler version 14.1. Coverity Fortran Syntax Analysis will
accept all of the standard language constructs and extensions normally accepted by
the Intel Fortran compiler of that version. However, the `--level
f95` flag causes all language elements incompatible with the Fortran
95 standard (obsolescent, deleted, or supported only in a newer standard) to be
flagged.

## Example 4

```
> cov-run-fortran --dir idir -- -ff file1.f
```

This will use Coverity Fortran Syntax Analysis to analyze
file1.f using the default compiler configuration, but
forcing the interpretation of the input according to the free-form source form.
