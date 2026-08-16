---
title: "Emit web application archives or directories (build capture only)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/emit-web-application-archives-or-directories-build-capture-only-.html"
content_id: "CJYb15lAQ_QBPjlSWMBIeg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:03.950699+00:00"
---

# Emit web application archives or directories (build capture only)

Before analyzing a Java EE servlet-based web application emitted using build capture, it is first necessary
to emit any non-source files, such as JavaServer Pages (JSPs) or those in a
packaged web application archive. This is in addition to any compiled Java
source that might have been captured already. Additional defects can be reported
based on these files.

Note:
Unlike build capture, `coverity capture` for Java enables the capture of JSPs (by default), therefore it would be redundant to
manually emit any JSPs or archives. See the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

Packaged and deployable Java web applications might take the form of WAR or EAR archive files, directories
containing a WEB-INF/web.xml file (equivalent to an
unpacked WAR file), or directories containing a META-INF/application.xml file (equivalent to an
unpacked EAR file).

If the build does not generate any WAR or EAR file but the project does contain JavaServer Pages (JSPs), these can also be emitted
using `coverity capture`. See the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

1. **[Recommended]** Prior to emitting the JSP files, you can pre-compile
   JSP files to ensure that the JSP files will compile and that the classpath
   is specified appropriately.
2. If the previous step is successful, emit the JSPs in preparation for the analysis.

   To capture a single web application archive, use the following command:

   ```
   > cov-emit-java --dir <intermediate_directory> \ 
     --webapp-archive path/to/archive_file_or_dir
   ```

   For details about this command line, see the
   `--webapp-archive` option documentation
   in the Coverity 2026.6.0 Command Reference.

   Important:
   You need to emit the JSP files so that the analysis can find and report issues it finds in them.
   If these files are not present in the WAR file, false negatives will occur, particularly in XSS defect reports.

   It is also important to emit the original JSP source, even in cases where the build normally
   pre-compiles the JSP files into classes and packages those into the WAR file.

   The web application archive or directory should not contain obfuscated classes.

   To emit multiple WAR or EAR files, you can run `cov-emit-java` multiple times,
   use multiple instances of the `--webapp-archive` command option,
   or use one of the following command options: `--findwars`,
   `--findwars-unpacked`, `--findears`, or `--findears-unpacked`.

If you run into issues at this stage, see the JSP-related troubleshooting information in
Running a security analysis on a Java web application.
