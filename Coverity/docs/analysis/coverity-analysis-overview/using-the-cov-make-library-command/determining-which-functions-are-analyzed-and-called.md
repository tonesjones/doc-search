---
title: "Determining which functions are analyzed and called"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/determining-which-functions-are-analyzed-and-called.html"
content_id: "FEQtEm5y6OqFEEtn_1QxrA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:19.471836+00:00"
---

# Determining which functions are analyzed and called

Knowing which functions are unimplemented is useful for determining which functions to
model. The
<intermediate_directory>/output/callgraph-metrics.[csv|txt]
files list which functions are implemented and unimplemented, and how many callers each
function has. These file are generated when you add the
`--enable-callgraph-metrics` option to the
`cov-analyze` command.

Coverity Analysis uses the build process to model and analyze functions,
in one of the two following ways:

- If the build process captures a function’s definition, the function is treated as
  though it is implemented, and Coverity Analysis analyzes the
  function to build a model for it.
- Otherwise, the function is treated as though it is unimplemented, and does not have
  an explicit model (as specified by the `--model-file` option). In
  this case, Coverity Analysis makes assumptions about the function
  in a way that avoids reporting false positives in callers—unless Coverity Analysis has been configured not to do so; for example, by
  using the option `-co RESOURCE_LEAK:allow_unimpl`.

Coverity Analysis provides a model library of common unimplemented
functions such as `malloc()`.

Coverity Analysis also tracks how many times functions, both implemented
and unimplemented, are called. This number is the total number of callers that call a
function, both directly and indirectly (through one or more other functions). The number
of callers for an unimplemented function is useful for determining which functions are a
high priority to model. Looking at the number of callers of implemented functions can be
useful as well for understanding the code base’s architecture.

**To find out which functions are analyzed and called:**

1. When you run the `cov-analyze` command, add the
   `--enable-callgraph-metrics` option.

   Note: The option
   `--enable-callgraph-metrics` has been deprecated for Kotlin,
   Go, Python, and JavaScript/TypeScript. The option is still supported for C/C++,
   C#, and Java.
2. When the analysis completes, open the file
   <intermediate_directory>/output/callgraph-metrics.csv.
   This file lists each function as implemented or unimplemented. The number next to
   each function is the total number of direct and indirect callers for that
   function.
3. To see which functions might be good candidates for modeling, look for unimplemented
   functions that have a high number of callers.

The following table describes columns in the file that can help you determine which
functions are analyzed and called.

Table 1. Important Data in Callgraph Metrics Files (CSV format)

| CSV Column | Details |
| --- | --- |
| call_count | Estimated number of calls to the function. (See `unmangled_name` for the name of the function.) Note: The `call_count` estimates the total number of calls to the function. This value counts both direct and indirect calls (including recursive (R) calls). The Calls value displayed by Coverity Connect counts only the number of direct (syntactic) calls to the function. Because of this, these two values can differ. |
| TU | Indicates whether the function has been implemented. TU = -1  Function is not implemented.  TU ≠ -1  Function is implemented. For additional detail about the values, you can run the following command:  ``` cov-manage-emit --dir <dir> -tu N list ``` |
| qualifiers | C  Compiler-generated function  V  Virtual function  R  Recursive function  T  Templated function |
| cycle_id | Important for recursive (R) functions. |
| module | Helps identify the source of the model information. |
| model_type | Indicates whether a model for the function was found and whether it is a built-in or user-created model.  No_Model  The function is not modeled.  User_Model  The function was modeled by a user.  Builtin_Model  The function was modeled by Coverity developers.  Collected_Model  The function model was specified through`--derived-model-file`. |
| model_file | Provides the path to a model file if the function is modeled.  - For unmodeled function (where `model_type` is   `No_Model`): None - For function modeled by a user (where   `model_type` is `User_Model`):   Filepath to model.xmldb - For a built-in model (where `model_type` is   `Builtin_Model`): Filepath to   builtin-models.db |
