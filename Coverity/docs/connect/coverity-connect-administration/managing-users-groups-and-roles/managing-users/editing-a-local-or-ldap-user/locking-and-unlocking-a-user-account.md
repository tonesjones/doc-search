---
title: "Locking and unlocking a user account"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/locking-and-unlocking-a-user-account.html"
content_id: "GPATuXO4Mhml62mbaXgMJQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:32.846457+00:00"
---

# Locking and unlocking a user account

You can lock or unlock a user account. Users that are locked out of Coverity Connect can
regain access through a password recovery email, if you have enabled password recovery
(for details, see Configuring sign-in settings) and have configured email.

Important:
These steps do not apply to a soft lockout policy, which can happen when no local
password policy has been configured.

Note:
Compare locking out to Disabling a user account.

**To lock or unlock a user account:**

1. Navigate to Configuration > Users and Groups, select the individual user to unlock.
2. In User Details, click Edit.
3. Under Additional Actions, toggle Lock account to lock or unlock a user account.

   Note:
   If a user has been locked out automatically due to a local password policy timeout interval,
   you need to deselect Lock account to re-enable access.
