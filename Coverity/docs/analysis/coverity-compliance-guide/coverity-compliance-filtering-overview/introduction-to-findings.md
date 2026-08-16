---
title: "Introduction to Findings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-findings.html"
content_id: "wZL7RRlyYmiWsZysK9D_xg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:38.603209+00:00"
---

# Introduction to Findings

Let's begin by examining the concept of *findings*. When you run Coverity Analysis
on your codebase, the tool locates potential coding problems. Each of these potential
coding problems is called a *finding*. When you commit your findings to the
Coverity Connect database (using the `cov-commit-defects` command),
each finding is persisted as an *issue*. From a data point of view, a finding is
very lightweight and consists of only a few pieces of information. An issue, on the
other hand, comprises numerous data fields that track the issue's evolution and history
as it is triaged, worked on, resolved, and so forth.

Note: In the context of Coverity Analysis, findings are called *defects* or sometimes
*errors*. In the context of Coverity Connect, issues are also called
*defects*.

The commit process normally transforms all findings into issues. This behavior often
provides the best outcome. However, for codebases that must comply with a coding
standard, such behavior can easily result in an unmanageable number of issues. This is
where Coverity Compliance Filtering can help. Coverity Compliance Filtering enables you
to intelligently filter out unimportant and less important findings before they are
persisted as issues, enabling you to vastly reduce the number of issues that developers
see at any point in time.

The filtering system is policy-based. It lets you specify patterns based on the location
and compliance type of findings. For example, you could create a filtering policy that
matches all findings located in the path src/main/c/lib and whose
compliance type includes all findings in MISRA C 2012, rule 2.5. Your policy also lets
you prioritize findings that match such a pattern by assigning them a score (1–9). A
threshold control enables you to choose which findings to persist, according to their
assigned scores. The findings' scores are also persisted, which allows developers to
sort and search for issues according to their priority.

To help you make policy decisions, Coverity Compliance Filtering lets you run reports on
your codebase findings. At a glance, you can see how many findings of which types are
present, where they are in the codebase, and whether they will be filtered out or
persisted as issues at commit. As your developers fix issues, you can easily adjust your
policies to send them more issues and help them focus on those you have decided are most
important.
