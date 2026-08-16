---
title: "Security Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-report.html"
content_id: "R8bMeN1AdHK6p_bySaAj3w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:03.639277+00:00"
---

# Security Report

The Security Report has additional keys for defining assurance levels and severity
mappings:

```
security-report:
    assurance-level-score: 90
    assurance-level: AL1
    severity-mapping: Carrier Grade
    severity-mapping-description:
    custom-severity-mapping:
        modify-data: very high
        read-data: very high
        dos-unreliable-execution: very high
        dos-resource-consumption: very high
        execute-unauthorized-code: very high
        gain-privileges: very high
        bypass-protection-mechanism: very high
        hide-activities: very high
```

**Assurance level**

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `assurance-level` | String | Indicates the level and its minimum acceptable score for the report to be considered passing.  The following values are available: AL1, AL2, AL3, and AL4. | AL1 | Yes |
| `assurance-level-score` | Integer | Indicates the assurance level score.  There are four assurance levels, representing security scores that are greater than or equal to 60, 70, 80, and 90.  When choosing the proper assurance level, consider its potential for damage to life, property, or reputation. For example, an application with high damage potential should have a high assurance level. | 90 | No |

**Custom severity mapping**

| Field | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `bypass-protection-mechanism` | String | Indicates if the attacker tries to bypass application or system protection mechanisms. The following values are available: very high, high, medium, low, very low, and informational. | Very high | No |
| `custom-severity-mapping` | String | If the severity mapping is set to `Custom`, then update the `custom-severity-mapping` with specific settings and values.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `dos-resource-consumption` | String | Indicates when a weakness creates a denial of service due to excessive resource consumption by the application.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `dos-unreliable-execution` | String | Indicates when the weakness creates a denial of service due to unreliable execution of the application.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `execute-unauthorized-code` | String | Indicates when an attacker tries to execute code that they do not have authority to execute.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `gain-privileges` | String | Indicates when an attacker tries to gain privileges that should not be available to them.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `hide-activities` | String | Indicates that an attacker might try to hide activities from visibility in an audit.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `modify-data` | String | Indicates when an attacker tries to modify data in the application.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `read-data` | String | Prevents the attacker from reading data that is private to the application.  The following values are available: `very high`, `high`, `medium`,`low`, `very low`, and `informational`. | Very high | No |
| `severity-mapping-description` | String | Indicates the description for the custom severity mapping. | N/A | No |

**Severity mapping**

This standalone mapping specifies the name of the severity map (formerly known as a
vignette), which is used to calculate an issue's severity values.

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `severity-mapping` | String | Indicates the name of the set of severity mappings used to determine the score of each issue. The first three mappings are built-in. | N/A | Yes |

For more information about Security Report configuration, see the "Security Report configuration file".
