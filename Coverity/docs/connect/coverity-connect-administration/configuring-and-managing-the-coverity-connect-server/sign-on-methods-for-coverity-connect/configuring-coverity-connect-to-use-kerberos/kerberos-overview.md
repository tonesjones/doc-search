---
title: "Kerberos overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/kerberos-overview.html"
content_id: "m6WAmM91WFy4ekgBbhIMYQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:43.472279+00:00"
---

# Kerberos overview

Kerberos is a suite of services that implement Single Sign-On (SSO). Kerberos enables a
client and a server (security principals) to authenticate each other securely on an
unsecure network, and conduct encrypted communications. The Kerberos protocol is
operated by the Key Distribution Center (KDC). The KDC comprises two services: an
Authentication Server (AS) and a Ticket Granting Service (TGS).

When a client wishes to access a resource on a server, the client first contacts the KDC
and provides an account name and password. The AS accesses Azure Entra ID to verify
the credentials, and if verified, grants a Ticket Getting Ticket (TGT) to the client.
When the client needs to access a server in the domain, the client submits the TGT back
to the Ticket Granting Service of the KDC, which then grants a service ticket and
session keys to the client. The client presents the service ticket to the server, which
then authenticates the ticket and the client.

The service ticket is typically valid for a day, but the interval can be set by the Kerberos
administrator. Each time the user needs to obtain a new service ticket, he will have to
execute `kinit`. See Obtaining an initial Kerberos ticket.

In Coverity, when Coverity Connect is configured to use Kerberos, it will use Kerberos
authentication for LDAP users from LDAP servers associated with the Kerberos server.

Attention: Coverity Connect does not use Kerberos for local users, including the
built-in Admin user account.
