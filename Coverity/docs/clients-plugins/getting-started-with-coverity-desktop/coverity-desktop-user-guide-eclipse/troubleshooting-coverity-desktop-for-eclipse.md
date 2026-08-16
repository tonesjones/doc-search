---
title: "Troubleshooting Coverity Desktop for Eclipse"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-coverity-desktop-for-eclipse.html"
content_id: "T2B8fHVYNzJuot7ZIq0OaQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:20.205653+00:00"
---

# Troubleshooting Coverity Desktop for Eclipse

This troubleshooting section provides instructions for fixing the following common issues
with Coverity Desktop:

1. Coverity Desktop plug-in not displayed in the IDE
   after installation, despite appearing in the list of installed plug-ins
2. Coverity Desktop cannot connect to Coverity Connect using domain names
3. Local analysis causing
   PermGen memory issues
4. Eclipse crashes
   when opening context help
5. When
   inspecting and triaging issues, the Eclipse plug-in sometimes opens a
   file with a `coverity_external_files` prefix
6. Clicking the CWE
   link in the Details view does not open the correct URL
   on Linux platforms
7. The
   `cov-emit-java` tool is not being invoked during
   analysis when using a non-standard builder configuration (Ant Builder,
   custom made builder, etc)
8. Expected
   Java source code files are not appearing in the list of translation
   units returned by the `cov-manage-emit` tool
9. Analysis
   returns the error message "`Cannot find any compiler outputs for
   Java files`" when using a non-standard builder configuration
   (Ant Builder, custom made builder, etc)
10. LDAP users:
    My Outstanding filter not returning expected
    results in Issues view
11. Analyze Entire Workspace command attempts to
    analyze files that aren't part of the build, causing errors
12. The "
    Uncaptured Source Files" dialog appears and
    pressing the "Capture Build and Analyze" button
    does not resolve the problem
13. Unable to open remote
    issues and filepath displays in red text in the Issues view, despite
    files being present in your workspace
14. [ERROR]
    No snapshot in stream "streamName" has analysis
    summaries...

## Coverity Desktop plug-in not displayed in the IDE after installation, despite appearing in the list of installed plug-ins

The Coverity Desktop plug-in requires Java 1.8+ to run. (Note that
you must install the 32-bit Java version if you use a 32-bit IDE. This applies to
both WindRiver 3.2 and QNX 4.7 32-bit only). To fix this issue, install Java 1.8 or
later, and update your IDE executable to launch with the correct Java version:

For Eclipse and QNX:
:   1. Navigate to the IDE's install directory.
    2. Locate the executable file that is used to launch the IDE (
       eclipse.exe for example). There
       should be an associated .ini file with
       the same name (for example, eclipse.ini
       ).

       If the .ini file does not exist, create
       it.
    3. Open the .ini file and look for the
       argument, `-vm` . If present, add the path to
       the new Java executable directly below the
       `-vm` line. Otherwise, add
       `-vm` to the file, with the path to the
       new Java executable on the following line.

       Note: Make sure that:
       - The `-vm` and the path are on
         separate lines.
       - The path points directly to the Java executable -
         not just the Java home directory.
       - If `-vmargs` is present in the
         file, the `-vm` argument and path
         must come before it.
    4. Run the IDE's executable file. You should be able to see the
       Coverity features now.

For WindRiver
:   To launch WindRiver with the appropriate Java version, launch the IDE
    from the command line, using the `-vm`  argument:

    From the command line, enter the IDE's executable file name, followed
    by " `-vm
    path_to_java_executable`".

## Coverity Desktop cannot connect to Coverity Connect using domain names

1. Try to turn off your firewall.
2. If you use proxy settings, try to include all necessary domain names into
   your proxy exceptions.

## Local analysis causing PermGen memory issues

Note: The Permanent Generation space is removed in Java 1.8. The JVM will ignore the
options `-XX:PermSize` and `-XX:MaxPermSize` .

On Eclipse, running local analysis using the default memory settings might cause
PermGen memory issues. To increase the default PermGen space, add the following
arguments to the command line:

```
       -XX:PermSize=64M -XX:MaxPermSize=384M
