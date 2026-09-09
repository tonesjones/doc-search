---
title: "SMTP Authentication Setup"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/smtp-authentication-setup.html"
content_id: "Spphu_yq55ajqHYEHeMDow"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:38.540985+00:00"
content_hash: "0909a7f94c3d8f9e21c68a3edbf5fc8272af423a43d59ad17b18127e35a69be3"
---

# SMTP Authentication Setup

SRM supports four authentication modes for SMTP. The two OAuth 2.0 modes
(`clientCredentials` and `refreshToken`) provide
automatic token management — SRM fetches and refreshes the Bearer access token on its
own with no manual rotation required. The other two modes
(`basic` and `oauthToken`) use static credentials
configured directly in `codedx.props`.

| Use case / Provider | Authentication method | `smtp.modeType` |
| --- | --- | --- |
| Microsoft Exchange Online / Office 365 | OAuth 2.0 Client Credentials (automatic) | `clientCredentials` |
| Google Workspace (Gmail SMTP), Yahoo Mail | OAuth 2.0 Authorization Code / Refresh Token (automatic) | `refreshToken` |
| Any provider supporting username/password | Basic authentication (static) | `basic` |
| Any provider supporting Bearer tokens | Static OAuth 2.0 access token (manual rotation) | `oauthToken` |

## Client Credentials (Microsoft Exchange Online)

The Client Credentials grant is the simpler of the two flows. SRM authenticates
directly to the token endpoint using the client ID and secret — no user interaction
is required.

**Prerequisites:** Register an application in Azure Active Directory with the
`SMTP.Send` permission and generate a client secret.

Add the following to `codedx.props`:

```
smtp.sender       = notifications@example.com
smtp.host         = smtp.office365.com
smtp.port         = 587
smtp.auth         = true
smtp.tls          = true
smtp.user         = notifications@example.com
smtp.modeType     = clientCredentials
smtp.clientId     = <your-application-client-id>
smtp.clientSecret = <your-client-secret>
smtp.tokenUrl     = https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token
smtp.oauthScope   = https://outlook.office365.com/.default
```

Note: The `smtp.oauthScope` value
`https://outlook.office365.com/.default` is required for
Microsoft Entra v2.0 token endpoints when using app-only (Client Credentials)
access. Omitting it will cause the token request to fail.

SRM will automatically fetch a new access token when the current one expires. No
further action is required after initial configuration.

## Authorization Code / Refresh Token (Google Workspace, Yahoo)

Google Workspace and Yahoo Mail do not support the Client Credentials grant for SMTP.
They require a user to grant consent at least once, after which SRM stores the
resulting refresh token and uses it to obtain access tokens automatically.

**Prerequisites:**

- For Gmail: Create an OAuth 2.0 credential in Google Cloud Console with
  `https://mail.google.com/` as an authorized scope. Add
  `https://<srm-host>/x/smtp-oauth/callback` as an
  authorized redirect URI.
- For Yahoo: Register an application in the Yahoo Developer Console with SMTP
  send permission and the same callback URI.

**Step 1 — Add the following to `codedx.props`:**

```
smtp.sender       = notifications@example.com
smtp.host         = smtp.gmail.com
smtp.port         = 587
smtp.auth         = true
smtp.tls          = true
smtp.user         = notifications@example.com
smtp.modeType     = refreshToken
smtp.clientId     = <your-oauth2-client-id>
smtp.clientSecret = <your-oauth2-client-secret>
smtp.tokenUrl     = https://oauth2.googleapis.com/token
smtp.authorizationUrl = https://accounts.google.com/o/oauth2/v2/auth
smtp.redirectUri  = https://<srm-host>/x/smtp-oauth/callback
smtp.oauthScope   = https://mail.google.com/
smtp.additionalOAuthParams = access_type -> offline, prompt -> consent
```

Note: The `access_type -> offline` and `prompt -> consent`
parameters are required by Google to issue a refresh token. Without them, only a
short-lived access token is returned.

**Step 2 — Authorize SRM to send email on behalf of the account:**

After saving the configuration, an admin must complete a one-time consent flow:

1. Log in to SRM as an administrator.
2. Navigate to `GET /x/smtp-oauth/authorize` in a browser (e.g.
   `https://<srm-host>/x/smtp-oauth/authorize`).
3. You will be redirected to the provider's consent screen. Sign in with the
   sender account and grant the requested permissions.
4. After approval, the provider redirects back to SRM. The refresh token is
   stored securely in the SRM database. You will be redirected to the
   projects page on success.

From this point forward, SRM automatically refreshes the access token as needed.
No further admin action is required unless the refresh token expires or is
revoked.

Important: If the refresh token expires (for example, due to extended
inactivity or the user revoking access), email sending will fail. The application
logs will contain the message *SMTP OAuth refresh token has expired or been
revoked*. To recover, repeat Step 2 above to re-authorize.

## Basic Authentication

Basic authentication uses a plain username and password. No OAuth registration or
consent flow is required. This mode is suitable for internal SMTP relays and any
provider that supports standard SMTP AUTH.

Add the following to `codedx.props`:

```
smtp.sender   = notifications@example.com
smtp.host     = mail.example.com
smtp.port     = 587
smtp.auth     = true
smtp.tls      = true
smtp.user     = notifications@example.com
smtp.password = <your-smtp-password>
smtp.modeType = basic
```

CAUTION:

The password is stored in plain text in
`codedx.props`. Ensure the file has appropriate filesystem
permissions and is not exposed to unauthorised users.

## Static OAuth Token

The `oauthToken` mode accepts a pre-obtained OAuth 2.0 Bearer
access token. SRM uses it as-is without any automatic refresh. When the token
expires, it must be manually replaced in `codedx.props` and SRM
must be restarted.

This mode is provided for backwards compatibility or environments where token
issuance is managed externally. For most deployments, the
`clientCredentials` or `refreshToken` modes are
preferred because they eliminate manual token rotation.

Add the following to `codedx.props`:

```
smtp.sender     = notifications@example.com
smtp.host       = smtp.example.com
smtp.port       = 587
smtp.auth       = true
smtp.tls        = true
smtp.user       = notifications@example.com
smtp.oauthToken = <your-bearer-access-token>
smtp.modeType   = oauthToken
```

Important: Access tokens are short-lived (typically 1 hour). When the
token expires, email sending will fail and an error will be logged. Update
`smtp.oauthToken` with a new token and restart SRM to
resume.

## Token Refresh Behavior

SRM caches the access token in memory and proactively refreshes it before expiry.
If the SMTP server rejects a token that SRM believes is still valid (for example,
after a server-side revocation), SRM automatically clears the cached token and
retries the failed email once with a freshly fetched token.

The refresh token itself (for `refreshToken` mode) is stored in the
SRM database and is updated automatically if the provider rotates it during a
token refresh.
