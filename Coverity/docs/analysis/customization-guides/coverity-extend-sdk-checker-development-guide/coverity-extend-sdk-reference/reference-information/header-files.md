---
title: "Header files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/header-files.html"
content_id: "qH9iCqDJjesWSe1PCjOxHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:02.427835+00:00"
---

# Header files

The many header files in the <install_dir>/sdk/headers
directory are necessary to compile an Coverity Extend SDK checker. However,
only the following subset of these files declare or define functionality that can be
used in an Coverity Extend SDK checker.

- ast/astnode.hpp — Defines the `ASTNode` class, the base class
  of abstract syntax tree (AST) node types, such as expressions and
  statements.
- ast/cc.ast — Defines the AST node types, representing statements,
  expressions, and so on. It serves as the source for the generated header
  ast/cc.ast.hpp.
- ast/cc_flags.hpp — Defines enumerations used by AST node types.
- `extend/extend-lang.hpp` — Defines the primary set of macros that an Coverity
  Extend SDK checker uses.

  Note that `extend-checker-types` is not useful for end users.
- symbols/field.hpp — Defines the `field_t` type, a
  `symbol_t` representing a data member.
- symbols/function.hpp — Defines the `function_t` type, a
  `symbol_t` representing a function.
- symbols/symbol.hpp — Defines the `symbol_t` type, which is
  the base type for all the symbols (such as variables and functions).
- symbols/variable.hpp — Defines the `variable_t` type, a
  `symbol_t` representing a variable (global or local,
  including static data members).
- types/extend-types.hpp — Defines the `type_t` hierarchy,
  representing types.
- types/scalar-types.hpp — Defines enums and macros to go with the
  `scalar_type_t` type.

You can also use standard C/C++ headers.
