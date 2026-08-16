---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "KA2QDU1YoU9XllIT5Y8OJw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:23.762304+00:00"
---

# Description

The `cov-security-da` command runs a dynamic analysis of Java and .NET bytecode
and a separate dynamic analysis of JavaScript templates. The Java/.NET analysis invokes
certain string-manipulation functions to detect whether they correctly escape or
sanitize unsafe values. The JavaScript template analysis dynamically renders observed
template files to detect interpolation sites that could be vulnerable to XSS.

Note: Coverity Security Dynamic Analysis for C# and Visual Basic
requires requires a Windows 64-bit or Linux 64-bit system that supports .NET 6.

The output of
the bytecode analysis primarily affects the XSS checker for Java, C#, and Visual Basic,
and the output of the template-DA analysis primarily affects the XSS checker for
Javascript.

By default, `cov-build` invokes `cov-security-da` as a final
step. This command needs to be invoked manually in the following situations:

- When `cov-build`, `coverity capture`, or `coverity
  scan` was invoked using the -no-security-da option
- After invoking `cov-emit-java`—for example, to capture a Web
  application archive (WAR) file
- When the intermediate directory has been manually modified

Because the Java/.NET dynamic analysis requires compiled bytecode, it cannot be used with a
Java file system capture. Similarily, the JavaScript template analysis will not be
invoked if a suitable JavaScript project can't be identified.
