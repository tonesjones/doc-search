---
title: "Custom analysis settings"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/custom-analysis-settings.html"
content_id: "L33w2buynVzlYxtT4l8g0g"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.188443+00:00"
---

# Custom analysis settings

Another use of coverity.conf is to specify custom
settings for Coverity Analysis.

Changing the settings used for Coverity Analysis is described in existing documentation.
We won’t go into details here. If you do edit coverity.conf
to specify custom settings, proceed with caution.

These are resources that provide more information about editing coverity.conf:

- The *Coverity Desktop Analysis User Guide* describes the
  coverity.conf settings in detail.

  The Coverity document set, which includes the *Desktop Analysis User Guide,* where
  coverity.conf is described, is installed on a
  client system when Coverity Analysis is installed.

  The default location of these documents depends on the operating system you
  are using. See the following table:

  Table 1. Where Coverity docs are installed by default

  | Platform | Location of Coverity documents |
  | --- | --- |
  | Linux or Mac | /Users/<username>/.blackduck/desktop/controller/installedtools/coverity-analysis/<version>/doc/en/ |
  | Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\controller\installedtools\coverity-analysis\<version>\doc\en\ |
- The following lesson on the Black Duck Community web site describes how to edit
  coverity.conf for use with Code Sight:
  [“How to Set Up the Coverity Desktop Analysis Configuration File – coverity.conf”](https://community.blackduck.com/s/article/How-to-setup-Coverity-Desktop-Analysis-Configuration-File-Coverity-conf).
