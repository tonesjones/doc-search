---
title: "Authenticating a server that uses a self-signed certificate"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/authenticating-a-server-that-uses-a-self-signed-certificate.html"
content_id: "61tJX2lEZsrXe7c89poPrA"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.689330+00:00"
---

# Authenticating a server that uses a self-signed certificate

You can connect to servers that use self-signed certificates

A self-signed certificate can be convenient to use, especially when working only with in-house material.
Self-signed certificates are most often encountered when connecting to servers that are deployed on-premises;
examples of these might be Black Duck, Coverity Connect, or Software Risk Manager servers.

When it encounters a self-signed certificate, Code Sight prompts you to either accept or reject the certificate.
If you accept it, Code Sight adds the accepted certificate to its trusted certificate pool. All future communications with this server will be trusted.

In Eclipse, IntelliJ, and Visual Studio, the accept/reject notice is displayed as a dialog.

Figure 1. Dialog prompting to accept or reject a self-signed certificate
  
 [image: In Eclipse or IntelliJ, an alert dialog prompts the user to accept or reject a self-signed certificate]

(Example from IntelliJ)

In VS Code, the accept/reject notice appears as a notification in the lower-right corner of the window:

Figure 2. VS Code notification about a self-signed certificate
  
 [image: In VS Code, a notification prompts the user to accept or reject a self-signed certificate]

(Example from VS Code)

VS Code displays details of the certificate only when you click View Details.
This display is comparable to the information displayed by Eclipse, IntelliJ, or Visual Studio.

## Unexpected notifications

On occasion, Code Sight might prompt you to accept or reject a certificate even when you are not trying to authenticate to a server. This can happen if:

- The certificate on the server has been changed to use a different self-signed certificate.
- You are connecting to the server through a proxy that is configured to issue self-signed certificates.
