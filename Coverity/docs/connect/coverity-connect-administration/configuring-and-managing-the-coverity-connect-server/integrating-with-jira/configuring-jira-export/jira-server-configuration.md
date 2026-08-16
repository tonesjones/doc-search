---
title: "JIRA server configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/jira-server-configuration.html"
content_id: "bsKHDWckAC0zoj0FHSfj_Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:15.638224+00:00"
---

# JIRA server configuration

Note: Before you begin the following procedure, be aware of the following:

- You must first create an API token associated with the Jira account you intend
  to use. Refer to the Atlassian Jira documentation for information on creating
  API tokens.
- If Coverity is deployed in the cloud, refer to "Add certificates to the
  Coverity Connect truststore" in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on importing a Jira
  self signed certificate.

The first step in configuring integration with Jira is establishing a connection to the Jira
server. To do so, complete the following steps:

1. Navigate to Configuration > System > Bug Tracking System: JIRA and click JIRA Server
   Configuration...
2. Enter the URL of your Jira server in the Location
   field.
3. Enter the username for your Jira account into the
   Username field.
4. Copy and paste an API token associated with your Jira account into the
   Password field, and then click Check
   Connection.

   At this point, you will see a message confirming a successful connection, or
   an error message explaining how you might correct the failed connection.
5. When you have a successful connection, click OK and
   move on to the project mapping step.

Note: Note that it might be necessary to disable the Jira Captcha feature prior to
connecting with the Jira server. To do so, complete the following steps:

1. Go to Jira administration and select System.
2. Click Edit Settings.
3. Change the value in Maximum Authentication Attempts
   Allowed to blank.
4. Click Update.

Note: In the case of connecting to a Jira server using SSL, it might be
necessary to import the Jira self-signed certificate into the Java keystore for
Coverity Connect.

1. Obtain the Jira SSL certificate (*.pem).
2. Execute `cd
   <install_directory>/jre/lib/security`
3. Make a backup of the `cacerts` file.
4. Execute `../../bin/keytool -importcert -keystore cacerts -file
   JIRA-CA.pem`
5. Restart Coverity Connect and confirm the connection.
