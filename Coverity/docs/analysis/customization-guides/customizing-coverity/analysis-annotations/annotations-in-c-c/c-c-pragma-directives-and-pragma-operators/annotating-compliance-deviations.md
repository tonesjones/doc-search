---
title: "Annotating compliance deviations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/annotating-compliance-deviations.html"
content_id: "3LvElC5IZJIMlIuuxvZruQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:22.627183+00:00"
---

# Annotating compliance deviations

You can use the `#pragma` directive or the `_Pragma()`
operator to mark locations in source code that deviate from a compliance
standard.

- The `#pragma` directive is supported by the C90 and later
  language standards.

  The syntax for this directive is `#pragma coverity compliance <directives>`.
- The `_Pragma()` operator is supported by C99, C++11, and later
  standards.

  The syntax for this operator is `_Pragma( "coverity compliance <directives>" )`.

  This operator allows suppression annotations to be included in macro definitions.
  (Hence, C90 or C++03-only target compilers might not be compatible with the
  operator.) Native compilers compliant to these standards will ignore
  `#pragma coverity` directives and native code compilation
  will not be affected.

1. In your source code, add the `#pragma` directive or the
   `_Pragma()` operator to note locations where code practice
   deviates from the standard.
2. Run `cov-analyze` with the
   `--ignore-deviated-findings` option.

   Any deviations or false positives annotated using the a pragma will be
   suppressed and will not be reported by Coverity Connect. You
   can apply this annotation to any Coverity checker by checker name. Your
   organization should provide guidance for the use of this kind of annotation
   with a given compliance standard.

   After you analyze source that contain compliance deviation annotations, the
   Coverity output directory will contain two files related to compliance
   deviations:

   - The annotations output file deviations.txt is a
     CSV-formatted list of the annotated defects.
   - The log file deviations-warnings.txt contains
     warnings on mismatched counts and unused deviations.

   **Example:**
   The following code shows an example of a deviation pragma:

   ```
   void fwdNullDeviation() {
       sint32_t *p = 0;
   #pragma coverity compliance deviate "FORWARD_NULL" "Intentional null deref"
       *p = 0;
   }
   ```

   In Coverity Connect reports, a deviation pragma, like a `//coverity` annotation,
   implies an "intentional" classification for the detected issue, and `false_positive` deviations
   imply a "false positive" classification.
