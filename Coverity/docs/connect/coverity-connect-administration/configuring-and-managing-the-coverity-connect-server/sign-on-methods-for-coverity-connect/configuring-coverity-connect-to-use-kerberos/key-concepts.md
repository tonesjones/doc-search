---
title: "Key concepts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/key-concepts.html"
content_id: "skhkalk8ZQtGqrk0uLroZA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:44.095492+00:00"
---

# Key concepts

- Keytab

  The keytab file ("key table") contains one or more entries, where each entry
  consists of a timestamp (indicating when the entry was written to the keytab), a
  service principal name, a key version number, an encryption type, and the
  encryption key itself. The keytab file is generated on each host in the Kerberos
  realm, and is used by Coverity Connect to authenticate clients.
- Fully Qualified Domain Name

  The fully qualified domain name (FQDN) is the complete domain name for a specific
  computer, or host, on a network. The FQDN consists of a hostname and a domain
  name. For example, in `mycomputer.mycompany.com`,
  `mycomputer` is the hostname, and
  `mycompany.com` is the domain name.
- Realm

  A Kerberos realm shares a common Kerberos database, and security principals
  within it can be authenticated to each other. It is conventionally written as an
  upper-case ASCII string.
