---
title: "fAST Dynamic checkers"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/fast-dynamic-checkers.html"
content_id: "sEzVdIh0efZ0S6n93cPByQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:44.595496+00:00"
content_hash: "89af4407743cc9950d29d82a4e060cbe10e424af059a353767346ace047c91e5"
---

# fAST Dynamic checkers

This reference lists all active and passive checkers used by fAST Dynamic to detect security vulnerabilities in web applications and APIs. You can enable or disable individual checkers.

The fAST Dynamic scan engine uses multiple *checkers* to detect vulnerabilities in the target web application or API.

Checkers are either active or passive:

- Active checkers directly interact with the target website or API. They will craft and send attack payloads and then observe the target web application or API's behavior in order to identify security concerns.
- To enable active checkers in scans, you must select the Perform Active Attacks checkbox when creating the DAST project. See [Create DAST projects for web applications and APIs](create-dast-projects-for-web-applications-and-apis.md).
- Passive checkers do not directly interact with the target web application or API. They observe requests and responses sent to and from the fAST Dynamic scan engine.

## Checkers in DAST scans

This table lists all checkers used in DAST scans by fAST Dynamic.

Each checker is assigned a unique code. To enable or disable checkers from DAST scans, add or remove checker codes from your `scan-settings.json` configuration file. See [Configure JSON scan settings and authentication profiles](configure-json-scan-settings-and-authentication-profiles.md) for more information. You can also modify the Checkers settings on the Scan settings subtab—see [DAST scan settings](dast-scan-settings.md) for more information.

Note: Certain checkers are associated with more than one class.

