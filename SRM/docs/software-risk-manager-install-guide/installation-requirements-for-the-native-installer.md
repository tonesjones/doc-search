---
title: "Installation Requirements for the Native Installer"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/installation-requirements-for-the-native-installer.html"
content_id: "aYUC2~fpdamRcLpCi22h3Q"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:46.536882+00:00"
content_hash: "3538cc0b36955be6c17bf5a1f7c68f67152fc5fbfccb1b1196461d3931083184"
---

# Installation Requirements for the Native Installer

The Native Installer has the following requirements.

## Software Requirements

Software Risk Manager is pre-packaged with most of its requirements. There are,
however, certain prerequisites for installations that will be leveraging the .NET
scanning support of Software Risk Manager.

Note: The bundled Dependency-Check periodically updates its database of vulnerabilities.
If Software Risk Manager is installed in an environment without a connection to the
internet, this update will not succeed. For more information, see the Internet Access
section.

### .NET Analysis

In order to run the bundled .NET tools supported by Software Risk Manager, the
[.NET Framework runtime](https://dotnet.microsoft.com/download) is required for Windows and
the Mono runtime is required for Linux. Additionally, Dependency-Check requires
the [.NET Core 8.0 SDK](https://dotnet.microsoft.com/download/dotnet-core/8.0) on all
platforms.

Note: The .NET Core 8.0 SDK is preferred over the .NET Core 8.0 Runtime, as the
Runtime may cause Dependency-Check .NET analyses to fail in some
environments.

### Windows Users

It is recommended that the latest version of .NET be installed.

Software Risk Manager is capable of running multiple .NET analysis tools on your
codebase. FxCop is a supported tool and is developed and distributed by
Microsoft. For Software Risk Manager to run FxCop on your behalf, you must
install it separately. Software Risk Manager will then automatically discover
its location and run it.

Software Risk Manager supports FxCop versions 10+ and will automatically discover
the location of the latest version of FxCop installed on your machine. If you
would like to provide a specific location, set the `fxcop.path`
property in the Software Risk Manager configuration file
(`codedx.props`). FxCop is a legacy analyzer that is no
longer available through Microsoft. Starting with Visual Studio 2019 and .NET
5.0, FxCop is replaced with Microsoft Code
Analysis (Roslyn) Analyzers.

### Linux Users

Software Risk Manager uses Chromium internally, which requires the following Linux
system packages to be available:

- ca-certificates
- libglib2.0-0
- libnss3
- libnspr4
- libatk1.0-0
- libatk-bridge2.0-0
- libcups2
- libdrm2
- libxkbcommon0
- libxcomposite1
- libxdamage1
- libxfixes3
- libxrandr2
- libgbm1
- libpango-1.0-0
- libcairo2
- libasound2
- fonts-liberation
- libxshmfence1
- libjpeg-turbo8
- libpng16-16

To install these, run one of the following commands depending on your Linux distribution:

**On Ubuntu/Debian-based:**

```
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    ca-certificates libglib2.0-0 libnss3 libnspr4 libatk1.0-0 \
    libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 \
    fonts-liberation libxshmfence1 libjpeg-turbo8 libasound2 libpng16-16
```

Note:
For Ubuntu 24.04+, some package names have changed. If the above fails for
`libasound2` or `libpng16-16`, use these
alternatives instead: `libasound2t64`, `libpng16-16t64`.

**On RHEL/CentOS/RPM-based:**

```
sudo dnf install -y \
    ca-certificates glib2 nss nspr atk at-spi2-atk cups-libs \
    libdrm libxkbcommon libXcomposite libXdamage libXfixes libXrandr \
    mesa-libgbm pango cairo alsa-lib \
    libxshmfence libjpeg-turbo libpng liberation-fonts
```

Note:
On older versions that use `yum` as the package manager, such as
RHEL/CentOS 7 and earlier, replace `dnf` with `yum`.

## Hardware Requirements

Hardware requirements vary, depending on how many Software Risk Manager projects will
be active at the same time, how frequently analyses will be conducted, whether
built-in tools are being used, the number of results from tools in use, how many
concurrent users are expected to use the system, and what other system interactions
might be setup. However, the following is the suggested hardware configuration
requirements based on deployment size.

Table 1.

| Deployment Size | CPU Cores | Memory | IOPs | Storage |
| --- | --- | --- | --- | --- |
| **Small** This configuration is recommended for supporting up to 100 projects with limited use of built-in tools, up to 1,000 analyses per day, and up to 8 concurrent analyses. | 4 cores | 16 GB RAM | 3,000 | 250 GB |
| **Medium** This configuration is recommended for supporting between 100 and 2,000 projects, up to 2,000 analyses per day, and up to 16 concurrent analyses. | 8 cores | 32 GB RAM | 6,000 | 500 GB |
| **Large** This configuration is recommended for supporting between 2,000 and 10,000 projects, up to 10,000 analyses per day, and up to 32 concurrent analyses. | 16 cores | 64 GB RAM | 12,000 | 1 TB |
| **Extra Large** This configuration is recommended for supporting over 10,000 projects, more than 10,000 analyses per day, and up to 64 concurrent analyses. | 32 cores | 128 GB RAM | 24,000 | 2 TB |

## Operating Systems Supported

The following operating systems are supported:

- Windows (10, 11, and Server 2016+)
- Linux (Ubuntu 18+, RHEL/CentOS 7+)
