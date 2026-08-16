---
title: "Associating a license term to a license"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/associating-a-license-term-to-a-license.html"
content_id: "8J0SNWnmPvKfu5fwJE6h4Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:52.120999+00:00"
---

# Associating a license term to a license

You can associate a new license term you created or an existing KnowledgeBase term to one
or more custom or KnowledgeBase licenses.

When a license term is associated to a license, that term will appear to users when
viewing licenses terms, for example, in the BOM.

Only users with the License Manager role can associate a license term to a license.

You can associate a term to a license when:

- Creating a license term. Click here for more information about creating a new term.
- Using the **License Terms** tab which lists all license terms:

    
   [image: License Terms tab]
- Using the **License Terms** tab for an individual license:

    
   [image: License Name - License Terms tab]

To associate a license term to one or more licenses:

Use these procedures to associate a license term to one or more licenses.

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: image]
3. Click [image: image] in the row of the
   license term and select **License Association**.

   The License Association dialog box appears.

     
    [image: License Association dialog box]
4. Use this dialog box to associate the term. To add a license: Begin typing the
   license name that you want to associate to this term. The list is type-ahead
   enabled, so you can see a list of available licenses that contain the text you
   have typed. Select the license and click **Add**.

   Enter additional license names to associate the term with additional
   licenses.
5. Optionally, select the licenses for which this term requires fulfillment:
   1. Select the check box next to the license where fulfillment of this term
      is required.
   2. Click **Require Fulfillment**. The Fulfillment Required icon ( [image: Term Fulfillment Required icon] ) appears in the table for the license where this term is
      required.

      Click **Remove Fulfillment Requirement** to remove
      the requirement that this term must be fulfilled.
6. Click **Close**.

To associate an existing license term to a specific license:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

     
    [image: License Management page]
3. In the **Licenses** tab, select the license name to display the *License
   Name*
   **Settings** tab.

     
    [image: image]
4. Select the **License Terms** tab to view the terms associated with this
   tab.

     
    [image: image]
5. Click **Add Term** to open the Add Term dialog box.
6. Select **Existing** to add an existing license term.

     
    [image: Add Term dialog box]
7. Begin typing the license name that you want to associate to this term. The list
   is type-ahead enabled, so you can see a list of available license terms that
   contain the text you have typed. This list displays all license terms – custom
   and KnowledgeBase terms.
8. Select the license term. The information for this term appears in the dialog
   box.
9. Optionally, select whether fulfillment is required for this term.
10. Click **Add**. The **License Terms** tab appears for this license with the
    new term added. The Fulfillment Required icon ( [image: Term Fulfillment Required icon] ) will appear for any required terms.
