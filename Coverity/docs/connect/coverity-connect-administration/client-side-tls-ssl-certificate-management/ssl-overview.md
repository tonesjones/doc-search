---
title: "SSL Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ssl-overview.html"
content_id: "rZe64np1CZadXxbfxmBbBg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:22.400310+00:00"
---

# SSL Overview

Secure Sockets Layer (SSL) is a suite of industry-standard protocols for creating
encrypted connections between servers and applications. It is used in Coverity for a
variety of applications. This section focuses only on clients (such as
`cov-commit-defects` and `cov-security-report`) of
Coverity Connect.

SSL is important because it makes possible encryption and authentication. Encryption
allows a client and a server to communicate across an open network, with the assurance
that anyone monitoring the communication will not be able to understand it.
Authentication allows the client to know that it is actually communicating with whom it
expects, and not with an impostor.

The name "SSL" actually refers to an older version of the software. Transport Layer
Security (TLS) is the name of the newer version, but it is also referred to as SSL/TLS,
or just SSL.
