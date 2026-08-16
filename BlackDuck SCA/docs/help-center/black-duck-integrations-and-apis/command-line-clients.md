---
title: "Command line clients"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/command-line-clients.html"
content_id: "ZvgqgI~cgpUKqW7PyBsqTg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:30.337345+00:00"
---

# Command line clients

For scripting in the command line, users have a choice between the original **Detect
client** (built by the Black Duck team for Black Duck SCA) and the **Bridge
CLI** client.

## Detect client

[Black Duck Detect](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/2767292a573dc549b9b4297b701af3ab.topic) is a scan client that
analyzes code in your projects and associated folders to perform compositional
analysis and find vulnerabilities.

It can be configured to send scan results to Black Duck, which generates risk
analysis when identifying open-source components, licenses, and security
vulnerabilities.

How Detect works:

1. Uses the project's package manager to derive the hierarchy of
   dependencies.
2. Runs the Black Duck signature scanner on the project. This might identify
   additional dependencies not known to the package manager.
3. Uploads both sets of results (dependency details) to Black Duck, which
   creates the Bill Of Materials (BOM) for the project/version.
4. You can view the output and analysis results in Black Duck SCA.

Detect consolidates the functionality of Black Duck, package managers, and continuous
integration plugin tools to perform the following tasks:

- Discover open-source components in your code.
- Map components to known security vulnerabilities.
- Identify license compliance and component quality risks.
- Set and enforce open-source use and security policies.
- Integrate open-source management into your DevOps environment.
- Monitor and alert users when new security threats are reported.
- Calculate security vulnerability risk in your code.
- Produce reports of the open-source analysis findings.
- Provide malware information if identified.

Note: Some scan types require specific feature licenses to execute. Contact
your Black Duck representative for further information.

## Bridge CLI client

[Bridge](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/eeb29c3010d96721ec9540ed4378aa41.topic) is useful when you want a unified
CLI for all the security tools offered by Black Duck Software: **[Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic), [Coverity Connect](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/220f271f3e64c95a08f1d515083a1a46.topic), [Black Duck SCA](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/9aea3062cf34aeb53b068f901c9eb5c2.topic), [Software Risk Manager](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/1e187c67274af26a43a623c0d7b53731.topic).**

Bridge does all the following:

- SAST and SCA scanning
- Scan in synchronous or asynchronous (non-blocking) mode
- Scan whenever new code is merged to a branch
- Scan whenever a pull request is created/updated
- Decorate PRs with comments
- Create Fix PRs (Black Duck SCA only)
- Generates a SARIF file
- Post results to SCM (GitHub advanced security)
- Post results to any supported server (see the list of products above).

For more information **see, [Bridge documentation](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/eeb29c3010d96721ec9540ed4378aa41.topic).**

Note: Bridge can do any of the above in an air gapped environment. See the individual
tool pages for more information.
