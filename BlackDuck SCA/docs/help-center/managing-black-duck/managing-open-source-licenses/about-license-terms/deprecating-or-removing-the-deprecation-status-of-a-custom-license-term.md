---
title: "Deprecating or removing the deprecation status of a custom license term"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/deprecating-or-removing-the-deprecation-status-of-a-custom-license-term.html"
content_id: "khT6fo0vwBlXKjYIn7yghw"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:16.829879+00:00"
content_hash: "04f6c9a8d16062532e2807b34780ddb7623942c991d2ec503c250e710e599f44"
---

# Deprecating or removing the deprecation status of a custom license term

You can deprecate a custom license term. Deprecating a custom license term is a global action – it applies to all licenses (custom and KnowledgeBase) that have this custom license term associated to it.

A deprecated custom license term is not available for new associations to licenses and cannot be edited. Existing licenses that have the deprecated term will still display the term to users in existing or new projects/components with no indication to these users that the term is deprecated.

Only users with the License Manager role can deprecate license terms.

To deprecate a custom license term:

Use these procedures to deprecate the term for *all* licenses that have this term associated to it.

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: License Terms tab]
3. Click [image: image] in the row of the license term and select **Deprecate**.

   The Deprecate a License Term dialog box appears.
4. Click **Deprecate** to confirm.

   The date and username of the user who deprecated this term appears in the **Last Updated** column.

   The [image: Deprecated message] label appears next to the license term where the term appears in the **License Terms** tabs in License Management.

   Note that the [image: Deprecated message] label does not appear to the BOM manager for any licenses that have this term associated to it.

To undo the deprecation status of a custom license term:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: License Term tab]
3. Click [image: image] in the row of the license term and select **Remove Deprecated Status**.

   The Deprecate a License Term dialog box appears.
4. Click **Remove Deprecated Status** to confirm. The [image: Deprecated message] label is removed from the license term.
