---
title: "Edit and review licenses"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/edit-and-review-licenses.html"
content_id: "A06KJcW6t3lPr1Dn4tAYqA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:44.902459+00:00"
content_hash: "e682bed73c43e3e8870b50781c1ea00507d09b4f6d8ba4a6474e0e05128d5064"
---

# Edit and review licenses

The License Manager allows you to view all the licenses in your portfolio plus all licenses available in the Black Duck KnowledgeBase. This allows the legal team to proactively take action on licenses, even if they are not currently used within the organization. Organization Admins can select from a license and edit specific fields in the license record to align it with their organization’s classification and review process.

- While these updates can be viewed on the Licenses tab (Portfolio > open an application > open a project > Licenses), they cannot be edited there.
- Updates to License Family and Status can also be filtered by/viewed/printed via Dashboards > Table - License Search.
- You can create component policies to monitor declared license family and license status.

The following fields can be edited on a license record:

| **Field** | **Description** | **Required (but does not need to be updated)** |
| --- | --- | --- |
| License Family | Assign the license to a family grouping | Yes |
| License Status | Set the review status for this license (see table below) | No |
| Notes | Add internal notes for your organization | No |
| Expiration Date | Record an expiration date (informational only) | No |
| License Text | Provide or update the full license text | Yes |

Note: License Family and License Text are required fields and must be set before saving. Expiration Date is informational only and does not automatically change the license status.

The License Status field supports the following values:

| **Status** | **Meaning** |
| --- | --- |
| Unreviewed | Default status. License has not yet been reviewed by the organization. |
| In Review | License is currently being evaluated. |
| Reviewed | License has been reviewed but no approval decision has been recorded. |
| Approved | License is approved for use within the organization. |
| Limited Approval | License is approved for use under specific conditions. |
| Rejected | License is not approved for use in the organization. |
| Deprecated | License is no longer in active use or has been superseded. |

1. Go to **Licenses** tab in the main navigation.
2. Click on a license name.
3. From the Details tab, click Edit license button. 

   Note: You need Organization Admin permission to edit.
4. Update as needed.
5. Select Save.

   Alternatively, you can select Reset to KnowledgeBase to restore a license's default values.
