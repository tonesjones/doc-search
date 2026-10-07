---
title: "Switching between multiple profiles"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/switching-between-multiple-profiles.html"
content_id: "aNf_GmLjmNbStItFTg4yWQ"
version: "12.0.0"
section: "Configuring Detect"
scraped_at: "2026-10-04T23:33:19.180823+00:00"
content_hash: "c8a52d23d2f7550924b229d10fa9be65786cc76378d140790937af5f686b9710"
---

# Switching between multiple profiles

A profile is, in effect, a set of pre-defined properties. You select the profile (property settings)
you want when you run Detect.

## Creating a profile

To define a set of properties for a profile, create a configuration file named *application-{profilename}.properties*
or *application-{profilename}.yml* in the current working directory, or in a subdirectory named *config*.
Populate it with property assignments as previously described.

## Selecting a profile on the command line

To select one or more profiles on the Detect command line, assign the the comma-separated list of profiles
to the Spring Boot property *spring.profiles.active*:

```
bash <(curl -s -L https://detect.blackduck.com/detect12.sh) --spring.profiles.active={profilename}
```

This capability is provided by Spring Boot. For more information, refer to
[Spring Boot's profile mechanism](https://docs.spring.io/spring-boot/docs/2.4.5/reference/html/spring-boot-features.html#boot-features-profiles).
