---
title: "Procedures for propagating CA certificates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/procedures-for-propagating-ca-certificates.html"
content_id: "72KC2MxFnzrxqTfUEDfY4A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:26.455966+00:00"
---

# Procedures for propagating CA certificates

These procedures are needed for propagating private CA root certificates. Guidelines are
presented below depending on network environment.

On Windows, use Azure Entra ID
:   By storing a certificate in AD, a network administrator can push the
    certificate to users' Root Certificate Store. See your AD documentation for
    information on how to do this.

On Unix/Linux, use the OS truststore
:   Using remote administration software such as Puppet, append CA certificates
    to /etc/ssl/certs/ca-certificates.crt, a PEM-formatted
    file.

Share a file via shared storage
:   If your client executables are provided via a shared volume, consider putting the CA certificates
    in the Installation truststore.

    Otherwise, consider putting the CA certificates in shared storage and referring to them as
    the Extra CA truststore.

Store a certificate file in your codebase
:   It can be used as an Extra CA truststore or copied to the User truststore.

Propagate using email
:   If you email a PEM-format certificate file as an attachment with an extension
    of .cer, a Windows user can add it to their Root
    certificate store by double-clicking on it.

    Similarly, a Macintosh user can add the certificate to their keychain.

    If your Unix/Linux users have root access, they can append the file to their OS truststore
    file.

    Otherwise, the attachment can be put in the User truststore.
