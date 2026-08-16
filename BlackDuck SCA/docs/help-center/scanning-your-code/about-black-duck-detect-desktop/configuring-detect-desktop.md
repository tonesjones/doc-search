---
title: "Configuring Detect Desktop"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-detect-desktop.html"
content_id: "1s2uYEfVJIEpPRt2WwGXSw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:28.644524+00:00"
---

# Configuring Detect Desktop

After installing Black Duck Detect Desktop, continue the installation process
by configuring your Black Duck settings.

1. Click [image: Settings icon] .
2. As described below, select one of the following tabs and complete the
   installation and configuration process:

   - Server Configuration
   - Proxy Server
   - Black Duck
     Detect
   - Updates

## Black Duck server configuration

To add a server:

1. Select the **Server Configuration** tab and click **Add
   Server**.
2. Specify the Black Duck Server URL. Enter the
   URL to the Black Duck server as you would type it in
   the browser, for example https://servername:8443/

   If required, enter context information, for example, if the
   X-Forwarded-Prefix header is being specified in a proxy server/load
   balancer configuration.
3. Enter your API key (user access
   token).
4. Click **Submit**.

Black Duck Detect Desktop connects to the Black Duck
server and displays the version of Black Duck you are connected
to.

To remove an API key or configuration:

1. Select the **Server Configuration** tab.
2. Click [image: File options icon] in the row of the server and select:

   - **Remove API Token** to remove this API token.
   - **Delete Configuration** to remove both the server and API token.

Note: Removing the API key does not delete the key in Black Duck.
It only removes it locally.

Detect Desktop automatically retrieves and uses the appropriate version of Detect CLI
based on the Black Duck instance it connects to. The CLI is
only downloaded if a different version is required, ensuring compatibility without
unnecessary updates. Additionally, Detect Detect respects and downgrade settings
configured in your Black Duck environment, so you don't need to
manage CLI versions manually.

## Proxy Server

Accessing Black Duck Detect Desktop through a proxy is supported. Black Duck Detect Desktop automatically uses your local system proxy
setup.

If you are required to manually enter your proxy settings or you do not require a
proxy, you can modify these default settings.

To modify the default proxy settings:

1. Select the **Proxy Server** tab.
2. Select either **No Proxy Server**, **Use System Proxy Server Settings**, or **Manual
   Proxy Configuration**.
3. If you selected **Manual Proxy Configuration**:

   1. Enter the following information:
      - Your proxy host name.
      - Port number.
      - Whether authentication is required.
      - Your username and password.

      If a proxy is enabled and authentication is required, you
      may have to re-enter your username and password.
   2. Click **Save**.
4. Restart the application.

## Black Duck Detect

Optionally, select **Black Duck Detect** and if necessary, define any Black Duck
Detect settings, clear any build tools you do not want to use, or manually configure
the path to the build tools.

## Checking for updates

You can check to see if there are updates to the Black Duck Detect (Desktop) by
selecting the **Updates** tab. The page lists the last time you checked for
updates. Click **Check for updates** to view if there are newer versions
available. This option is only available for Windows and MacOS systems.

## Certificates

When connecting to Black Duck, you can ignore invalid or insecure
SSL certificates.

1. Select the **Server Configuration** tab.
2. Check the **Ignore invalid or insecure SSL Certificates** checkbox.
3. Restart the application.

CAUTION:

This is a potentially unsafe operation. It should only be used if you must
connect to a system with an insecure or self-signed certificate.

Alternatively, if you want to imported a self-signed certificate, this can be done following
the standard keytool import process for your JRE.

Identify the location of the JRE being used by Black Duck Detect:

1. Click [image: Settings icon] , located in the upper right corner display the Settings page.
2. Select the **Black Duck Detect** tab.
3. Select **paths** from the Properties menu. Alternatively, type
   **paths** in the Search Properties search field to narrow the options
   displayed.
4. If the **Java Executable** field has no value, Black Duck Detect will use the
   JRE installed under `$JAVA_HOME` set in your system environment
   variables.

Now that the location of the JRE that Black Duck Detect is using is known, the certificate
should be imported to the relevant `cacerts` file (typically found in
the `lib\security` folder).

1. Within a terminal session, run the following command (changing the paths to suit):

   ```
   keytool -import -trustcacerts -keystore <path_to_keystore> -file <path_to_certificate> -alias <alias_for_cert>
   ```
2. You will be prompted for a password. Provide it and press enter.
3. You will be prompted whether or not to trust the certificate. Inspect the
   contents and accept as appropriate.

Note: It may be necessary to also import any intermediary certificates associated with a chain.
If you encounter any issues with the import process, please contact your IT
department.
