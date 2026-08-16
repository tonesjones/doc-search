---
title: "Running the Third Party Integration Toolkit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-the-third-party-integration-toolkit.html"
content_id: "bDeTtp5h~v9vDaj0X2YWNQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:26.288039+00:00"
---

# Running the Third Party Integration Toolkit

This section demonstrates the work-flow for running the Third Party Integration Toolkit.
Certain steps refer to the examples (the JSON file and its
referenced source
files), which are provided so you can see the relationship of the files and
how the information in the files is displayed in Coverity Connect. You can copy these
files and use them with `cov-import-results` as a demonstration of the
utility.

**To run the Third Party Integration Toolkit:**

1. Create a JSON file in the format shown in the JSON file
   example.

   There are some notes to consider for this step:

   - In the example, the `"file"` element references a file named
     missing_indent_source.c. This is the source file
     that contained the issue discovered by the checker that is described in the
     JSON file. All filenames must have absolute pathnames, so you will need to
     update the paths that are used in the example to match your directory
     structure.
   - See Import file reference on
     how to integrate multiple source files and their related issue data.
2. Run the `cov-import-results` command to extract the issue data from the JSON
   file. For example:

   `cov-import-results --dir dirEx --cpp doc_example.json` 
   - The command is located in
     <install_dir>/bin.

     Note: If you run
     separate `cov-import-results` commands or run
     `cov-import-results` after
     `cov-analyze`, you must add the --append option
     to add the results to the intermediate directory. Otherwise, the
     `cov-import-results` will replace the contents
     of the intermediate directory with the its results.
   - `--dir` specifies the intermediate directory from where
     you will commit your third party issues.
   - `--cpp` is the domain (language) for the issues. In this
     case, the domain is C/C++. The Third Party Integration Toolkit also
     accepts `--java` (Java), `--cs` (C#), and
     `--other-domain` (another domain/language).

     Note: You
     can only specify one domain at a time for
     `cov-import-results`. If you want to import
     issues from different domains, you must run separate
     `cov-import-results` commands and commit each
     of them (see the next step).
3. Commit the issues to Coverity Connect. For example:

   `cov-commit-defects --dir dirEx
   --host localhost --user admin --port 8008 --stream
   cov_imp_tst`

   If you have imported issues with different specified
   domains you need to run a separate `cov-commit-defects` command
   line for each domain type. The stream you commit to also must match the domain
   type that you specify.
4. Log into Coverity Connect, and navigate to your issues list.

   Figure 1. Coverity Connect with imported third-party issues
   [image: image]

   The image above shows how third-party issues are displayed in Coverity
   Connect. This display image is the result of a commit with the example import
   file using the example missing_indent_source.c source file (both are described in the next
   chapter). The call-outs denote the area of the Coverity Connect UI that displays
   the relevant import file elements. Additionally, the items listed below link to
   a description of the displayed elements:
   1. Issue listing:
      - issues:subcategory
   2. Source code in the Source browser:
      - issues:function
   3. Event information leading to the issue in the source:
      - issues:subcategory
      - issues:checker
      - events:description
      - events:main
   4. Occurrences tab describes event information that
      leads to the issue:
      - events:tag
      - events:file or issues:file
      - events:line

Note: If you have created custom checkers, you can import the issue results found by those
checkers using `cov-import-results`. By importing the results, you can
utilize the checker-based Coverity Connect and Coverity Policy Manager filters (such as,
by Impact rating and Checker name).

For information about creating custom checkers,
see the Coverity Platform 2026.6.0 User and Administrator Guide.

When
`cov-import-results` runs on high-density files (files with
more than 100 issues that also average more than 1 issue for every 10 lines of
code), the console will print a warning that names all the files that exceed the
threshold, and the import process will exclude all issues associated with the
affected files from the intermediate directory. This change prevents the Coverity
Connect source browser from becoming too crowded with issues.

To suppress this
density check (allowing all issues to be
imported) in
version 7.0, define the environment variable
COVERITY_ALLOW_DENSE_ISSUES when running the commands.
