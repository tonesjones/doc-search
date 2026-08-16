---
title: "Updated soft lockout policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/updated-soft-lockout-policy.html"
content_id: "olvp_KfUF_gmEaZwD81Pbw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:05.815770+00:00"
---

# Updated soft lockout policy

The following changes have been made to the Coverity Connect soft lockout policy:

- Restarting Coverity Connect no longer clears a soft lockout.
- The algorithm that interprets the
  `login.auth.check.failed.peruser.count` property has been
  updated. This property resides in the `cim.properties` file, if you
  choose to set it. This property previously required you to set it to one number
  lower than your desired number. For example, if you wanted to activate a soft
  lockout after 10 failed login attempts, you had to set this property to
  `9`. With this update, you would set it to `10`.
  In addition, the default value for this property has changed from `6`
  to `5`.
