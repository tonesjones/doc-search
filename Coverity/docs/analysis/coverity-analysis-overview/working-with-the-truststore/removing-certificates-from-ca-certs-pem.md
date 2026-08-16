---
title: "Removing certificates from ca-certs.pem"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/removing-certificates-from-ca-certs.pem.html"
content_id: "zB6JoO79GgKuJ6Mkl_S2fg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:24.531698+00:00"
---

# Removing certificates from ca-certs.pem

To stop trusting a certificate authority certificate in
ca-certs.pem, complete the following steps:

1. Split ca-certs.pem into separate certificates, as indicated in Viewing Certificate Authority certificates.
2. Rename ca-certs.pem to old-ca-certs.pem.
3. Use `openssl` or `keytool` on each certificate to find the
   ones you want to include in the new ca-certs.pem.
4. Concatenate the certificates you want to include, and write the result to a new
   ca-certs.pem file.
5. Test with `cov-commit-defects`.
