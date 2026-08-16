---
title: "Severity mapping: Mapping technical defects to severity levels"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/severity-mapping-mapping-technical-defects-to-severity-levels.html"
content_id: "200ODoao8nGkJC4r6iNQDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:15.578607+00:00"
---

# Severity mapping: Mapping technical defects to severity levels

A *severity mapping* is a mapping that determines the *severity* level of a
given *technical impact* associated with a software issue. *Technical impacts*
categorize the negative effects that can occur if an attacker exploits a particular
weakness in the target software. Not all weaknesses are exploitable, and not all
exploitable weaknesses are easy to exploit.

The Security Report is preconfigured with three built-in severity mappings (Carrier
grade, Web application, and Desktop application): the `Carrier grade`
severity mapping is the most stringent, and the `Desktop application` is
the least stringent. When you configure the report generator, you can also specify that
it use a custom severity mapping in which you can redefine severity levels for each
Technical Impact category.

Technical Impacts are divided into eight categories (as defined by CWE):

| Impact type | Meaning |
| --- | --- |
| Modify data | A weakness that could allow an attacker to modify memory or files on the host computer. |
| Read data | A weakness that could allow an attacker to read data that is not intended to be accessible to a user of the application. |
| Denial of service, unreliable execution | A weakness that can lead to crashes, freezes, and other malfunctions that can make the application unavailable to users. |
| Denial of service, resource consumption | A weakness that causes the application to use excessive CPU, memory, or storage resources, which degrades application performance. |
| Execute unauthorized code | A weakness that might allow an attacker to cause the application to execute code within or outside of the application in unintended ways. |
| Gain privileges | A weakness that might allow an attacker to perform privileged operations that are not intended to be available to a user of the application. |
| Bypass protection mechanism | A weakness that might allow an attacker to defeat or skirt protections that keep application users from reading, writing, or executing unauthorized resources. |
| Hide activities | A weakness that might allow an attacker to avoid detection. |

The severity mapping associates each Technical Impact with one of the following severity
levels:

- Informational (not included when calculating the Security Score)
- Very Low
- Low
- Medium
- High
- Very High

Issues that are found by Coverity Analysis might be associated with a CWE (Common
Weakness Enumeration) ID number. CWE ID numbers refer to CWE records, each of which
might have one or more Technical Impacts. If an issue has an **Issue
Kind** of **Quality** or **Security**
and its CWE record contains one or more of the eight types of Technical Impacts, that
issue will be included in the Security Report.

For an issue where its CWE ID maps to more than one of the eight technical impact values,
a single technical impact value will be assigned to the issue, where the highest
relevant severity level will determine which technical impact value gets assigned, with
ties for the highest severity level being broken arbitrarily.

Some issues found might not have a CWE ID; in that case, that issue cannot be associated
with a Technical Impact value and cannot be included in the Security Score. In this
case, the issue will be included in the **Issues Without CWE
Numbers** count of a Security Report's "Additional Quality Measures" section. That
section might also include issues that do have CWE IDs if the given CWE ID cannot be
mapped to at least one of the eight Technical Impact categories.

Note: Setting the same severity level for different tehnical impacts might result in an
issue being associated with different technical impacts from one generation of the
report to the next. This should not affect the overall security score.
