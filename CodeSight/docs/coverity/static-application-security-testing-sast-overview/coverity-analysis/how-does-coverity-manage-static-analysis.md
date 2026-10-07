---
title: "How does Coverity manage static analysis?"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/how-does-coverity-manage-static-analysis-.html"
content_id: "glbhaB24WfGM08kJTZKa8A"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.789570+00:00"
---

# How does Coverity manage static analysis?

Code Sight uses *Coverity Analysis* to analyze code.

Each time it scans a source file in your project, Coverity Analysis performs these overall steps:

1. Builds a syntax tree that models the program’s execution paths.
2. Traverses that tree, searching for problematic situations such as faulty logic, security breaches, tainted data, and so on.
3. Reports each *issue* found by this search.

The Local View tab displays lists of the issues found by the most
recent scan. See Viewing Code Analysis Issues.

Note:
There might be portions of code that *do not* lie on the execution path.
This is itself an issue, and Coverity Analysis reports it.

The Issue Details panel displays details about a particular issue, along with suggestions
for how you might fix that issue.

Remember:
Coverity Analysis searches for different types of issues.
*Quality issues* are software problems such as memory leaks.
*Security issues* are
vulnerabilities, especially those that arise when a system connects to the Internet.
*Rule issues* are various kinds of checks; the issues they report can include deviations from
in-house programming style or from an established industry standard.

Issues are often called *defects,* but sometimes it can help to think of an issue as simply
reporting a situtation that merits further investigation.
