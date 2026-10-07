---
title: "Defining conflicts for customer license terms"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/defining-conflicts-for-customer-license-terms.html"
content_id: "sYJ3gGUdzn617ZdEOClzew"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:17.336093+00:00"
content_hash: "cceb060806b7a047e31cfb61c93d89e29b517c25c0544468d6ae7ade45b98a4f"
---

# Defining conflicts for customer license terms

Black Duck has identified those KnowledgeBase license terms that are in conflict with other KnowledgeBase terms that have the same name but opposing responsibilities.

You can define the custom license terms for forbidden or required actions that are in conflict with Black Duck KnowledgeBase terms or with your custom license terms.

## Defining an incompatible term

You can define incompatible terms for your custom license terms with a forbidden or required responsibility, including deprecated custom license terms.

- A required license term can only be defined as incompatible to a forbidden license term.
- A forbidden license term can only be defined as incompatible to a required license term.

You cannot define incompatible terms for:

- Black Duck KnowledgeBase license terms
- Custom license terms with a permitted responsibility

To define an incompatible term:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: image]
3. Click [image: image] in the row of the custom license term and select **Incompatible Terms** to open the Incompatible Terms dialog box.

     
    [image: Incompatible Terms Dialog Box]
4. Type the incompatible license term name in the **Select Terms** field.

   Black Duck displays a list of terms that have the opposite responsibility as possible incompatible license terms; for example if you are defining conflicts for a forbidden license term, only required terms appear in the list.

   Select a term and click **Add**.
5. Optionally, repeat step 4 to add additional incompatible license terms.
6. Click **Close**.

## Viewing incompatible terms

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: image]
3. Click [image: image] in the row of the license term and select **Incompatible Terms** to open the Incompatible Terms dialog box which lists the incompatible terms for this license term.

     
    [image: Incompatible Terms Dialog Box]   

   Note that if a Black Duck KnowledgeBase license term does not have any incompatible license terms, the **Incompatible Terms** option is not available.

Tip: Use the **Has Incompatible Term(s)** filter to easily view all those license terms for which incompatible terms have been identified.

## Deleting incompatible license terms

You cannot delete incompatible terms defined for Black Duck KnowledgeBase license terms. You can only delete incompatible terms that you have defined for your custom license terms.

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

   Select the **License Terms** tab to display all license terms.

     
    [image: image]
3. Click [image: image] in the row of the custom license term and select **Incompatible Terms** to open the Incompatible Terms dialog box.

     
    [image: Incompatible Terms Dialog Box]
4. Click [image: Delete Icon] in the row of the custom term that you want to remove.
5. Click **Remove** to confirm.
