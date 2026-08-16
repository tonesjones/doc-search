---
title: "'#pragma coverity compliance' directive: further examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pragma-coverity-compliance-directive-further-examples.html"
content_id: "8fUUKm9dwDAZad22AVtvVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:23.937716+00:00"
---

# '#pragma coverity compliance' directive: further examples

Here are some more examples of using `pragma coverity
compliance`.

The following example illustrates the annotation of a single line:

```
#pragma coverity compliance deviate "MISRA C-2012 Rule 10.1" "Approval #994"
// code with the defect to be deviated
```

The following example illustrates the use of block annotation, defaulting to file
scope.

```
#pragma coverity compliance block deviate:2 "MISRA C-2012 Rule 10.2" "Approval #998"
#include "foo.h" // no Rule 10.2 defects in foo.h will be deviated
// code defect 1 to be deviated
// more good code
// code defect 2 to be deviated
// expect 2 defects to be deviated - warn otherwise
#pragma coverity compliance end_block "MISRA C-2012 Rule 10.2"
```

The following example illustrates the block annotation of an included file:

```
#pragma coverity compliance block(include) deviate "MISRA C-2012 Rule 5.2" "Approval #992"
#include "foo.h" // deviate any Rule 5.2 defects in the included file foo.h
                 // (and in any files foo.h transitively includes)
// code defect to be deviated
// more good code
#pragma coverity compliance end_block(include) "MISRA C-2012 Rule 5.2"
```

Multiple annotations are supported within a single `#pragma coverity
compliance` directive by listing multiple groups of
*classification[:count]*
*checker_name* [*comment]*. Enclose each group in parentheses.

If the annotation has block scope, each checker must be listed after the
`end_block` in a following `#pragma` directive. As an
alternative, individual `end_block`
*checker_name* directives can be used in additional following
`#pragma` directives, allowing different line-number ranges for some
of the multiple annotations. For example:

```
#pragma coverity compliance block \
(deviate:2 "MISRA C-2012 Rule 5.2" "Approval #992") \
(fp:2 "MISRA C-2012 Rule 10.1" "Approval #994") \
(deviate "MISRA C-2012 Rule 10.2" "Approval #998")
#include "foo.h" // no Rule defects in foo.h will be deviated
// code defect 1 ( [5.2)] to be deviated
// good code
// code false positive ( [10.1]) to be ignored
// good code
// code defect 1 ( [10.2]) to be deviated
// code defect 2 ( [5.2]) to be deviated
// code false positive 2 ( [10.1]) to be ignored
#pragma coverity compliance end_block "MISRA C-2012 Rule 5.2" "MISRA C-2012 Rule 10.2"
// code defect 3 ( [5.2]) - not deviated
#pragma coverity compliance end_block "MISRA C-2012 Rule 10.1"
```
