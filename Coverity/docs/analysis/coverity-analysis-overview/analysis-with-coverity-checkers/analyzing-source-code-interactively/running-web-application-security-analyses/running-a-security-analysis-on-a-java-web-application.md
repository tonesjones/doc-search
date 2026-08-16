---
title: "Running a security analysis on a Java web application"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-security-analysis-on-a-java-web-application.html"
content_id: "vWxi~sOfflMjkNCcoHNW1w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:03.308162+00:00"
---

# Running a security analysis on a Java web application

You can perform a security analysis on Java Enterprise Edition (Java EE), servlet-based
web applications. The workflow for the Java web application security analysis mostly
follows the typical pattern. The main differences are as follows (see also Emit web application archives or directories (build capture only)):

- If you use Java build capture, you should use `cov-emit-java` to make the
  contents of any WAR or EAR files available for analysis.
  See Emit web application archives or directories (build capture only).
- If the project contains JSP files that are not packaged into a WAR or EAR file, you can use `coverity capture` to emit the JSPs
  (see the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI).
  It is necessary to emit JSP files so that Coverity Analysis can analyze them and report issues on them.
- Unlike Java build capture, `coverity capture` enables the capture of
  JSPs by default, so manually emitting JSPs or archives would be redundant.
- Following capture (build capture or `coverity capture`), Coverity Analysis runs `cov-security-da`
  by default. The `cov-security-da` command extracts additional dataflow and sanitization information from bytecode libraries in the emit,
  to limit the number of false positive defects reported by the XSS checker. You can disable this step by using the --no-security-da option.
- Template Dynamic Analysis can also be run optionally after capture, by using the --run-template-da-on-emit option.
  Template DA extracts additional dataflow information from web pages created using web template languages such as jQuery®
  and React.js™.

Troubleshooting failures to compile or emit JSP files
:   - Failure can occur because the dependencies are not available on the classpath. This issue
      can be resolved by finding the dependencies and adding them to the
      classpath.
    - Failure can occur because the JSP file is not valid and would never compile in any
      reasonable application server. Such JSP files should be fixed, removed,
      or ignored depending on whether they are needed.

      Note that you can
      pre-compile JSP files as part of the build step to ensure that the
      JSP files will compile and that the classpath is specified
      appropriately.
    - Failure to emit can occur because the JSP file is a fragment and is only meant to be
      included as part of another JSP. Coverity Analysis attempts to identify
      such JSPs and log the files it is unable to emit.
    - If you encounter another sort of issue related to compiling or emitting JSP files, open a
      support case here:
      <https://community.blackduck.com/s/contactsupport>.

Troubleshooting web application security analyses for Java: Using COVERITY_DA_BLACKLIST to prevent certain fatal JRE errors
:   When web application security checkers analyze Java code,
    `cov-analyze` runs a sanitizer fuzzer to execute string
    manipulation code in your application. The sanitizer fuzzer runs in a JRE. If
    the JRE crashes at the analysis step called `Running dynamic analysis for
    Java Webapp Security`, followed by messages such as `A fatal
    error has been detected by the Java Runtime Environment` or
    `[WARNING] Failure in security DA`, you can set the
    COVERITY_DA_BLACKLIST environment variable to prevent the Coverity Analysis from
    executing the string manipulation code in your application that caused the
    problem.

    The value of this variable should be a comma-separated list of
    prefixes, which you set to prevent the direct loading of classes that start
    with any of those prefixes. For example, you might set the
    following:

    ```
    COVERITY_DA_BLACKLIST=com.acme.util,com.acme.text.util
    ```
