---
title: "SSL Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/ssl-configuration.html"
content_id: "luMlALTDgsTK6qbB46HE4g"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:52.787966+00:00"
content_hash: "22077b9385c72664702b075f7761a4cfe89805e70196d4d4eab99674e92e649b"
---

# SSL Configuration

What you do with the SSL configuration depends on your deployment scenario. By default,
the installer will setup Software Risk Manager dependencies to offer both HTTP and HTTPS
access to Software Risk Manager. This is sufficient for most evaluation scenarios. If,
however, you are deploying Software Risk Manager for production usage, then we recommend
that you use or obtain a valid SSL certificate for the host machine. If you don't use
your own certificates, HTTPS is enabled by default with a self-signed certificate
generated during installation. This will ensure secure communications to all clients
accessing Software Risk Manager. Note that if you use the default HTTPS option with the
self-signed certificate, most browsers will display a security warning when connecting,
which will need to be accepted to proceed with access to the site.

If Software Risk Manager will be used in a networked environment, using HTTPS to connect
is recommended. For example, once Software Risk Manager is installed, use
`https://<hostname>/srm` instead of
`http://<hostname>/srm` (substituting in your machine's
hostname).

Click the "Next" button if you're using the Software Risk Manager self-signed
certificate. Otherwise, use your own SSL certificate by getting the certificate and
associated private key in PEM-encoded X.509 format. (Some issuers refer to this as
“Apache format.”) Click "Do you want to import your own SSL certificate?" and browse to
those files.

[image: image]

## Replacing the SSL Certificate Post-Install

If you completed your installation using the Software Risk Manager self-signed SSL
certificate (as shown above), you can replace this self-signed certificate with your
own SSL certificate. You might do this if you skipped importing your own SSL
certificate due to certificate failure and you now have a new SSL certificate.

To replace the SSL certificate after Software Risk Manager installation:

1. Get your SSL certificate in PEM-encoded X.509 format (name the file
   `server.crt`) and the private key for the certificate in
   PEM format (name the file `server.key`).
2. Copy the two files into the following directory:
   `<your-srm-install-directory>/apache2/conf/certs`.
3. Restart your Software Risk Manager Apache service. You can do this in the
   manager app or in the Services area on your control panel.
