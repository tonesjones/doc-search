---
title: "Getting linkage information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/getting-linkage-information.html"
content_id: "Au~4KCI4kiJTCZEssH5rvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:04.899753+00:00"
---

# Getting linkage information

For C and C++ source code, the same file is sometimes compiled several times with different
command-line options. Due to the inherent difficulty of tracking linkage information,
the `cov-analyze` command cannot automatically determine which files are
linked together. To avoid errors in function call resolution (especially in C code,
which does not have any name mangling), you can use the `--tu-pattern` or `cov-link`
to indicate which files should be analyzed togther.

The following two examples cover common uses of this feature. For a complete list of
command-line options and additional examples, see the `cov-link` documentation in the Coverity 2026.6.0 Command Reference.

**Example 1**

Assume that you have a single project productA with two target
architectures, ARM and MIPS. Each function is compiled twice, possibly using different
semantics. For example, arrays do not have the same size, and you have OVERRUN false
positives. Assume that the target architecture is specified to the compiler by
`-march=<arch>`. Use the following steps to resolve the
duplicate function calls:

1. Run the build:

   ```
   > cov-build --dir productA_dir
   ```
2. Run separate analysis for the 2 architectures:

   ```
   > cov-analyze -dir productA_dir --tu-pattern "arg(\"-march=arm\")"
   > cov-commit-defects --dir productA_dir --target "ARM target" --stream productA-ARM 
   > cov-analyze -dir productA_dir --tu-pattern "arg(\"-march=mips\")"
   > cov-commit-defects --dir productA_dir --target "MIPS target" --stream productA-MIPS
   ```

   This
   creates two separate snapshots with target attributes named ARM target and MIPS
   target. You can run the commands to analyze and commit the arm-emit and
   mips-emit data concurrently, if you specify a different output tag for each. To
   do this, use the `--output-tag` option to
   `cov-analyze` and `cov-commit-defects` (but
   note that incremental analysis caching is specific to a given output tag, so if
   not running concurrently it’s preferable not to use one)

**Example 2**

In this example, assume that you have two projects named proj1 and
proj2 that share the library lib. The two
projects define the same functions with different semantics, so you need linkage
information. Assuming that the source files are located in directories named
proj1, proj2, and
lib, use the following steps to resolve the duplicate function
calls:

1. Run the build:

   ```
   > cov-build --dir proj1_proj2
   ```
2. Run the analysis and commit the defects for proj1 and proj2, each analyzed separately but
   together with the shared library, by using project-specific command lines. Here
   we’ll use output tags that allow running concurrently:

   ```
   > cov-analyze --dir proj1_proj2 --tu-pattern "(file(\"/lib/\") || file(\"/proj1/\"))" \
       --output-tag proj1
   > cov-commit-defects --dir proj1_proj2 --output-tag proj1 --description "proj1" \
       --stream proj1 
   > cov-analyze --dir proj1_proj2 --tu-pattern "(file(\"/lib/\") || file(\"/proj2/\"))" \
       --output-tag proj2
   > cov-commit-defects --dir proj1_proj2 --output-tag proj2 --description "proj2" \
       --stream proj2
   ```
