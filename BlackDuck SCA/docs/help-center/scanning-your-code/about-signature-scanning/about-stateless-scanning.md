---
title: "About Stateless Scanning"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-stateless-scanning.html"
content_id: "H2zeUF5xkmJz2jZBvWPYEA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:42.425430+00:00"
---

# About Stateless Scanning

Stateless Scan is a scan mode that does not create or use any permanent storage within
Black Duck, thus there is no bill of material (BOM) stored. It is used to quickly find
policy violations within the designated scan target. In order to use the Stateless
Signature Scan, you must have the following:

- Black Duck Detect 8.2.0 or later
- Black Duck 2023.1.0 or later
- Hosted KnowledgeBase
- Match as a Service must be enabled

## Enabling Stateless Scan mode

Enable this feature by adding [--detect.blackduck.scan.mode=STATELESS](https://community.blackduck.com/s/document-item?bundleId=detect&topicId=properties/configuration/blackduck-server.html&anchor=detect-scan-mode-advanced&_LANG=enus) to
a run of Detect.

## Restrictions and Limitations

Stateless Scan Mode has a unique set of restrictions, mode of configuration and set
of results. It is similar to Rapid Scan Mode however it differs in that it supports
usage of the SIGNATURE_SCAN tool:

1. A limited subset of Tools can be run.

   - The currently supported tools are: DETECTOR, BAZEL,
     SIGNATURE_SCAN and DOCKER.
   - The Stateless Scan will not persist on Black Duck.
   - All other tools are disabled when running in Stateless Scan
     mode.
2. Stateless Scan and non-persistent SIGNATURE_SCAN

   - To perform a non-persistent Signature Scan in Stateless mode,
     SIGNATURE_SCAN must be included within
     `--detect.tools`.
   - Permitted tools omitted from the detect.tools list will not be
     run.
3. Stateless Scan requires Black Duck
   policies.

   - Stateless Scan only reports components that violate policies.
   - If no policies are violated or there are no defined policies,
     then no components are returned.
4. Stateless Scan does not support
   `detect.policy.check.fail.on.severities`

   - Black Duck Detect will fail with
     `FAILURE_POLICY_VIOLATION` if any component
     violates Black Duck polices with a CRITICAL or BLOCKER
     severity.
   - Stateless Scan supports the same policy conditions as Rapid Scan.
     Click here for a list of policy conditions that are
     supported by Stateless Scan.
5. Stateless Scan does not support
   `detect.policy.check.fail.on.names`
6. Stateless Scan will not create a Project or Version in Black Duck.
7. Stateless Scan when running `SIGNATURE_SCAN` requires
   communication with Black Duck.

## How to invoke a stateless scan

To invoke Stateless scan only:

- `--detect.tools=SIGNATURE_SCAN
  --detect.blackduck.scan.mode=STATELESS`

To invoke Stateless package manager scans:

- `--detect.tools=DETECTOR
  --detect.blackduck.scan.mode=STATELESS`
- `--detect.tools=BAZEL
  --detect.blackduck.scan.mode=STATELESS`
- `--detect.tools=DOCKER
  --detect.blackduck.scan.mode=STATELESS`
- `--detect.target.type=IMAGE
  --detect.blackduck.scan.mode=STATELESS`

## Stateless scan results

Unlike persistent scans, no data is stored on Black Duck and all scans are done
transiently. These scans are primarily intended to be fast, although the
`SIGNATURE_SCAN` can take some time as communication with Black
Duck is a requirement.

The results are saved to a json file named
'name_version_BlackDuck_DeveloperMode_Result.json' in the Scan Output directory,
where name and version are the project's name and version.

```
2021-07-20 13:25:18 EDT INFO  [main] --- Stateless Scan Result: (for more detail look in the log for Stateless Scan Result Details)
2021-07-20 13:25:18 EDT INFO  [main] ---
2021-07-20 13:25:18 EDT INFO  [main] --- 		Critical and blocking policy violations for
2021-07-20 13:25:18 EDT INFO  [main] --- 			* Components: 0
2021-07-20 13:25:18 EDT INFO  [main] --- 			* Security: 5
2021-07-20 13:25:18 EDT INFO  [main] --- 			* License: 0
2021-07-20 13:25:18 EDT INFO  [main] ---
2021-07-20 13:25:18 EDT INFO  [main] --- 		Other policy violations
2021-07-20 13:25:18 EDT INFO  [main] --- 			* Components: 101
2021-07-20 13:25:18 EDT INFO  [main] --- 			* Security: 0
2021-07-20 13:25:18 EDT INFO  [main] --- 			* License: 0
2021-07-20 13:25:18 EDT INFO  [main] ---
2021-07-20 13:25:18 EDT INFO  [main] --- 		Policies Violated:
2021-07-20 13:25:18 EDT INFO  [main] --- 			Security Vulnerabilities Great Than Or Equal to High
2021-07-20 13:25:18 EDT INFO  [main] --- 			Warn on Low Security Vulnerabilities
2021-07-20 13:25:18 EDT INFO  [main] --- 			Warn on Medium Security Vulnerabilities
2021-07-20 13:25:18 EDT INFO  [main] ---
2021-07-20 13:25:18 EDT INFO  [main] --- 		Components with Policy Violations:
2021-07-20 13:25:18 EDT INFO  [main] --- 			Apache PDFBox 2.0.12 (maven:org.apache.pdfbox:pdfbox:2.0.12)
2021-07-20 13:25:18 EDT INFO  [main] --- 			Handlebars.js 4.0.11 (npmjs:handlebars/4.0.11)
2021-07-20 13:25:18 EDT INFO  [main] ---
2021-07-20 13:25:18 EDT INFO  [main] --- 		Components with Policy Violation Warnings:
2021-07-20 13:25:18 EDT INFO  [main] --- 			Acorn 5.5.3 (npmjs:acorn/5.5.3)
```
