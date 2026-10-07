---
title: "Project-specific ‘coverity.conf’ files"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/project-specific-coverity.conf-files.html"
content_id: "9cJy2XlL2jm_ioOP~qEjzg"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.799724+00:00"
---

# Project-specific ‘coverity.conf’ files

A project-specific coverity.conf file contains details about the project to analyze, and how to do so.

The project-specific configuration must be manually created. There should be one project-specific coverity.conf file
per project per development environment.

Each developer who works on that code base should use the same project-specific coverity.conf,
and the project-specific configuration should be stored at the root of the project.
The easiest way to ensure this is to store the coverity.conf file in the root directory of
the same repository as the code itself.

The project-specific configuration can specify a variety of things:

- When Coverity Analysis communicates with Coverity Connect (and *not with Coverity on Polaris),*
  the project-specific file must specify the server and the stream to use, as described in
  Configure Coverity Analysis to use Coverity Connect.
- The project-specific file can also customize the way Coverity Analysis runs.
  These are described in Alternative configuration settings and the subtopics that follow.

## Alternative configuration settings

Whether your client system connects via a Coverity on Polaris server or a Coverity Connect server,
you can use the project-specific coverity.conf file to specify custom analysis settings.

There are a number of reasons you might want to use a project-specific coverity.conf file:

1. As already described, to specify the Coverity Connect server and the Coverity Connect stream.

   This applies only when Coverity Analysis connects to a Coverity Connect server.
   It does not apply when Coverity Analysis connects via Coverity on Polaris.
2. To specify an alternative installation directory for Coverity Analysis.

   To do so, you would use the `KnownInstallation` object: Please see the
   *Coverity Desktop Analysis User Guide*
   for details.
3. To specify a compiler configuration that is *not the standard configuration* for the IDE you use.

   See “Special-purpose compiler configurations”.
4. To specify alternative build tools.

   Certain development environments *require* explicit build specification.
   See “Frequently asked questions”
5. For Code Sight running Coverity Analysis in Eclipse or in Visual Studio, to enable MISRA compliance testing.
   See “Enabling MISRA compliance testing”.
6. To specify custom analysis settings.

   Analysis settings are described elsewhere.
   There are too many to list here,
   but Custom analysis settings
   lists resources for learning about analysis options.

Important:
The coverity.conf JSON file format is standard for desktop configurations of Coverity Analysis.
For more information about it, please see the *Coverity Desktop Analysis User Guide*.
