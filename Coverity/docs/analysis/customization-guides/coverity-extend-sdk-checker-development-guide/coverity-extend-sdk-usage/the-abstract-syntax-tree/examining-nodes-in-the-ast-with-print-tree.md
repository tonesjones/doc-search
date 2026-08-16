---
title: "Examining nodes in the AST with print_tree"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examining-nodes-in-the-ast-with-print_tree.html"
content_id: "S6aE4ln~kVRcYUqtdqOY1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:28.869800+00:00"
---

# Examining nodes in the AST with print_tree

You can use the print_tree function to return detailed information about
each node of the AST, as shown in the print_tree checker next:

```
// print_tree.c
// Coverity Extend SDK checker printing the AST tree at every node
        
#include "extend-lang.hpp"     // Coverity Extend SDK API
        
START_EXTEND_CHECKER( hello, simple );
        
ANALYZE_TREE()
{
    print_tree(CURRENT_TREE);
}
        
END_EXTEND_CHECKER();
        
MAKE_MAIN( hello )
        
// EOF
```

The source code and makefile for this checker are located in the
<install_dir>/sdk/samples/print_tree directory.

Like the hello
checker, this checker prints every abstract syntax tree that is passed into the
ANALYZE_TREE function. However, the `print_tree`
checker returns much more detailed information than the `hello` checker.
You can use `print_tree(CURRENT_TREE)` to expose detailed information
about an AST node. For example, the exact kind and many other details of each program
element are exposed by the `element` structure, which you can see in the
output below.

If you run this checker on the sample program at
<install_dir>/sdk/samples/print_tree/test1/print_tree_test.cpp
the output has the following format:

```
[STATUS] Reading call graph
[STATUS] Computing class hierarchy
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing call graph
[STATUS] Starting analysis run (analysis pass)
|0----------25-----------50----------75---------100|
***************************************************tree = S_compound:
  loc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:5
  endLoc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:9
  stmts = {
    element = S_decl:
      loc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:6
      decl = Declaration:
        var = "x"
        init = IN_expr:
          expr = E_intLit:
            cached_hash = 0
            type = int
            i = 1
            original_expr = <null Expression>
        destructionCode = <null Statement>
        initCode = S_expr:
          loc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:6
          expr = E_assign:
            cached_hash = 0
            type = int
            target = E_variable:
              cached_hash = 0
              type = int
              var = "x"
            op = 21
            src = E_intLit:
              cached_hash = 0
              type = int
              i = 1
              original_expr = <null Expression>
        destroyStmts = {
          tree = S_destroy
        }
    element = S_expr:
      loc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:7
      expr = E_assign:
        cached_hash = 0
        type = int
        target = E_variable:
          cached_hash = 0
          type = int
          var = "x"
        op = 9
        src = E_intLit:
          cached_hash = 0
          type = int
          i = 5
          original_expr = <null Expression>
    element = S_return:
      loc = /nfs/foo2/extend/samples/print_tree/test1/print_tree.test.cpp:8
      expr = E_variable:
        cached_hash = 0
        type = int
        var = "x"
      isImplicit = 0
  }
```
