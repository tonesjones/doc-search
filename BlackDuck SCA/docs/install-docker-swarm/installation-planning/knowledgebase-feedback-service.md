---
title: "KnowledgeBase Feedback Service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/knowledgebase-feedback-service.html"
content_id: "FgDrU6QPBYQMWkQz~sNbOA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:35.156269+00:00"
---

# KnowledgeBase Feedback Service

The KnowledgeBase feedback is used to enhance Black Duck KnowledgeBase (KB)
capabilities.

- Feedback is sent when you make BOM adjustments to the component, version, origin,
  origin ID, or license of a match made by the KB.
- Feedback is also sent if you identify unmatched files to a component; it is not
  sent for manually added components that do not have files associated with
  them.
- Feedback is used to improve the accuracy of future matches. This information also
  helps Black Duck to prioritize resources so that components which are important to
  our customers can be examined in more detail.

Important: No customer-identifiable information is transmitted to the KB.

## User-agent analytics

The KnowledgeBase uses originating user-agent analytics to improve the scalability of
of KnowledgeBase services and improve quality of service for users.

The additional header information increases the header size of outgoing HTTP requests
to the KnowledgeBase. It is possible that some intermediate egress proxies (customer
managed) may require reconfiguration to support the additional header size, but this
scenario is unlikely.

## Disabling the feedback service

By default, the KnowledgeBase feedback service is enabled: adjustments that you make
to a BOM are sent to the KnowledgeBase.

- You can override the feedback service by using the
  `BLACKDUCK_KBFEEDBACK_ENABLED` environment variable. A
  value of false overrides the feedback service and BOM adjustments are not
  sent to the KnowledgeBase.

- To disable the feedback service, add
  `BLACKDUCK_KBFEEDBACK_ENABLED=false` to the
  `blackduck-config.env file`.

Note: Set the value to true to re-enable the feedback service.
