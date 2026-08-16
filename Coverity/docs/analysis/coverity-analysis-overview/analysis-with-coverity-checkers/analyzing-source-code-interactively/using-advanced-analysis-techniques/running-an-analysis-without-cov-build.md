---
title: "Running an analysis without 'cov-build'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-an-analysis-without-cov-build-.html"
content_id: "IBfRcqQg5~iuj5CL6OMbSg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:18.171264+00:00"
---

# Running an analysis without 'cov-build'

Sometimes it is difficult or impossible to build a complete code project. In this case,
you can still analyze source code: As an alternative to using the
`cov-build` command, you can first compile your source in debug
mode, using the standard compiler for the language in question (for example,
`javac` or `vbc`). After you compile, use the
language-specific version of `cov-emit` (for example,
`cov-emit-java` or `cov-emit-vb`) to parse the
source. Finally, run `cov-analyze` to complete the analysis.

1. Compile your code base using debug information.

   Building in debug
   mode (for example, with the `-g` option to
   `javac`, or with the `debug="true"` Ant
   compile task) allows Coverity Analysis to analyze the compiled code. In the
   standard analysis flow (see Steps to generate an analysis), the
   `cov-build` command automatically runs the compiler in
   debug mode.
2. For each time you invoke the compiler, run the appropriate version of
   `emit` as well, using the `--compiler-outputs`
   option. This captures a build of your source code to the intermediate
   directory.

   Important: You must run the `emit`
   command on the same source and class files (those class files specified in the
   classpath) on which you ran the compiler. The
   `--compiler-outputs` must point either to all of the possible
   parent directories of the compiler outputs, or to a common parent directory for
   all of the compiler outputs.

   For
   example:

   ```
   > cov-emit-java --findsource src \
     --findjars lib;build-lib/ --dir my/intermediate/dir \ 
     --compiler-outputs build/classes/;build/junitclasses/
   ```

   Note: On
   Windows systems, the semicolons ( `;` ) shown in the example
   serve as path separators. On Unix-style platforms (including macOS and Linux),
   the path separators should be colons ( `:` ).

   For more
   detailed information about this command, see the
   `cov-emit-java`
   description in the Coverity 2026.6.0 Command Reference.
3. Run `cov-analyze`.

   For guidance, see The analysis.
4. Commit the defect data to the Coverity Connect database.

   For guidance, see The commit.
