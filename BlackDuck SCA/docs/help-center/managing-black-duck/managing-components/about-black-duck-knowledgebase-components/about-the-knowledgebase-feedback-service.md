---
title: "About the KnowledgeBase Feedback Service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-the-knowledgebase-feedback-service.html"
content_id: "8UEQAmwPo8glDeWbji2~bg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:19.667660+00:00"
---

# About the KnowledgeBase Feedback Service

The KnowledgeBase Feedback Service allows users to submit feedback on component and
vulnerability data in Black Duck, helping to improve the accuracy
of the Black Duck KnowledgeBase (KB). Feedback is sent when specific adjustments are
made to components or matches identified by the KB.

When feedback is sent:

- **Component adjustments**: Feedback is submitted when the component itself is adjusted or
  when a component's license is modified. Other component adjustments do not
  trigger feedback submission. Other component adjustments do not trigger feedback
  submission.
- **File adjustments**: Feedback is sent only when the component matched to a specific file
  is changed.
- **BOM adjustments**: Feedback is also triggered when making adjustments to a component,
  version, origin, origin ID, or license for a match made by the KB.
- **Unmatched files**: If you manually identify an unmatched file to a component, feedback
  is sent. However, feedback is not sent for manually added components that do not
  have associated files.

Note: No customer-identifiable information is transmitted to the KB.
