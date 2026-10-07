---
title: "Checker Policy Enforcement in Cloud Native Coverity"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/checker-policy-enforcement-in-cloud-native-coverity.html"
content_id: "EToSwUBeXoog5hoIBQVXGw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:22.662614+00:00"
---

# Checker Policy Enforcement in Cloud Native Coverity

Checker Policy Enforcement (CEP) applies to Cloud Native Coverity scans using the
same policies and enforcement logic as on-premises Coverity Connect.

Policies are defined and managed in Coverity Connect by an administrator. When a CNC
scan is committed to Coverity Connect, the effective policy for the project is checked
automatically. No additional configuration is required in the CNC workflow to enable
policy enforcement.

For information about creating and managing checker policies, see "Coverity Checker Policy Enforcement overview".

## How enforcement works in CNC

Policy enforcement in CNC follows the same model as on-premises Coverity Connect.
The difference is where the enforcement checkpoints execute:

- The compliance check happens automatically when results are committed to
  Coverity Connect at the end of the CNC scan.
- Coverity Connect resolves the effective policy for the project and returns a
  compliance result.
- If the scan does not comply with the effective policy, Coverity Connect
  responds based on the configured non-compliance handling setting — either
  rejecting the commit or accepting it with a warning. See "Configuring non-compliance handling".

## Optional pre-check before submitting to the ScanFarm

Before submitting a scan to the ScanFarm, you can optionally run `coverity
verify-compliance` on your local machine to check whether the scan
configuration satisfies the effective policy. This lets you detect non-compliance
before the scan is submitted and processed.

The pre-check uses the same command and connection options as on-premises workflows.
See "Checking policy compliance before committing".

## Non-compliance in CNC

When a CNC scan is rejected or warned at commit time, the compliance result is
surfaced in Coverity Connect. Check the scan details in the Scans page for
information about which policy setting was not satisfied. See Annunciations.

To resolve a rejected scan, rerun the scan with a configuration that satisfies the
effective policy, then resubmit.

## Coordinator and Subscriber deployments

In Coordinator/Subscriber CNC deployments, CEP operates independently per cluster
member. Each cluster member enforces its own global and project policies. There is
no synchronization of policy assignments between cluster members.
