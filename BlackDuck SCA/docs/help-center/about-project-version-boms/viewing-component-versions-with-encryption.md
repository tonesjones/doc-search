---
title: "Viewing component versions with encryption"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-component-versions-with-encryption.html"
content_id: "eFMMUxBMiloMPb11c56QiQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:15:02.209367+00:00"
---

# Viewing component versions with encryption

Attention: This feature is not enabled by default in Black Duck
and must be activated by adding the feature to your Product Registration key.

Open source software can use or implement cryptographic algorithms which can impact your
organization from security and compliance perspective.

On the compliance side, whenever you send software out of the country – for example, on a
computer, as source code, or compiled into an application that is for sale – depending
upon where you live, you may be required to adhere to certain governmental regulations
regarding the export of cryptography. This is especially true of strong cryptographic
algorithms which may require licenses to export, however the regulations have eased in
recent years.

On the security side, companies may be interested in understanding if open source is
using weak cryptography or obsolete hashing mechanisms. Using a cracked (or insecure)
cryptographic algorithm can add unnecessary risk to your organization, especially if
well-known techniques exist to break the algorithm. Understanding algorithms in use can
help companies comply with security standards.

Black Duck helps you identify the component versions that
have encryption algorithms.

- A cryptography filter in the component version BOM page identifies those component versions with encryption.
- A cryptography icon ( [image: Cryptography icon] ) appears in the BOM page for any component version with encryption
  algorithms.

Select the component version to open the *Component Version* page and then select
the **Cryptography** tab:

  
 [image: Cryptopgraphy tab]   

- The table lists the encryption algorithms found in this component version.
- The warning symbol ( [image: Warning icon] ) indicates that this algorithm has a known weakness.
- Select an algorithm from the table to view more information, such as a
  description, key lengths, originator, licensing, and patent information.

  Possible values for key lengths, with key length values where applicable,
  are:

  - Single Fixed Key Length
  - Multiple Fixed Key Lengths
  - User Definable Key Length within a Closed Range
  - User Definable Key Length Unconstrained
  - No Encryption or No Key Used

Note that the **Cryptography** tab does not appear if a component version does not
have encryption algorithms.

Note: While components added manually to existing BOMs will display cryptography information,
legacy BOMs may require a rescan for cryptography data to appear.

For more information on federal regulations, visit the Bureau of Industry and Security's
(BIS) website: [https://www.bis.doc.gov](https://www.bis.doc.gov/)
