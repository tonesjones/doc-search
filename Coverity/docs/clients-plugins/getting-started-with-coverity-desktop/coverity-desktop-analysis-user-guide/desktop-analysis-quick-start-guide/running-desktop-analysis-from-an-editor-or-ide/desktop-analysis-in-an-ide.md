---
title: "Desktop Analysis in an IDE"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktop-analysis-in-an-ide.html"
content_id: "qrehkR70cmo1OGip9HaIxg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:48.911536+00:00"
---

# Desktop Analysis in an IDE

When Desktop Analysis is set up to work in an IDE, the coverity.conf
configuration file can be used to deploy various settings to Desktop Analysis IDE users.

Note: Visual Studio currently supports all of the settings below, while the other IDEs only
support setting up the following settings pages:

- Coverity Connect
- Stream
- SCM

The Visual Studio plug-in takes advantage of the ability to specify settings on
a per analysis configuration basis and also allows you to specify specific checker
settings or extend_checker settings. This, along with user specified variables allow
users to deploy very complex consistent settings to all users by creating the
coverity.conf configuration file and check it into your
Source Code Management (SCM) repository, usually in the root directory

Below are some coverity.conf examples that can be helpful for
Desktop Analysis in the IDE plug-in.

**Example 1:** Configure a default custom tools location, while allowing users to override
it by specifying the `cov_install_dir` in their user-specific
coverity.conf file if they need to:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "variables": {
        "cov_install_dir": "C:\\Program Files\\Coverity\\cov-analysis-8.7.0"
    },
    "settings": {
        "known_installations": [
            {
                version: "$(version)",
                platform: "$(platform)",
                kind: "cov-analysis",
                directory: "$(var:cov_install_dir)"
            }
        ]
    }
}
```

**Example 2:** To preconfigure some checkers for two named analysis configurations with
specific settings (this can be expanded to customize settings for different analysis
configuration names), use something like:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "server": {
            "url": "<URL of Connect server; must include protocol and port number>",
        },
        "stream": "teststream",
        "scm": {
            "scm": "git"
        },
        "conditional_settings": [
            {
                "when": {
                    "configurations": [
                        "Default",
                        "Alternate AC 1"
                    ]
                },
                "settings": {
                    "cov_run_desktop": {
                        "reference_snapshot": "latest",
                        "checkers": {
                            "UNREACHABLE": {
                                "enabled": true
                            },
                            "IDENTICAL_BRANCHES": {
                                "enabled": false
                            }
                        }
                    }
                }
            }
        ]
    }
}
```
