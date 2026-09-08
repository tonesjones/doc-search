---
title: "Visual Log Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/visual-log-configuration.html"
content_id: "B8Y5ws8StN1OOj1JAhDO6w"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:33.636777+00:00"
content_hash: "1837f07888d19dea9f2e04d264ff923bfcb0ad455b3f5e18a9565e55434a8af4"
---

# Visual Log Configuration

By default, the visual log will not record `successful-login` events. To
enable this, set the `auth.logging.recordSuccess = true`.

**Note:** Changing this property will not retroactively reveal successful logins that
occurred previously, as this setting determines whether to *record* successful
logins, not whether to *show* them.
