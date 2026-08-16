---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "UvY8wlpBkAq4w3ybA7fJRg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:36.762810+00:00"
---

# Description

Sometimes the same file is compiled several times with different command-line options. To
avoid errors in function-call resolution (especially in C code, which does not have name
mangling), you can use the `cov-link` command to create a new
intermediate directory that contains a subset of the files that are in your original
intermediate directory. This new intermediate directory can then be analyzed without
function-call resolution issues.

The input consists of an intermediate directory (with an emit repository), plus a set of
translation units. The translation units are either collected dynamically from the emit
repository with the `--collect` option, or they are specified inside one
or more of the link files that were previously created with
`cov-link`.

Typically, `cov-link` is first called with the `--collect`
option to produce a link file. You can look at this file for clues on which filters to
apply to generate an intermediate directory with just the subset of files that you are
interested in. Once you have an idea of which filters you need to apply, you can call
`cov-link` again with your filters to produce a new intermediate
directory. This new intermediate directory can then be analyzed.

**To use the `cov-link` command:**

1. Run `cov-link` with the `--collect` and
   `--output-file` options. This operation collects linkage
   information on all files compiled in an emit directory.
2. Create one or more additional link files by filtering information using either an
   argument or a portion of the pathname that was used during command-line
   compilation. Compiled files are identified based on:

   - A portion of the pathname to the file when it was compiled. Use the
     `--source-file-regex` option to specify a Perl
     regular expression to use when looking at the pathname.
   - The options given on the command line when it was compiled. Use the
     `--compile-arg`,
     `--compile-arg-regex`, `--no-compile-arg`,
     and `--no-compile-arg-regex` options to group by
     command-line options.
3. Use the link files created in the previous steps, and the emit repository in the
   original intermediate directory, to create a new intermediate directory with an
   emit repository with resolved function calls.
4. Use `cov-analyze` on the new intermediate directory.

For more information, including detailed examples, see the Coverity Analysis 2026.6.0 User and Administrator Guide. Detailed examples can also be found in
Coverity Analysis > Coverity Analysis Usage > Analysis with
Coverity Checkers > Setting up Coverity Analysis for a production environment >
Integrating Coverity Analysis into a build system > Integrating Coverity Analysis into the build environment
> Getting linkage information
