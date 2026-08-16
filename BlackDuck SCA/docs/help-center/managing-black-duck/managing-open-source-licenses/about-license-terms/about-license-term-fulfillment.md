---
title: "About license term fulfillment"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-license-term-fulfillment.html"
content_id: "qfKHLbzfCBuTW9Qx0QAiXg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:47.153939+00:00"
---

# About license term fulfillment

License Managers can define which license terms require fulfillment.

The fulfillment status of a license term is defined for a term at the license level, as
not all instances of a license term may require fulfillment. This allows you to easily
define the fulfillment requirements for a license term,

The work flow for license term fulfillment is:

1. License Managers determine the license terms that require fulfillment. Fulfillment
   can be defined when:
   - Associating a license term.
   - Viewing all terms for a specific license.
   - Creating a new term or adding an existing term for a specific
     license when using the *License Name*
     **License Terms** tab.
2. The System Administrator enables the
   *Project Version's*
   **Legal** tab.
3. BOM Manager's use the **Term Fulfillment** tab on the *Project Version's*
   **Legal** tab to view all license terms that require fulfillment and indicate which license terms are fulfilled.

Note the following:

- It may take time for license term fulfillment requirements to appear on the
  **Legal** tab.
- Policy managers can create a policy rule that will trigger a violation when there are
  unfulfilled license terms.

  Note that the **Term Fulfillment** tab on the **Legal** tab must be enabled
  so that a user can indicate that a term is fulfilled. If the **Legal** tab is
  disabled, which is the default setting, a user will be unable to indicate that a
  term is fulfilled, and policy violations cannot be cleared.
- License term fulfillment status can be cloned.
- A new project version report,
  `license_term_fulfillment_date_time.csv` lists the
  license terms and fulfillment status for a project version.
