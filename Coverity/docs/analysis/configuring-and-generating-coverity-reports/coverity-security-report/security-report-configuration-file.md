---
title: "Security Report configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-report-configuration-file.html"
content_id: "7fwmjTRyL7WL~YYrKPwFsQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:13.632180+00:00"
---

# Security Report configuration file

Configuration values determine the information displayed on the title
page of your report and specify notification information for your project. You can
specify configuration information in your config.yaml configuration
file. (A config.yaml template file is shipped with the Report
Generators and is installed in the config/ directory.)

Here is an example .yaml configuration file:

```
################## Sections that apply to all reports #############
version:
     schema-version: 7
connection:
    url: https://coverity.example.com:8443/
    username: admin
    ssl-ca-certs:
project: "My project"
title-page:
    company-name: ABC
    project-name:
    project-version: 0.9
    logo:
    organizational-unit-name: Widgets
    organizational-unit-term: Division
    prepared-for: "Jane Doe"
    project-contact-email: prj@abc.com
    prepared-by: "John Smith"
locale:
issue-cutoff-count: 200
snapshot-id:
snapshot-date:
issue-kind:
components:
```

```
################## Coverity Security Report #############
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
    hide-lines-of-code: NO
```

Note: This report requires the additional report configuration settings
listed in the example above. This ensures that the report results are
properly included in the output.

The config.yaml file can also include a
section to specify which version of SANS the report should use (and the OWASP version as
well). This section is used for the CVSS, Security, Software Integrity, OWASP and
PCI-DSS reports.

```
# Some reports display information about OWASP/SANS
#   owasp possible values are: 2017, 2021, 2025
#   sans possible values are: 2012, 2021, 2022, 2023
report-cwe-version:
    owasp:
    sans:
```

The following table describes the Security Report specific settings.

| Key | Description |
| --- | --- |
| `assurance-level` | [Mandatory] A level indicating the minimum acceptable score for the report to be considered passing. Possible values are the following: AL1, AL2, AL3, and AL4. Default value: AL1 |
| `assurance-level-score` | [Optional] There are four Assurance Levels, representing Security Scores of greater than or equal to 60, 70, 80, and 90. When choosing the Assurance Level, consider the potential for damage to life, property, or reputation. An application with high damage potential should have a high Assurance Level. Default value: 90 |
| `bypass-protection-mechanism` | [Optional] Custom field. Indicates that an attacker has tried to bypass application or system protection mechanisms. Default value: `very high` |
| `custom-severity-mapping` | [Optional] If the severity mapping is set to `Custom`, then this entry introduces some specific custom settings, whose descriptions follow. Each custom field can be set to one of the following values: `very high`, `high`, `medium`, `low`, `very low`, or `informational`. Default value for each field: `very high` |
| `dos_resource-consumption` | [Optional] Custom field. Indicates when a weakness creates a denial of service due to excessive resource consumption by the application. Default value: `very high` |
| `dos-unreliable-execution` | [Optional] Custom field. Indicates when a weakness creates a denial of service due to unreliable execution of the application. Default value: `very high` |
| `execute-unauthorized-code` | [Optional] Custom field. Indicates when an attacker tries to execute code that it does not have authority to execute. Default value: `very high` |
| `gain-privileges` | [Optional] Custom field. Indicates when an attacker tries to gain privileges that should not be available to it. Default value: `very high` |
| `hide-activities` | [Optional] Custom field. Indicates when an attacker tries to modify data in the application. Default value: `very high` |
| `hide-lines-of-code` | [Optional] Specify whether to display LOC (Lines of Code) information. Possible values are `YES` and `NO`. The default value is `NO` (LOC information will be displayed in the report). |
| `severity-mapping` | [Mandatory] The name of the set of severity mappings used to determine the score of each issue. See the documentation for a description of the severity mapping. The first three mappings are built-in. `Custom` indicates that the mapping identified by `custom-severity-mapping` and `severity-mapping-description` should be used. Valid values are `Carrier Grade`, `Web application`, `Desktop application`, and `Custom`. Default value: `Carrier Grade` |
| `severity-mapping-description` | [Optional] Descriptive text for custom severity mapping. |

The following table describes the keys that apply to all reports.

