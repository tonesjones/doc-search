---
title: "Sensitive data overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sensitive-data-overview.html"
content_id: "kVbdxmDFt~WqbZmr6Y7~LA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:23.855302+00:00"
---

# Sensitive data overview

Many web applications and APIs do not properly protect sensitive data such as
financial, healthcare, and Personal Identifying Information (PII).

Without protection, attackers can steal or modify such weakly protected data to conduct
credit card fraud, identity theft, or other crimes. Sensitive data can be compromised if
it does not have extra protection such as encryption at rest or in transit, and it
requires special precautions when exchanged by using a browser.

Checkers concerned with sensitive data include the following (remember that the set of
checkers can change with each release of Coverity):

- SENSITIVE_DATA_LEAK
- UNENCRYPTED_SENSITIVE_DATA
- WEAK_PASSWORD_HASH
