---
title: "Resolving LLM analysis errors"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/resolving-llm-analysis-errors.html"
content_id: "YcbBwEWK7kGu8tuzs_RAyA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:32:58.781809+00:00"
---

# Resolving LLM analysis errors

When LLM errors occur during analysis of AI-augmented SAST checkers, the Issues View displays a notification indicating that some issues may not be shown.

Starting in Coverity 2026.9, a notification appears in the top-right of the Issues View (Modern UI only) when all of the following conditions are met:

- The AI-augmented SAST checker plug-in was configured and enabled during the analysis.
- One or more LLM errors occurred during the analysis, such as a network timeout, expired API key, or credit limit exceeded.
- The analysis was committed to the stream you are currently viewing.

The notification indicates that during the latest analysis, some IDOR candidates could not be verified by the LLM due to errors. As a result:

- Those candidates are not shown as issues — they are dropped.
- The actual number of IDOR vulnerabilities in your code may be higher than what is displayed.

1. Note the notification in the Issues View.
2. Navigate to your CI system or scan logs and open analysis-log.txt.
3. Search for LLM-related error messages to identify the root cause.

   Common causes include an invalid API key, unreachable URL, or credit limit exceeded.
4. Resolve the issue by updating credentials, fixing network connectivity, or adding credits as needed.
5. Re-run the analysis.

   On the next successful scan, the IDOR checker verifies all candidates and reports confirmed vulnerabilities.

Note: The notification appears only in the Modern UI Issues View. It is not shown in the classic Coverity Connect UI.

Note: The notification does not affect other (non-AI-augmented) checkers. All other defect detection continues normally regardless of LLM errors.

Note: If the LLM is not configured and the analysis finds no IDOR candidates
(or the IDOR checker is not enabled) then no notification is shown.

For more information, see:

- [IDOR checker reference](https://docs.blackduck.com/r/sigma/latest/sigma-checker-reference/idor.html)
- [Configuring the AI-augmented SAST checker plug-in](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/configuring-the-ai-augmented-sast-checker-plug-in.html)
- [Security considerations for the AI-augmented SAST checker plug-in](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/security-considerations-for-the-ai-augmented-sast-checker-plug-in.html)
