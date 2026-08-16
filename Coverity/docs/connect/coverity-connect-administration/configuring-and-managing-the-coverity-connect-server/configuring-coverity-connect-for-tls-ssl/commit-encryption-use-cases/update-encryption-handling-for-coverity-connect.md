---
title: "Update encryption handling for Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-encryption-handling-for-coverity-connect.html"
content_id: "A8qsMA9Dma1jHgvwQJYsxA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:35.209266+00:00"
---

# Update encryption handling for Coverity Connect

Edit the Coverity Connect properties file located at
<install_dir>/config/cim.properties.
Set the standard encryption level of incoming commits by adding a line,
`commit.encryption=<value>`, to
cim.properties.

Acceptable values for `commit.encryption` are as follows:

`required`
:   Each commit connection must be encrypted. Any commit from a
    `cov-commit-defects` client that declines
    to open a TLS/SSL connection will be rejected.

`preferred`
:   Coverity Connect will open a TLS/SSL connection if required or
    preferred by the client. If not, the commit will continue
    unencrypted. This is the default value for
    `commit.encryption`.

`none`
:   Coverity Connect will refuse any client request to connect
    through TLS/SSL, and will only receive commits in the clear.

Important:
After you edit cim.properties, you must restart the Coverity Connect server for changes to take effect.
