---
title: "The explain Subcommand"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-explain-subcommand.html"
content_id: "Vz3n_Pdexk_F6WkQC0Tujw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:34.555693+00:00"
---

# The explain Subcommand

## Syntax

sigma
explain <check_name>|<checker_name>

## Description

The explain subcommand displays information about a specific check or
checker.

For a *check*, this information includes:

- Parent checker;
- The issue description and its remediation;
- The languages the check supports;
- The tags for information about frameworks, domains, or security
  concerns;
- The CWEs supported;
- Enablement status;
- Default severity

For a *checker*, this information includes:

- A summary and the checker description
- The list of checks
- The languages the checker supports (across all checks)
- The tags for information about frameworks, domains, or security concerns; the tags shown
  for a checker is the union of the tags for its checks.
- The CWEs supported

## Ouput of `sigma explain access_to_secret_kubernetes`

```
Parent Checker
access_to_secret

Issue Description
The secrets resource is granted get, list, or watch access on the Kubernetes API.
This can allow an attacker to view Kubernetes cluster or external resources whose
credentials are stored in secrets.

Remediation
Avoid granting get, list, or watch permissions for secrets.

Languages
JSON, YAML

Tags
Kubernetes, Iac, Cis_benchmark, Info_leak, Authz

CWE
284

Default Enablement
Enabled

Default Severity
low
```

## Output of `sigma explain access_to_secret`

```
Summary
Access to secret

Checker Description
This checker detects cases where access is granted to the Secrets object. This can
expose credentials, tokens, and other sensitive information stored in this object to
an attacker.

Checks
fabric8_kubernetes, java_kubernetes, kubernetes, node_kubernetes,
terraform_kubernetes

Languages
HCL, JSON, Java, JavaScript, TypeScript, YAML

Tags
Info_leak, Authz

CWE
284
```
