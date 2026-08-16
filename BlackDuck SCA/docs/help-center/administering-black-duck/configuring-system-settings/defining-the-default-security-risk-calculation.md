---
title: "Defining the default security risk calculation"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/defining-the-default-security-risk-calculation.html"
content_id: "PnKy1IF3bs8QPLOu5T7iOw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:05.570997+00:00"
---

# Defining the default security risk calculation

Users with the system administrator role can update the preferred security ranking by selecting
from the CVSS versions and source options below. These rankings will be used to
determine and calculate risk in each of your projects.

To configure the default security risk calculation:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Click **Security Risk Ranking**.
5. Select the desired **CVSS Version** to assess the risk scores within your projects.

   By default Black Duck defines security risk initially using CVSS v4.x
   scores.

   For more information on the Common Vulnerability Scoring System, see the [3.1](https://www.first.org/cvss/v3.1/specification-document) and [4.0](https://www.first.org/cvss/v4.0/specification-document) specification documents.
6. Select the desired **Record Type** that will be used to calculate risk categories
   within your projects.

   Black Duck uses BDSA and NVD to calculate
   risk.

   Note: You must have BDSA enabled on your product
   registration key to take advantage of this feature.
7. Click **Save**.

   A confirmation dialog box appears. Do one of the following:

   - Click **Confirm**.

     The VulnerabilitySummaryFetchJob starts once you click **Confirm**.

     Refresh the page to update the status of these jobs on this page. You can
     also view the status on the Jobs page.

     Once these jobs complete, the new security rankings appear in the Black Duck UI.
   - Click **Cancel**.

     The security risk configuration ranking returns to its previous
     order.

Note the following:

- Changing the security risk configuration will result in revised security risk
  calculations for all project version BOMs and may result in new policy
  violations. These calculations may take a *considerable amount of time* to
  complete.
- The ability to change the security risk ranking is disabled if the security risk
  configuration has been reconfigured and jobs are running to recalculate security
  risk. Once the jobs are completed, the security risk ranking can be
  reconfigured.
- If a CVE record has a related BDSA record (or vice versa), it cannot be remediated unless
  that vulnerability record type is prioritized in the Security Risk Ranking. This
  is due to the fact that the non-prioritized vulnerability record is not being
  used as a determinant and is not used to calculate security risk.
