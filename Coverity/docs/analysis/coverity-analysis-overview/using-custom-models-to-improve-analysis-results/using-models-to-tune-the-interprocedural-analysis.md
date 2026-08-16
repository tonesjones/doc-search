---
title: "Using models to tune the interprocedural analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-models-to-tune-the-interprocedural-analysis.html"
content_id: "S2OpJ8z~gP3_HziJEh0jHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:58.128070+00:00"
---

# Using models to tune the interprocedural analysis

For its cross-procedure source code analysis, Coverity Analysis infers a model of each
function, whether from the actual source code or from a handwritten model. The engine
automatically detects those cases where a constant is returned, a variable holding a
constant is returned, or a comparison between the return code and a constant indicates
the return value.

If the contextual behavior involves operations that are more complex than assignments to
constants, comparisons with constants, and simple arithmetic, Coverity Analysis might
not correctly infer the abstract behavior of the function or method without additional
assistance. In such a case, it is necessary to create models that provide directions to
Coverity Analysis.

**Examples: C/C++ interprocedural contexts detected by the Coverity Analysis analysis**

- In the following example, Coverity Analysis automatically infers that this
  function returns 0 when memory is not allocated.

  ```
  // Basic return value dependence:
  void* malloc(size_t sz)
  {
      void* allocated_ptr;
      if (<detect out of memory condition>) {
          return 0;
      }
      allocated_ptr = <get pointer from Operating System>;
      return allocated_ptr;
  }
  ```
- In the following function, ptr is only dereferenced when
  flag is equal to `9`. In general,
  whenever Coverity Analysis sees a constant directly or can, through assignments
  or comparisons, determine that a variable is compared against a constant, it
  will note the constant and the comparison type (equal to, not equal to, less
  than, or greater than) in the function's behavioral model.

  ```
  // Basic argument dependency
  void dereference_pointer(int* ptr, int flag)
  {
      if (flag == 9)
          *ptr = 9;
          return;
  }
  ```

Coverity Analysis does not track context based on the value of global or static,
file-scope variables. It makes very conservative assumptions about when those variables
can be modified, rendering their analysis relatively ineffective. If the behavior of a
function contextually depends on a global variable's value, it is best to conservatively
model that function. For example, if you're modeling a deallocation function, then make
that function always deallocate the supplied pointer regardless of the global variable's
value. This eliminates the numerous false positives that function may produce. While it
will also eliminate bugs due to incorrect usage of that function, the tradeoff between
bugs and false positives favors the conservative solution.

Note: To avoid unexpected results, do not move derived model files from one platform to
another.
