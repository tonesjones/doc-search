---
title: "START_EXTEND_CHECKER"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/start_extend_checker.html"
content_id: "brVGpaR4UEhHzmJbO7xogA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:06.381197+00:00"
---

# START_EXTEND_CHECKER

**Synopsis**

```
START_EXTEND_CHECKER( checker_name, checker_type );
```

**Description**

The START_EXTEND_CHECKER macro call ends section (1) and begins section (2). This macro begins a class declaration.

**Arguments**

`checker_name` is the name of your checker. This is the same name as the
name of the source file (without the `.c` extension). This name is used
by Coverity Connect to identify defect reports that are created by your
checker.

`checker_type` is one of the following:

- `simple`— Checker type used for flow-insensitive (stateless)
  checkers. It has no store. For more information about the store, see The store.
- `int_store`— Checker type used for flow-sensitive (stateful)
  checkers. Its store maps from expressions to integers; the exact meaning of the
  integers is up to you to establish.
- `type`— A special kind of checker that has no store and does not
  analyze abstract syntax trees. It visits each class that has been defined. See
  ANALYZE_CLASS.
