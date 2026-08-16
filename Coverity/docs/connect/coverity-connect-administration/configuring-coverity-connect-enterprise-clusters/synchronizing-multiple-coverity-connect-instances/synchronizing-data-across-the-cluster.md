---
title: "Synchronizing data across the cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synchronizing-data-across-the-cluster.html"
content_id: "ApvV2ixqlz~vc_ZOYiDfSg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:39.882007+00:00"
---

# Synchronizing data across the cluster

When a developer triages an issue through the Coordinator or through a Subscriber, the
update propagates by way of one or more Triage
Stores in the Coordinator to other members of the cluster. In this way, the
Coordinator is responsible for synchronizing triage data updates across Coverity Connect
Subscribers.

Figure 1. Example: Coverity Connect coordination
  
 [image: image]

As Figure 1 shows, a developer triages
CID 123 in Stream X of CIM1 (a Subscriber), a stream that is associated with Triage
Store 1 (TS1) on the Coordinator. After receiving notification of the change in triage
data from the Subscriber, the Coordinator updates the other Subscribers (CIM2 and CIM3).
The new triage data is synchronized for each matching issue found in TS1 streams.

Note that the triage data of the matching issue in Stream C of Project 2 (CIM 3) is not
updated because Stream C belongs to TS2, not TS1. For this reason, the Stream C issue
appears in a different color than the others in the figure.

Table 1 identifies the updates to the
triage data of CID 123 that are shown in Figure 1.

Table 1. Triage data updates

| Coverity Connect | Location | Project | Matching issues | Stream | Triage Store 1 | Data |
| --- | --- | --- | --- | --- | --- | --- |
| Subscriber CIM1 | New York | — | ✓ | X | ✓ | updated |
| Coordinator CIM | London | — | ✓ | A | ✓ | updated |
| Subscriber CIM2 | Tokyo | — | ✓ | E | ✓ | updated |
| no | F | not updated |
| Subscriber CIM3 | Bangalore | 1 | ✓ | Y | ✓ | updated |
| no | B | no | not updated |
| 2 | ✓ | Z | ✓ | updated |
| C | no | not updated |

Note: It is possible that the CIDs will not display properly on the subscriber if the
coordinator is unavailable. The CIDs will display correctly when the coordinator becomes
available again.
