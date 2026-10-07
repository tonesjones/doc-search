---
title: "Multiple occurrences of an issue"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/multiple-occurrences-of-an-issue.html"
content_id: "xY3VTK9TlrKcJXkvBZyglQ"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:54.021570+00:00"
---

# Multiple occurrences of an issue

If an issue occurs more than once, the Issue Details panel notifies you by displaying an additional Occurrences field.

Figure 1. Occurrences field in the Issue Details panel
  
 [image: Issue Details > Occurrences field]

You can open the drop-down list to go directly to one of the occurrences, or you can click one of the the left/right arrows
to either side of the drop-down list, in order to step through the occurrences in sequence.

Important:
If, after you correct the code and scan again, an issue does not disappear from the list,
this does not necessarily mean that your fix was wrong.
Different paths through the same code can sometimes lead to the same issue.
This is why the Issue Details panel reports multiple occurrences of the same issue.

When a static-analysis issue occurs more than once, the
Contributing Details panel
can help you see if different occurrences arise from the same contributing logic, or if there are multiple
areas of contributing code that might be problematic.

When all occurrences of the issue have been resolved, the issue should disappear from the
Issues list altogether.
