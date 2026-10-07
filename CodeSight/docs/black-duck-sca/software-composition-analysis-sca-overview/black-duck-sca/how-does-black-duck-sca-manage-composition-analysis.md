---
title: "How does Black Duck SCA manage composition analysis?"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/how-does-black-duck-sca-manage-composition-analysis-.html"
content_id: "3jXtooOVif6W1T5SQAgeAw"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.629662+00:00"
---

# How does Black Duck SCA manage composition analysis?

Black Duck SCA analyzes source code by comparing its components to a database
of open-source software that tracks known issues.

As performed by Black Duck, the analysis involves the following steps:

1. Run Rapid Scan Static (also known as Detect) to scan the current code base and obtain components from the package manager configuration files in the project.
2. Check these components against the KnowledgeBase, on the Black Duck server,
   to learn of security vulnerabilities, policy family,
   and other metadata: This information helps to understand the nature of the component.
3. Recommend ways to mitigate certain vulnerabilities;
   for example, upgrading the version of a component that is out of date.

The following illustration shows an overview of this process:

Figure 1. Software Composition Analysis with Black Duck
  
 [image: Black Duck scanning overview]
