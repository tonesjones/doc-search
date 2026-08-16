---
title: "Statement patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/statement-patterns.html"
content_id: "ywxrMGR34M5EDw8GYaqtuQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:27.227597+00:00"
---

# Statement patterns

Each kind of statement has its own pattern to match it:

- `AnyStatement` (also `StmtPat`) — Match any
  statement.
- `DoWhilePat` — Match a `do` statement.
- `ExprStmt` — Match a statement containing a single expression,
  for example `a++;`.
- `IfPat` — Match an `if` statement.

  Note that the guard expression for `if`, `for`,
  and `while` is normalized to a Boolean, and the match
  expression must agree with this normalized form. For example:

  ```
  int f();
    
  if (f()) { ... }
  ```

  The test is normalized by the parser to:

  ```
  if (f() != 0) { ... }
  ```

  Hence, to match this, use:

  ```
  CallSite call;
  MATCH(IfPat(call != 0))
  ```

  There is an example of this in
  ><install_dir>/sdk/samples/patterns/patterns.cpp.
- `ForPat` — Match a `for` statement.
- `WhilePat` — Match a `while` statement. See
  ><install_dir>/sdk/samples/whileloopassign/whileloopassign.cpp
  for some examples.
- `SwitchPat` — Match a `switch` statement.
- `ReturnPat` — Match a `return` statement. You
  can specify whether a value is returned. While there is always a return
  statement even when falling through the end of a function, you should use
  the 
  `ANALYZE_END_OF_PATH`
   handler to respond to control flow that exits the function.
- `Try` — Match a `try/catch` statement.
- `AsmPat` — Match an `asm` statement.
- `LoopPat` — Matches `for`,
  `while` and `do` statements. This pattern
  does not match loops with a condition of constant 0, for example it won't
  match:

  ```
  do {} while (0);
  ```

  because this isn't a loop. You can use
  `DoWhilePat` to match this case.

  Use:

  ```
  ExprPat loop_cond;
  LoopPat loop(loop_cond);
  ```

  to match a loop and pull out the conditional
  expression. You can then check the conditional (for example is a <= b, or
  a > b) and act accordingly.
