---
title: "Defining the scan name"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/defining-the-scan-name.html"
content_id: "vgrBNKuATrZSo52DS0O4Xw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:50.517739+00:00"
---

# Defining the scan name

Hub-872By default, the name of a scan, as
shown on the Scans page, is a combination of the host name of the server that ran the
scan and the path to the code. This name is created when you run the scan. You may want
to specify a different name.

Some examples of why you may want to specify a scan name are:

- You are using a continuous integration build system and have multiple
  slave/client servers running a scan. Each slave/client server has a different
  host name. Depending on which slave/client server completes the scan, there can
  be duplicate scan files for the same scan. Your BOM may also be inaccurate as
  old scans are included although the code has been rescanned.

  By entering a unique scan name, duplicate scan files are eliminated. Your BOM no
  longer contains old scans as multiple slaves/clients can now run the same scan:
  the newest scan replaces the existing scan as the most current scan for given
  code.
- You have many different build system work spaces that you scan and you want to
  reuse the same workspace for multiple projects. By using a different name for
  the scans, you can use the same workspace and have the code point to different
  projects.

To specify a name, use the `--name` parameter when using the command line and provide a unique
name for a scan. This name appears on the Scans page.

Note the following:

- Scan names are case insensitive. Scan1, scan1, and SCAN1 are considered the same
  name.
- Scans with the same host and path but different names are considered different
  scan files.
- The host name of the server that ran the scan and the path to the code are shown
  in the **Scan Details** table in the *Scan Name* page.
