---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "xsdJY7YwODFaMcR9KBUGzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:43.387701+00:00"
---

# Examples

## Example 1:

```
> cov-configure --config myTest/coverity_config.xml --msvc
> cov-test-configuration --config myTest/coverity_config.xml MyTests.json
```

Output of the `cov-test-configuration` example:

```
Section [0] My Section Label
Tests run: 1, Failures: 0, Errors: 0

Sections run: 1, Tests run: 1, Failures: 0, Errors: 0
```

In this example, all tests passed.

## Example 2:

```
> cov-test-configuration --config myTest/coverity_config.xml OtherTests.json
```

Output of the `cov-test-configuration` example:

```
Section [0] My Section Label
Tests run: 1, Failures: 0, Errors: 0

Section [1] Microsoft C/C++
Tests run: 5, Failures: 2, Errors: 1

Section [1] Microsoft C/C++: Test [0]: Assertion [contains][2] failed
Given input: cl -c foo.c
Expected   : output contains bob
Actual     : cov-emit.exe ... --c --microsoft --no_alternative_tokens \
-w --ignore_calling_convention --microsoft_version 1300 \
--no_stdarg_builtin -D_USE_ATTRIBUTES_FOR_SAL=0 foo.c 

Sections run: 2, Tests run: 6, Failures: 2, Errors: 0
```

The example shows two test failures. Failures are `assertion`
operators that failed. Errors are failures that were encountered when executing
`cov-translate`.

The ellipsis (`...`) in the example represents other arguments that
`cov-translate` adds to make `cov-emit`
imitate the `cl` input more precisely.
