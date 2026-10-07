---
title: "Security Lenses overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/security-lenses-overview.html"
content_id: "nkvUFFiZQ7Xbxka8IMfJKw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.958706+00:00"
---

# Security Lenses overview

Security Lenses help security practitioners identify, review, and prioritize issues
using **Security Impact** classifications in Coverity Connect. Security Lenses provide
additional context for evaluating issues and help users focus on security-relevant
issues.

## Security Lenses and Security Impact

Security Lenses use the following **Security Impact** classifications to provide
additional context to evaluate issues:

| Security Impact | Explanation |
| --- | --- |
| Very High | Could enable severe adverse impact with the highest remediation priority. |
| High | Could enable significant adverse impact and should be addressed promptly. |
| Moderate | Could enable meaningful adverse impact and should be addressed through planned remediation. |
| Low | Could enable limited adverse impact or require additional conditions to become significant. |
| Very Low | Could enable minimal adverse impact in the analyzed context. |
| None | No security impact is assigned for the issue. |

Security Impact is separate from the existing Quality Impact classification.
Security Impact helps prioritize security risks, while Quality Impact helps
prioritize software reliability and quality concerns.

## How Security Impact is assigned

The SAST analysis engine assigns Security Impact values at the checker and
subcategory levels. Security Impact uses the NIST 800-30 categorical scale:
**Very High**, **High**, **Moderate**, **Low**, and
**Very Low**. Issues that are not associated with a supported security
context have a Security Impact value of **None**.

Security Impact is a fixed property produced by the analysis engine. Users cannot
modify Security Impact values in Coverity Connect.

In this release, Security Impact applies to C/C++ MISRA and SEI CERT checkers that
have a security context. Checkers outside a security context and non-applicable
quality rules have a Security Impact value of **None**.
