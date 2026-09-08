---
title: "JVM System Properties"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/jvm-system-properties.html"
content_id: "ZeMfILRbxDrWNV1Qm8Oh~A"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:32.453021+00:00"
content_hash: "f9e1aa5320b5860bf11aecca2f530aaeb20ff31aeec2162b7414bb909e07a731"
---

# JVM System Properties

You can set custom system properties for the JVM process that hosts Software Risk
Manager. To do so, use the prefix `codedx.jvmprops.` on a line in your
`codedx.props` file. For example, to set the
`http.proxyHost` system property to `1.2.3.4`, add the
following line:

```
codedx.jvmprops.http.proxyHost = 1.2.3.4
```

Note that specifying a setting this way will overwrite existing settings in the JVM. For
example, it is possible to overwrite the `user.home` property, which may
be used by logic within Software Risk Manager. Use care that you don't overwrite an
important value.

For a non-exhaustive list of system properties to be aware of, see
https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html.
