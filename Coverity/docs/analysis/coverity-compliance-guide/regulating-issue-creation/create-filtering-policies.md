---
title: "Create filtering policies"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-filtering-policies.html"
content_id: "SOQbPRmYN0yV8wlTEt5nfQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:44.914791+00:00"
---

# Create filtering policies

After analyzing the findings report and deciding on the filtering policies you want, it's
time to put them in place:

1. Open the findings report containing the priority filter you want to use.
2. Display the Priority Filter tab of the findings report
   spreadsheet and input your filtering policies using the following description as
   a guide.

   The Priority Filter tab groups rows into three functional
   sections:

   - Threshold Score – This row defines the threshold
     score for scoring policies.
   - Scoring Policies – Each row in this section
     defines a scoring policy. Findings that match the specified Path and
     Compliance patterns and fall below the threshold score will be excluded.
     Those that match the patterns and meet the threshold will be scored as
     indicated by the Score column.
   - Blocking Policies – Each row in this section
     defines a blocking policy. Findings that match the specified Path and
     Compliance patterns will be excluded.

   Inputting Path patterns is straight forward, but inputting Compliance patterns is
   more complicated because patterns for internal nodes (or clades) and patterns
   for leaf nodes (or taxa) use a different syntax. There are also some syntactical
   differences that depend on the particular publication. The following table
   provides examples of internal-node and leaf-node Compliance patterns for each
   supported publication:

   Table 1. Example Compliance patterns

   | Description | Example compliance pattern |
   | --- | --- |
   | Leaf node for MISRA C 2004 rule | `MISRA C-2004 Rule 2.4` |
   | Internal node for MISRA C 2004 group of rules | `MISRA/C 2004/2` |
   | Leaf node for MISRA C 2004 directive | MISRA C 2004 does not specify directives. |
   | Internal node for MISRA C 2004 group of directives | MISRA C 2004 does not specify directives. |
   | Leaf node for MISRA C 2012 rule | `MISRA C-2012 Rule 1.1` |
   | Internal node for MISRA C 2012 group of rules | `MISRA/C 2012/Rule/1` |
   | Leaf node for MISRA C 2012 directive | `MISRA C-2012 Directive 4.6` |
   | Internal node for MISRA C 2012 group of directives | `MISRA/C 2012/Directive/3` |
   | Leaf node for MISRA C++ 2008 rule | `MISRA C++-2008 Rule 3-1-1` |
   | Internal node for MISRA C++ 2008 group of rules | `MISRA/C++ 2008/3/1` |
   | Leaf node for MISRA C++ 2008 directive | MISRA C++ 2008 does not specify directives. |
   | Internal node for MISRA C++ 2008 group of directives | MISRA C++ 2008 does not specify directives. |
   | Leaf node for AUTOSAR C++ 14 rule | `AUTOSAR C++14 A27-0-4` |
   | Internal node for AUTOSAR C++ 14 group of rules | `AUTOSAR/C++14/A/0` |
   | Leaf node for CERT C rule | `CERT CON30-C` |
   | Internal node for CERT C group of rules | `CERT/C/ARR` |
   | Leaf node for CERT C++ rule | `CERT FIO51-CPP` |
   | Internal node for CERT C++ group of rules | `CERT/C++` |

Note: Policy matching order of preference is as follows:

1. Findings are first compared for a match against blocking policies. Findings
   that match any blocking policy are excluded.
2. Findings that do not match any blocking policy are then compared against
   scoring policies in the order in which the policies are listed, from top to
   bottom.
3. Findings are scored by the first matching scoring policy.
