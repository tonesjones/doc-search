---
title: "CVSS report profile"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cvss-report-profile.html"
content_id: "Klim6oz2OIcAB9vqe7T5YQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:15.637968+00:00"
---

# CVSS report profile

A CVSS Report profile contains application-specific CWE-CVSS vector mappings. It is based
on application type and is created by the security expert. Examples include web
applications, mobile applications, and embedded applications.

The CVSS Report profile should be structured like the following:

```
{
    "version"       : 1,
    "type"          : "CVSS profile",
    "AV"            : "N",
    "AC"            : "L",
    "PR"            : "L", 
    "UI"            : "N", 
    "cweMap"        : [{        
            "cwe" : 4,
            "cvssMetrics" : {
                "S" : "U",
                "C" : "N",
                "I" : "N",
                "A" : "N"
            }
        },
        {
            "cwe" : 7,
            "cvssMetrics" : {
                "S" : "U",
                "C" : "N",
                "I" : "H",
                "A" : "H"
            }
        }
    ] 
}
```

In creating your CVSS Report profile, please note the following:

- For initial validation, the `"version"` field should be set to the
  CVSS Report Generator profile version. Currently this is `1`.
  (*Do not use* the Coverity version number: This will cause an error.)

  The `"type"` field should be set to `"CVSS profile"`.

  If a user's profile contains a mismatch for these values, an error will occur causing CVSS Report Generator to quit.
- The values `"AC"`, `"AV"`, `"PR"`, and `"UI"` are independent of CWE.
  They differ based on application type.
- The `"CWEMap"` contains CWE-CVSS metric mappings.
- If a given defect has a `"cwe"` value of `"C"` and you provide `"F"`,
  a CWE-to-CVSS-vector mapping file, then the CVSS vector will be taken from:
  1. The value for `"C"` in `"F"`, or, if none, ...
  2. The value for the ancestor with the highest CVSS score of `"C"` defined in `"F"`,
     or, if none, ...
  3. The value for `"C"` in the built-in configuration (master .json file) or, if
     none, ...
  4. The value for the ancestor with the highest CVSS score of `"C"` in the
     built-in configuration, or, if none, ...
  5. A vector whose CVSS score is zero (that is, a CWE value of `0`).

Note:
These profiles do not need to cover OWASP Top 10 / SANS Top 25 CWEs, as these are
already covered in the Coverity CVSS Report.
