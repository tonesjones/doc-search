---
title: "Restoring the original text and family of a KnowledgeBase license"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/restoring-the-original-text-and-family-of-a-knowledgebase-license.html"
content_id: "f0aZR5KiWsa7iF0u5Lf66A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:01.604290+00:00"
---

# Restoring the original text and family of a KnowledgeBase license

If a user with the License Manager role has modified the text or license family of a
KnowledgeBase license, they can restore that license to its original values, as defined
by the Black Duck KnowledgeBase.

To restore a KnowledgeBase license:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

     
    [image: License Management page]
3. Do one of the following:
   - Click [image: Down arrow] and select **Restore**  in the row of the KnowledgeBase
     license that you want to restore to display the Restore KnowledgeBase
     License dialog box.
   - Select the KnowledgeBase license name to display the *License Name*
     **Settings** tab. In the **Restore KnowledgeBase License**
     section, click **Restore original**.
4. Click **Restore** in the Restore KnowledgeBase License dialog box.

   In the License Management page, the source for this license reverts to
   **KnowledgeBase**.

   - If the license family or text were the only changes made to the license
     (as defined on the **Settings** tab), the values in the **Last
     Updated** and **User** columns are removed.
   - If additional changes were made (as defined on the **Settings** tab),
     the values in the **Last Updated** and **User** columns displays
     the date and username when the last of these changes occurred.

Note: This procedure does not restore the KnowledgeBase *license terms* to their original
values. Click here for
more information on restoring KnowledgeBase license terms.
