---
title: "How Coverity products integrate into a build system"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/how-coverity-products-integrate-into-a-build-system.html"
content_id: "5Kr0vFsLuGznnaBa2NTn1Q"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:35.665512+00:00"
---

# How Coverity products integrate into a build system

Before you make decisions about how to deploy Coverity products into your development
environment, it is important to understand how they can be integrated. This section
shows how Coverity products are integrated into a typical build environment.

It is important to recognize the various deployment options and recommendations so that
you can make decisions about the hardware to which you will install and implement
Coverity components. After you have identified how you want to deploy your Coverity
system, you should use the hardware
recommendation chapter of this manual to set up your environment.

This section begins with a diagram and explanation of a basic build system. The
subsequent deployment figures in the section below build upon the basic to show how
Coverity tools are integrated into a build system.

Note: Note that for the diagrams that depict Coverity deployments, the dotted lines
represent features or tools that are optional.

The following image shows a high-level view of a basic build system:

[image: image]

**The build process flow is as follows:**

1. The software developer makes changes or additions to a section of code.
2. When the developer is satisfied with her/his changes, the code is checked into a
   source control management (SCM) system.
3. Build execution instructions (such as Makefiles) are invoked through a continuous integration
   (CI) tool (such as Jenkins) upon receiving notification by the check-in process to
   the SCM. See also Coverity integrations and APIs.
4. The code is built at the scheduled interval. In this case, nightly.
5. Build success or failure is reported by the CI tool and notification of the result
   is sent to the organization.
6. Meanwhile, the developer uses a bug tracking system to locate and manage possible
   bugs that are found in the software.
7. The developer fixes the assigned bugs. The process repeats.
