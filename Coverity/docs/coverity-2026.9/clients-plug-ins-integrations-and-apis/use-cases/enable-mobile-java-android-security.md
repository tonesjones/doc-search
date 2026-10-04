---
title: "Enable mobile Java Android security"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enable-mobile-java-android-security.html"
content_id: "1qiYNj5L8oSaH5Feddsd7w"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:03.146223+00:00"
---

# Enable mobile Java Android security

The following configuration specifies that Android security checkers should be enabled
(`android-security: true`).

```
capture:
  build:
    clean-command: mvn clean
    build-command: mvn install

analyze:
  checkers:
    android-security: true

commit:
  connect:
    stream: humanoid-android
    url: https://connect.example.com
```
