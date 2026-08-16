---
title: "Updating the IBM RTC plugin"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/updating-the-ibm-rtc-plugin.html"
content_id: "uTDFEpp7nIfxVCtO9gwpgA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:35.853995+00:00"
---

# Updating the IBM RTC plugin

The IBM RTC plugin has been replaced with the Eclipse plugin.

Starting in release 2019.09, when upgrading the IBM RTC plugin, you might encounter a
screen that prompts you to evaluate the changes to be applied before continuing. The
changes consist of the renaming of the plugin feature from
`com.coverity.desktop.java.ibm.feature.feature.group` to
`com.coverity.desktop.java.feature.feature.group`.

When the installer tells you "Your original request has been modified" and shows you in
the **Details** pane that Coverity Desktop Java Analysis has already been installed,
you should click **Next** and proceed with the installation.
