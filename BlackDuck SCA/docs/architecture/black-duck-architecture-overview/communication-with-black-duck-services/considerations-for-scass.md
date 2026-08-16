---
title: "Considerations for SCASS"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/considerations-for-scass.html"
content_id: "geELGMjWfSegmvwK0s3Ntg"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:46.294858+00:00"
---

# Considerations for SCASS

As organizations increasingly rely on the SCA Scan Service (SCASS) hosted at
**scass.blackduck.com**, it is essential to address the security aspects of the
communication sessions involved. This section provides an overview of security
considerations, clarifications on data handling, and guidance for customers to ensure a
smooth rollout of SCASS.

## Security Concerns

In our engagement with customers, concerns were raised regarding the security of
communication sessions with the SCASS service. Key points of concern include:

- The nature of data transmitted between systems.
- The internal processing changes and their implications for security.
- Assurance that the SCASS rollout complies with the customer’s security
  protocols.

## Clarification on Data Transmission

In response to these concerns, we want to clarify the following:

- **No Changes to Data Transmission:**

  There have been no alterations to the data that is transmitted between our
  systems. The integrity and confidentiality of the data remain intact.
- **Internal Processing Changes:**

  The modifications made are solely related to how we internally process
  queries and data. These changes are backend improvements and do not impact
  the customer experience or data handling practices.
- **Exception for Binary and Container Scanning:**

  It is important to note that the only exception to this is with binary and
  container scanning features, which have not yet been rolled out. Customers
  should be aware of this when planning their usage of SCASS.

## Implementation Guidance

To facilitate a successful implementation of SCASS while addressing security
concerns, we recommend the following steps for customers:

1. **Review Security Policies:**

   Ensure that your organization's security policies align with the use of SCASS
   and that all team members are aware of the changes.
2. **Engage Security Teams:**

   Involve your security officers in reviewing the clarifications provided to
   ensure that all potential risks are assessed and addressed.
3. **Monitor Rollout Progress:**

   Keep track of the SCASS rollout and any updates regarding binary and
   container scanning features. Stay informed about any changes that may affect
   security practices.
4. **Provide Feedback:**

   Share any further concerns or feedback with your Black Duck representative to
   ensure that your security needs are met effectively.

The security of communication sessions with SCASS is of utmost importance. By
understanding the nature of the changes and taking proactive measures, customers can
confidently roll out SCASS while maintaining robust security practices. For
additional questions or support, please contact your Black Duck
representative.
