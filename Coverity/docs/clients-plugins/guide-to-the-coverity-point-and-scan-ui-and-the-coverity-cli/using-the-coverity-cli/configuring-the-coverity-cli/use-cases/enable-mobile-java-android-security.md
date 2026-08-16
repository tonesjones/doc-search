---
title: "Enable mobile Java Android security"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enable-mobile-java-android-security.html"
content_id: "1qiYNj5L8oSaH5Feddsd7w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:57.467069+00:00"
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
