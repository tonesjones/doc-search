---
title: "About locked out user accounts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-locked-out-user-accounts.html"
content_id: "hG4XtaIHRNSsU7g7_3EDbw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:46.111479+00:00"
---

# About locked out user accounts

A user will be locked out of their account for 10 minutes if they fail to enter the
correct password after 10 attempts. After the 10th failed attempt, a message will appear
on the login page notifying the user that their account is locked.

Log files contain information by username on successful logins, unsuccessful logins, and
account lockouts.

Note: This lockout feature does not apply to users logging in using SAML or LDAP.
