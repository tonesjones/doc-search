---
title: "SMTP Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/smtp-configuration.html"
content_id: "r8ijsvwdlKdI9dKp4l6nSw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:37.854905+00:00"
content_hash: "9fadd264b46cbf63d90aaf5e5e676a8ef9bffc40e3f77d180610365cedf72e4f"
---

# SMTP Configuration

To support policy email notifications, a valid SMTP configuration is required. The
following properties are used to configure SMTP:

- `smtp.sender` - [required] the address the email is being sent from.
- `smtp.host` - [required] the SMTP server being used to send email.
- `smtp.user` - the username for the SMTP server (the sender email
  address). Required when using OAuth 2.0 authentication.
- `smtp.password` - the password for the SMTP server, if basic
  authentication is used.
- `smtp.oauthToken` - a static OAuth 2.0 access token for the SMTP
  server. This token must be manually rotated when it expires. For automatic token
  management, use `smtp.modeType` instead.
- `smtp.port` - [default: 25] the port of the SMTP server.
- `smtp.auth` - [default: false] true/false, if authentication is being used.
- `smtp.tls` - [default: false] true/false, if TLS is being used.
- `smtp.additionalProps` - a list of additional SMTP properties to
  configure the SMTP server. These are expected as comma-separated
  `key -> value` pairs. For example:
  `smtp.additionalProps = mail.smtp.ssl.enable -> true, mail.smtp.ssl.trust -> *`
  You can refer to the full list of available SMTP properties
  [here](https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html#:~:text=is%20NOT%20supported.-,Properties,-The%20SMTP%20protocol).

## OAuth 2.0 Configuration

The following properties enable automatic OAuth 2.0 token management, where SRM fetches
and refreshes the Bearer token automatically. See
SMTP Authentication Setup for
full setup instructions for each provider.

- `smtp.modeType` - the authentication mode. Accepted values:
  - `clientCredentials` - OAuth 2.0 Client Credentials grant.
    SRM fetches and refreshes access tokens automatically using the client ID
    and secret. Suitable for Microsoft Exchange Online / Office 365. See
    Client Credentials setup.
  - `refreshToken` - OAuth 2.0 Authorization Code grant. SRM
    uses a stored refresh token to obtain access tokens. Required for Google
    Workspace (Gmail) and Yahoo Mail, which do not support the Client
    Credentials grant for SMTP. See
    Authorization Code setup.
  - `basic` - standard username and password authentication
    (`smtp.user` + `smtp.password`). See
    Basic Authentication setup.
  - `oauthToken` - static OAuth 2.0 access token
    (`smtp.oauthToken`). Must be manually rotated when it
    expires. See
    Static OAuth Token setup.
- `smtp.clientId` - [required for `clientCredentials`
  and `refreshToken` modes] the OAuth 2.0 Application (Client) ID
  registered with the identity provider.
- `smtp.clientSecret` - [required for `clientCredentials`
  and `refreshToken` modes] the OAuth 2.0 client secret.
- `smtp.tokenUrl` - [required for `clientCredentials`
  and `refreshToken` modes] the token endpoint URL of the identity
  provider (e.g.
  `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`).
- `smtp.authorizationUrl` - [required for `refreshToken`
  mode only] the authorization endpoint URL of the identity provider (e.g.
  `https://accounts.google.com/o/oauth2/v2/auth`).
- `smtp.redirectUri` - [required for `refreshToken`
  mode only] the redirect URI registered with the identity provider. Must be set to
  `https://<srm-host>/x/smtp-oauth/callback`.
- `smtp.oauthScope` - the OAuth 2.0 scope to request.
  - [required for `refreshToken` mode] — e.g.
    `https://mail.google.com/` for Gmail, or
    `https://outlook.office.com/SMTP.Send offline_access`
    for Microsoft delegated access (the space separates two OAuth 2.0 scopes).
  - [recommended for `clientCredentials` mode] — Microsoft
    Entra v2.0 token endpoints require a scope; use
    `https://outlook.office365.com/.default` for Exchange
    Online app-only access. Omitting this will produce a warning and may
    cause token fetch to fail.
- `smtp.additionalOAuthParams` - [optional, `refreshToken`
  mode only] additional parameters to append to the OAuth 2.0 authorization URL, as
  comma-separated `key -> value` pairs. For example:
  `smtp.additionalOAuthParams = access_type -> offline, prompt -> consent`
  (required by Google to obtain a refresh token).

  CAUTION:

  Parameter values must not contain commas. Pairs with
  comma-containing values are silently ignored.
