---
title: "Example: tracking the sign of expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-tracking-the-sign-of-expressions.html"
content_id: "EGB3OWucur2mlb1Qy6TEOQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:36.219636+00:00"
---

# Example: tracking the sign of expressions

The previous store functions (except for `MATCH_STATE`) are demonstrated
in sign.cpp, a checker that tracks the sign of expressions. See
<install_dir>/sdk/samples/sign/sign.cpp or sign checker.

After some preliminary code to define the abstract domain, it uses the store to remember
sign information for variables and expressions.

When it sees certain function calls, it prints out some of the information that it is
tracking. Since we haven't yet covered the output routines, this checker just uses
cout.

The sign.test.c file (see
<install_dir>/sdk/samples/sign/test1/sign.test.c)
provides some basic input to the sign.cpp checker:

```
// sign.test.c
// test input for 'sign' checker
  
void whatis(int);
void print_store();
unsigned something();
int foo(int x, int y)
{
  whatis(x);
  whatis(y);
  int n_one = -1;
  int zero = 0;
  int one = 1;
  whatis(n_one);
  whatis(zero);
  whatis(one);
  whatis(n_one + zero);
  whatis(n_one + one);
  whatis(n_one - one);
  whatis(one + one);
  x = 3;
  y = 3;
  whatis(x+y);
  x = -3;
  y = -3;
  whatis(x+y);
  x = 0;
  x = x+1;
  whatis(x);
  unsigned u = something();
  whatis(u);
  
  x = zero - u;
  whatis(x);
  whatis(x + y);
  print_store();
  
  return 0;
}
// EOF
```

Complete the same steps that you followed for the hello checker as follows:

1. Run `build-checker` on sign.cpp
   (`build-checker sign`).
2. Copy `sign` to the Coverity Analysis bin
   directory.
3. Run `cov-build` on the sign.test.c
   file.
4. Run the `sign` checker on the intermediate directory.

A portion of the output is shown next:

```
sign.test.c:10: "x" has unknown value
sign.test.c:11: "y" has unknown value
sign.test.c:17: "n_one" has value AV_NEGATIVE
sign.test.c:18: "zero" has value AV_ZERO
sign.test.c:19: "one" has value AV_POSITIVE
sign.test.c:21: "(n_one + zero)" has value AV_NEGATIVE
sign.test.c:22: "(n_one + one)" has unknown value
sign.test.c:23: "(n_one - one)" has value AV_NEGATIVE
sign.test.c:24: "(one + one)" has value AV_POSITIVE
sign.test.c:28: "(x + y)" has value AV_POSITIVE
sign.test.c:32: "(x + y)" has value AV_NEGATIVE
sign.test.c:36: "x" has value AV_POSITIVE
sign.test.c:39: "u" has value AV_POS_ZERO
sign.test.c:42: "x" has value AV_NEG_ZERO
sign.test.c:43: "(x + y)" has value AV_NEGATIVE
sign.test.c:45: print_store:
  "y" has value AV_NEGATIVE
  "x" has value AV_NEG_ZERO
  "u" has value AV_POS_ZERO
  "zero" has value AV_ZERO
  "one" has value AV_POSITIVE
  "n_one" has value AV_NEGATIVE
  "-1" has value AV_NEGATIVE
  "0" has value AV_ZERO
  "1" has value AV_POSITIVE
  "(n_one + zero)" has value AV_NEGATIVE
  "(n_one - one)" has value AV_NEGATIVE
  "(one + one)" has value AV_POSITIVE
  "3" has value AV_POSITIVE
  "(x + y)" has value AV_NEGATIVE
  "-3" has value AV_NEGATIVE
  "(x + 1)" has value AV_POSITIVE
  "(zero - u)" has value AV_NEG_ZERO
  17 mappings
```
