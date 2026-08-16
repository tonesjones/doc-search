---
title: "External network access"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/external-network-access.html"
content_id: "nkgwJhTlN04NmT3LCzuDDg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:12.527384+00:00"
---

# External network access

Update information is hosted on the Black Duck Customer Portal, and access to this site is
mediated by an authentication proxy server. When querying and downloading analysis
updates, a Coverity Connect instance must present a valid license ID to the proxy
server.

To support Coverity Analysis updates, a Coverity Connect instance must be configured so
it can reach external web addresses. It may be necessary to configure your firewall to
allow messages to and from the Authentication Proxy URL (<https://updates.lic.blackduck.com>).

Update packages are downloaded directly from Amazon Web Services. It may also be
necessary to allow messages to and from `https://s3.amazonaws.com/cdtpincrementals/*`.
