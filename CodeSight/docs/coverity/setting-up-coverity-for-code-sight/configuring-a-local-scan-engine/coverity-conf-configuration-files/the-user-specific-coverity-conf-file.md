---
title: "The user-specific ‘coverity.conf’ file"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/the-user-specific-coverity.conf-file.html"
content_id: "QVWUODc8u6vQ8YDz7_Z00Q"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.739191+00:00"
---

# The user-specific ‘coverity.conf’ file

When the Code Sight plug-in runs, and Coverity is configured to use a Coverity Connect server, Code Sight searches for a user-specific coverity.conf file on your local system.

- If Code Sight finds a local coverity.conf file, it uses the information that is stored there to locate the local installation of Coverity Analysis.
- If it does *not* find a preexisting coverity.conf file, then it does the following:
  1. Downloads Coverity Analysis from the server being used.

     This requires you to specify a URL for the server, and to authenticate yourself.
  2. Coverity then creates a new user-specific coverity.conf file, and saves it to the expected location for a local Coverity configuration file.

     The default location for the user-specific coverity.conf file depends on which platform you are running, as shown in the following table:

     Table 1. Default location of the coverity.conf file

     | Platform | Location of coverity.conf |
     | --- | --- |
     | Linux or Mac | /Users/<username>/.coverity/ |
     | Windows | C:\Users\<Username>\AppData\Roaming\Coverity\ |

The default location where Code Sight installs Coverity Analysis also depends on your platform:

Table 2. Default location of the Coverity Analysis installation

| Platform | Location of Coverity |
| --- | --- |
| Linux or Mac | /Users/<username>/.blackduck/desktop/ |
| Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\ |

Code Sight only reads the `known_installations` property from the user-specific configuration file.

As the name of the `known_installations` field implies, a system can have more than one installation of Coverity Analysis, and the user-specific coverity.conf file can accommodate this, as shown in the following sample JSON code:

```
{
    "format_version": 1,
    "settings": {
        "known_installations": [
            {
                "platform": "macosx",
                "directory": "/Users/<username>/.blackduck/desktop/controller/\
installedtools/coverity-analysis/2024.03",
                "kind": "cov-analysis",
                "version": "2024.03"
            },
            {
                "platform": "macosx",
                "directory": "/Applications/cov-analysis-macosx-2024.06",
                "kind": "cov-analysis",
                "version": "2024.06"
            },
            {
                "platform": "macosx",
                "directory": "/Users/<username>/.blackduck/desktop/controller/\
installedtools/coverity-analysis/2024.06",
                "kind": "cov-analysis",
                "version": "2024.06"
            }
        ]
   },
   "type": "Coverity configuration"
}
```

When more than one Coverity Analysis installation is present, Code Sight chooses the one that supports the active project and stream, when these apply. Otherwise, it uses the most recent of the installations.
