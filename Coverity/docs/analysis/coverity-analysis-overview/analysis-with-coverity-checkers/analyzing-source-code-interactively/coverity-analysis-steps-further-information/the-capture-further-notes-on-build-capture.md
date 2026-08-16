---
title: "The capture: Further notes on build capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-capture-further-notes-on-build-capture.html"
content_id: "P3YFciYDmuxDyU5Eojurkw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:53.550872+00:00"
---

# The capture: Further notes on build capture

The following table contains further notes about the capture process, organized by language.

Table 1. Build capture notes

| Topic | Notes |
| --- | --- |
| Java code capture (including for Android and web application security analyses) | - For Java, if the Java build capture is used, the build   command should compile all class files. If you plan to   analyze a Java EE, servlet-based application, the build   command should also package the Web Archive (WAR,   .war) file (alternatively, you   can simply specify a directory with the unpacked   contents of the WAR file when you reach the next step in   this procedure). - For Java analyses of Android applications, see Running a security analysis on an Android mobile application. - Example that uses Ant:    ```   > cov-build --dir /foo/xalan_j_2_7_0_analysis ant   ```     This UNIX-based example assumes you have previously changed the directory to a Xalan build directory   that uses the standard Ant build.xml file. - Using the `cov-build` command with Java   requires a supported Sun/Oracle JDK. For information   about supported JDKs, see the   Coverity 2026.6.0 Installation and Upgrade Guide - If you cannot use `cov-build`, see the procedure described in   Running an analysis without 'cov-build'. |
| ASP.NET web application capture | See Capturing an ASP.NET (4.0 or earlier) web application. |
| ASP.NET Core web application capture | See Capturing an ASP.NET Core (2.0 or later) web application. |
| Interpreted code base capture (including JavaScript, Python, PHP, and Ruby files) | For interpreted languages, see "Support matrix" in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI. |
| Non-ASCII code capture | For C and C++ builds, if you are building non-ASCII code, you need to add the `--encoding <character_encoding>` option to the `cov-build` command. |
| Builds on the IBM AIX operating system | AIX installations do not include the `cov-build` or `cov-analysis` commands. To complete the AIX build and analysis tasks, see AIX. |
| Cygwin | If you intend to use Cygwin, see Using Cygwin to invoke 'cov-build'. |
