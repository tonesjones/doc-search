---
title: "Deviations in reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deviations-in-reports.html"
content_id: "ZmyLhtXSScT40AFHusb_mw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:52.325287+00:00"
---

# Deviations in reports

Attention:
The information in this section applies only to CERT, Hyundai, and MISRA reports.

Reports for these standards indicate the number of deviations and can provide details about the indicated deviations.

However, the count of deviations *only includes issues categorized (triaged) as "Intentional"* within
Coverity Connect.

Figure 1. Deviations count (highlighted) in a Hyundai report
  
 [image: Hyundai compliance report showing count of deviations]

Figure 2. Deviations count (highlighted) in a MISRA report
  
 [image: MISRA compliance report showing count of deviations]

Issues that have been triaged via the compliance configuration file, or via a pragma in C/C++ source code,
*are not included* in reports.

## Using `"deviation"` in a coding standard file

In a coding standard file, you can use the `"deviation"` field to specify a deviation
for a particular rule ID.
For example:

```
"deviation": "Directive 4.15"
```

... or:

```
"deviation": "MC-ARR-002"
```

As previously mentioned, the count of deviations does not include deviations created this way.
On the other hand, the *existence* of such a deviation is mentioned.

Figure 3. Mention of a deviation (highlighted) in a MISRA report
  
 [image: MISRA compliance report that mentions a deviation]

If your compliance configuration file provides a `"reason"` field along with the
`"deviation"` field, this text appears in the report.
For example:

```
"deviation": "MC-ARR-001"
"reason": "This rule is currently disabled in the analysis configuration."
```

Figure 4. Deviation (highlighted) with "reason" text in a Hyundai report
  
 [image: MISRA compliance report that mentions both a deviation and the reaso for it]
