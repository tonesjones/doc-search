---
title: "Coverity language support"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-language-support.html"
content_id: "cgEooquCmCS_~Wye1ZhMSg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:54.115448+00:00"
---

# Coverity language support

Coverity Analysis support can vary by programming language.

Table 1. Support by language

| Language | Capture Mode | Coverity Desktop Analysis | Coverity Extend SDK | CodeXM | Churn | Coding Standards & Vulnerability Reports | Language Versions | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APEX™ | `coverity capture` (the Coverity CLI) | No | No | No | No bound | CWE Top 25  OWASP Top 10 | Version agnostic |  |
| C/C++ | Build capture | Yes | Yes | Yes | <5% | - AUTOSAR C++14 R19-03 ISO/IEC TS 17961: 2013, Cor 1   2016 - MISRA C 2004: 1st Ed 2004.10, 2nd   Ed with Tech Cor 1 2008.07 - MISRA C 2012: 1st Ed 2013.03, Amendment 1   2016.04, Tech Cor 1 2017.06, Amendment 2 2020.02,   Amendment 3 & 4 2024.6 - MISRA C 2023: 2024.6 - MISRA C 2025: 2025.12 - MISRA C++ 2008: 2008.06 - MISRA C++ 2023: 2026.6 - SEI CERT C: 2016 Ed, POSIX rules, L1, most L2, some   L3 recs - CWE Top 25 - CWE On the Cusp - Hyundai-C 4.1: 2026.6 - Hyundai-Cpp 4.1: 2026.6 | C++98  C++23  C++20  C++17  C++14  C++11  C++03  C99  C89  C17  C11 |  |
| C# | Build capture | Yes | Yes | Yes | <5% | CWE Top 25  OWASP Top 10 | Up to C# 14 | Less than 5% churn is expected for build capture. |
| C# | `coverity capture` (the Coverity CLI) | No | Yes | Yes | No bound | CWE Top 25  OWASP Top 10 | Up to C# 14 |  |
| CUDA® | Build capture | Yes | No | Yes | No bound | - AUTOSAR C++14 R19-03 ISO/IEC TS 17961: 2013, Cor 1   2016 - MISRA C 2004: 1st Ed 2004.10, 2nd   Ed with Tech Cor 1 2008.07 - MISRA C 2012: 1st Ed 2013.03, Amendment 1   2016.04, Tech Cor 1 2017.06, Amendment 2 2020.02,   Amendment 3 & 4 2024.6 - MISRA C 2023: 2024.6 - MISRA C 2025: 2025.12 - MISRA C++ 2008: 2008.06 - MISRA C++ 2023: 2026.6 - SEI CERT C: 2016 Ed, POSIX rules, L1, most L2, some   L3 recs - SEI CERT C++ 2016 Ed - CWE Top 25 - CWE On the Cusp |  |  |
| Dart | `coverity capture` (the Coverity CLI) | No | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| Docker | `coverity capture` (the Coverity CLI) | No | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| Fortran | Standalone | No | No | No | No bound |  | Fortran 77  Fortran 90  Fortran 95  Fortran 2003  Fortran 2008  Fortran 2018 | Fortran Syntax Analysis performs buildless capture through the `cov-run-fortran` command. |
| Go | Build capture | Yes | No | Yes | No bound | OWASP Top 10 | Go 1.25–1.26 |  |
| Go | `coverity capture` (the Coverity CLI) | Yes | No | Yes | No bound | OWASP Top 10 | Go 1.25–1.26 |  |
| Java® | Build capture | Yes | Yes | Yes | <5% | CWE Top 25  CWE On the Cusp  OWASP Top 10  OWASP Mobile Top 10  SEI CERT Java,    online version    Hyundai Java 4.1 | Up to Java 26 | Less than 5% churn is expected for build capture. |
| Java | `coverity capture` (the Coverity CLI) | No | Yes | Yes | No bound | CWE Top 25  CWE On the Cusp  OWASP Top 10  OWASP Mobile Top 10  Hyundai Java 4.1 | Up to Java 26 |  |
| JavaScript® | `coverity capture` (the Coverity CLI) | Yes | Yes | Yes | <5% | OWASP Top 10 | ECMAScript 5–14 | ECMAScript 14 is also known as ECMAScript 2023. |
| Kotlin™ | Build capture | No | No | No | No bound | OWASP Mobile Top 10 | Kotlin  2.0.0-2.0.21, 2.1.0-2.1.10 |  |
| Objective-C® / Objective-C++® | Build capture | Yes | No | No | No bound |  |  |  |
| PHP | `coverity capture` (the Coverity CLI) | No | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| Python® | `coverity capture` (the Coverity CLI) | Yes | No | Yes | No bound | OWASP Top 10 | Python 3.x–3.13 |  |
| Ruby | `coverity capture` (the Coverity CLI) | Yes | No | No | No bound | OWASP Top 10 | CRuby 2.0-3.4 and equivalents |  |
| Rust (beta) | Build capture | No | No | No | No bound |  | Rust 1.92.0 (stable), Edition 2021 and 2024 | Beta release |
| Scala | `coverity capture` (the Coverity CLI) | Yes | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| Swift® | `coverity capture` (the Coverity CLI) | No | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| Terraform | `coverity capture` (the Coverity CLI) | No | No | No | No bound |  | Version agnostic. See ["Language Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html). |  |
| TypeScript | `coverity capture` (the Coverity CLI) | Yes | No | No | No bound | OWASP Top 10 | TypeScript 1.0–5.2 |  |
| Visual Basic® | Build capture | Yes | No | No | No bound | CWE Top 25  OWASP Top 10 | Up to Visual Basic 16 |  |

Note:
The preceding table combines supported coding standards (AUTOSAR, MISRA, and CERT) and
supported vulnerability reports (CWE and OWASP) into one column in order to conserve space.

Not all rules and directives in the listed coding standards are
supported. For information on how to run a code analysis using one of the
supported coding standards, see "Running coding-standard analyses"
in the Coverity Analysis 2026.6.0 User and Administrator Guide.

Coverity Analysis automatically finds defects listed in the supported vulnerability reports when you enable all security checkers.

Remember:
From report to report, there might be discrepancies in the CWE Top 25/40 values assigned to issues, but both CWE values are valid.

CWEs have a parent-child relationship. Because of this, a child can be considered the same CWE as its ancestor.
So the discrepancies arise because, when Coverity assigns a Top 25/40 rank to an issue, some reports only consider assigning CWEs from the Top 25,
while other reports consider the Top 40 as well.

Follow the links for more information on these topics:

- Supported platforms, compilers, language versions, and frameworks, see
  "Supported languages,
  compilers, and frameworks for Coverity Analysis" in the Coverity 2026.6.0 Installation and Upgrade Guide.
- Coverity Desktop Analysis, see the Coverity
  Desktop Analysis
  2026.6.0 User Guide.
- Checker development and the CodeXM language and libraries, see
  Coverity
  CodeXM Checkers Development Guide.
- Checker development and the Coverity Extend SDK, see Coverity Extend SDK 2026.6.0 Checker Development Guide.
- Build capture mode, see Build capture (for compiled languages) in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.
- Coverity CLI `coverity capture` command, in the "CLI Commands" section of the Coverity 2026.6.0 Command Reference.

For checkers, see the "Checker Enablement and Option Defaults by Language" table in the Coverity 2026.6.0 Checker Reference (HTML only). For deployment information, see the
following table.

Table 2. Deployment Considerations

|  |  |  |
| --- | --- | --- |
| Build and target platforms | Varies by language: See "Supported platforms". | Coverity 2026.6.0 Installation and Upgrade Guide |
| Memory Requirements | Varies by programming language: See "Hardware and network recommendations and requirements". |
