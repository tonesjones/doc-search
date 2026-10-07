---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "d9bE6awRxyi~tS8Kgpt~2A"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:32.278342+00:00"
content_hash: "e72172883230916d459c09a262c7569d6f9f77ed24e3b8818f740fbe2acbcdf0"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-25500). Added mechanisms for users running on AWS to enable a workaround for this issue. Users experiencing this issue are encouraged to contact Black Duck support if they see high CPU usage from the upload-cache service. This issue will be fixed in the upcoming Black Duck 2023.10.0 release.
- (HUB-38587). Fixed an issue where the `kbMatchTimeoutProperty` was set inadvertantly to a hardcoded value (100000ms). It will now read it from the `blackduck-config.env` file as expected.
- (HUB-38735). Fixed an issue where upgrading from PostgreSQL 9.6 or PostgreSQL 11-based Black Duck versions to Black Duck 2023.4.1 could cause postgres-upgrader to fail and not start up the application when using the PostgreSQL container.
- (HUB-38815). Fixed an intermittent `ResourceAccessException` error in Black Duck rapid scans that could cause the scans to fail.