| Class Name | Checker Code | API/Web | Active/Passive | CWE™ \* | CVSSv3 | Severity\*\* |
| --- | --- | --- | --- | --- | --- | --- |
| Open Redirect | OR | Web | Active | CWE-601 | 4.3 | Medium |
| Local File Inclusion | LFI | Web | Active | CWE-22, CWE-98 | 7.5 | High |
| HTTP Response Splitting | HRS | Web | Active | CWE-113 | 5.3 | Medium |
| Stored Cross-Site Scripting (XSS) | XSS.STO | Web | Active | CWE-79, CWE-80 | 9.6 | Critical |
| HTTP Verb Tampering | AM | Both | Active | - | 6.5 | Medium |
| ASP.NET Debugging Enabled | ASPDEBUG | Web | Active | CWE-11, CWE-11 | 0 | Low |
| Path Traversal | PATHTRAV | Both | Active | CWE-22, CWE-73, CWE-426 | 5.8 | Medium |
| Shellshock | SHELL | Web | Active | CWE-78 | 10 | Critical |
| Command Injection | CMD | Both | Active | CWE-78 | 9.8 | Critical |
| Direct Request | FILE | Web | Active | CWE-425 | 8.6 | High |
| HTML Injection | SPOOF | Web | Active | CWE-94 | 4.3 | Medium |
| Incorrect Authorization | AUTHBYPASS | Both | Active | CWE-863 | 7.7 | High |
| Log4Shell | LOG4J | Web | Active | CWE-20, CWE-400, CWE-502, CWE-917 | 10 | Critical |
| Server-Side Request Forgery | SSRF | Both | Active | CWE-610, CWE-918 | 7.2 | High |
| Backup File Disclosure | BAK | Web | Active | CWE-425, CWE-530 | 5.3 | Medium |
| Resource Server Does Not Correctly Validate JWTs | JWT.NOVERIFY | Both | Active | CWE-284, CWE-287, CWE-863 | 9.1 | Critical |
| Frameable Resource | XFS | Web | Active | CWE-1021 | 4.3 | Medium |
| DOM-Based Cross-Site Scripting | XSS.DOM | Web | Active | CWE-79 | 6.1 | Medium |
| Insecure Deserialization | ID | Web | Active | CWE-502, CWE-913 | 9 | Critical |
| Null Byte Injection | NULLBYTE | Web | Active | CWE-158 | 5.6 | Medium |
| CORS - Authenticated Access Allowed from Arbitrary Origin | CORS | Web | Active | CWE-284, CWE-942 | 5.4 | Medium |
| SQL Injection | SQLI | Both | Active | CWE-89 | 9.8 | Critical |
| Blind SQL Injection | SQLI | Both | Active | CWE-89 | 9.8 | Critical |
| PHP Code Injection | PHPI | Web | Active | CWE-95 | 8.6 | High |
| Spring4Shell | S4S | Web | Active | CWE-94, CWE-917 | 9.8 | Critical |
| NoSQL Injection | NOSQLI | Both | Active | CWE-943 | 9.8 | Critical |
| Reflected Cross-Site Scripting (XSS) | XSS.REF | Both | Active | CWE-79 | 6.1 | Medium |
| SSL/TLS Configuration Vulnerable to POODLE | SSL | Web | Active | CWE-326 | 3.1 | Low |
| Deprecated TLS Protocol Version | SSL | Web | Active | CWE-326, CWE-327 | 4.8 | Medium |
| API Rate Limiting | APIRL | Web | Active | CWE-400, CWE-770, CWE-799 | 8.6 | High |
| Cross-Site WebSocket Hijacking | COWSH | Web | Active | CWE-352 | 5.4 | Medium |
| Cross Site Scripting | XSS | Web | Active | CWE-79 | 6.1 | Medium |
| Insecure HTTP Methods Enabled | AM | Web | Active | CWE-650, CWE-749 | 7.3 | High |
| Directory Search | DIR | Web | Active | CWE-22 | 5.3 | Medium |
| Weak SSL/TLS Configuration | SSL | Web | Active | CWE-327 | 6.5 | Medium |
| XML External Entity (XXE) Injection | XXE | Both | Active | CWE-611 | 8.3 | High |
| Unrestricted File Upload | FUP | Web | Active | CWE-434 | 6.5 | Medium |
| Resource Server Accepts the None Algorithm for JWTs | JWT.NONE | Both | Active | CWE-287, CWE-807 | 9.1 | Critical |
| Middleware Authorization Bypass | NEXTJSBYPASS | Web | Active | CWE-285, CWE-863 | 9.1 | Critical |
| Heartbleed | SSL | Web | Active | CWE-119 | 7.5 | High |
| Apache Struts - S2-045 | STRUTS | Web | Active | CWE-20 | 9.1 | Critical |
| VirtualDirContext JSP Disclosure | TOMJSPDISC | Web | Active | CWE-200 | 7.5 | High |
| Secure Cookie Attribute Not Set | COOKIES | Web | Passive | CWE-614 | 4.8 | Medium |
| Autocomplete HTML Attribute Not Disabled for Sensitive Fields | PASSAUTO | Web | Passive | CWE-525 | 3.3 | Low |
| Password in HTTP Response | PASSDISC | Web | Passive | CWE-522 | 3.1 | Low |
| Database Error Message Disclosure | SQLERR | Web | Passive | CWE-209 | 3.1 | Low |
| Captcha Detected | CAPTCHA | Web | Passive | CWE-200 | 0 | Low |
| Insecure Content-Security-Policy Header | CSP | Web | Passive | CWE-693 | 3.7 | Low |
| Credit Card Number Disclosure | CCN | Web | Passive | CWE-312, CWE-319 | 5.8 | Medium |
| Using Deprecated HTTP Headers | DEPHEADERS | Web | Passive | CWE-477 | 0 | Low |
| Server Error | SERVERERR | Both | Passive | CWE-209, CWE-544, CWE-550, CWE-703, CWE-755, CWE-756 | 4.3 | Medium |
| SSN Disclosure | SSN | Web | Passive | CWE-359 | 2.4 | Low |
| Internal Path Disclosure | IP | Web | Passive | CWE-209, CWE-497 | 3.7 | Low |
| F5 BIG-IP Cookie Information Disclosure | II | Web | Passive | CWE-212 | 5.3 | Medium |
| NetScalar Cookie Information Disclosure | II | Web | Passive | CWE-200, CWE-212, CWE-311 | 5.3 | Medium |
| Sensitive Form Over HTTP | FORMHTTP | Web | Passive | CWE-310, CWE-311, CWE-319 | 5.3 | Medium |
| Sensitive Data in Query String Parameter | SESSION | Web | Passive | CWE-200, CWE-598 | 3.7 | Low |
| Use of Deprecated or Insecure Components | INSOBJ | Web | Passive | CWE-1104 | 0 | Low |
| Resource Server Accepts the None Algorithm for JWTs | JWTALG | Both | Passive | CWE-287, CWE-807 | 9.1 | Critical |
| Sensitive Cookie with Improper SameSite Attribute | COOKIES | Web | Passive | CWE-1275 | 3.1 | Low |
| Vulnerable Library | VULNLIB | Web | Passive | CWE-1104 | 3.7 | Low |
| Missing Content-Security-Policy Header | MISSCSP | Web | Passive | CWE-693 | 3.7 | Low |
| Missing X-Content-Type-Options Header | MISSHEADERS.XCONTENT | Both | Passive | CWE-693 | 3.1 | Low |
| HTTPS Not Enabled | HTTP | Web | Passive | CWE-319 | 7.4 | High |
| Cross-Site Request Forgery (CSRF) | CSRF | Web | Passive | CWE-352 | 6.5 | Medium |
| Verbose Error Messages (with Stack Trace) | ST | Both | Passive | CWE-209 | 3.7 | Low |
| HttpOnly Cookie Attribute Not Set | COOKIES | Web | Passive | CWE-1004 | 3.4 | Low |
| Directory Listing Enabled | DIR | Web | Passive | CWE-548 | 5.3 | Medium |
| Fingerprinting | FINGER | Web | Passive | CWE-497 | 0 | Low |
| HTTP Strict Transport Security (HSTS) Not Implemented | MISSHEADERS.HSTS | Web | Passive | CWE-310, CWE-311, CWE-319 | 3.7 | Low |
| Missing Cache Control Header | MISSHEADERS.CACHE | Web | Passive | CWE-525, CWE-693 | 0 | Low |
| Internal IP Disclosure | II | Web | Passive | CWE-212 | 3.7 | Low |
| Inefficient Regular Expression Complexity | BLINDREDOS | API | Active | CWE-1333 | 7.5 | High |
| Improper Neutralization of Section Delimiters | BLNS | API | Active | CWE-145 | 5.3 | Medium |
| Uncontrolled Resource Consumption | ERRAMP | API | Active | CWE-400 | 2.6 | Low |
| Expired or Revoked Token Not Rejected | EXPR | API | Active | CWE-613 | 6.8 | Medium |
| Non-Null Argument Enforcement (GQL) | NONNULLARG | API | Active | CWE-20 | 0 | Low |
| HTTP Response Splitting | RESPSPLIT | API | Active | CWE-113 | 5.3 | Medium |
| Accept Header Validation | ACCEPTVAL | API | Active | CWE-20 | 5.3 | Medium |
| Classic Buffer Overflow | BUFFOF | API | Active | CWE-120 | 7.3 | High |
| Content-Type Validation | CTVALIDATION | API | Active | CWE-20 | 5.3 | Medium |
| Mass Assignment | ASSIGN | API | Active | CWE-862, CWE-915 | 4.3 | Medium |
| Non-Null Type Enforcement (GQL) | NOFIELD | API | Active | CWE-754 | 0 | Low |
| YAML Injection | YAMLI | API | Active | CWE-20 | 9.8 | Critical |
| API Broken Object Level Authorization | BOLA | API | Active | CWE-285, CWE-639 | 7.5 | High |
| Authentication Leakage | AUTHLEAK | API | Passive | CWE-294 | 6.5 | Medium |

\* Common Weakness Enumeration (CWE™) refers to a formal list of common types of software weaknesses, which may result in vulnerabilities. For more information, see the CWE List at <https://cwe.mitre.org/data/index.html>. CWE is a trademark of The MITRE Corporation.

\*\* Severity is calculated based on the CVSS score.
