---
title: "Test web applications and APIs with Polaris fAST Dynamic"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/test-web-applications-and-apis-with-polaris-fast-dynamic.html"
content_id: "F6JRhs0B6zpQUoQRA5KkhQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:38.951264+00:00"
content_hash: "8cbc819a21304226bf8662145b3573e85864cc435ecc8af81434abd43f2f9246"
---

# Test web applications and APIs with Polaris fAST Dynamic

With Polaris fAST Dynamic, you can perform rapid, self-service dynamic application security testing (DAST) of web applications and APIs. Testing of targets in private networks is supported through the Polaris secure tunnel feature and associated workflow in the Bridge CLI.

## About DAST

Dynamic application security testing (DAST) is an AppSec testing methodology that examines web applications and APIs at runtime by simulating attacks to identify potential vulnerabilities. DAST is known as "black-box testing". DAST tools have no visibility of a web application's source code, internal interactions, or designs at the system level. They observe a web application from the outside in, examine its running state, and observe its responses to simulated attacks. The application's responses to these simulations help determine whether it's vulnerable and might be susceptible to a real malicious attack.

## About Polaris fAST Dynamic

Polaris fAST Dynamic is a dynamic analysis engine and UI that brings self-service DAST capabilities to the Polaris platform.

**Key features**

- Advanced DAST scanner optimized for single-page applications (SPAs), JavaScript frameworks, and APIs.
- Fully automated DAST testing, tightly integrated with the Polaris UI and API, with fast project onboarding and scan initiation.
  - Includes AI-assisted annotation for BOLA issues within API specifications.
- Securely access internal web applications and APIs (inside private networks) with the secure tunnels feature, powered by the Teleport Access Platform.
- Authenticated DAST scans:
  - Support for several site and API authentication methods, including AI-assisted authentication, Simple, SAML, and multi-factor authentication (MFA) via email or TOTP.
  - Capture site login flows using Selenium or Chrome Recordings.
- Smart Settings: DAST scan settings are auto-configured in a pre-flight phase.
- Optimized checkers deliver low false positives while providing accurate vulnerability detection—emphasizing high-value checks that identify the highest-risk issues.
- Scales to accommodate a large number of DAST projects without compromising on performance.
- View DAST issues alongside SAST and SCA issues and triage by severity.
- Run DAST tests from pipelines using the Bridge CLI, including on internal applications.
- Developer Detail Dynamic report gives an overview of all DAST issues in the selected application scope.

CAUTION:

fAST Dynamic is intended for scanning pre-production web applications and APIs only.

## Active attacks

fAST Dynamic includes functionality to *perform active attacks* on your pre-production web applications and APIs.

If you select the Perform Active Attacks checkbox when creating a DAST project, fAST Dynamic will simulate real-world attacks by sending various inputs and then observing the application's or API's behavior. For more details, see [fAST Dynamic checkers](test-web-applications-and-apis-with-polaris-fast-dynamic/fast-dynamic-checkers.md).

Warning:

Be aware that these attacks can degrade the application and expose sensitive data.

## DAST projects and profiles

In the Polaris data model, DAST projects represent web applications and APIs—both external and internal—that are targeted for dynamic application security testing (DAST). Each DAST project is associated with a DAST profile. The profile defines scan settings used to test the target for vulnerabilities and a separate authentication profile that handles authentication by the scanner. For certain API checkers, such as those for detecting BOLA issues, you must create more than one authentication profile.

DAST projects are separate from SAST & SCA projects.

You can create multiple DAST projects across your applications, up to the maximum quantity defined in your DAST entitlement (see [Subscriptions and Entitlements in Polaris](../understand-polaris/subscriptions-and-entitlements-in-polaris.md)). For example, an application might contain one DAST project for a web application and one for a REST API.

You can view the number of DAST projects used and remaining in your entitlement on the Projects tab. For example:

[image: dast projects count]
