---
title: "Logging in to Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/logging-in-to-black-duck.html"
content_id: "Oe18R592kpVGiDiMf85wSw"
version: "2026.7"
section: "Getting Started with Black Duck"
scraped_at: "2026-08-08T15:32:35.573011+00:00"
---

# Logging in to Black Duck

To access Black Duck SCA, you need to log in through your browser.
Logging in gives you access to project data, including projects that may be restricted
to your team and organization.

Note: You must have valid login credentials. If you do not have a username or password,
contact your Black Duck administrator.

## Login options

Depending on how your organization has configured authentication, you may be able to
log in using:

- Local Black Duck credentials: A username and password
  created by your administrator.
- LDAP credentials: Your organization's directory service login (if LDAP is
  enabled).
- SAML-based single sign-on (SSO): You may be directed to your company's login
  provider (if SAML is configured).

Note: If Multi-Factor Authentication (MFA) is enabled, it only applies to users logging in with
local credentials. Users authenticating through SAML or LDAP will not be prompted
for MFA.

If you're unsure which method applies to you, reach out to your administrator for
guidance.

## Steps to log in

1. Open a browser and navigate to the Black Duck URL
   provided by your system administrator. The URL typically follows this
   format:

   ```
   https://<your-black-duck-server-hostname>
   ```
2. Enter your username and password.

   - Passwords are case-sensitive.
   - If this is your first login or your password doesn't meet the
     system's security requirements, you'll be prompted to change it.
     Follow the on-screen password rules to complete the update.
3. Click **Login**.
4. If MFA is enabled on your instance, you'll be prompted to configure it the first time you log in:

   - A QR code will be displayed.
   - Use a supported authentication app (such as Google Authenticator) to
     scan the QR code.
   - Enter the 6-digit code from your app to complete the setup.

## After logging in

On your first login, you'll land on an empty Dashboard.

  
 [image: Empty Dashboard]   

To populate your dashboard with data, you need to scan
your code and map it to a project version. These steps are covered in the
next section of this guide.

By default, the Dashboard shows:

- My Projects: Projects you've created or been assigned to.
- Watching: Projects or components you've marked to monitor.

You can also create custom dashboards by
saving searches for specific projects, versions, or components you care about. Saved
searches will appear on your Dashboard for quick access.
