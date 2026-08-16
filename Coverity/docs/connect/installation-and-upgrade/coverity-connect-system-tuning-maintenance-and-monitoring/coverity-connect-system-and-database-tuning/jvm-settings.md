---
title: "JVM settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/jvm-settings.html"
content_id: "8DW7sqquc0szVsp1gay5Qg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:14.505319+00:00"
---

# JVM settings

This section includes tuning recommendation for the Java Virtual Machine. JVM parameters
for Coverity Connect must be placed in the
<install_dir>/config/system.properties files in the
`java_opts_post` attribute. Do not use quotes. This allows the
default parameters to be overridden.

To display your current JVM options, use the following command:

```
java -server -XX:+UnlockDiagnosticVMOptions -XX:+PrintFlagsFinal -version
```

During installation, the installer sets the following JVM parameters, depending on the
performance tuning options you chose:

For Production installation tunings:

```
-Xms512m
-Xmx<75% of the Total System Memory>
```
