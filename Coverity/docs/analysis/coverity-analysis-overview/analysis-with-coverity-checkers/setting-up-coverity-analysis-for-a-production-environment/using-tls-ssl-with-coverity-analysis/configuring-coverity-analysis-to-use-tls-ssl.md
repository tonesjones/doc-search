---
title: "Configuring Coverity Analysis to use TLS/SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-coverity-analysis-to-use-tls/ssl.html"
content_id: "MImBUbSFtqWUve61OZPeAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:19.754747+00:00"
---

# Configuring Coverity Analysis to use TLS/SSL

This procedure allows you to use TLS/SSL with commands that send data to Coverity Connect,
such as `cov-commit-defects`, `cov-run-desktop`, and
`cov-manage-history`. Note that it discusses authentication modes
described in TrustStore overview.

1. Make sure that Coverity Connect is configured to use TLS/SSL.

   For the setup procedure, see
   "Configuring Coverity
   Connect to use TLS/SSL" in Coverity Platform 2026.6.0 User and Administrator Guide.
2. Verify browser access to Coverity Connect over HTTPS.

   Simply type the Coverity Connect URL,
   including the HTTPS port number into your browser, for
   example:

   ```
   https://connect.example.com:8443/
   ```
3. If necessary, install a certificate on each client, using one of the following modes:
   - The fully authenticated mode: If your certification authority certificate is in
     ca-certs.pem (which is typical if you paid an
     external certification authority entity, such as Verisign, for your
     certificate), no action is needed. Otherwise, follow the instructions in
     Adding a certificate to ca-certs.pem.
   - The trust-first-time mode: If you use the Coverity Connect self-signed certificate that was
     installed with Coverity Connect and you commit using trust-first-time, no
     action is needed.
4. Use `cov-commit-defects` to test a commit using TLS/SSL.
5. Inspect the new certificate, if any, in the TrustStore.

   For details on viewing
   certificates, see Working with the TrustStore.
