---
title: "Configuring the Coverity Connect Downloads page"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-coverity-connect-downloads-page.html"
content_id: "qMS3UpyIvrThHkJgbAElIw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:57.137246+00:00"
---

# Configuring the Coverity Connect Downloads page

The Downloads page is available through the Coverity Connect User
menu. This page provides a central location in which users can:

- Download the Coverity Desktop product packages for Eclipse, QNX Momentics,
  Wind River Workbench, IBM RTC, Visual Studio, IntelliJ, and Android
  Studio.
- Eclipse Update site
- Coverity Desktop Analysis Tools
- Gradle Plug-In
- Coverity Desktop Reports, which include the MISRA Report, Security Report,
  and Coverity Integrity Report
- Software Development Kits
- Other content, such as scripts or additional documentation. For information
  about making this content available, see Configuring Coverity Desktop and shared files through the Downloads page.

By default, the Coverity Connect installer includes the Coverity Desktop 2026.6.0 packages so that they are ready to download. There is no extra
configuration required. A user with appropriate credentials can sign into Coverity
Connect, go to the Downloads page, and download the appropriate
Coverity Desktop installation file. Eclipse and Visual Studio users can also obtain a
link to the Coverity Desktop update or gallery site, so the IDE can search for and
install the most current version of the plug-in that is made available through the
Downloads page.

In order for the Eclipse update site to work properly with an SSL connection, the update
site requires a valid certificate installed for the Coverity Connect server. Otherwise
users will have to download the plug-ins and install them locally.
