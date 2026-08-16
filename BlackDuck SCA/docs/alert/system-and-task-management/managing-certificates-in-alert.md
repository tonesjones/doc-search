---
title: "Managing Certificates in Alert"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/managing-certificates-in-alert.html"
content_id: "zZGxOywqTkOAe7GIjDlP5w"
version: "8.4.0"
section: "System and Task Management"
scraped_at: "2026-08-08T23:46:40.257413+00:00"
---

# Managing Certificates in Alert

You can use the **Certificates** page to add any required certificates to enable
secure communication.

Tip: When you want to test a connection to a Black Duck SCA server or an external
channel and you receive a PKIX error you may be missing the certificates required to
secure the connections.

This section explains how you add, edit, and delete certificates from the system.

To create, edit, or delete certificates, click Certificates on the left navigation panel
to open the Certificates page and select either the Server or Client tab depending on
which type of certificate you wish to configure.

Figure 1. Certificates
[image: Certificates]

## Server certificate

- Select the **Server** tab.
- To add a new certificate, click **+New**, populate the following fields and save.
  - Alias
  - Certificate content

Figure 2. Certificate content
[image: Certificate content]

- To delete a certificate, select the checkbox in the row that represents the
  certificate and then click the **Delete** button.
- To edit a certificate, double-click the row for the user, or click the
  **Edit** icon.

Figure 3. Certificate content edit
[image: Certificate content]

- When you disable **Enable Auto-Refresh** on the **Certificates** screen a
  **Refresh** button appears, which enables you to refresh the
  display.
- Use the search box to search for installed certificates.

## Client certificate

- Select the **Client** tab.
- To add a certificate, populate the following fields and then save.
  - The certificate key password
  - The certificate key content
  - The client certificate content

    Note: Only one
    client certificate is supported at a time and all certificate values
    are all stored encrypted in the Alert database.

Figure 4. Client certificate content
[image: Certificate content]

- To delete the certificate, select the **Delete** button.

## Custom certificates

You can specify a custom `jssecacerts` or `cacerts` file to be used as the
Alert trust store. These are mounted like Docker secrets to secure this sensitive
information.

- The `jssecacerts` file takes **precedence** over the `cacerts`
  file.
- If neither file can be found in the secrets directory, Alert creates a new trust
  store file.
