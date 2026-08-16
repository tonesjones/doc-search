---
title: "Comparison evaluation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/comparison-evaluation.html"
content_id: "91OgjbNsQqHQn1A1akmCQw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:46.710724+00:00"
---

# Comparison evaluation

The ANALYZE_CONDITION function begins by attempting to match the input
condition with each of the six relational operators:

```
for (int i=0; i < NUM_RELATIONAL_OPERATORS; i++) {
  RelationalOperator *relop = relationalOperators[i];
  if (MATCH_COND(Binop(relop->treeCode, a, b))) {
```

When it finds a match, it abstractly evaluates the arguments `a` and
`b`; an unmapped expression corresponds to
`AV_UNKNOWN`:

```
    if (!GET_STATE(a, va)) { va = AV_UNKNOWN; }
    if (!GET_STATE(b, vb)) { vb = AV_UNKNOWN; }
```

It then performs the abstract comparison by doing a table lookup:

```
    AbstractComparisonResult &res = relop->map[va][vb];
```

If the comparison is infeasible, that is, it could not possibly have evaluated to true,
then we abort analysis of the current path:

```
    if (!res.consistent) {
      force_backtrack();
    }
```

Otherwise, if incorporation of the new constraint has led to a refinement of the abstract
value of `a` or `b`, then the store is updated
accordingly:

```
if (res.newAValue != va) {
  SET_STATE(a, res.newAValue);
}
if (res.newBValue != vb) {
 SET_STATE(b, res.newBValue);
}
```

With these refinements, the `sign3` checker is able to confirm that
<install_dir>/sdk/samples/sign3/test1/sign3.test.c never
converts a negative integer to `unsigned` even though there are three
places that have implicit conversions from `int` to
`unsigned`. A portion of the output is shown next:

```
matched conditional "x >= 0"; "x" = AV_UNKNOWN, "0" = AV_ZERO
  refined "x" to AV_POS_ZERO
matched conditional "y > 0"; "y" = AV_NEG_ZERO, "0" = AV_ZERO
  backtracking due to inconsistency
matched conditional !"y > 0"; "y" = AV_NEG_ZERO, "0" = AV_ZERO
matched conditional "x == z"; "x" = AV_POS_ZERO, "z" = AV_UNKNOWN
  refined "z" to AV_POS_ZERO
matched conditional !"x == z"; "x" = AV_POS_ZERO, "z" = AV_UNKNOWN
matched conditional !"x >= 0"; "x" = AV_UNKNOWN, "0" = AV_ZERO
  refined "x" to AV_NEGATIVE
```
