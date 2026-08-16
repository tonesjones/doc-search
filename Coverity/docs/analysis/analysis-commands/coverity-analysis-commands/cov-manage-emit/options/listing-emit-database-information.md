---
title: "Listing emit database information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/listing-emit-database-information.html"
content_id: "4IcvKkH1uupLDlV3pBvp0A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:49.463742+00:00"
---

# Listing emit database information

The `find` sub-command lists information stored in the emit DB such as
symbol names, locations, and definitions. By default, all translation units are included
in the results. You can optionally restrict the translation units used in these
operations with the `--tu` and/or `--tu-pattern`
options.

What is being matched by the regular expression (regex) is, in C++, the mangled name of the
symbol (according to the IA64 C++ ABI, see <https://itanium-cxx-abi.github.io/cxx-abi/abi.html#mangling>), of which the actual identifier is always a substring. In C,
what is matched is just the identifier.

find regular expression [OPTIONS]
:   There are four kinds of symbols: functions, classes, global variables, and
    enumerations. If you specify `find regular
    expression`, then the listing for the matching
    regex command is the symbol name, the kind of entity, the declaration
    location, and the definition TU.

You can control the information that is returned by using the following options:

--kind {f | c | e | g}
:   Restricts the search to certain types of entities. The choices are
    `f`, `c`, `e` and
    `g`, for function, class, enum, and global,
    respectively.

--print-callees
:   For a function, lists the set of functions it calls. Does not list
    information on other entities.

--print-codexm
:   Lists the entity's abstract syntax tree (AST) definition as CodeXM
    patterns.

    CodeXM is a specialized language used to write customized checkers that run
    using the Coverity engine.

--print-definitions
:   Lists the entity's definition syntax by pretty-printing the AST
    definition.

--print-debug
:   Lists the entity's AST definition in debug (indented tree) mode.

The `find` sub-command accepts multiple operands and applies each of
them as an inclusive filter when searching for symbols. In the following example, the
first invocation of `cov-manage-emit` displays all symbols (global_1
and global_2). .

```
$ cat t.c
int global_1 = 1;
int global_2 = 2;

$ cov-emit --dir covint t.c
Emit for file '/tmp/t.c' complete.

$ cov-manage-emit --dir covint find .
Matching global: global_1
 declared at:
   /tmp/t.c:1:5-/tmp/t.c:1:12
 defined in TU 1 with row 1
Matching global: global_2
 declared at:
   /tmp/t.c:2:5-/tmp/t.c:2:12
 defined in TU 1 with row 2
```

The following two examples supply a regex command that selects exactly one of those
symbols.

```
$ cov-manage-emit --dir covint find global_1
Matching global: global_1
 declared at:
   /tmp/t.c:1:5-/tmp/t.c:1:12
 defined in TU 1 with row 1

$ cov-manage-emit --dir covint find global_2
Matching global: global_2
 declared at:
   /tmp/t.c:2:5-/tmp/t.c:2:12
 defined in TU 1 with row 2
```

The following invocation specifies multiple regex commands that select both symbols.

```
$ cov-manage-emit --dir covint find global_1 global_2
Matching global: global_1
 declared at:
   /tmp/t.c:1:5-/tmp/t.c:1:12
 defined in TU 1 with row 1
Matching global: global_2
 declared at:
   /tmp/t.c:2:5-/tmp/t.c:2:12
 defined in TU 1 with row 2
```
