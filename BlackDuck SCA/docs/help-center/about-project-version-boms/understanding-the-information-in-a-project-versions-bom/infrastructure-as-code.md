---
title: "Infrastructure as Code"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/infrastructure-as-code.html"
content_id: "4v3Zvb1cK0pBTqSvL59rNA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:29.388506+00:00"
---

# Infrastructure as Code

Infrastructure as Code (IaC) is the management and provisioning of infrastructure
(networks, virtual machines, load balancers, and connection topology) through code
or configuration files instead of through manual processes.

If your scan included Infrastructure as Code, you will see the current amount of Open
issues displayed on the right side of the Risk graphs. You can then expand the IaC
link to view the Total amount of IaC issues and Dismissed issues.

  
 [image: image]   

You can then take action on the Infrastructure as Code issues discovered in your BOM
by clicking either the Open link or the amount to the left of the Open link. This
will open a dialogue box displaying all the IaC issues.

  
 [image: image]   

From here, you can:

- Expand a row to see specific details of the nature of the issue. This
  information includes a description of the issue, the severity, the suggested
  remediation, and the code location of the issue.
- Dismiss an issue. By toggling the slider in the Dismiss column, you can mark
  an issue as dismissed. This means that you have either remediated the issue
  or have chosen to ignore it.
- Filter the list. Click the Filter button to add filters to the list. Options
  include Issue, Severity, and Status.

For more information regarding Infrastructure as Code scanning, please refer to the
[Sigma User Guide](https://docs.blackduck.com/access?ft:originId=8607ec183dfd342846fcacc96c21a4d0/393e4547639cab7b6885aabefaabb61c.topic).
