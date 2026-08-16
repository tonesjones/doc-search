---
title: "IP allowlisting on EKS with NGF"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ip-allowlisting-on-eks-with-ngf.html"
content_id: "zVlazs1iIP7pJJlKZyTe0A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:42.895661+00:00"
---

# IP allowlisting on EKS with NGF

Use `gatewayAllowedSourceRanges` or `allowedSourceRanges`
as described in the [IP Allowlisting](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1&ga=1#ip-allowlisting) section. Both require
`externalTrafficPolicy=Local` on the NGF Service and the NLB
configured in IP mode (as shown in Step 2) to preserve the original client source IP
through the load balancer.

Without `externalTrafficPolicy=Local`, the NLB performs SNAT and the NGF
pod sees the NLB node IP, not the client IP — making source IP–based allowlisting
ineffective.
