---
title: "Code Sight version 2019.6"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2019.6.html"
content_id: "az5I0vq55HpZImqQcCKczw"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.288994+00:00"
---

# Code Sight version 2019.6

The 2019.6 release of the Black Duck® Code Sight™ plug-in introduces new features
and fixes various bugs.

## New features

- The plug-in now supports C/C++ analysis in Eclipse®.
- New IDEs are now supported:
  - PyCharm®
  - WebStorm™
- Visual Studio® and Eclipse can now test for compliance with MISRA coding standards.

  To enable MISRA testing, add the following entry to the `"settings"` section of your
  `coverity.conf` file:

```
"cov_run_desktop": {
    "coding_standard_configs": [
        "$(code_base_dir)/MISRA_c2012_7.config"
    ]
}
```

- Code Sight can now authenticate with a Polaris server configured for single sign-on (SAML/SSO).
  It authenticates using an access token obtained from the Polaris server.
- The Code Sight plug-in for Eclipse now supports multiple unique projects in a single workspace.

## Bug fixes

- Self-signed certificates are now accepted for authentication when
  your `coverity.conf` file has the following line in its
  `"server"` section:

  `"on_new_cert": "trust"`

  This enables any new certificate to be trusted automatically.

  UD-2623
- Code Sight now correctly supports downloading zip and tar.gz files as installers
  from the Coverity Server. UD-2413
- If a local license is expired or invalid, Code Sight now attempts to retrieve a new license from the server. UD-1749
- If more than 100 projects were open on Polaris, this caused problems when synchronizing Code Sight triage data.
  This is now fixed. UD-2944
- In Visual Studio, the Code Sight window was not always visible by default for first-time users.
  This is now fixed. UD-2633
- This release fixes an issue where triage data was not synchronized with the server after restarting the IDE. UD-2655
- Code Sight for Visual Studio would fail to start when a Windows user name contained spaces.
  This is now fixed. UD-2891
- In Code Sight for Visual Studio, projects organized using Solution Folders would sometimes fail to capture C/C++ or C# source files.
  This is now fixed. UD-2799
