---
title: "Variable substitution"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variable-substitution.html"
content_id: "Z3Dkmd3oHxt9Kz9nO5wYyg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:22.315423+00:00"
---

# Variable substitution

In the JSON file, variables are substituted with values from two sources:

- Coverity Connect fields
- Optional `"variables"` section in the JSON file

For example, the following expression is replaced with values from both a Coverity
Connect field and the `"variables"` section.

`"component": "<configMap[component]|defaultComp>"`

Given the following `"variables"` section, this expression will resolve as
follows:

1. The Coverity Connect field `component` is used for the map lookup,
   and succeeds if it matches `"CC_Other"`. Then the result is
   `"Other"`
2. Otherwise, the value for `"defaultComp"` is substituted, which is
   `"Cov Test Component"`.

```
     "variables" : {
       "defaultComp" : "Cov Test Component",
       "configMap" : {
       "CC_Other" : "Other"
           }
```

The following rules apply to variable substitution:

1. Use "<foo>" syntax to mean the substitution of the value of input variable
   foo.
2. Use the set of defect fields listed in "JSON file to import" above as inputs. For
   example, "<fixtarget>" is replaced by the parser with the contents of the
   defect's fixtarget field.
3. Use a map of user-defined variables defined in the JSON as inputs, using the same
   syntax as the previous requirement. For example, if the variables include "foo"
   : "bar", then the syntax "<foo>" indicates that the string "bar" (without
   the quotes) should be substituted.
4. Variable names must be taken from [a-zA-Z0-9]. The parser will verify
   this.
5. Since the defect field names and the variable names are drawn from the same
   namespace, they must not collide. The parser implementation will require and
   verify this.
6. Use the syntax "<foo[bar]>" to mean that:
   - The value of "bar" and "foo" will be looked up in the input
     space.
   - The value of "foo" will be used as a map and a lookup performed using
     the value of "bar".
   - Both "foo" and "bar" must exist in the input space. The value of
     "foo" must be a map. The map must contain an entry for
     "bar".
7. Use the syntax "<foo[bar]|baz>" to mean the same as "foo[bar]" except that
   if the map lookup fails, the value of "baz" from the input space (which must be
   present, whether or not the lookup succeeds) is substituted.
8. In addition to any number of substitutions, value strings may include any number
   of characters expressible in JSON. To express the "<" character, "<<"
   is used.
