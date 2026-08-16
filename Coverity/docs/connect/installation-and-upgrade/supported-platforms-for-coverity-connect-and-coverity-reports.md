---
title: "Supported platforms for Coverity Connect and Coverity Reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/supported-platforms-for-coverity-connect-and-coverity-reports.html"
content_id: "Hah8YuVj_nnBKXX9dl6M6w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:42.185270+00:00"
---

# Supported platforms for Coverity Connect and Coverity Reports

Coverity Connect and Coverity Reports support the following server platforms and browsers.

Table 1. Coverity Connect and Coverity Reports server platform support

| Host OS | Host OS version | 32- or 64-bit | Hardware architecture | Notes |
| --- | --- | --- | --- | --- |
| Windows | Windows workstation releases: Windows 10 or higher. Windows server releases: Windows Server 2012 or higher. | 64-bit | x86_64 | **Deprecation notice:** Support for Windows Server 2012 is deprecated and will be removed in a future release. |
| Linux | Linux Kernel 3.10.0-123 or higher, `glibc` 2.18 or higher. |  |

Table 2. Coverity Connect and Coverity Reports browser support

| Browser | Version | Notes |
| --- | --- | --- |
| Internet Explorer | 11 | **Deprecation notice:** Support for Internet Explorer is deprecated as of 2022.6.0 and will be removed in a future release. |
| Microsoft Edge | Windows 10-supported versions |  |
| Firefox | Mozilla-supported versions | Coverity supports only the Firefox and Chrome versions that are under maintenance, and deprecates all end-of-life versions. |
| Google Chrome | Google-supported versions |
| Safari | 8 and later | **Deprecation notice:** Support for versions of Safari that Apple no longer supports is deprecated, and will be removed from a future release. |

The Coverity Desktop plug-ins for Eclipse, Microsoft Visual Studio, and other supported IDEs
require the same version for the Coverity Analysis and Coverity Connect installations
for which Coverity Desktop is configured to use. If you use Coverity Desktop, you must
upgrade all Coverity products together to the same version.

## Coverity Connect software requirements

Coverity Connect requires the following software on the server-side operating system:

- On Windows:
  - `kernel32.dll`
  - `powrprof.dll`
  - `versionhelpers.h`
- On Linux:
  - `glibc`
  - `netstat`
  - `udev`

Coverity Connect requires the following software on the client side:

- A supported browser. See Table 2, above.
- JavaScript enabled.
- Display resolution of at least 1024 x 768 pixels recommended.

Coverity Connect supports TLS v1.2. Client tools that invoke Coverity Connect should also
be TLS v1.2-compliant. For example, OpenSSL requires version 1.0.1 or newer, and cURL
requires version 7.3.4.0 or newer.

The Coverity Connect server is bundled with the following software:

- Apache Tomcat 10.1.48
- PostgreSQL supported
  versions (the embedded database)
- OpenJDK 17.0.12

External PostgreSQL database:

- In addition to the embedded database, Coverity Connect supports the PostgreSQL external
  database versions listed in PostgreSQL supported
  versions.
- The configuration, deployment, and management of external databases should be
  handled by experienced PostgreSQL DBAs.
- If you are running PostgreSQL 18 on older operating system versions (RHEL 8,
  Ubuntu 20, Debian 11, and so on), you must ensure that OpenSSL 3 is available
  before installing PostgreSQL 18.
