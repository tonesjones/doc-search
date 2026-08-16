---
title: "Setting up and resetting two-factor authentication"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/setting-up-and-resetting-two-factor-authentication.html"
content_id: "dqcyqVyYbl1PSWvAbBxvRQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:28.597734+00:00"
content_hash: "1b6ae977e9baeb3960d447ab8d7419b92b4d63ab6c412de26f235322584bfa9b"
---

# Setting up and resetting two-factor authentication

## About two-factor authentication on Polaris

Polaris uses two-factor authentication (2FA) by default. Users provide a username and password when signing into the web UI, and then provide a one-time passcode that Polaris shares by way of an app on the user's mobile device.

## Set up 2FA

While two-factor authentication is enabled, all new users must connect their accounts with a 2FA app when they sign in to Polaris for the first time. This is done by scanning a QR code that appears on screen during the first sign in.

[image: setup 2fa]

## Reset 2FA

If a mobile device is lost, replaced, or destroyed, a user may need to have 2FA reset to access Polaris.

The reset can be initiated by an Organization Admin. If an Admin is locked out, only another Admin can reset 2FA; a user cannot reset their own access. If the organization has only one Organization Admin, Black Duck Support can restore access if the Admin is locked out. We recommend having more than one Organization Admin.

To reset 2FA, do the following.

1. Go to My Organization > Users.
2. Select a user.
3. Under Authentication Management, select Reset 2FA.

[image: reset 2fa]

The user receives an email inviting them to reset 2FA, and a link in the email leads to a new QR code.

Note: The link to reset 2FA expires after 24 hours. Resetting 2FA does not affect the user's password.
