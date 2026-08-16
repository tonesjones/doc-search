---
title: "Organize, Triage, and Resolve"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/organize-triage-and-resolve.html"
content_id: "xRUK1UcxcCFreB7z2_Z_Vg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:21.763060+00:00"
---

# Organize, Triage, and Resolve

The developer or Dev/Ops can use a number of different clients to *organize* and
*triage* the issues found and committed during analysis: Each of these clients
provides descriptions of the issues and shows where the issues exist in the source
code.

- **Coverity Connect** is a Web-based application that enables you to manage and
  fix issues found using Coverity Analysis and third-party tools.
- **Desktop Analysis** can be used from the command line, or from your IDE if you
  use a plug-in. Supported plug-ins include Eclipse, IntelliJ, or Visual Studio
  IDE.
- **Code Sight** is a plug-in that runs in a number of IDE applications and helps
  you quickly find quality and security issues in your source code. It highlights
  issues directly in the environment's editor.
- **Coverity Policy Manager** is accessible from the Connect GUI. You use it to
  build decomposed and aggregated views of your software, and you use your findings to
  better align reporting with business objectives. As an example, you might want to
  separate internal and external applications. Or you might want to look at only
  Web-facing components, or to look at only components that handle
  personally-identifiable information, and so on. Many applications consist of
  safety-critical parts plus much larger (in terms of lines of code) user interfaces,
  and you might want to focus on the safety-critical parts.

Using these tools, you can organize your Coverity Analysis results. You can sort and
organize issues based on issue type and priority, you can assign some for immediate
resolution, and you can schedule less critical issues for the future. Integration with
SCMs, email, and bug tracking systems, such as JIRA, allows you to use existing
processes to carry out this work.

Once issues have been organized and prioritized, they can be triaged. Triage data and
history are stored in a common database. All issues are categorized into a single
workflow so developers can see what needs to be resolved first. A developer might do one
or more of the following:

- Receive notification (email, JIRA work item, and so on) or log into Coverity Connect
  and look at source code.
- Review the defect: debug, run another program, and so on.
- Fix/Dismiss, and so on, according to workflow and type of defect.

**Documentation Resources**

- Coverity Platform 2026.6.0 User and Administrator Guide
- Coverity Platform 2026.6.0 SOAP Web Services API Reference
- Coverity Platform 2026.6.0 REST Web Services API Guide
