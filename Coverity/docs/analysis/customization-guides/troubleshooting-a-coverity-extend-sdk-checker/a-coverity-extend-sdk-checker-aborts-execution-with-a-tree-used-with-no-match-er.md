---
title: "A Coverity Extend SDK checker aborts execution with a Tree used with no match error."
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/a-coverity-extend-sdk-checker-aborts-execution-with-a-tree-used-with-no-match-error..html"
content_id: "Q5xpwJFj9~lS00P4W6ZujA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:03.064082+00:00"
---

# A Coverity Extend SDK checker aborts execution with a Tree used with no match error.

Example:

```
[STATUS] Reading call graph
[STATUS] Computing callgraph.
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Incremental analysis could not be used - this may take a while.
[STATUS] Starting analysis run (analysis pass)
|0----------25-----------50----------75---------100|
*******************************************|
extend-patterns.hpp:111:operator
P5_tree: Tree used with no match in pattern Var 
SM NAME: a_never_follows_b
ANALYZING: a_never_follows_b_test.cpp:_Z5test6i
LINE 50: "B()"
0xb23c80 0xb23c68 call_expr, NAME: _Z1Bv TYPE: void
-0xb23c38 0xb23c20 addr_expr TYPE: void (void)*
 -0xb23f08 0xb23bc0 function_decl NAME: _Z1Bv, public TYPE: void (void)
This application has requested the Runtime to terminate it in an unusual way.
Please contact the application's support team for more information.
Returned with error code 0x3 at function 6.
```

Solution:

A pattern has been used before it matches anything.

For example, you can get this error if you run the following checker:

```
#include "extend-lang.hpp"
START_EXTEND_CHECKER( a_never_follows_b, int_store );
ANALYZE_TREE()
{
CallSite a( "A" );
CallSite b( "B" );
Var v;
tree t;
int i;
if( MATCH( b ) ) {
SET_STATE( v, 1 );
ADD_EVENT( v, "B", "B is called" << v );
}
else if( MATCH( a ) ) {
FOREACH_IN_STORE( t, i ) {
ADD_EVENT( v, "A", "A is called" << v );
COMMIT_ERROR( t, "A", "A is follows b" << t );
}
}
// CLEAR_STATE( v );
}
END_EXTEND_CHECKER();
MAKE_MAIN( a_never_follows_b )
```

against the following test case:

```
extern void A();
extern void B();
// OK
void test1() {
  A();
}
// OK
void test2() {
  B();
}
// OK
void test3() {
  A();
  B();
}
// Defect
void test4() {
  B();
  A();
}
// OK
void test5(int x) {
  if (x) {
    A();
  } else {
    B();
  }
  if (!x) {
    B();
  } else {
    A();
  }
}
// Defect
void test6(int x) {
  if (x) {
    A();
  } else {
    B();
  }
  if (!x) {
    A();
  } else {
    B();
  }
}
```
