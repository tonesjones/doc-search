---
title: "Configuring the soft lockout policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-soft-lockout-policy.html"
content_id: "Sg0wfJFWDOvSheVeIVf61Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:27.873486+00:00"
---

# Configuring the soft lockout policy

Coverity Connect implements a default *soft lockout policy* that temporarily
prevents an affected user or users from logging in after a set number of consecutive,
failed, login attempts. Such a lockout can be triggered by an excessive count of
consecutive, failed, login attempts made either by a particular local user or from a
particular IP address. In the first case, only the local user who made the failed login
attempts is locked out. In the second case, all users who attempt to log in from that
particular IP address are blocked from further attempts.

These are the soft lockout policy's default values:

- Maximum number of consecutive, failed, login attempts allowed for any particular
  local user: 5
- Maximum number of consecutive, failed, login attempts allowed from any particular IP
  address: 20
- Period of time that a user must wait until the lockout is lifted (unless lifted
  manually by an administratior): 30 minutes

  Any attempt to log in during a soft
  lockout resets this timer. For example, if the lockout duration is 30 minutes
  and the user tries to log in after 29 minutes have elapsed, the user must wait
  another 30 minutes before attempting to log in.

An administrator can see in the Users and Groups panel that a user
is temporarily locked out. However, to unlock that user the administrator must access Configuration > System > Authentication and Sign-In > Sign In Log and then click the Unlock All option, which
unlocks *all* of the temporarily locked-out users and IP addresses. This panel has
no control that can unlock an individual user by name.

Note:

- The soft lockout feature can affect any user including the admin account.
- Restarting Coverity Connect does not clear a soft lockout.
- Enabling a local password policy automatically disables the soft lockout policy
  for local users (the soft lockout policy for IP addresses is unaffected). See
  Configuring a local password policy for information about
  enabling a local password policy.

If necessary, you can reconfigure the soft lockout policy by adding properties to your
cim.properties file as described below
(cim.properties is located in the
<coverityConnectInstallDir>/config/ directory):

CAUTION:

The soft lockout policy's default values were chosen to optimize the
security of Coverity Connect, so we recommend that you do not change them.

**To configure the maximum number of consecutive, failed, login attempts allowed per
local user:** Add a property named
`login.auth.check.failed.peruser.count` to your
cim.properties file. For example, the following setting
temporarily blocks login attempts by a local user after three consecutive, failed, login
attempts by that user:

```
login.auth.check.failed.peruser.count=3
```

**To configure the maximum number of consecutive, failed, login attempts allowed per IP
address:** Add a property named
`login.auth.check.failed.perip.count` to your
cim.properties file. For example, the following setting
temporarily blocks login attempts from an IP address after five consecutive, failed,
login attempts from that IP address:

```
login.auth.check.failed.perip.count=5
```

**Configuring the duration of a soft lockout:** To configure the duration of a soft
lockout, add a property named
`login.auth.check.failed.reset.delay.minutes` to your
cim.properties file. For example, the following entry changes
the duration of a soft lockout from 30 to 45 minutes:

```
login.auth.check.failed.reset.delay.minutes=45
```
