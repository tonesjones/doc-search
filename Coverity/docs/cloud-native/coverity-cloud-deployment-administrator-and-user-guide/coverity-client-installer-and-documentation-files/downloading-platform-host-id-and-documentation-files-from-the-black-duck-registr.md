---
title: "Downloading platform, host ID, and documentation files from the Black Duck registry using curl"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-platform-host-id-and-documentation-files-from-the-black-duck-registry-using-curl.html"
content_id: "8bsTNWvLSsTATT2BdM6yTg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:36.516414+00:00"
---

# Downloading platform, host ID, and documentation files from the Black Duck registry using curl

This section describes how to download platform files, host ID generate files, and
documentation files as needed from the Black Duck private Docker registry using the
`curl` command.

The `curl` command syntax is:

```
curl https://repo.blackduck.com/coverity-releases/{release}/{filename} -o {filename} -u {user:password}
```

For example, to download a documentation file::

```
curl https://repo.blackduck.com/coverity-releases/2026.6.0/doc_en.zip
   -o doc_en.zip -u <user:password>
```

where `user` and `password` are the credentials available
on your Software Licenses page of the Black Duck Community website by clicking
View/Request Docker Registry Credentials.
