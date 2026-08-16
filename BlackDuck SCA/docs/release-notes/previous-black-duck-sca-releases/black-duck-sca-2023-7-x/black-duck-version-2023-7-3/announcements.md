---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "Y2Ded0k3q6Yj5W60ua3PIg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:37.750282+00:00"
---

# Announcements

## Security Advisory for curl and libcurl (CVE-2023-38545, CVE-2023-38546)

Black Duck is aware of the security issue relating to curl and libcurl which was
disclosed by the maintainer and original creator of the project on October 3, 2023.

CVE-2023-38545 impacts curl versions 7.69.0 through and including 8.3.0 and addresses
a buffer overflow flaw that impacts both libcurl and the curl command line tool. The
overflow can occur during a SOCKS5 handshake. If the handshake is slow, a
user-supplied, unusually long hostname may not be resolved, and instead be copied
into a target buffer for which it may exceed the allocated size. Heap-based buffer
overflows such as these are known to lead to crashes, data corruption, and even
arbitrary code execution.

CVE-2023-38546 is associated with a cookie injection flaw, but curl maintainers
suggest that the series of conditions that must be met makes the likelihood of
exploitation low. The versions impacted by this vulnerability are 7.9.1 through and
including 8.3.0. Upgrading to curl 8.4.0 resolves the issue. Users are also advised
to call curl_easy_setopt(cloned_curl, CURLOPT_COOKIELIST, "ALL"); after every call
to curl_easy_duphandle();.

We believe that there is limited exposure to Black Duck’ products, services and systems.
To the extent we have had exposure, we have upgraded to the latest version of curl
to remediate the situation.

For more information, please visit:

- [Preparing for critical libcurl and curl vulnerabilities (CVE-2023-38545)](https://www.blackduck.com/blog/critical-libcurl-curl-vulnerabilities.html)
- [How to respond to the curl and libcurl vulnerabilities](https://www.blackduck.com/blog/curl-libcurl-vulnerabilities-response.html)
