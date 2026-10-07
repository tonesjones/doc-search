---
title: "Issue details: Coverity (SAST)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/issue-details-coverity-sast-.html"
content_id: "8k6peOcEUwWojPin~4tJwA"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.839863+00:00"
---

# Issue details: Coverity (SAST)

Typically, Code Sight does not display issue details until you click to highlight one of the issues in the Issues list.
When an issue is highlighted, the Issue Details display shows specific information about the issue.

Figure 1. Issue Details
  
 [image: Issue Details]

For an issue found by Coverity (SAST), the detailed information includes
a link to locate the issue in the source code, along with links to related issues.
The Details view includes the name of the checker that detected the issue.
If the issue was a coding-standard violation, the Details view and the editor display the
number of the rule that was violated.

Figure 2. Coding-standard issue in the VS Code editor
  
 [image: Message in VS Code editor shows the number of a coding-standard violation]

The Details view can also include suggestions as to how you might correct the source.

## Issue ID values

If you are running scans while synchronized with a server, the Issue ID
displays a Coverity ID (a CID), or a Coverity on Polaris ID.
If you are running standalone scans, the Issue ID shows a value generated locally
by Code Sight (as shown in the image above).

The length of the Issue ID is a clue to its origin:

- A Coverity ID, CID, is typically in the neighborhood of 5 digits long;
  for example, 10332.
- A Coverity on Polaris ID is typically very long;
  for example, f60cfca6b53597df8be3194e50eb0e9e80c0181e698827d24fd0158be1dfcbe1.
- The length of an ID generated locally by Code Sight is somewhere in between;
  for example, e490a2da41b5323a880639d14621cc64.

On the Issues view, you can use the search field
to search for Issue ID values.

## Access to eLearning

For some kinds of issues, a section of the Details display shows links to Black Duck Security
eLearning pages that might be relevant. This means that if, for example, the analysis finds
a possible SQL Injection vulnerability, we provide you with training on just what an SQL
Injection is and how you can avoid this issue in the future.

Figure 3. Links to Security eLearning pages on the Issue Details panel
  
 [image: Links to Security eLearning pages]

Attention:
Access to Security eLearning is licensed separately from Coverity.
To view these pages, you or your organization must have a subscription and login information.
