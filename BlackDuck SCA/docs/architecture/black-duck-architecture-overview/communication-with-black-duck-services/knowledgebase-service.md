---
title: "KnowledgeBase service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/knowledgebase-service.html"
content_id: "L20IiTdsmUIzdyrZ~DSq2Q"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:45.186836+00:00"
---

# KnowledgeBase service

Via web services, the Black Duck KB provides the Black Duck
application with the most up-to-date information about open-source software without
requiring regular updates on your Black Duck server. New
vulnerability data is added to the KB hourly; new searchable open-source components
are added daily; and new signatures for matching are added 2-3 times per week. Other
big data services are updated quarterly.

  
 [image: KnowledgeBase services]   

The signatures of your scanned code are used to match signatures of the open-source software
in the KB to identify the open-source software contained in your code. These
signatures consist of one-way, encrypted MD5 or SHA1 hashes of file system meta-data
and file content. The use of MD5/SHA-1 is purely for signature hashing and is not
used for any cryptographic purpose. These signatures (collections and hashes) are
sent by the Black Duck application to the KB service. No source or
binary code is ever sent off premises. The signatures are formatted as a JSON
document and transmitted over HTTPS connections. The scan document can send file
paths, file sizes, and some SHA-1 or clean SHA-1 signatures to the Black Duck
server. Black Duck does post-processing on this data to create additional
proprietary signatures.

Again, customer data sent to increase the accuracy of matching services is not persisted in
the KB. It is used during the BOM matching process and deleted afterwards. For those
reasons, no logs are produced during this process.

Additionally, the separation of customer data is enforced by the design of the
architecture.

Note: The KBMATCH_SENDPATH parameter has been deprecated as of 2023.4.0 and will be removed in a
future update. Black Duck users with Match as a Service (MaaS) enabled will not be
able to use this parameter. Customers wanting to continue using this option will
need to contact Black Duck support to have MaaS disabled for their Black Duck
registration keys.

The matching service is described in more detail below.

- **Match service overview**

  The client POSTs a JSON document representing a tree structure of scanned nodes,
  with a set of signatures per node to the match endpoint. The endpoint determines
  if there are any matches to those signatures. If there are, it returns a JSON
  document with the same nodes that were sent to the match service, and adds to
  the document the matches from the KB for each node.
- **URL format**

  https://<server>/kbmatch/api/v1/matches/<end-point>?authToken=< >
- **Header**

  X-BDS-AuthToken:<>
- **Request body data**

    
   [image: Request body data]
- **Response**

    
   [image: Response]   

  As can be seen from the example above, matching open-source components are returned to the
  Black Duck application using GUIDs. These GUIDs are then
  used to retrieve metadata on each of the open-source components using KB
  services for vulnerabilities, licenses, and other information.
- **KnowledgeBase feedback service**

  In the same way that signatures and hashes are sent up to the match service, occasionally
  these same pieces of information will be sent associated with a specific
  component and version. This is done in cases where users have corrected
  (“adjusted”) an identification. This “vote” is recorded absent any customer
  context whatsoever and is used simply to increase the accuracy of the matching
  capability. It is in our customers' best interest to share this data as it helps
  improve the overall quality for the KB. However, if it is desired to not share
  this data, please refer to the section “Disabling the Black Duck KnowledgeBase
  feedback service” in the Black Duck installation guide.
