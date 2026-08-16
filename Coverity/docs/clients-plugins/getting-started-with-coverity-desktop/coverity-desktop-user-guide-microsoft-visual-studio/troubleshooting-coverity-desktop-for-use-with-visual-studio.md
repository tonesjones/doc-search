---
title: "Troubleshooting Coverity Desktop for use with Visual Studio"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-coverity-desktop-for-use-with-visual-studio.html"
content_id: "_kYcDwQjqBG6FPcSzvn40Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:51.389508+00:00"
---

# Troubleshooting Coverity Desktop for use with Visual Studio

This troubleshooting section provides instructions for fixing the following common issues
with Coverity Desktop:

1. Coverity Desktop returns an upgrade error when using a new
   MSBuild version on an older version of Visual Studio
2. LDAP users: My Outstanding filter not returning expected
   results in Issues view
3. The "Uncaptured Source Files" dialog appears and
   pressing the " Capture Build and Analyze" button does not
   resolve the problem
4. Unable to open remote issues and filepath displays in red text in the Issues
   view, despite files being present in your solution
5. [ERROR] No snapshot in stream "X" has analysis
   summaries...
6. Connecting over SSL with self signed Coverity Connect
   certificates

## Coverity Desktop returns an upgrade error when using a new MSBuild version on an older version of Visual Studio

These errors may include:

- `error VCBLD0010: project requires upgrade`
- `error MSB4036: "VCBuild" task was not found`

If either of these errors are encountered, try running a different build engine
by navigating to Coverity > Analysis Configurations > Advanced: Build, and selecting a different version of MSBuild from the
Build and Solution build
configuration sections.

## LDAP users: My Outstanding filter not returning expected results in Issues view

Be sure that you have logged into the Coverity Connect server using the
full LDAP username format: user@domain.

## The "Uncaptured Source Files" dialog appears and pressing the " Capture Build and Analyze" button does not resolve the problem

This situation occurs if a file specified for analysis is not among those that Coverity Desktop recognizes as having been compiled during the
build capture. Try the following potential solutions:

Solution 1: Files not meant for analysis
:   In the case that the files in question are never captured because they
    are not actually part of the project (and so not meant for analysis),
    proceed with your analysis by clicking  Analyze Captured
    Files Only.

    It may also be useful to exclude these files from all future analyses. To
    do so, check the box to always ignore the files in question, or navigate
    to Coverity > Analysis Configurations > Advanced: File Exclusions. This will open the File Exclusions window, where you
    can specify any files you want excluded from your local analyses.

Solution 2: Confirm your compiler configurations
:   It is possible that the file you are attempting to analyze uses a compiler that has not yet
    been configured in Coverity Desktop. If this could be
    the case, please run the `cov-configure` utility to
    configure the compilers that are used by your project (see the Coverity 2026.6.0 Command Reference for more information).

    After adding any new compilers, be sure to recapture the build by
    selecting Capture Build from the
    Coverity menu, and try the analysis
    again.

Solution 3: Non-primary source file capture
:   If the file you are attempting to analyze is a non-PSF, such as a header
    file, then it is necessary to use the
    --record-with-source option for the build capture.
    Navigate to Coverity > Analysis Configurations > Advanced: Build and select Use
    --record-with-source.

    After selecting the --record-with-source option, be sure
    to recapture the build by selecting Capture Build
    from the Coverity menu, and try the analysis
    again.

If none of these solutions resolve the issue, contact <https://community.blackduck.com/s/contactsupport>.

## Unable to open remote issues and filepath displays in red text in the Issues view, despite files being present in your solution

This is likely caused by a discrepancy between remote and local file paths. To fix
this, make sure that your file path mappings are configured correctly:

1. Navigate to Coverity > Analysis Configurations > Advanced: File Path Mappings.
2. In the first box, enter the incorrect path prefixes to be stripped (displayed
   in red in the Issues view).

   Note: You can click  See an Example to see an example
   scenario for using File Path Mapping.
3. In the second box, enter the local paths you want to be searched in place of
   the stripped paths.
4. Click  OK to save and exit.

## [ERROR] No snapshot in stream "X" has analysis summaries...

If the SCM analysis option was used, and the codebase has a last updated date before
the reference snapshot was committed to the stream:

1. Update your codebase and push the changes (so your SCM repository will be
   last updated after the snapshot was committed).
2. Re-run SCM analysis again on the newly updated codebase.

## Connecting over SSL with self signed Coverity Connect certificates

If you are working with an instance of Coverity Connect that uses a
self signed certificate, you will need to ensure that the certificate is trusted by
Internet Explorer. To do so, complete the following steps:

1. Open Internet Explorer

   Note: You must run IE as an administrator to complete the following
   steps.
2. Navigate to Coverity Connect, at
   `https://hostname:port.`
3. Select Continue to this website, when prompted.
4. Select the certificate error in the navigation box.
5. Select View Certificate.
6. Click  Install Certificate.

In some configurations, using the  Install Certificate option
may not be sufficient. If you complete these steps and are still unable to securely
connect with the server, complete steps 1-5 above, then follow the process
below.

1. From the Certificate view dialog, select the
   Details tab and click  Copy to
   File.
2. Complete the Certificate Export Wizard to save the
   certificate to a temporary location.
3. Open Microsoft Management Console (MMC) and navigate
   to  File >  Add/Remove Snap-in.
4. Double-click on the Certificates snap-in to launch the
   Certificates snap-in wizard.
5. Select Computer Account and click 
   Next.
6. Select the Local Computer option and click 
   Finish.
7. Click  OK to close the Add or Remove
   Snap-ins dialog.
8. In the explorer pane, navigate to  Certificates (Local Computer) >  Third Party Root Certification Authorities.
9. Right-click on the Certificates folder, and select  All Tasks >  Import....
10. Use the wizard to import the file saved in step 2.
11. Close and re-open Internet Explorer.
12. Navigate to Coverity Connect, at
    `https://hostname:port.`
13. Internet Explorer should no longer raise any security certificate
    warnings.

If the certificate is not correctly signed, the connection will continue to fail.
Ensure with your Coverity Connect administrator that the signature is
properly formatted, with the First and Last name field set to
the hostname or ip address for Coverity Connect.
