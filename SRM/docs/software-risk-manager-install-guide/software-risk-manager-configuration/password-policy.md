---
title: "Password Policy"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/password-policy.html"
content_id: "MolUdKpdZ2jV30XJPdDjIA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:23.682608+00:00"
content_hash: "1ffa704bd2d6b80ea278bfb7862b9426f5eae38d5c7444d2f9777552101da8b4"
---

# Password Policy

Software Risk Manager can be configured to have new/edited local user passwords meet
certain requirements.

The defaults for SRM’s password requirements are listed below; however, requirements can
be specified by setting the appropriate properties:

- `local-password-policy.minimum-length = 12` - Require a minimum
  length [default: 12].
- `local-password-policy.maximum-length = 1048576` - Require a
  maximum length [default: 1048576].
- `local-password-policy.contains-lowercase = false` - Require a
  lowercase character [default: true].
- `local-password-policy.contains-uppercase = false` - Require an
  uppercase character [default: true].
- `local-password-policy.contains-number = false` - Require a number
  [default: true].
- `local-password-policy.contains-special-character = false` - Require
  a special character (e.g. $ ! # %) [default: true].
- `local-password-policy.common-check.enabled = true` - Require
  passwords to be distinct from an internal set of known compromised passwords [default: true].
- `local-password-policy.unique-password-check.enabled = true` - Require
  passwords to be distinct from the last *n* previously used passwords, where *n* is configurable [default: true].
  - `local-password-policy.unique-password-check.num-to-check = 10` - The last *n* previous passwords to prohibit a user from setting as their password [default: 10].
- `local-password-policy.reset-on-first-login = true` - Require that users set a
  new password when logging in for the first time [default: true].
- `local-password-policy.reset-after-admin-sets-password = true` - Require that
  users set a new password when an admin resets their password [default: true].
- `local-password-policy.max-password-age = 12 months` - Require that users set a new
  password after a set amount of time since it was last reset. This can be disabled by setting a value
  of 0 [default: 12 months].
