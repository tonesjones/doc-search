---
title: "About license families"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-license-families.html"
content_id: "3Y8~bnPUmTSAJxsa9kww2w"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:26.894514+00:00"
---

# About license families

The use of open source software is managed through licenses that allow the software to be
utilized, modified, and/or shared under defined terms and conditions. The conditions
regarding the reuse of open source software can vary from things you can do (rights),
things you cannot do (restrictions) and things you must do (obligations) in order to
comply with the license. Black Duck tracks over 2,900 open sources
licenses that can range from those with few restrictions and obligations to those with
many restrictions and obligations.

Depending upon the nature of these restrictions and obligations, some licenses are deemed
to be riskier than others, as they require more management and care to ensure compliance
with the license terms. Typically, the riskiest licenses are those that are reciprocal
in nature. Reciprocal licenses, often pejoratively called “Viral Licenses”, are those in
which the license terms can extend beyond the open source code itself and can try to
apply to other code as well. The other code could be modifications to the open source,
or even simply code that uses the open source code in a way that triggers the reciprocal
nature of the licenses. Once triggered, it is possible that in order to be in compliance
to the license, developers who create software applications may need to treat the entire
application as under the open source license and comply with all these obligations for
the entire application. This could include the obligation to provide all the source code
for the application (not just the open source) and allowing people who receive the
application to modify and redistribute it without restrictions. This may be in conflict
with a proprietary license model.

Please note, the legal aspects of managing open source licenses can be complicated and
often it is best to seek legal counsel when making decisions about open source licenses
and creating policies regarding their use. Legal counsel can best help determine if the
license rights, restrictions, and obligations apply in a particular scenario. However,
in order to help customers manage these risks in a simple and effective way, Black Duck categorizes open source licenses into license families for
purposes of risk calculations and the definition of open source policy rules. These
families range from those that are highly reciprocal to those with few obligations and
restrictions. These license families, called KnowledgeBase licenses are:

- Restrictive Third Party Proprietary

  Licenses in the Restrictive Third Party Proprietary family are for the licenses
  which cover other company’s commercial proprietary code. Typically Restrictive
  Third Party Proprietary licenses have restrictions on the use of the code and
  can be risky.
- Permissive

  Permissive Licenses tend to not place restrictions on the use of the open source
  code and generally have few obligations. Companies, for the most part, view
  these licenses as easy to manage and non-risky.
- Reciprocal

  Reciprocal licenses are those in which the license terms can easily apply to the
  overall body of work (like the AGPL) depending upon how it is used. However,
  typically the reciprocal nature of the license is triggered by distribution.
  Therefore, companies who distribute software in some fashion are generally
  concerned with highly managing software under these types of licenses.
- Internal Proprietary

  Licenses in the Internal Proprietary family are typically for your licenses which
  are used to cover your company-owned proprietary software. Licenses in this
  family tend to not place restrictions on your use of the code and are generally
  not very risky when you use code with licenses in this family.
- Unknown

  In this case, Black Duck was unable to determine the license
  for a component. Additional review should be done to determine the license for
  this component.
- Weak Reciprocal

  Licenses in this family can be reciprocal, but they are intended for open source
  software that is expected to be combined with other software under other
  licenses and therefore they tend to have a smaller reach. In this case,
  depending upon how the software is used, the reciprocal nature may simply cover
  modifications to the OSS and do not necessarily apply to the whole body of work.
  Companies who distribute software generally need to be keenly aware of these
  licenses, but tend to allow usage of components under these licenses with
  guidelines as to how they can be used. Staying in compliance and not triggering
  the reciprocity of the license tends to be easier.
- AGPL (Affero General Public License)

  Licenses in the AGPL family tend to be highly reciprocal. The reciprocity can be
  easily triggered depending upon how the component is incorporated into the
  overall body of work and how much the original work is based upon the open
  source code. In addition, the obligations can apply when software is exposed
  over a network (for example, the internet). Companies who distribute software
  applications (either on a device or as media/downloads) or create software as a
  service (SaaS) applications need to pay particular attention to software under
  these licenses in order to ensure compliance.

The following table shows the license family for the top 20 open source licenses used in
open source projects:

| License Family | Examples |
| --- | --- |
| Affero General Public License (AGPL) | - GNU Affero General Public License v3 or later |
| Reciprocal | - GNU General Public License (GPL) 2.0 or 3.0 - Sun GPL with Classpath Exception v2.0 |
| Weak Reciprocal | - Code Project Open License 1.02 - Common Development and Distribution License (CDDL) 1.0 or   1.1 - Eclipse Public License - GNU Lesser General Public License (LGPL) 2.1 or 3.0 - Microsoft Reciprocal License - Mozilla Public License |
| Permissive | - Apache 2.0 - Artistic License - BSD License 2.0 (2-clause Simplified, 3-clause, New, or   Revised) - Do What The F*ck You Want To Public License - ISC License - Microsoft Public License - MIT License - Zlib-Libpng License |
| Unknown | N/A |

## Managing license families

Users with the License Manager role
can use the License Families page to manage their license families. From this page
you can view the KnowledgeBase license families or create custom license
families.

To view the License Families page:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] → **Licenses Families**.

     
    [image: License Families tab]   

   The table contains the following information:

   - **License Family**. The name of the license family category.
   - **Source**. The source for this license. Possible values are:

     - KnowledgeBase. From Black Duck KnowledgeBase.
     - Custom. Custom license family.
   - **Last Updated**. The date that the license family was created or last updated and the
     username of the user who created or last updated this license
     family.

   Use the **License Family Source** filter to limit the information shown on this page.
   Filter options are Custom or KnowledgeBase.
3. Click the desired license family. This will open a modal displaying the following
   information:

     
    [image: License Family modal]   
   - **License family category**. The description for this license
     family. Categories include Restrictive Third Party Proprietary,
     Permissive, Reciprocal, Internal Proprietary, Unknown, Weak
     Reciprocal, AGPL.
   - **Risk Profile**. The license risk as determined by the component usage and its
     distribution.
