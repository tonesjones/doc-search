---
title: "Dissecting the hello checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dissecting-the-hello-checker.html"
content_id: "62PJoEmYohFhiGRuaSXRGQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:26.277023+00:00"
---

# Dissecting the hello checker

This section describes each line of hello.cpp.

The following include is for the header file that contains declarations for the classes,
functions, and macros that comprise the Coverity Extend SDK API:

```
#include "extend-lang.hpp"  // Coverity Extend SDK API
```

The headers are explained in detail in Header files.

The next line declares that the name of the checker is hello and that
it is a *simple* checker:

```
START_EXTEND_CHECKER( hello, simple );
```

Here, `simple` means that the checker is flow-insensitive: the checker is
stateless, and the Abstract Syntax Tree (AST) nodes are not visited in any particular
order. An AST is a tree-shaped data structure that represents the phrase structure of
the concrete input syntax (for more information, see The Abstract Syntax Tree). >Note that subsequent
sections will introduce you to examples of flow-sensitive checkers. The Coverity
Extend SDK macros such as START_EXTEND_CHECKER and
ANALYZE_TREE are explained in Handler functions.

The next line starts the principal function of a checker:

```
ANALYZE_TREE()
```

The body of ANALYZE_TREE is called for every AST in the program that
is undergoing analysis. The ASTs are passed one at a time, and as they arrive, each one
is then the CURRENT_TREE.

The next line prints the current AST to standard output:

```
{
  cout << "ANALYZE_TREE: " << CURRENT_TREE << endl;
```

The next line prints the current AST as an issue report:

```
  OUTPUT_ERROR("ANALYZE_TREE: " << CURRENT_TREE);
```

This report is also stored in an intermediate directory output file,
output/hello.errors.xml. Note that, as discussed in Output, not every call to
OUTPUT_ERROR results in a user-visible issue report. For example,
if the path along which the issue is found is later determined to be infeasible, the
report is suppressed. Consequently, printing to standard output is useful as a debugging
aid, but OUTPUT_ERROR should be used for the actual issue
reports.

The Extend SDK defines *pattern types* which can be used to determine if the current
AST node meets certain criteria. As an example, here we create a pattern which matches
return statements by declaring a variable ret of type `ReturnPat`. The
MATCH predicate determines whether the current AST node being processed by the checker
matches the pattern. See Patterns for more details.

The `print_tree` function displays detailed information about the AST
node; for more information, see Examining nodes in the AST with print_tree

```
  ReturnPat ret;  
  if( MATCH(ret) ) print_tree(CURRENT_TREE);
}
```

The next line signals the end of the checker:

```
END_EXTEND_CHECKER();
```

The final line creates main(), the entry point to the checker
executable. The name of the checker is passed as an argument.

```
MAKE_MAIN( hello )
```
