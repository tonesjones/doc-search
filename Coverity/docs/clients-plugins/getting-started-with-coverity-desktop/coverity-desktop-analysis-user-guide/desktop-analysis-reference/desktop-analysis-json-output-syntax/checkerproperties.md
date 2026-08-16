---
title: "CheckerProperties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkerproperties.html"
content_id: "Y_Fg_~OWk4Sz6I8LR5KR_Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:07.168038+00:00"
---

# CheckerProperties

This object contains information that puts this defect into broad classes of related
defects according to various classification schemes, some that are industry standard,
and some that are created by Coverity. (The term "checker properties" is legacy
nomenclature.)

category: string
:   The English name of the Coverity-defined broad category into which this defect falls. It is
    refined by `subcategoryShortDescription`.

categoryDescription: string
:   This legacy attribute is the same as "category".

cweCategory: string
:   [CWE](http://cwe.mitre.org/)
    classification. It is either a CWE ID as a decimal integer, or the string
    "none".

issueKinds: [string]
:   Alphabetically sorted list of strings indicating the "kind" of issue. The valid strings
    are:

    - QUALITY

      The defect is likely to affect the perceived quality of the product that
      contains it.
    - SECURITY

      The defect may be a security vulnerability.
    - TEST

      This is a test policy violation, meaning the tests do not adequately exercise the
      associated code.

    Added in version 3.

eventSetCaptions: [string]
:   A list of descriptions for each of the event sets appearing in the top-level issue
    occurrence.

impact: string
:   Level of the potential impact of the issue. Values are `High`,
    `Medium`, `Low`, or
    `Audit`.

impactDescription: string
:   This legacy attribute is the same as "impact".

subcategoryLocalEffect: string
:   The local effect of the given subcategory.

subcategoryLongDescription: string
:   Long description of the nature of the subcategory.

    This attribute is a subset of HTML.
    Specifically, it may contain the elements "`a`",
    "`br`", "`code`",
    "`em`", and "`i`". The
    "`a`" element may contain the "`target`"
    and "`href`" attributes. All attributes are delimited by
    double-quote characters. There may be numeric entity references, both
    decimal and hexadecimal, as well as "`lt`",
    "`gt`", and "`amp`" named
    entities.

subcategoryShortDescription: string
:   This is a refinement of the "category" attribute. It corresponds to the "Type" column in
    Coverity Connect.

MISRACategory: string
:   Category for MISRA defects, one of `Advisory`, `Required`, or
    `Mandatory`. This field is optional. When not present,
    the whole field is absent, `null` is not used. (Always absent
    before version 7.)
