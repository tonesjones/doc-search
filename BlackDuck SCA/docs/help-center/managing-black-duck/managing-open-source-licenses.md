---
title: "Managing open source licenses"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-open-source-licenses.html"
content_id: "4pdr8gzllQYMeXwm2el55Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:25.678508+00:00"
---

# Managing open source licenses

[HUB-7046]The use of open source
software (OSS) is managed through licenses that allow you to use, modify, and/or share
the software under defined terms and conditions. The conditions regarding the reuse of
open source software can vary from things you can do (rights), things you cannot do
(restrictions) and things you must do (obligations) in order to comply with the
license.

Best practices for the redistribution of open source software include identifying all OSS
content in the distribution and ensuring compliance to licensing obligations. Virtually
all open source licenses contain an attribution clause as part of the licensing
obligation. The attribution clause requires that the source of the software, and
generally the copyright holder, be identified. Compliance with the attribution clause of
these licenses generally takes the form of an attribution document, sometimes called a
Notices File, which lists all OSS and the appropriate copyright and license
information.

With Black Duck, you can create accurate and compliant open source
notice file reports at a project/release level. Black Duck
provides the actual license text for the MIT, variants of the BSD, and the ISC licenses,
which are the top components in our KnowledgeBase, based upon customer usage.

For example, the following is an HTML version of the Notices File report from Black Duck:

  
 [image: HTML version of the Notices File report]   

You can edit and maintain the data needed to create this report. The notice files can
then be included with the distribution or incorporated into documentation to satisfy the
attribution obligation.

## Suggested work flow

To manage component licenses using Black Duck:

1. With the assistance of your legal counsel, determine the best combination of
   licenses for your company’s work. This planning work can help you determine
   whether you need to make changes to a BOM to bring a project into
   compliance.
2. Use the License Management
   page to view licenses currently used by your company and existing
   license families.
   - If a component uses a license that is not available from Black Duck KnowledgeBase, users with the License Manager role can
     create custom licenses or edit KnowledgeBase
     licenses.
   - If a license family does not accurately reflect your license risk,
     users with the License Manager role can create custom license families.
   - If a license term does not accurately reflect a license obligation,
     users with the License Manager role can manage license
     terms of their custom or KnowledgeBase licenses.
3. Create policy
   rules that trigger violations when components do not comply with
   your license policies.
4. Review the BOM for any license policy violations and determine what to do
   with components that are in violation of a rule.
5. Determine whether you want to enable deep license
   data.
6. Review the BOM for license accuracy:
   - Research components that have Unknown License or License Not Found
     values.
   - Review components that have license
     risk. Confirm that the usage of the component is correct as the combination of
     project distribution, usage, and license determines the license
     risk.
   - For components that have disjunction (OR) licenses, investigate and
     decide which license you plan to use.
7. Review copyright
   statements and/or review detected copyright statements. Optionally edit the Black Duck
   KnowledgeBase copyright statements and/or create custom copyright
   statements.
8. Create the Notices File report. Optionally, make these modifications to the
   report contents:
   - Determine if any components or subprojects should be excluded from the report.
   - Add attribution statements.
   - Edit
     the license text if necessary.
