---
title: "Understanding the AppData Directory"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-the-appdata-directory.html"
content_id: "B5bI~l~VOuVT~n~dQ3rmcA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:17.907633+00:00"
content_hash: "28a20afdff0df527bf77cda4cef7856a54ecf9c105805cf63640eae5d74bf23f"
---

# Understanding the AppData Directory

Software Risk Manager needs a place to store a variety of files, such as the analysis
inputs it receives that the source code that it uses to display in the *Finding
Details* page, log files, and configuration files. These files are placed in the
Software Risk Manager appdata directory. This directory also contains important
information from the ongoing Software Risk Manager usage activity; therefore, it is
recommended that this directory be in a stable location that is periodically backed
up.

The location of the appdata directory is set during installation. By default, the appdata
directory is located in the following locations:

- For Windows: `C:\ProgramData\Software Risk
  Manager\codedx_appdata\`
- For Linux (installed as root): `/var/opt/srm/`
- For Linux (installed as non-root:
  `/home/srm_data/codedx_appdata/`
- For Docker: `/opt/codedx/`
