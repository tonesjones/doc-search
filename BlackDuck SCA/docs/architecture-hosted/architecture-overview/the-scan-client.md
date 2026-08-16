---
title: "The Scan Client"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/the-scan-client.html"
content_id: "64j4MtkheUy~jC4WiY7TIg"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:51.645570+00:00"
---

# The Scan Client

The Scan Client performs the task of scanning a file system, collecting data, and
sending it to the Black Duck server for open source software (OSS) matching. This
software always runs locally, on the customer's premises or wherever the files to be
scanned are located. As the Scan Client examines the files, it generates
“signatures” of the files and directories it is scanning and collects other metadata
like file path and file/directory sizes in order to accurately identify open source
code; refer to the diagram on page 1 to see what is additionally sent. This
information is used to match against information in the Black Duck KnowledgeBase to
determine the open source components/versions that are contained in the software
being analyzed. As part of its operation, if the Scan Client can connect to the
specified Black Duck server, it will check its current version against that server
and update itself if necessary.

There are various options for running the Scan Client – it can be used via Black Duck
Detect and integrated into CI Tools (for example, Jenkins), standalone (either with
a CLI or GUI), or as a Docker container for scanning other containers. The typical
best practice is to run the scan client as part of Black Duck Detect.

In addition to running a component-level signature scan, the client can also
optionally perform other scan functions. If desired by the end user, it can
also:

1. Run a type of string search analysis on textual-based files looking for license
   text and copyright statements.
   - The string search matches only returns the match category, file name,
     and byte offset (location inside the file) where the match was
     found.
   - For copyright matches, it also uploads textual content (the copyright
     statement).
2. Wait for component analysis to complete and scan unmatched files for OSS snippets.
   - Snippet scanning creates codeprints (one-way cryptographic hashes)
     over fragments of the files via a sliding window method which are
     then used to match for OSS.
   - It does not capture, store, or send any textual file content to the
     Black Duck KB for analysis. All code stays behind the company
     firewall. Only hashes are transferred.
3. Encrypt and upload scanned source to the Black Duck server for snippet
   side-by-side comparison, or license and copyright display in the Black Duck UI.
   - Uploading code is an optional feature that must be enabled at the
     server and scan levels.
   - If the server is enabled for source upload (which includes defining a
     company-specific encryption key) and the user indicates they wish to
     upload source files, the client will encrypt and upload the OSS
     files scanned for snippets and strings to the Black Duck Server. See
     the *Black Duck upload service* section for more
     information.

Most of these activities can be controlled either at the Black Duck Server level if the
behavior is not desired. For example, if required by company policy, one can set the
Black Duck server to not accept upload of encrypted source files.

Contact Black Duck Support to enable uploading for source files.
