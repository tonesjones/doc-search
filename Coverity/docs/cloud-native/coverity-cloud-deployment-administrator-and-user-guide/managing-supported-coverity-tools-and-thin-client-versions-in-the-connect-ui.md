---
title: "Managing supported Coverity Tools and Thin Client versions in the Connect UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-supported-coverity-tools-and-thin-client-versions-in-the-connect-ui.html"
content_id: "XUh93c5wytOJwJZEwFwqiQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:43.605685+00:00"
---

# Managing supported Coverity Tools and Thin Client versions in the Connect UI

As of release 2023.6.0, Coverity Scan Service supports the use of many versions of Thin
Client to perform scans. End users/programmers can download one of several available
versions of Thin Client to run scans. Similarly, CI/CD commands can download one of many
versions of Coverity Tools artifacts to run scans as supported by the installed Coverity
version.

This chapter describes, for the Coverity cloud administrator, how to maintain the
Coverity Tools/Thin Client versions that are available either by CI/CD or end users to
perform scans. For CI/CD, you are managing the Coverity Tools artifact versions,
including a default version, that are available to initiate scans from a CI/CD command.
For end users/programmers, you are managing Thin Client versions that the end users can
download from the Connect UI Thin Clients window to their client system.

- For CI/CD, you are managing the Coverity Tools artifact versions, including a
  default version, that are available to initiate scans from a CI/CD command. The
  default version feature makes it easier to manage CI/CD pipelines as you do not
  need to change pipelines to support multiple versions of Thin Client.
- For end users/programmers, you are managing Thin Client versions that the end
  users can download from the Connect UI Thin Clients window to their client
  system. The Thin Client files within each uploaded Coverity Tools artifact are
  also available for end users to download from the Thin Clients window of the
  Coverity Connect UI.

For Coverity client support information, see Coverity client support matrix.

If you are performing an upgrade of Coverity cloud deployment, refer to Upgrading a Coverity cloud deployment.

Note:

You must be a Connect administrator to perform the procedures described in this
chapter.

In this chapter, the user is a developer or anyone that will use the Thin Client to
run scans.

Before continuing with the procedures in this chapter, ensure that the Helm chart
deployed successfully and that you can access the Connect UI.

An administrator performs the following tasks to manage Coverity Tools artifact and Thin
Client versions that are available for either CI/CD or end users:

- For an air-gapped Coverity Kubernetes cluster that is not connected to external
  networks, download the Coverity Tools artifact from the Black Duck private registry. See Downloading a Coverity toolkit artifact from the Black Duck repository.
- As of the 2023.12.0 release, for connected (non-air-gapped) deployments, supported
  Coverity Tools artifact versions can be automatically uploaded one at a time as
  selected in the Connect UI. After being uploaded, the Coverity Tools artifact
  versions and Thin Client versions are available for CI/CD or end users to run
  scans.
- Upload Coverity Tools artifact versions as needed to Connect. See Uploading Coverity Tools artifacts to the Connect UI.

  Note: If
  this is an initial installation or an upgrade, and if scan tool synchronization
  is configured, Coverity Tools artifact version 2026.6.0 is
  automatically uploaded into the Available Coverity Tools
  window of the Coverity Connect UI.
- Set the default Coverity Tools version for CI/CD. See Setting the default Coverity Tools version for CI/CD pipelines.
- Unset the default Coverity Tools version for CI/CD. See Unsetting the default Coverity Tools version for CI/CD pipelines.
- Change the default Coverity Tools version for CI/CD. See Changing the default Coverity Tools version for CI/CD pipelines.
- Archive a Coverity Tools version. See Archiving a Coverity Tools version.
- Delete a Coverity Tools version. See Deleting a Coverity Tools version.
