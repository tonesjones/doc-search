---
title: "Sign-on methods for Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sign-on-methods-for-coverity-connect.html"
content_id: "rnV_6ikuRxHPWTFX6Jtw1A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:35.849259+00:00"
---

# Sign-on methods for Coverity Connect

Coverity Connect provides a few alternatives for managing the way users can sign on. See
the following list:

LDAP
:   (Lightweight Directory Access Protocol) LDAP manages access to a remote,
    *enterprise* server. Information on the remote server can include
    user authentication data such as user names and passwords. You can use LDAP
    to authenticate users without using the other possible options; however,
    LDAP does not provide a single sign-on solution (SSO).

    CAUTION:

    If an installation sets up SAML SSO to support groups, this
    supersedes the LDAP group-management settings.

Kerberos
:   Kerberos is a suite of services that works in conjunction with LDAP, and
    includes support for single sign-on.

    Kerberos does not provide support for groups. With Kerberos, LDAP is needed
    to manage group support.

SAML
:   (Security Assertion Markup Language) The SAML method can work in conjunction
    with LDAP, but it delegates identity management to a server that acts as an
    identity provider (*IdP),* rather than to the enterprise server
    itself.  Third-party solutions are available to manage IdPs and
    provide single sign-on services.

    Attention: The Coverity Connect SAML implementation will work with
    any multi-factor authentication (MFA) that has been set up on the IdP.

    SAML optionally supports groups. If SAML support for groups is enabled, then
    there is no need to use LDAP. In the case of group assignment, the SAML
    settings supersede the LDAP settings.

    A Coordinator server can optionally be configured to use single sign-on with
    SAML.

Reverse proxy
:   Reverse proxy is a general-purpose way to provide single sign-on. It used
    mainly by clients who maintain their own, custom gatekeeping
    server.

Among these alternatives, SAML single sign-on (SAML SSO) is the most general-purpose
method of managing user authentication. Coverity Connect continues to support the LDAP,
Kerberos, and reverse-proxy methods in order to accommodate customers who have a prior
investment in an older method, or who have particular system setup requirements.
