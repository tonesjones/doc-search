---
title: "Uploading Coverity Tools artifacts to the Connect UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/uploading-coverity-tools-artifacts-to-the-connect-ui.html"
content_id: "itWbjMmLdK6s9HAuSXQaxw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:44.450232+00:00"
---

# Uploading Coverity Tools artifacts to the Connect UI

Note: You must be a Connect administrator to upload Coverity Tools
artifacts to the Coverity Connect UI.

Note: The Thin Client files within each uploaded Coverity Tools
artifact are also available for end users to download from the Thin Clients window of
the Coverity Connect UI.

Note: With an AWS S3 Express bucket configured, you can NOT upload a
`coverity-all-platforms-<version>.tar.gz` file from the
Connect UI. See Configure AWS S3 Express Helm keys.

Important: In this section, you are uploading one or more
Coverity Tools artifact files to Coverity Connect. These are the
`coverity-all-platforms-<version>.tar.gz` files that
you downloaded from the Black Duck registry. See Coverity client installer and documentation files. Coverity
Tools contains the Thin Client installer that programmers/end users download from the
Connect UI to their client systems.

Important: If your environment has an external network
connection (non-air-gapped) and if you set the scan tool synchronization Helm keys
(Set Helm keys to enable scan tool synchronization), the Coverity Tools default version
(2026.6.0) is uploaded to Connect when you perform a Helm
install. In this case, you can run scans using the default 2026.6.0
version without needing to perform any other uploads described in this section. If you
need to upload other Coverity Tools versions, continue with the steps in this
section.

For users to run scans in the Scan Service, the administrator must maintain all
currently-used Coverity Tools versions in the Available Coverity
Tools window of the Connect UI. As administrator, you upload Coverity
Tools versions as needed, and over time, maintain the Coverity Tools versions available
through the Connect UI.

To upload a Coverity Tools version into the Coverity Connect UI:

1. In a browser window, open the cloud instance of the Coverity Connect UI and login as
   `ADMIN`.
2. On top right of the window, select Configuration > Configure Coverity Tools.
3. In the Configure Coverity Tools window, click Add Coverity
   Tools. A pop-up opens:

   [image: image]
4. In the pop-up, perform the appropriate sub-steps:

   - Use the following steps to use scan tool synchronization to automatically
     download a Coverity Tools version from the Black Duck registry and upload it to Connect:

     Note: You must have set the scan tool synchronization
     Helm keys as described in Set Helm keys to enable scan tool synchronization.

     1. In the popup window, click Select a version
        and in the dropdown, select the version.
     2. Click the active Upload button.
     3. The selected version is downloaded from the Black Duck registry, then uploaded to
        the cloud storage bucket and are available in the Connect UI for
        to download. A status pop-up provides upload status. For
        example, `Status: UPLOAD_INITIATED`:

        [image: image]

        The upload can take several minutes.
        Once the upload completes, the pop-up should indicate
        `Status: COMPLETED`.

        [image: image]
   - Use the following steps to upload a Coverity Tools version that you
     downloaded from the Black Duck registry using
     `curl`:

     Note: These substeps assume
     that you have downloaded the
     `coverity-all-platforms-<version>.tar.gz` file for
     the desired version from the Black Duck
     private Docker registry and can access the files locally.

     1. In the popup window, click Choose file.
     2. Browse and select the
        `coverity-all-platforms-<version>.tar.gz`
        file for the Coverity toolkit version you need to upload. For
        example, `coverity-all-platforms-2026.6.0.tar.gz`
     3. Click Upload.

        The Coverity Tools image is
        uploaded to Connect and a pop-up window provides tool setup
        status information. Once the setup completes, the pop-up should
        indicate `Status: COMPLETED`.
     4. Repeat this sub-procedure for each Coverity Tools version that needs
        to be uploaded.
5. When the Coverity Tools setup completes and the Status is COMPLETED, click
   Close.

   The uploaded Coverity Tools version appears in the Available Coverity
   Tools window. These Coverity Tools versions will be available for
   users to run scans.

Note: Do not change the
`coverity-all-platforms-<version>.tar.gz` file names.

If an upload succeeds, you will see all Coverity Tools platforms for the selected version
in the Download drop down in the Coverity Connect UI as described
in Installing Coverity Thin Client on a client system.

If an upload fails. the file will not appear in the Download drop
down. In this case, try again to upload the desired
`coverity-all-platforms-<version>.tar.gz` file.

Each user who needs to install the Thin Client on their client system can download the
installer from the Download drop down in the Coverity Connect UI
as described in Installing Coverity Thin Client on a client system.
