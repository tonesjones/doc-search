---
title: "Abstract comparison"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/abstract-comparison.html"
content_id: "zsYsn8pSRNhMflyen2~poQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:46.048812+00:00"
---

# Abstract comparison

The core of the checker is in the section titled *abstract comparison*, which defines what
it means to compare two abstract values using operators like `<` and
`==`. Whenever an operator `<op>` is used to
compare abstract values `a` and `b`, and we follow the
path where the comparison yields true, there are several possible consequences embodied
in `AbstractComparisonResult:`

1. We might decide that the comparison could not possibly have yielded true, in
   which case its truth is *inconsistent* with the current abstract state.
   For example:

   ```
   int x = 0;
    if (x < 0) {
     // inconsistent, i.e., unreachable
   }
   ```
2. We might discover new facts about `a` or `b`.
   For example:

   ```
   int x = 0;
   if (x == y) {
     // discover that 'y' equals 0 as well
   }
         
   if (y <= 0 && z >= 0) {
     // discover: y <= 0
     // discover: z >= 0
     if (z == y) {
       // discover: y == 0 and z == 0
     }
   }
   ```
3. We might discover no new information. For example:

   ```
   if (x < y) {
     // lacking any previous information about 'x' and 'y', the
     // constraint 'x < y' cannot be expressed in our abstraction
   }
   ```

In the `sign3` checker, this computation is performed by the
`abstractComparison` function. This function is probably more
complicated than ones you write, but illustrates the general technique in a realistic
setting.

Because there are six relational comparison operators, there are six precomputed abstract
relation tables stored in the `relationalOperators` global variable. The
RelationalOperator class effectively maps from an AST tree code
to an abstract operator table.
