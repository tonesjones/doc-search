---
title: "Using the Coverity Point and Scan UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-coverity-point-and-scan-ui.html"
content_id: "ytulpCTnNcv7ZtuSttI5SQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:46.834247+00:00"
---

# Using the Coverity Point and Scan UI

This section explains how to use Coverity Point and Scan to launch the
application, scan your code project, and view the results.

## Launch Coverity Point and Scan:

1. Coverity Point and Scan is shipped in the Coverity Analysis
   kit. To launch it, double-click the application icon or the executable file
   (depending on your operating system).
2. Click Get Started.

   A Coverity Connect Instance
   dialog displays.
3. In the dialog, specify the URL for your Coverity Connect instance, and then
   click Next.

   Note: Obtain the
   Coverity Connect URL from the system administrator or as communicated by
   your organization.

   Note: For administrators, if
   scans are run in a Coverity cloud deployment, and if storage service custom
   domains are used within the Coverity cloud deployment, when you create a
   domain, you also need to specify the URL of each domain within the
   `cim.properties` file. For Coverity cloud administrators,
   to create a custom storage service domain, refer to Storage service custom domains.
4. Enter your user name and password, and then click Sign In.

   Note:
   When the target Coverity Connect instance is configured to
   support Single Sign-on (SSO), you can use SSO to sign in.

   For more
   information about Single Sign-on, see "Configuring Coverity Connect to use SAML" in
   the Coverity Platform 2026.6.0 User and Administrator Guide.

## Create a scan and run it:

1. In the upper left-hand corner of the window, click +New Scan.

   A
   Select Source Code dialog displays.
2. You can drag and drop an existing source code project into the dialog, or you can choose the
   directory that contains the source code project you want to scan.

   Once you
   have chosen a project, the New Scan dialog displays.
3. Use the fields in the New Scan dialog as follows:

   Source Code
   :   Displays the name of the source code file you selected in the
       previous step.

   Use build commands to capture source code
   :   Check this box if you are scanning a Java project or a C, C++, C#,
       Objective-C, Objective-C++, or Visual Basic project, you are running
       Point and Scan on a machine in a build environment, and you know
       what the clean and build commands are to clean and build the
       project.

   Configuration File
   :   Choose a configuration file to use for the scan.

       If you don't choose a configuration
       file, Coverity Connect generates a new one
       automatically.

   Project Name
   :   You can choose Scan to New Project  and
       specify the project name, or you can choose Scan to
       Existing Project.

   Stream Name
   :   Specify the name of the stream.
4. Click Begin Scan.

   Coverity Point and Scan creates
   the specified project and stream in Coverity Connect, and
   displays information about the scan as it processes your files. The feedback
   consists of messages from the Command Line Interface (CLI) that is doing the
   work.

## View the results of the scan:

1. When the scan is done, Coverity Point and Scan displays the results in its
   main application page; for example:

   Figure 1. Coverity Point and Scan main application
   window
   [image: Window displaying results of Point and Scan]

   - The colored circle and the colored squares indicate the severity of the
     issues found: High, Medium, Low, or Audit level.
   - The other numbers indicate the number of files captured and the
     percentage of those files that were in the language of interest.
2. In the main application window, click the Files Captured value to see
   a Diagnostics page that shows a graphic representation of the results; for
   example:

   Figure 2. Coverity Point and Scan diagnostics
   [image: Window displaying a graphic representation of the scan results]

   These are the tiles that appear on the Diagnostics page:

   Summary
   :   Summarizes the number of files captured, the number of lines of code
       scanned, the success rate of the scan, and the percentage of the
       language of interest that the scan encountered.

   Files by Status
   :   Summarizes the number of files that were successfully scanned, along
       with the number that were incomplete, failed, or ignored. To see a
       list of the files in one of these categories, click that specific
       box.

   Source Files by Language
   :   Summarizes the number of files in each language encountered. To see
       a list of the files in a particular language, click that specific
       box.

   Files by Path
   :   This is a heatmap that shows the proportion of files in the project,
       according to the top-level directory in which they are located.

       Clicking one of the colored rectangles takes you to a list view
       of that particular directory.

       Note: The map does not show hidden directories.
3. In the main application window, you can click the percentage number
   (<language> Files) to see a detailed list of
   the scan results.

   You can limit the files shown by using the filters at the
   top of the list to filter for Capture Status,
   File Type, or Path.
   File Type displays a tree of files arranged by
   kind (source, configuration, and so on) and language.

In this section:

- Looking at individual issues
- Rescanning and reconfiguring
