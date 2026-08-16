---
title: "SAML SSO configuration parameters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/saml-sso-configuration-parameters.html"
content_id: "iKmQWq4NqDQLMlJ5eOoyZg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:49.952669+00:00"
---

# SAML SSO configuration parameters

These are the fields to use when you create or update a SAML SSO configuration for
Coverity Connect.

  
 [image: image]   

Disabled
:   When this box has a check mark, this particular SAML SSO configuration is
    disabled.

    Because you cannot delete a SAML SSO configuration until there are no more
    users associated with this configuration, Disabled
    provides a convenient alternative to deleting a SAML configuration.

Display Name
:   The name of the current SAML SSO configuration. This is the name that appears
    below the SAML Configuration entry in the list of
    configuration choices at the left of the Configuration -
    System dialog.

    Default: `saml`

SP Entity ID
:   The name of the service provider entity (also known as an *Audience
    URI)*.

    This value must be a valid string and must be no longer than 1024
    characters.

    Download SP Metadata button. Clicking this opens a
    file dialog to download the SP metadata associated with your Coverity
    Connect server.

IdP Metadata
:   Clicking the Browse button opens a file dialog to
    obtain the metadata for the identity provider.

    Important: Some IdP applications include the authentication certificate in the
    metadata. Coverity Connect *does not* automatically add such a
    certificate to the keystore. You must add the certificate manually, as
    described in the next section, Creating a SAML SSO configuration.

    CAUTION:

    If you use Azure Entra ID Federation Services (ADFS) as
    your IdP, authentication will fail unless you have specified a
    Name ID. To do so, follow these steps:

    1. In ADFS, create a rule that maps an LDAP
       E-Mail-Addresses attribute to an
       Outgoing Claim Type of
       E-Mail-Addresses.
    2. Also in ADFS, create a transform rule that maps the incoming
       claim type of E-Mail-Addresses to an
       outgoing claim type of Name ID, and set
       the outgoing name ID format to Email.
    3. If Coverity Connect was running, exit the application and then
       restart it.

SAML Groups
:   When on, Coverity Connect checks whether the metadata from the IdP includes a
    `groups` attribute. If it does, a user who logs in is
    added to the specified groups and removed from others. Users inherit
    permissions from the groups they belong to.

    This option is provided for customers who want their IdP app (rather than
    LDAP settings) to handle all authentication and authorization for Coverity
    Connect.

    Note:

    Groups must be manually created in Coverity Connect before SAML login. Group auto-creation is not supported.

    When you create a group in Coveirty Connect, ensure the group name matches the name of the same group in your IDP.

    CAUTION:

    If you set up SAML SSO to support groups, the `groups` attribute should be enabled and configured in the IdP.
    This option supersedes the LDAP group-management settings.
