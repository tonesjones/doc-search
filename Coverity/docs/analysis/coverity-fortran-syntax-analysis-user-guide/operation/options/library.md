---
title: "Library"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/library.html"
content_id: "ihFrm9m2C~ppv1Jk4AlM9A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:16.205917+00:00"
---

# Library

`-create`
:   Create new library file. If more than one library file is specified, the
    library file to be created must be the first in the list. Default:
    `-ncreate`.

`-include`
:   Include all program units from the library file in the analysis. To prevent
    the string following the option to be interpreted as an option argument, you
    can terminate the option with ”–”. Default:
    `-ninclude`.

`-include` *sub list*
:   Include specified program units from library file in the analysis. The
    specified program units must be separated by a ”`;`”, a
    ”`:`”, or a ”`,`”. Default:
    `-ninclude`.

`-library`
:   The filename specified is a Coverity Fortran Syntax Analysis library file. Default:
    `-nlibrary`. The current directory is searched first if
    the given library file path is relative. If that fails and the library name
    is a simple name (without path components), the `models`
    directory in the installation tree is also searched.

`-update`
:   Update library file. If the file does not exist, it will be created. Default:
    `-nupdate`.

    Library options are local only and must be specified right in front of the
    name of the library file on which they must operate.
