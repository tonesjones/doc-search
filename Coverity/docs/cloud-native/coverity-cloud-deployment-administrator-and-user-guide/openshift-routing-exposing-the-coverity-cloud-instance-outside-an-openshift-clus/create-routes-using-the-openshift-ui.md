---
title: "Create routes using the OpenShift UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-routes-using-the-openshift-ui.html"
content_id: "xfqSaSG2Q5cuQV6Qk7RlWQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:54.544475+00:00"
---

# Create routes using the OpenShift UI

You can use the OpenShift UI in a browser to create a secure route that exposes the
Coverity Connect service in the OpenShift cluster to Coverity clients, as follows:

1. Login to either the OpenShift UI as administrator.
2. Select the project.
3. Go to Networking/Rules.
4. Select Create Route.
5. In the Create Route window, configure the following:
   - Name: Enter a unique name for the route.
   - Hostname: Let OpenShift automatically generate the
     host name. This is the fully qualified domain name (FQDN) that clients use
     to access Connect when exposed by an OpenShift route.

     Important: The Connect `cim`
     hostname must not exceed 46 characters in length. This restriction
     excludes the `https://` characters that are used when you
     specify a URL, and excludes any port definition.
   - Path: /
   - Service: Select the Connect service name. For
     example, `cnc-cim-cim`.
   - Target Port: Select port
     8080.
   - Security: Select Secure
     route.
   - TLS Termination: Select
     Edge.
   - Certificate: Browse for the TLS certificate. It must
     be a .crt certificate (not .csr certificate).
   - Key: Provide the certificate private key name.
