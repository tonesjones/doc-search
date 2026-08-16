---
title: "Triage attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triage-attributes.html"
content_id: "MKJtaF_a5otskVSbsxmaXw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:14.991993+00:00"
---

# Triage attributes

A Coverity administrator (or user with proper permissions) must create and configure the custom
triage attributes known as CVSS attributes before the CVSS Report Generator is run. Once
the CVSS attributes have been configured, the `cov-generate-cvss-report
--scores` command syntax updates the attribute values according to the
CWE-CVSS metric mappings in the
config/Master_CWE_CVSS_Base_Score_Mapping-v1.json file or
<security-profile-file>.json file.

Note: To create custom triage attributes, open the **Configuration -
Attributes** dialog box in the Coverity Connect GUI using the Configuration > Attributes menu option.

These are the CVSS attributes you must create:

## CVSS_Audited

`<CVSS_Audited>` is a pick list type attribute. This attribute controls
whether or not the <CVSS_Vector> value is updated when a report is generated.

These are the possible values:

- `No` – The `<CVSS_Vector>` value is
  automatically updated when a report is generated. This should be the default
  value.
- `Yes` – The `<CVSS_Vector>` value is not
  updated when a report is generated.

After generating a report and reviewing `<CVSS_Vector>`, the
reviewer can set `<CVSS_Audited>` to `Yes`, which
prevents the value in `<CVSS_Vector>` from being updated
automatically by any subsequent report generation. The reviewer can update the value
in `<CVSS_Vector>` manually, if desired.

## CVSS_Score

`<CVSS_Score>` is a text type attribute. This attribute's value is computed
from `<CVSS_Vector>`. There is no default value. The CVSS score
generator sets this attribute at each run.

## CVSS_Severity

`<CVSS_Severity>` is a pick list type attribute. This attribute's value is
computed from `<CVSS_Score>`.

`<CVSS_Severity>` has five possible values:
`Critical`, `High`, `Medium`,
`Low`, and `None`. There is no default value. The
CVSS score generator sets this attribute at each run.

## CVSS_Vector

`<CVSS_Vector>` is a text type attribute. This attribute's value drives all
of the other computations and is calculated using static analysis data. There is no
default value. The report generator sets this attribute at each run (unless
`<CVSS_Audited>` is set to Yes). You can manually edit the
value if the CVSS vector needs to be adjusted.
