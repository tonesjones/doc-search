---
title: "Defining your version of JRE for Signature Scanner"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/defining-your-version-of-jre-for-signature-scanner.html"
content_id: "mtBkoeOoepS7pbv3Hu4njw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:36.727720+00:00"
---

# Defining your version of JRE for Signature Scanner

The Java Runtime Environment (JRE) is included with the download of the Signature Scanner. As a result, you do not need to configure the JRE or
the JAVA_HOME environment variable.

However, there may be situations that require you to use your version of JRE, for example
you have self-signed certificates stored in a preferred version of Java or your company
policy prohibits using the version of the JRE included with Signature Scanner. In these instances, you can set the BDS_JAVA_HOME
environment variable to define the installed version of JRE Signature Scanner should use. The Signature Scanner will
then use this version when scanning components.

Note: If you do not configure BDS_JAVA_HOME, Signature Scanner uses the version
of JRE packaged with the download of the Scanner.

To configure the BDS_JAVA_HOME environment variable on Windows:

1. Access the System Properties dialog box. For example, from the Control Panel,
   click  **System > Advanced System Settings**.
2. Select the **Advanced** tab and click **Environment Variables**.
3. In the Environment Variables dialog box, under **System Variables**, click
   **New**.
4. Enter the following information:

   **Variable name**: BDS_JAVA_HOME

   **Variable value**: `<path to JRE>`
5. Click **OK**.

To configure the BDS_JAVA_HOME environment variable on Linux or Mac OS X:

1. Start a terminal session.
2. At the command line, type

   ```
   export BDS_JAVA_HOME=<path to JRE>
   ```
3. Close the terminal session.
