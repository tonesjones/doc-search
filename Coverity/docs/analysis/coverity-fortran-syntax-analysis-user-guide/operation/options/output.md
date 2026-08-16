---
title: "Output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/output.html"
content_id: "xrDzG6Uv37j6Xj1W_ZswWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:15.566388+00:00"
---

# Output

`-l`
:   Make a list file. The list filename is composed from the first source or
    library filename encountered, where the suffix is replaced by
    `.lst`. Delimit the option by `--`.
    Default: `-nl`.

`-l -`
:   Write the list file to `stdout`. Default:
    `-nl`.

`-l` *file*
:   Make a list file with filename *file*. Default:
    `-nl`.

`-plen` *l*
:   Place a maximum of *l* lines on a page, *l* >= 20. By default the
    IDE automatically takes the value from the page setup characteristics.
    Default for the command line version: `-plen 62`.

`-pwid` *w*
:   Place a maximum of *w* characters on a line, 60 <= *w* <=
    255. By default the IDE automatically takes the value from the page setup
    characteristics. Default for the command line version: `-pwid
    100`.

`-refstruct` *file*
:   Specify the name of a file in which the reference structure will be stored in XML format. If no
    filename is specified, the filename is fckrs.xml. See
    also Reference structure (Call tree). Default:
    `-nrefstruct`

`-moddep` *file*
:   Specify the name of a file in which the module dependencies will be stored in XML format. If no
    filename is specified the filename is fckmd.xml. See
    also Display of module dependencies. This is a command line option only.
    Default: `-nmoddep`

`-shinc`
:   List lines included from include files. Default:
    `-shinc`.

`-shsub`
:   Show source code and cross references of program units and subprograms. The listing of source
    code lines can be suppressed by disabling the `-shsrc`
    option. See Program-unit cross references. Default: `-shsub`.

`-shsrc`
:   List source code. To list source code the `-shsub` option must be in effect also.
    See Program-unit cross references. Default: `-shsrc`.

`-shsngl`
:   Include unreferenced constants, namelist groups and procedures, declared in
    include files or modules, unreferenced common-block objects and unreferenced
    imported module variables in the program-unit cross-references. Default:
    `-shsngl`.

`-shprg`
:   Show cross-reference listings of the program. See also Global program cross references. Default: `-shprg`.

`-shref`
:   Show the complete reference structure of the referenced procedures. See also Reference structure (Call tree). Default: `-shref`.

`-shref` *root list*
:   Show the reference structure for the roots specified. The specified roots
    must be separated by a ”`;`”, a ”`:`”, or a
    ”`,`”. Default: `-shref`.

`-shcom`
:   Show cross-reference listings of common-block objects. See also Cross references of common-block objects. Default: `-nshcom`.

`-shcom` *com list*
:   Show cross-reference listings of common-block objects of specified common
    blocks. The specified common blocks must be separated by a
    ”`;`”, a ”`:`”, or a ”`,`”.
    Default: `-nshcom`.

`-shmodtyp`
:   Show cross-reference listings of public module derived types. See also Cross references of public module derived types. Default:
    `-nshmodtyp`

`-shmodtyp` *mod list*
:   Show cross-reference listings of public module derived types of specified
    modules. The specified modules must be separated by a ”`;`”,
    a ”`:`”, or a ”`,`”. Default:
    `-nshmodtyp`.

`-shmodvar`
:   Show cross-reference listings of public module data. See also Cross references of public module data. Default: `-nshmodvar`

`-shmodvar` *mod list*
:   Show cross-reference listings of public module data of specified modules. The
    specified modules must be separated by a ”`;`”, a
    ”`:`”, or a ”`,`”. Default:
    `-nshmodvar`.

`-shmoddep`
:   Show the dependencies of modules. Default:
    `-nshmoddep`

`-shmoddep` *root list*
:   Show the dependencies of modules of specified modules. The specified modules
    must be separated by a ”;”, a ”`:`”, or a
    ”`,`”. Default: `-nshmoddeproot`.

    The options `-l`, `-plen`,
    `-pwid`, `-shcom`,
    `-shmod`, `-shmoddep`,
    `-shprg`, `-shref` are global only and must be
    specified before the filename of any source or library file. The other
    output options can also be specified locally to overrule the global setting
    temporary. See The usage of analysis options.
