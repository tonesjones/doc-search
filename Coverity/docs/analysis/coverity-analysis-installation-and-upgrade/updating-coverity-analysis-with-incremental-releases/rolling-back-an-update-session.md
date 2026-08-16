---
title: "Rolling back an update session"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/rolling-back-an-update-session.html"
content_id: "YUqTNgjUKdt211fWY8mu7A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:23.812490+00:00"
---

# Rolling back an update session

Because `cov-install-updates` installs update packages transactionally,
it is unlikely to leave the installation in an unusable state. On the other hand, it is
possible that updates will affect your analysis results in ways that you find
undesirable.

To handle this scenario, `cov-install-updates` provides a
`rollback` subcommand. This command will roll back all of the
updates added in the most recent update session.

Note: An update session is one invocation of the `cov-install-updates
install` command. Subsequent invocations overwrite the rollback data, so
only data from the last session is retained.

Only files which were actually changed during the last installation session are rolled
back. Other files which were modified after the update session will not be affected by a
rollback.
