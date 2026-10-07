---
title: "Issue details: Black Duck SCA"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/issue-details-black-duck-sca.html"
content_id: "_yOy3snhN2rG_rP~S9p72g"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.685515+00:00"
---

# Issue details: Black Duck SCA

Typically, Code Sight does not display issue details until you click to highlight one of the issues in the Issues list.
When an issue is highlighted, the Issue Details display shows specific information about the issue.

## Policy violations

For Code Sight to display Black Duck SCA reports of policy violations,
the Black Duck server must be configured as follows:

- The policy rule needs to be applicable to Rapid Scan mode.
- The policy rule can be set to either All Projects or Subset of Projects.

  Code Sight does not do matching on project properties (such as names, tags, and so on) for Subset of Projects.
  Only the policy rules that specify exclusions of project properties (for example, not in) will work with Code Sight.
- The policy rule will be tested if the Component and Vulnerability conditions apply.

## SCA issues in Eclipse, IntelliJ, and Visual Studio

[image: image]
 For an issue found by Black Duck SCA, the diamond-shaped issue icon highlights the number of issues found.
This is followed by a list of open-source components that result in the issue;
the names of the security vulnerabilities detected;
the names of policy violations detected;
and then by further details such as the license used and dates and times on which the issues were detected.

Figure 1. Details panel for an SCA issue
  
 [image: Details panel for composition analysis]

(Example from IntelliJ)

Each occurrence of an issue shows an icon that indicates whether the issue is a direct (declared) dependency
or a transitive (indirect) dependency:

[image: image]  Direct dependency

[image: image]  Transitive dependency

## SCA issues in VS Code

VS Code displays SCA issues in the LOCAL VIEW in the left-hand side bar.

Figure 2. LOCAL VIEW with SCA issues in VS Code
  
 [image: VS Code display of SCA issues]

To launch a new SCA scan in VS Code, use a scan configuration.

To see the details about an issue, click its entry.
Code Sight displays the details in an Editor tab.

Figure 3. SCA issue details in VS Code editor
  
 [image: VS Code display of SCA issue details]
