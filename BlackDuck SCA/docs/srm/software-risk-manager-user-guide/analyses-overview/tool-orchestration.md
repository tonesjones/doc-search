---
title: "Tool Orchestration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/tool-orchestration.html"
content_id: "Pflh1XxpJpAXc9B9l_62sA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:42.735791+00:00"
content_hash: "d188c47b7068837a6919464db094227829ea23a5979f275ec26e43b72ad274df"
---

# Tool Orchestration

When the Tool Orchestration Service is enabled, Software Risk Manager can orchestrate
analyses that run in whole or in part on your Kubernetes (k8s) cluster. (See the Tool
Orchestration Configuration section in the *Software Risk Manager Install
Guide* for instructions to enable this feature.)

A Software Risk Manager analysis may run one or more built-in code scanners. Many of
those tools can run on your Kubernetes cluster when you enable the tool orchestration
feature. Those that cannot, such as Dependency Check, will continue to run on the
Software Risk Manager web server.

The following table shows which bundled tools Software Risk Manager can run on your k8s
cluster.

Table 1.

| Bundled Tool | Tool Orchestration Support |
| --- | --- |
| Brakeman | Yes |
| CheckStyle | Yes |
| CPPCheck | Yes |
| DependencyCheck | No |
| ESLint | Yes |
| FxCop (user-installed) | No |
| Gendarme | Yes |
| JSHint | Yes |
| PHP Code Sniffer | Yes |
| PHP MD | Yes |
| PMD | Yes |
| Pylint | Yes |
| Retire JS | No |
| ScalaStyle | Yes |
| SpotBugs | Yes |
| ZPA CLI | Yes |

Software Risk Manager also includes the following tool orchestration capabilities that
run only on your k8s cluster:

- Checkmarx
- Security Code Scan
- ZAP

A single Software Risk Manager analysis can have tools running on both the webserver and
on multiple nodes of your k8s cluster. All tool outputs will be combined into one
analysis that either succeeds or fails as a whole, provided the Software Risk Manager
web server remains online throughout the analysis.

If the Software Risk Manager web application unexpectedly restarts, a built-in fail-safe
lets Software Risk Manager receive k8s analysis results from abandoned orchestrated
analyses. Software Risk Manager will lose any results from bundled tools in this case,
so a restart of the Software Risk Manager web application is one scenario where Software
Risk Manager may process results from a partially completed analysis. When Software Risk
Manager detects an orchestrated analysis that it is not tracking, a message will appear
on the Orchestrated
Analyses page.

You can configure Software Risk Manager to run additional tools by implementing other
add-in tools.

For additional information, see the following sections:

- Resource Requirements
- Scanning a Request File
- Adding a Tool
