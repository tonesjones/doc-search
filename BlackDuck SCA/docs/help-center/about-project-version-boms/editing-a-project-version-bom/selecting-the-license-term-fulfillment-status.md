---
title: "Selecting the license term fulfillment status"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/selecting-the-license-term-fulfillment-status.html"
content_id: "0G7_GU3eDMDRXBc6vmf8gw"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:13.091565+00:00"
content_hash: "4769ac2438dccb6bb6cab9bd1dbe2942e3091b813831e03d488137b082287dd1"
---

# Selecting the license term fulfillment status

Once a License Manager user defines the required license terms, and a System Administrator enables the Term Fulfillment setting, BOM Manager users and other authorized users can indicate the fulfillment status of a license term by using the *Project Version***Legal** tab.

By default, the fulfillment status of a license term is unfulfilled.

To change the fulfillment status for a license term::

1. From a project version BOM, select the **Legal** tab, and if necessary, the **Term Fullfilment** tab, to view a list of license terms that require fulfillment.

     
    [image: Legal tab]   

   By default, the **Legal** tab is filtered to show all license terms that are not fulfilled.

   The tab displays the following information:

   | Column | Description |
   | --- | --- |
   | **Fulfillment** | Indicates fulfillment status:  - [image: Unfulfilled License Term icon] indicates this license term is not fulfilled. - [image: Fulfilled License Term icon] indicates this license term is fulfilled. |
   | **Term Name** | License term name.  Select the term to display the Term Fulfillment dialog box from which you can manage the fulfillment status for all licenses that have this term. |
   | **Responsibility** | Indicates the responsibility for this term. Possible values are Required, Forbidden, or Permitted. |
   | **Category** | Category for this license term. |
2. Select a license term to view all licenses with this license term in this BOM which require fulfillment.

   The Term Fulfillment dialog box appears.

     
    [image: Term Fulfillment dialog box]   

   This dialog box lists the component name and version, license that includes this term, and the username and date that this license term was last updated.

   - [image: Unfulfilled License Term icon] indicates this license term is not fulfilled.
   - [image: Fulfilled License Term icon] indicates this license term is fulfilled.
3. Select one or more checkboxes to denote the fulfillment status.

   To select all terms on a page, select [image: Checkbox] located at the top of the table.
4. Select **Mark as fulfilled** to indicate this license term is fulfilled or **Mark as unfulfilled** to indicate this license term is unfulfilled.
5. Click **Close**.