| Key | Description |
| --- | --- |
| `components` | [Optional] A comma-separated list of Coverity Connect component names, which include component map names. If the components are listed here, the report will include data only for the listed components; for example: Default.lib or Default.src. |
| `connection` | The URL of the Coverity Connect instance. The `url` and `username` fields are mandatory. |
| `connection:ssl-ca-certs` | [Optional] Lists the pathname to a file containing additional CA certificates that are used in establishing a secure HTTPS connection through a TLS/SSL handshake. Pathnames must be entered in PEM format. |
| `connection:username` | [Mandatory] Coverity Connect username. |
| `connection:url` | [Mandatory] Lists the URL of the Coverity Connect instance. This URL must not include user name and password. |
| `issue-cutoff-count` | [Optional] Some reports display information about individual issues. These reports bound the number of issues displayed in order to control the size of the report. This bound is called the issue cutoff count. It is used for CVSS, Security, PCI DSS, Mobile OWASP, and OWASP reports. Maximum value is 10000 for Security report. Default value: 200 |
| `issue-kind` | [Optional] A comma-separated list of Coverity Connect issue kinds. If issue kinds are listed here, the report will include only issues of the listed kinds. The possible values for `issue-kind` are as follows:  - `Quality` - `Security`  The following line is an example of using this option:  ``` issue-kind: Quality ``` |
| `locale` | [Optional] Locale of the report. Default value: `en_US`  The Coverity Integrity report also supports `ja_JP`.  The CVSS report, MISRA report and Security report also support `ja_JP`, `ko_KR`, and `zh_CN`. |
|  |  |
| `on-cert-trust` | Allows users to trust self-signed certificates sent by Coverity Connect. There are two possible values: `trust` or `distrust`. Use `trust` to accept, use, and store a self-signed certificate for reuse. Use `distrust` to reject connections from servers using self-signed certificates. Not used by DISA ASD STIG and Mobile OWASP reports. Default value: `trust` |
| `project` | [Mandatory] Name of the Coverity Connect project. |
| `report-cwe-version: owasp` | Specifies the version of OWASP to use in an OWASP Web report. The default version to use is 2017. You can generate a 2021 report, instead. It is used for CVSS, Security, Software Integrity, OWASP, and PCI-DSS reports. |
| `report-cwe-version: sans` | Specifies the version of SANS to use in a SANS report. The default version to use is 2019. You can generate a 2021, 2022, or a 2023 report, instead. It is used for CVSS, Security, Software Integrity, OWASP, and PCI-DSS reports. |
| `snapshot-date` | [Optional] Retrieves the most recent snapshot of each stream in the project whose date is less than or equal to the given date. Format is DD/MM/YYYY. |
| `snapshot-id` | [Optional] Retrieves the defects of a specific snapshot id, instead of using the latest snapshot id of all the streams associated with the project. |
| `title-page` | Describes the fields in the title page of the report. |
| `title-page:company-name` | [Mandatory] Name of your company. |
| `title-page:logo` | [Optional] Path to a logo file for your company. Valid image types are BMP, GIF, JPG, and PNG. The maximum allowed image size is 210 pixels wide by 70 pixels high. Note that backslash characters in a path must be doubled. |
| `title-page:organizational-unit-name` | [Mandatory] Name of your division, group, team or other organizational unit. |
| `title-page:organizational-unit-term` | [Mandatory] Organizational unit term (e.g., division, group, team). |
| `title-page:prepared-by` | [Mandatory] Name of the entity that prepared the report. |
| `title-page:prepared-for` | [Mandatory] Name of the entity for which the report was prepared. |
| `title-page:project-contact-email` | [Mandatory] Project contact email address. It is used for the following reports: CVSS, Integrity Report, PCI DSS, Mobile OWASP, and OWASP2017. Not used by other reports. |
| `title-page:project-name` | [Optional] Name of the software development project. May be distinct from the Coverity Connect project name. |
| `title-page:project-version` | [Mandatory] Lists the project version number. |
| `version:schema-version` | [Mandatory] Sets the version number for the .yaml file's schema. Changes that alter the semantics of the parts of the schema that are independent of the report in a non-additive way must trigger an increment of this number. |

For more information about schema configurations, see Configuring report generators
