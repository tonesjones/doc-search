---
title: "Account Lockout"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/account-lockout.html"
content_id: "WoF7drRHmVDUqf40GeJmgg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:23.080559+00:00"
content_hash: "6083a3920ced032f8db2b5ccaa9cef78aac0539672c063303e2a34d22a7511a5"
---

# Account Lockout

Software Risk Manager will automatically lock user accounts that are attempting to log in too many times. When a user's account is locked,
they can no longer log in until the account is unlocked. An account will either unlock after the set lockout duration has elapsed, the password is reset, or when it was manually unlocked by an admin. Admins may view locked accounts and unlock them on the users page.

Note that SRM only locks local user accounts. Other authentication schemes such as LDAP, SSO, etc., are not subject to these rules and may have rules of their own.

All of these parameters for lockout may be customized via the following props:

- `auth.lockout.enabled` – [default: true] Determines if the account lockout feature is enabled or not. Note that setting this to `false` will not unlock already locked accounts
- `auth.lockout.timespan` – [default: 15 minutes] The time period in which the log in attempts must occur
- `auth.lockout.attempts` – [default: 5] The number of failed attempts that must occur before the account is locked
- `auth.lockout.duration` – [default: 1 hour] How long the account will be locked for. After the lockout duration, a user can attempt to log in again. This value may be set to `0` if an indefinite lockout is desired
