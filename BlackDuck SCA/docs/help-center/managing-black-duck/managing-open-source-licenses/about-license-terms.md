---
title: "About license terms"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-license-terms.html"
content_id: "QdA_DH47IWi3HLsOqFjb8Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:45.611986+00:00"
---

# About license terms

License terms are the provisions in the license which grant rights or impose restrictions
on the use of the software under that license. They summarize the conditions regarding
the reuse of software that is contained in the text of the license. They indicate the
things you can do (permitted), the things you cannot do (forbidden) and the things you
must do (required) to comply with the license. Please note that the license terms
provide by the Black Duck application are just general summaries of the license and
cannot be taken as legal advice.

You can create custom license terms and manage existing KnowledgeBase license terms to
ensure that you meet the legal obligations associated with a license. Manage license
terms to help your developers know the legal obligations associated with a license and
to help you bring a project into compliance with licensing obligations.

Users with the License Manager role
can:

- Create, edit, or delete custom license
  terms.
- Associate a custom or KnowledgeBase license term to one or more
  custom or KnowledgeBase licenses.
- Remove custom license
  terms from custom or KnowledgeBase licenses.
- Remove KnowledgeBase
  license terms from custom licenses or KnowledgeBase licenses that were not
  originally defined by Black Duck KnowledgeBase.
- Deprecate custom license terms.
- Disable or restore KnowledgeBase
  license terms for a KnowledgeBase license.
- Determine if the license term requires
  fulfillment.

## Suggested work flow

To manage custom and KnowledgeBase license terms:

1. With the assistance of your legal counsel, review the license terms
   associated with Black Duck KnowledgeBase licenses. However, please note that
   not all licenses will have pre-defined license terms and not every condition
   of use may be represented by Black Duck-provided license terms. The license
   terms provided by the Black Duck application are just general summaries of
   the license and cannot be taken as legal advice or replace a legal
   review.
2. Determine if there are any Black Duck KnowledgeBase terms that need to be
   modified to more accurately reflect your legal obligations.
   - You can disable KnowledgeBase terms associated with Black Duck
     KnowledgeBase licenses so that these terms are not shown to your end
     users.
   - Optionally, you can create new custom terms and then associate them
     to KnowledgeBase licenses either in addition or replacing an
     existing KnowledgeBase term.
3. If you created custom licenses, determine if you need to create new custom
   license terms or associate existing KnowledgeBase terms to the custom
   license.
4. Continue the review process, as you may wish to eventually deprecate a custom
   license term or remove a KnowledgeBase term.

## License terms process

If, after reviewing the existing terms, you determine that you need to create new
license terms, do the following:

1. Create
   categories to manage your license terms. Categories are used to
   manage your license terms.

   You can also create a category while creating a license term.
2. Create a custom license
   term.
3. Associate the new term to one or more licenses.

The **License Terms** tab shows all license terms for custom and KnowledgeBase
licenses.

To view the License Terms tab:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **Licenses**.

   The License Management page appears.

     
    [image: License Management page]
3. Select the **License Terms** tab.

     
    [image: License Terms tab]   

   The table provides the following information:

| Column | Description |
| --- | --- |
| **Term** | Term name.  Hover over the name to view the description for this term.  For custom license terms, select the name to open the Edit a License Term dialog box. |
| **Source** | The source for this term. Possible values are:   - KnowledgeBase. This is a standard term from Black Duck KnowledgeBase. - Custom. A license term you created. |
| **Responsibility** | Responsibility for this license term. Possible values are:   - Permitted - Forbidden - Required |
| **Category** | Category for this license term.  License terms from Black Duck KnowledgeBase have **KnowledgeBase** as the category. Custom license terms list the category defined when adding the term. |
| **Last Updated** | Date that the license term was last updated and the username of the user who updated this term.  The column lists **Never** for KnowledgeBase license terms. |