```

For example:

```
       % eclipse -vmargs -XX:PermSize=64M -XX:MaxPermSize=384M
```

The memory size needed depends on your system, so suggested settings to try are:
256M, 384M, or 512M. For more information about PermGen settings, see the Eclipse
documentation at [http://wiki.eclipse.org/FAQ_How_do_I_increase_the_permgen_size_available_to_Eclipse%3F.](http://wiki.eclipse.org/FAQ_How_do_I_increase_the_permgen_size_available_to_Eclipse%3F)

## Eclipse crashes when opening context help

Upgrade to the most recent Java Runtime Environment.

For additional information, please refer to Eclipse Bug 353740. <https://bugs.eclipse.org/bugs/show_bug.cgi?xml:id=353740>

## When inspecting and triaging issues, the Eclipse plug-in sometimes opens a file with a `coverity_external_files` prefix

This occurs because the Eclipse plug-in can not locate the file inside the workspace,
so it creates a hidden project called `coverity_external_files` to
load the file and show markers as if it were part of the workspace. Sometimes the
file is not found because of links in a project that cause the source file and the
project to have different path prefixes.

If the file that was opened inside the `coverity_external_files` path
is located in the current workspace, then the plug-in needs additional information
to locate that file. To resolve this situation, complete the following steps:

1. Navigate to Preferences > Coverity Analysis > Central Analysis .
2. Ensure that the View and triage issues from Coverity
   Connect check box is selected.
3. Click the Issue Location... button.
4. Add the strip path to your local source files in the  Strip
   remote path prefixes dialog.

After closing the preferences dialog and refreshing the Issues view, opening
an issue should open the proper file that is found in the workspace as expected.

## Clicking the CWE link in the Details view does not open the correct URL on Linux platforms

If the CWE link does not open to the correct location, right-click the link and copy the URL.
Then paste the URL into your web browser.

## Non-standard builder errors

This is a common issue with non-standard builder configurations, which can manifest
in one of three ways:

- *The `cov-emit-java` tool is not being invoked during
  analysis when using a non-standard builder configuration (Ant Builder,
  custom made builder, etc)*
- *Expected Java source code files are not appearing in the list of
  translation units returned by the `cov-manage-emit` tool*
- *Analysis returns the error message "`Cannot find any compiler
  outputs for Java files`" when using a non-standard builder
  configuration (Ant Builder, custom made builder, etc)*

This is likely caused by your .class files being written to an
unexpected location that the Eclipse plug-in can not find. To fix this issue, ensure
that the output folders are configured correctly for each source folder by
completing the following steps:

1. Right-click on the project in the Project Explorer 
   and select Properties .
2. Open the Java Build Path page.
3. Check the Allow output folders for source folders 
   checkbox.
4. Expand each source folder entry in the Source folders on build
   path pane.
5. For each Output folder, select it and click
   Edit...

   1. Choose the Specific output folder option.
   2. Enter the path of the output folder relative to the source
      folder.
6. Create a new Analysis Configuration for the project (the changes may go
   undetected if you reuse an existing Analysis Configuration).
7. Run the new Analysis Configuration.

[image: image]

## LDAP users: My Outstanding filter not returning expected results in Issues view

Be sure that you have logged into the Coverity Connect server using the
full LDAP username format: user@domain.

## Analyze Entire Workspace command attempts to analyze files that aren't part of the build, causing errors

For any files in your workspace that should be excluded by Desktop Analysis, a
resource filter should be added:

1. Right-click on the project that contains the extra files in the
   Project Explorer tab.
2. Click on Properties .
3. Expand the Resource menu, and select
   Resource Filters .
4. Click Add... to create a new filter, excluding any
   files or directories from inclusion in the project.
5. Apply your changes to finish adding the filter.

## The "Uncaptured Source Files" dialog appears and pressing the "Capture Build and Analyze" button does not resolve the problem

This situation occurs if a file specified for analysis is not among those that Coverity Desktop recognizes as having been compiled during the
build capture.

For C/C++, try the following potential solutions:

Solution 1: Files not meant for analysis
:   In the case that the files in question are never captured because they
    are not actually part of the project (and so not meant for analysis),
    proceed with your analysis by clicking Analyze Captured Files
    Only .

    It may also be useful to exclude these files from all future analyses. To
    do so, check the box to always ignore the files in question, or navigate
    to Coverity > Configuration > Coverity Analysis > Local > Analysis and click on the File Exclusions
    button. This will launch the Local Analysis File
    Exclusions dialog, where you can specify any files you
    want excluded from your local analyses.

Solution 2: Confirm your compiler configurations
:   It is possible that the file you are attempting to analyze uses a
    compiler that has not yet been configured in Coverity Desktop. Navigate to Coverity > Configuration > Coverity Analysis > Local > Compiler Configuration and confirm that all of the compilers used by your
    project are configured for use.

    After adding any new compilers, be sure to recapture the build by
    selecting Capture Build of Entire Workspace  from
    the Coverity menu, and try the analysis
    again.

Solution 3: Non-primary source file capture
:   If the file you are attempting to analyze is a non-PSF, such as a header
    file, then it is necessary to use the
    `--record-with-source` option for the build capture.
    Navigate to Coverity > Configuration > Coverity Analysis > Local > Build and select Use --record-with-source
    .

    After selecting the --record-with-source option, be sure to
    recapture the build by selecting Capture Build of Entire
    Workspace from the Coverity menu,
    and try the analysis again.

This problem is usually very rare when analyzing Java source code, but if it does
occur, please try the following solution:

Solution 1: Files not meant for analysis
:   In the case that the files in question are never captured because
    they are not actually part of the project (and so not meant for
    analysis), proceed with your analysis by clicking Analyze
    Captured Files Only.

Solution 2: When using a custom Java build command, ensure the working directory is correct
:   If you have:

    - Imported Java source code from some original location
      into a project in your workspace
    - Elected to copy the files into the workspace rather than
      establishing links in the workspace to the original
      location
    - Supplied a custom Java build command

    Then ensure that the working directory under Coverity > Configuration > Coverity Analysis > Local > Build matches the location of the project directory within
    the workspace. If the working directory refers to the original
    location rather than the location within the workspace, then
    although the build may succeed, the wrong set of files will be
    compiled and the plug-in will continue to complain that the expected
    files were not build-captured.

If none of these solutions resolve the issue, contact <https://community.blackduck.com/s/contactsupport>.

## Unable to open remote issues and filepath displays in red text in the Issues view, despite files being present in your workspace

This is likely caused by a discrepancy between remote and local file paths. To fix
this, make sure that your file path mappings are configured correctly:

1. Navigate to Coverity > Analysis Configurations > Advanced > File Path Mapping.
2. In the first box, enter the incorrect path prefixes to be stripped (displayed
   in red in the Issues view).

   Note: You can click See an Example to see an example
   scenario for using File Path Mapping.
3. In the second box, enter the local paths you want to be searched in place of
   the stripped paths.
4. Click OK to save and exit.

## [ERROR] No snapshot in stream "streamName" has analysis summaries...

If the SCM analysis option was used, and the codebase has a last updated date before
the reference snapshot was committed to the stream:

1. Update your codebase and push the changes (so your SCM repository will be
   last updated after the snapshot was committed).
2. Re-run SCM analysis again on the newly updated codebase.

If you are attempting to analyze your program without using snapshot summaries, and
your stream does not contain snapshots with analysis summaries, the build command
will fail with this message. To work around this issue, please select the 'Go
Offline' menu item and retry.

Please note, if you encountered this issue while running Analyze with
Configuration and use the suggested workaround, the analysis will
also be run in a disconnected state. If you do not want this, use Capture
Build while offline, then select the 'Go Online' menu item (to start
working online) before retrying the Analyze with
Configuration command.
