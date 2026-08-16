---
title: "The '#pragma coverity compliance' directive"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-pragma-coverity-compliance-directive.html"
content_id: "20oRMU~s5_OC1IQWd2Yngw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:23.293746+00:00"
---

# The '#pragma coverity compliance' directive

The `#pragma coverity compliance` directive lets a scan deviate from
reporting compliance issues.

The language standards C90 and later support `#pragma`.

This directive is introduced by `#pragma coverity compliance`, and
then is followed by directive instructions.

The directive instructions allow you to specify the following basic elements:

- The *scope* where the directive is applied: a line, a file, and so on
- The *classification* of the defect found: either a false positive or a
  deviation
- The *checker name* for the rule whose violation is to be ignored
- Comments

Syntax variations are shown in the sections that follow. The following element is
used in multiple variants:

- A `directive` is shorthand for
  `classification[:count] checker_name
  [comment]`.

## Single line, single checker annotation:

```
#pragma coverity compliance classification[:count] "checker_name" ["comment"]
```

The line scope is the line that contains `#pragma coverity compliance`
and the line that immediately follows.

As of release 2025.6.0, if the number of defects is greater than the value specified in the `count` field, Analysis does not apply the annotation
and no logging appears in applied-annotations.csv.
A warning about this does appear in deviations-warnings.txt.

## Single line, multiple checker annotation:

```
#pragma coverity compliance (directive) [(directive) ...]
```

## Block scope annotation:

```
#pragma coverity compliance block [(block_scope)] directive
    ...
#pragma coverity compliance end_block [(block_scope)] checker_name [checker_name ...]
```

... where `block_scope` is either `file` or
`include`.

If the *block_scope* is not present, it defaults to `file`.

The `file` scope excludes any intervening `#include`
files. The `include` scope includes any direct or transitive
`#include` files.

## Scope-definition values

- *scope* defines the lines in a source file where checker defects are
  subject to the annotation. Scope is either `line` (by default) or
  `block`, which can also cover included files. A scope is
  distinct for each checker, and scopes for different checkers can overlap.

  For
  a given checker, single line annotations have precedence over
  `block(file)`, which has precedence over
  `block(include)`. That is, finer-grained scopes have
  precedence over coarser-grained scopes. This allows for the inclusion of
  `false_positive` within a `deviate`
  block.
- *classification* can be either `deviate` or
  `false_positive` (abbreviated `fp`), depending
  on how you want defects found within *scope* to be reported.
- *count* specifies the number of defects expected to be found in the
  annotation scope. This value is optional.
  As of release 2025.6.0, if `count` is specified and the number of defects is greater than the
  `count` value, Analysis does not apply the annotation
  and no logging appears in applied-annotations.csv.
- *checker_name* is the name of the checker producing defects to be managed
  by the annotation. The name is either a string or an identifier name. Matches
  are not case-sensitive.
  - If the name is given as a string, this must be the checker name exactly
    as documented in the Coverity 2026.6.0 Checker Reference.

    For
    example, the string for MISRA C-2012 Rule 10.2 is "MISRA C-2012 Rule
    10.2".
  - If the name is given as an identifier, this must be the checker name
    with separator characters replaced by the underscore characters.

    For
    example, the identifier for "MISRA C-2012 Rule 10.2" is
    `MISRA_C_2012_Rule_10_2`.

    This convention
    is mainly a convenience to avoid character escaping in the argument
    string of the `_Pragma()` operator.
- *comment* is an optional user string that explains the reason for
  annotating the deviation.

You can use the backslash character for line continuation; for example:

```
#pragma coverity compliance block \
(deviate:2 "MISRA C-2012 Rule 5.2" "Approval #992") \
(fp:2 "MISRA C-2012 Rule 10.1" "Approval #994") \
(deviate "MISRA C-2012 Rule 10.2" "Approval #998")
```

Attention: Use care if your source code includes guards. Because the order of inclusion in
the source code determines when included files are expanded, it's important
for include annotation blocks to ensure the included file is expanded in the scope.

Results from include block annotations might be inconsistent when passing
preprocessed source code to Coverity. This might happen when using the
`cov-build` options
`--preprocess-next` or
`--preprocess-first`.

Note: When using string syntax for identifier names, *do not* replace spaces and
other non-alphanumeric characters with underscores.

That is, the deviation should
be as follows:

```
#pragma coverity compliance block(include) deviate MISRA_C_2012_Rule_7_2 "Approval #994"
```

...
or as the following:

```
#pragma coverity compliance block(include) deviate "MISRA C-2012 Rule 7.2" "Approval #994"
```

*Do
not* encode a checker name as follows:

```
#pragma coverity compliance block(include) deviate "MISRA_C_2012_Rule_7_2" "Approval #994"
```
