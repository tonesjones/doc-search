---
title: "Using Polaris secure tunnel"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-polaris-secure-tunnel.html"
content_id: "ujTpwayr_6ZR9fvYpIti0g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:04.874343+00:00"
---

# Using Polaris secure tunnel

A Polaris secure tunnel is an outbound-only encrypted connection from a machine inside a private network to the Polaris cloud platform, established by running Bridge CLI with the `polaris-secure-tunnel` workflow. This topic describes what a secure tunnel is and the system requirements for the machine that runs it.

## What is Polaris secure tunnel?

Polaris secure tunnel is an outbound-only encrypted connection from a machine inside a private network to the Polaris cloud platform. The tunnel is established by running Bridge CLI with the `polaris-secure-tunnel` workflow on a machine that can reach the on-premise SCM server or internal DAST target, such as a web application or API. The tunnel must remain running for Polaris to communicate with the on-premise SCM or DAST target.

No inbound firewall changes are required. The connection is always initiated outbound from the network.

Note: The `polaris-secure-tunnel` workflow uses the [Teleport Access Platform](https://goteleport.com/) for connectivity. Teleport is integrated with Bridge CLI and requires no separate account setup or installation.

## System requirements

To use Polaris secure tunnel, the machine running Bridge CLI must meet the following requirements:

- macOS or Linux (64-bit) with kernel version 2.6.32 or later and glibc version 2.18 or later. Debian and ARM distributions are not supported.

  Note: The `polaris-secure-tunnel` workflow does not run on Windows at this time. As a workaround, it can be run from Windows Subsystem for Linux (WSL) using the Linux version of Bridge CLI. Ensure that the Bridge binary and working directory are both located in the Linux filesystem (for example, `/home/user/...`). WSL cannot open a socket in the Windows filesystem (for example, `/mnt/c/example/path/...`).
- CPU: At least 1 GHz processor (multi-core recommended for improved performance).
- Memory: 512 MB RAM minimum; 1 GB or more recommended.
- Storage: At least 100 MB of free disk space for installation, with additional space for logs as required.

## When to use Polaris secure tunnel?

A secure tunnel is required in any scenario where Polaris needs to communicate with a resource that is not publicly accessible. There are two main use cases:

**On-premise SCM integration**
:   When source code is hosted on a self-hosted SCM instance (such as GitHub Enterprise Server or GitLab) inside a private network that Polaris cannot reach directly. A secure tunnel allows Polaris to clone repositories, trigger scans, and post results back to the SCM, e.g. by adding pull request comments, without requiring inbound firewall changes.

**Internal DAST targets**
:   When a web application or API targeted for dynamic application security testing (DAST) is hosted inside a private network and is not reachable from the internet, a secure tunnel allows Polaris fAST Dynamic to reach and scan the target from the Polaris UI.
