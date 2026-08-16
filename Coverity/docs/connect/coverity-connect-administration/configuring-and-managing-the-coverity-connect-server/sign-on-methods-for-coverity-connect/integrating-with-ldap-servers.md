---
title: "Integrating with LDAP servers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integrating-with-ldap-servers.html"
content_id: "yYRodPE41AKCuRDYjBIdCQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:36.448831+00:00"
---

# Integrating with LDAP servers

Lightweight Directory Access Protocol (LDAP) is used in organizations to centralize the
storage of information common to many applications, particularly related to
authentication, such as a user name (ID) or password. LDAP allows site administrators to
enter this information only once, and all LDAP-compliant applications can use this
central resource.

LDAP is used for authentication of users and for retrieving external properties stored in
LDAP that are of interest to Coverity Connect, such as an email address and a user's
full name. These attributes are replicated in the Coverity Connect database. Coverity
Connect uses LDAP group information.

You can use LDAP authentication for user sign-in so that Coverity Connect does not have
to save user passwords locally.

Note: It is important that Coverity Connect users retain their identities even in the event
of configuration or organizational changes. If a person's identity is not maintained in
Coverity Connect, issues that include that person in triage records (for example, issue
owner designations) will appear to have originated with a different person.

LDAP
servers maintain user identities. When considering whether to add an LDAP server to
Coverity Connect, ask yourself whether the new server will refer to the same persons
as the old server. If the answer, generally, is "yes", you should modify the
existing LDAP server configuration in Coverity Connect to point to the new server
rather than add an additional LDAP server configuration.
