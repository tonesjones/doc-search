---
title: "Enabling Secure Code Warrior"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-secure-code-warrior.html"
content_id: "XxltKCUVZ81MbvAnrUN8Sg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:06.711734+00:00"
---

# Enabling Secure Code Warrior

To enable Secure Code Warrior, edit your `cim.properties` file to include
the following property setting:

```
securecodewarrior.enabled=true
```

You can find `cim.properties` in the
`<coverityConnectInstallDir>/config/` directory.

You must restart the Coverity Connect server for this change to take effect.

After setting this property and restarting the server, the Coverity Connect GUI displays
a Secure Code Warrior section below the CWE section near the top of the right-hand
pane:

Figure 1. Example: Secure Code Warrior section
  
 [image: image]
