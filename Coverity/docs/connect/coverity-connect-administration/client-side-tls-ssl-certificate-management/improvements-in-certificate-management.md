---
title: "Improvements in certificate management"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/improvements-in-certificate-management.html"
content_id: "ZZ6Qu8MGCt8vb_Kquv7fWg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:24.600049+00:00"
---

# Improvements in certificate management

Prior to Coverity 8.0 there were various difficulties in managing certificates. Coverity
8.0 solves these difficulties.

- Few Coverity SSL client applications accept self-signed certificates. Other
  applications needed to be provided with certificates in other ways. In Coverity
  8.0, all clients can accept self-signed certificates.
- CA root certificate propagation was difficult. Customers with private CAs had to
  manually propagate CA root certificates to every SSL client. Now, several
  features make this task easier.
- There were multiple types of truststores, and several ways to update each type, which was
  difficult to document and manage. Now, most truststores are in PEM format,
  facilitating updates.
