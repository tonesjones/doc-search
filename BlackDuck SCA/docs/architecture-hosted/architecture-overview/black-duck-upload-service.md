---
title: "Black Duck upload service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-upload-service.html"
content_id: "G3Lp6JKsXIOPtGvupgVhHA"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-10-04T23:32:22.221032+00:00"
content_hash: "ceecb72745b2b1379d46d31e2db1728a6ab74ef49c53ac9243a4c2f09b7a690f"
---

# Black Duck upload service

Customers can optionally decide to upload their source files to be used in reviewing snippet matches or embedded licenses and copyrights in the Black Duck UI. If not enabled, the system will still function, however users will not be able to view match content in the UI.

If source upload is desired, customers can work with Black Duck support to enable this feature. When enabled, Black Duck creates a master key which is used to encrypt and decrypt the source files. The master key is stored encrypted (AES-GCM-256 with a key length of 32 bytes) via the customer-specific key.

During a scan, the scan client sends the source file contents to the Black Duck instance via SSL/TLS-secured endpoint(s) and with the proper authorization token. An upload endpoint receives the source file contents via HTTPS. Access to the endpoint is secured via the generated and verified Black Duck JSON Web Token (JWT). The source files are stored via their associated file signature – no files are stored with their file name. Files are encrypted upon receipt via the master key.

The web application requests the file contents via the given file signature. The source file is transmitted via HTTPS over the network. The individual source file is unencrypted for viewing in the Black Duck web application via the master encryption key.

In addition to encryption, the uploaded files also are deleted according to the data retention policy as defined by the customer. By default, this is 180 days, Customers can work with Support to modify this default setting.
