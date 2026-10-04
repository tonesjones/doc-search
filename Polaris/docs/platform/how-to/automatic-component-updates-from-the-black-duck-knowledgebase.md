---
title: "Automatic component updates from the Black Duck KnowledgeBase"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/automatic-component-updates-from-the-black-duck-knowledgebase.html"
content_id: "FyxpH9tDc4qhH0qWsBtbZA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.138549+00:00"
content_hash: "d30e82803e9afe999ba7ec5e4f3e26998d863b925f58af1f1f97e5092703df09"
---

# Automatic component updates from the Black Duck KnowledgeBase

Certain changes to components in the Black Duck KnowledgeBase™ are automatically synchronized with Polaris. These include:

- The issues associated with a component origin change in the KnowledgeBase. These include:
  - New issues are added to a component origin, or issues are removed from a component origin.
  - An issue's vulnerability score changes.
  - An issue's severity changes.
  - An issue's CISA KEV status changes.
  - An issue's upgrade guidance changes.
- A component's security risk changes in the KnowledgeBase.
- A component, component version, or component origin's metadata changes in the KnowledgeBase. This includes license definitions, license terms, license metadata, and other component metadata.
- A component, component version, or component origin is deleted in the KnowledgeBase.
- A component or component version is migrated (that is, the unique ID for a component or component version changes) in the KnowledgeBase.

  Tip: In the Issue Details panel, an Out of date tag appears when you open an issue linked to a migrated component or component version. We recommend you run a new SCA test when this appears.

Note: Changes in the KnowledgeBase are synchronized with Polaris every 3 hours, and each time you run an SCA test. Risk scores, and the quantity of issue and component policy violations may change when this occurs.

To view issues that were added to a project as a result of automatic synchronization, open a completed test's results and use the Found post-test filter. For more information, see [Find issues captured after a test](find-issues-captured-after-a-test.md).

## Reports, dashboards, and notifications

It can take up to 60 minutes for changes (resulting from automatic synchronization with the KnowledgeBase) to appear in reports and dashboards, and for email notifications about critical and high vulnerabilities to be sent.

Note: For more information about vulnerability notification emails, see [Vulnerability notifications](vulnerability-notifications.md).
