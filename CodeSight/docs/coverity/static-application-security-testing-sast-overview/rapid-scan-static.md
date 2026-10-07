---
title: "Rapid Scan Static"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/rapid-scan-static.html"
content_id: "Owdj_WXzgs3_6EaT123Y8Q"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.643439+00:00"
---

# Rapid Scan Static

Rapid Scan Static is one of the engines that Code Sight can run to perform *static application security testing* (SAST; also known as *static analysis*).

Compared to Coverity Analysis, Rapid Scan Static is meant to be fast and easy to use.

Rapid Scan Static is an ideal solution for rapidly evolving projects,
for cloud adopters, and for those who are just starting their application security journey and need to assess
their code without a major investment of time and resources.

Rapid Scan Static uses the *Sigma* engine, which has its own set of checkers to report actionable results that developers can fix right away, at their desktop.
It does not generate reports or evaluate compliance with standards such as MISRA.
You can find a thorough description in the
[Sigma User Guide](https://documentation.blackduck.com/bundle/sigma-ug/page/topics/sigma_user_guide.html).

This engine can scan not only source code, but its accompanying text-based metadata.
See the Code Sight Support Matrix for details.

Rapid SAST scans are strictly local: Rapid Scan Static does not rely on communication with a centralized server.
