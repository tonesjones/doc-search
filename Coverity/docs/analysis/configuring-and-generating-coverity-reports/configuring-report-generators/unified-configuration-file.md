---
title: "Unified configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unified-configuration-file.html"
content_id: "vOyCWobNQCJ1KsEnSgPbsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:05.579198+00:00"
---

# Unified configuration file

You can use the same `.yaml` configuration file to configure all of the
reports for the same project. You can have multiple configuration files (saved under
different `.yaml` file names) for different projects.

Here is what the unified configuration file looks like with all sections included.

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
################## CERT report #############
cert-report:
	target-level: F
```

```
################## Black Duck Software Integrity Report #############
bdsir-report:
    analysis-date: 01/15/2019
    legal-text:
    show-checker-details:
    include-false-positive: YES	
```

```
################## Coverity Integrity Report #############
cir-report:
    project-description:
    project-details:
    target-integrity-level:
    high-severity-name:
    unspecified-severity-name:
    trial:
    loc-multiplier:
    include-low-impact:
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

```
################## DISA ASD STIG report #############		
disa-stig:
    ds-version: V5
report-warning-text:
	"Warning: This document contains technical data, export of which is restricted by the Export Administration Regulations (EAR).
	Disclosure to foreign persons without prior U.S Government approval is prohibited.
	Violations of these export laws and regulations are subject to severe civil and criminal penalities."
```

```
# Some reports display information about OWASP/SANS
#   owasp possible values are: 2017, 2021, 2025
#   sans possible values are: 2012, 2021, 2022, 2023
report-cwe-version:
    owasp:
    sans:
```
