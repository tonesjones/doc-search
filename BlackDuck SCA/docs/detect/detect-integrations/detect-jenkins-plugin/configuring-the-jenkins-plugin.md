---
title: "Configuring the Jenkins Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/configuring-the-jenkins-plugin.html"
content_id: "XQXE09KQRr7wOBXQM1kVTw"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:58.728387+00:00"
---

# Configuring the Jenkins Plugin

Use the following process to configure the Black Duck® Detect for Jenkins plugin. Note that the supported credential format is API token. SAML or username/password authentication are not supported.

1. After installing, navigate to **Manage Jenkins** > **Configure System**.
2. Navigate to the **Detect** section, and complete the following.

   1. **Global download strategy**: Depending on your desired deployment method, select either the option to **Install Air Gapped Detect as a Tool Installation** or **Download via scripts or use DETECT_JAR** from the drop-down list.

   Figure 1. Global download strategy Air Gap.
   [image: Global download strategy Air Gap]

   Figure 2. Global download strategy Scripts/Jar.
   [image: Global download strategy Scripts/Jar]
3. **Black Duck SCA URL**: Specify the URL of your Black Duck SCA server instance.
4. **Black Duck SCA credentials**: To add credentials, click **Add** > **Jenkins**, and select API Token as the credential that you want to add and populate the relevant fields.
   When you add credentials, you can select those credentials that you want from the drop-down menu to authenticate to the Black Duck SCA server.

   1. For user API tokens, select **Secret text** from the menu in the **Kind** drop-down, then provide your Black Duck SCA access token in the **Secret** field that appears.

   Figure 3. Input access token secret.
   [image: Inputting the access token secret]
5. The **Advanced...** option displays for Black Duck SCA. Advanced settings enable you to specify values for:

   1. **Black Duck SCA connection timeout** (in seconds).  The default value is 120.
   2. **Trust Black Duck SCA certificates**: Select the checkbox to allow (SSL) certificates from Black Duck SCA.

   Figure 4. Configure timeout and SSL.
   [image: Configure connection timeout and SSL]
6. Click **Test Connection to Black Duck SCA** to verify that your settings are correct. If so, a *Connection successful!* status displays.
7. Click **Save**.
