---
title: "The static analysis solution"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-static-analysis-solution.html"
content_id: "t~dbb1jRutZGimloHMsPlg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-10T21:31:16.382689+00:00"
---

# The static analysis solution

Coverity is a static analysis solution that makes it possible to address software issues early
in the development life cycle by analyzing source code to identify the following kinds
of problems:

- Software quality and security issues
- Violations of common coding standards

The static analysis solution includes analysis tools as well as management tools.
Analysis tools scan your code and flag issues. Management tools allow you to store
results, to fine-tune the testing configuration, to monitor trends, and to produce
reports. You can also use Coverity tools to manage issues found by third-party tools.

As a testing method, static analysis offers the following advantages:

- You can test code as soon as there is one function that can be parsed. You don't need to have
  a buildable or working system to do analysis.

  Static analysis allows you to
  correct problems before they become embedded in your code and require costly
  fixes or workarounds.
- You test every possible path through your code.

  As applications grow, achieving test
  coverage using dynamic testing methods becomes costly and computationally
  prohibitive. Coverity can test all paths through the code, even ones that are
  extremely difficult to test manually such as error conditions that would only be
  triggered in the case of hardware failure.
- It is deterministic: Analysis of the same code base yields the same results.
- It is able to analyze large code bases very quickly. Coverity uses algorithms that are
  designed to scale for large applications.

To find issues, Coverity first scans your code and then calculates a call graph. Based on
the dependencies defined in the graph, it derives all possible paths through your code.
Finally, it traverses every path looking for events that result in security or quality
issues, and it displays those issues as they occur in your source, with information
about each issue's cause and remediation.

Here is an example of the sort of information displayed for an issue:

Figure 1. Example: Information Displayed for an Issue
[image: image]

In addition to flagging the Main Event (issue), the analysis engine can also identify
contributing events and control structures related to the offending issue. That is,
Coverity doesn't just analyze code within the context of a specific function, but
analyzes execution flows. Hence a defect might start in one function and terminate in
another function or class. In each case, Coverity explains how it determines that an
issue exists.

Analysis can be carried out using either build-based (for compiled languages) or
buildless capture methods. Which method you choose depends on the source language and on
the amount of work you are willing to invest in configuring the analysis.
