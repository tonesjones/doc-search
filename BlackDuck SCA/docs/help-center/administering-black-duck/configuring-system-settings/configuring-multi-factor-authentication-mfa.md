---
title: "Configuring Multi-Factor Authentication (MFA)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-multi-factor-authentication-mfa-.html"
content_id: "qdNeHVhVfiybZw6WiMrDZA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:07.501661+00:00"
---

# Configuring Multi-Factor Authentication (MFA)

To enhance the security of your account, Multi-Factor Authentication (MFA) can be enabled
in Black Duck. MFA adds an extra layer of protection by requiring
not only a username and password but also a time-based, one-time password (TOTP)
generated through a QA code scan. This ensures that even if your password is
compromised, access to your account will still require a verification code from your
authenticator app.

Please note, MFA is not compatible with Single Sign-On (SSO) or Security Assertion Markup
Language (SAML) based authentication methods. However, SAML can be configured after MFA
is enabled. In such cases, MFA will apply only when local users log in, as SSO and SAML
rely on external identity providers for authentication, bypassing MFA in Black Duck.

## Enabling or disabling MFA

To enable or disable MFA:

1. Log into Black Duck as a system administrator user.
2. Click **Admin** → **System Settings** → **Local Authentication**.
3. Switch the **Multi-Factor Authentication** toggle to **Enabled** or
   **Disabled**.

Note: Enabling and disabling MFA applies to all users in the system. MFA cannot be enabled
or disabled for individual users. Once activated or deactivated, this setting applies
universally across the platform.

## Configuring MFA secret time-to-live

Black Duck enforces a time-to-live (TTL) period for MFA secrets, ensuring they expire
after a set duration or when a new secret is requested. This expiration time is
configurable, allowing administrators to adjust the validity period to align with
their security policies. The default TTL period is two (2) minutes.

To configure MFA secret expiration:

1. Locate and open the Black Duck configuration file where
   system-wide settings are managed (e.g., blackduck-config.env or Helm values
   file if deployed in Kubernetes).
2. Add or update the following parameter to define the desired expiration time
   (in minutes):

   ```
   MFA_SECRET_TIME_TO_LIVE_MINUTE=<desired value in minutes>
   ```
3. If running Black Duck in a containerized environment,
   restart the necessary services to apply the changes.

## Scanning the QR code to set up MFA

Once Multi-Factor Authentication (MFA) has been enabled, the next step is to
configure an authenticator app to generate time-based, one-time passwords
(TOTPs).

1. **Choose an authenticator app**

   You will need an authenticator app installed on your mobile device. If you
   don't already have one, you can download a free app from your app store.
   Popular options include:

   - Google Authenticator (available on Android and iOS)
   - Microsoft Authenticator (available on Android and iOS)
   - Okta Verify (available on Android and iOS)
2. **Open the app**

   After installing the authenticator app, open it and prepare to scan a QR
   code. Each app may have slightly different navigation, but typically you
   will find the option to Add Account or Scan QR Code from the main menu.
3. **Scan the QR code**

   You can find the QR code in two places:

   - After logging into Black Duck using your
     username and password. This is where you will typically configure
     your MFA for the first time.
   - On your Profile page by clicking your *name* user button on the
     top right of the page and then selecting the **Profile**tab. If
     you choose to reset your MFA configuration, a new QR code
     will be generated from here.

   Using your authenticator app, scan the QR code shown on your screen. This
   links the app with your account and generates a unique TOTP for future
   logins.

   Tip: Ensure your phone's camera has access to focus properly on the
   QR code. Most apps will automatically recognize and scan the code in a few
   seconds.

   If you are unable to scan the QR code, many apps offer the option to manually
   enter the key by selecting an option like "Enter Key Manually" in the
   authenticator app.
4. **Verify the code**

   After scanning the QR code, the authenticator app will start generating
   6-digit codes that refresh every 30 seconds. Input the current code in the
   **Passcode** field.
5. **Complete setup**

   Once you've entered the correct code, the setup process is complete. You will
   now be prompted to enter a verification code from the authenticator app each
   time you log into the product.

## Resetting your or a user's MFA configuration

If the user needs to reset their Multi-Factor Authentication (MFA) configuration,
they can easily do so from their Profile page. Alternatively, a user administrator
user can initiate the reset process for any user through the Users page. Resetting
the MFA will require the user to go through the initial MFA setup process again,
including scanning the QR code and linking the account with an authenticator
app.

To reset your MFA configuration as a user:

1. Go to your Profile page by clicking your *name* user button on the top
   right of the page and then select **Profile**.
2. Under the **Profile** tab, click the **Reconfigure MFA** button found
   in the **Authentication** section.

   Warning: This action cannot be undone.

To reset a MFA configuration as a user administrator:

1. Click **Admin** → **Users**.
2. Select the desired user from the list displayed.
3. Click the **Reset User MFA** button in the **Local Authentication**
   section. The user will then be asked to reconfigure MFA upon their next
   login.

## Account locking

If a user enters an incorrect Multi-Factor Authentication (MFA) code or password ten
times consecutively, their account will be temporarily locked for 10 minutes. If you
find yourself locked out, please reach out to your user administrator for
assistance.
