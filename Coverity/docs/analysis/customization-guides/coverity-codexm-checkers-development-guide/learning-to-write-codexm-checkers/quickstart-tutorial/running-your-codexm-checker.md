---
title: "Running your CodeXM checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-your-codexm-checker.html"
content_id: "X0Uz1RY44pcLJ55MJFsT7A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:36.116638+00:00"
---

# Running your CodeXM checker

Let's run the checker that we've just created.

Your code base might not actually have any `goto`
statements—and we'd rather not have you put one in if that's the case—but we would like you to see some results,
so here is a simple C program with a `goto` in it, just for this purpose:

[image: C code follows]

```
#include <stdio.h>

void donothing() {
    // Absolutely nothing
}

void function(int x, int y) {
    int z;
    if(x > 42) {
        goto pastIt;
    }

    donothing();
    pastIt:
    z = x * y;

    printf("z = %d", z);
}
        
void main() {
    function(1, 2);
}
```

Save this as `mygoto.c`, and run one of the variants of `cov-build` as shown below, depending on which compiler you have at hand:
`gcc` or the Microsoft® C/C++ compiler `cl`.
This builds your intermediate directory—we've named it `mycxm`—which you can reference when you run your CodeXM checker.

[image: Command line follows]

```
$ cov-build --dir mycxm gcc -o mygoto.o mygoto.c
```

... or:

[image: Command line follows]

```
$ cov-build --dir mycxm cl -o mygoto.o mygoto.c
```

Note:
If you are using a different compiler—and assuming that it is available on your path—simply substitute
that compiler's command name for `gcc` or `cl`, above.

Now that we have an intermediate directory, we can get back to running our CodeXM checker, as follows.

To apply your checker to the little sample we gave you, execute the following command line:

[image: Command line follows]

```
$ cov-analyze --dir mycxm --codexm mychecker.cxm
```

Once the analysis is complete, its output should appear something like this:

[image: Command output follows]

```
Using 36 workers as limited by CPU(s)
Looking for translation units
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing links for 1 translation unit
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing virtual overrides
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing callgraph
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Topologically sorting 3 functions
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing node costs
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Running analysis
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Exporting summaries
|0----------25-----------50----------75---------100|
****************************************************
Analysis summary report:
------------------------
Files analyzed                 : 1
Total LoC input to cov-analyze : 2526
Functions analyzed             : 3
Paths analyzed                 : 6
Time taken by analysis         : 00:00:02
Defect occurrences found       : 1 NO_GOTO
```

Typically you would use `cov-commit-defects --dir intermediate-dir` to commit your results to Coverity Connect.
For the purposes of this exercise (and when rapidly developing a CodeXM checker), you can also quickly inspect the results by invoking
`cov-format-errors`, as follows:

[image: Command line follows]

```
$ cov-format-errors --dir mycxm --html-output errs
```

When this finishes, you should find a directory, errs/, that contains some HTML files, notably
index.html.
To view the defects found by the analysis, use a browser to open index.html.

This concludes our QuickStart. To learn more, you can read further in this manual.
