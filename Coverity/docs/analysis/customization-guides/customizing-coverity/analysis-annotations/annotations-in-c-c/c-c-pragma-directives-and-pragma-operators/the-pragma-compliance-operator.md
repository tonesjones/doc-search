---
title: "The '_Pragma()_' compliance operator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-_pragma-_-compliance-operator.html"
content_id: "4FJKpQUQ_FhNJKb0mjnMmQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:24.598689+00:00"
---

# The '_Pragma()_' compliance operator

The `_Pragma()` operator notates deviations from reporting compliance
issues, just as the `#pragma` directive does.

The C99, C++11, and later standards support `_Pragma()`.

The two examples that follow have the same effect.

The following example illustrates the annotation of a single line using
`#pragma`:

```
#pragma coverity compliance deviate "MISRA C-2012 Rule 10.1" "Approval #994"
// code with defect to be deviated
...
```

The following example illustrates the annotation of a single line using
`_Pragma()`:

```
_Pragma("coverity compliance deviate MISRA_C_2012_Rule_10_1 'Approval #994'")
// code with defect to be deviated
...
```

The syntax for invoking the `_Pragma()` operator is
`_Pragma("string-literal")`, where
`"string-literal"` is a string enclosed in double
quotes. Typically the argument contains `coverity compliance
deviate`, followed by a checker name, followed by an optional comment.

If the checker name or the comment contains a space, then additional, embedded quotes
are needed. (This is the case for the comment in the example immediately above.) The
embedded quotes can be single quotes, or they can be double quotes escaped with a
backslash ( `\` ).

The following are all properly formatted invocations of
`_Pragma()`:

```
_Pragma( "coverity compliance deviate checker-name comment" )
_Pragma( "coverity compliance deviate 'checker name' 'another comment'" )
_Pragma( "coverity compliance deviate \"checker name\" \"another comment\"" )
```

The following example shows the use of the operator within a macro:

```
#define EXAMPLE(a) \
_Pragma("coverity compliance deviate MISRA_C_2012_Directive_4_6 \"Approval #102\"") \
int a;
...
EXAMPLE(myVar); // deviation will be on this line
```

The `_Pragma()_` directive can include a `count` operator. As
of release 2025.6.0, if the number of defects is greater than the value specified in
the `count` field, Analysis does not apply the annotation and no
logging appears in applied-annotations.csv.
A warning about this does appear in deviations-warnings.txt.
