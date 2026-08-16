---
title: "Signal release notes"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-release-notes.html"
content_id: "4RKMpkO6EtmpgrOkKE9r0Q"
version: "latest"
section: "Signal release notes"
scraped_at: "2026-08-13T00:04:59.839396+00:00"
---

# Signal release notes

## July 2026

- Bug fixes and technical improvements.
- Improved 429 error handling with exponential backoff. Previously, when the LLM gateway returned
  a 429 error code requesting a retry, all retry attempts were made in rapid
  succession, causing them to fail and preventing the file from being
  processed correctly. Retry attempts are now spaced using exponential
  backoff, improving reliability when rate limits are encountered.
- Pre-scan cost estimator for large codebases. When a scan targets a codebase larger than a
  configurable file-count threshold (default: 500 files), Signal runs a pre-scan estimator before
  starting the actual scan. This gives the user a low/mid/high range for input
  tokens, output tokens, and a wall-clock curation before the user commit to a
  potentially expensive run. The estimate is printed to the log along with
  language composition and enabled stages, then the user is prompted to
  confirm before the scan proceeds. Non-interactive environments auto-proceed
  after logging the estimate. If any sampled single-file-analysis calls were
  served from the LLM cache from a prior run, the projected numbers are not
  able to reflect the true cost. The estimator detects this and prints a
  warning.
- Updated default SFA model. Signal now supports Claude Sonnet
  4.6, and this is now the default model used for single file analysis.
- Console progress update for the dataflow agent. Added progress logging in the dataflow and
  oversight agents so the users can see real-time status while the dataflow
  agent is running.
- Enhanced cryptography analysis. Reviewed and improved the cryptography detection prompt,
  including evaluation of Post-Quantum Cryptography (PQC) handling and
  oversight agent coverage for crypto-related findings.
- Crash recovery for Dataflow Agent. Signal periodically writes
  a checkpoint file during the expensive dataflow agent phase. On restart,
  previously completed tasks are skipped and only the remaining work is
  considered. The results are merged before handing off to oversight.
- Auto-export SFA results. For scans exceeding 500 dataflow tasks, Signal automatically writes 2 hidden dot-files
  that appear and disappear in the same directory as
  `--report-file`: `.{report_file}.sfa.json`
  (interim SFA report file) and `.{report_file}.df_checkpoint`
  (checkpoint file). Both files are removed when the scan completes
  successfully. High disk usage is expected and will be optimized in
  subsequent releases.

## May 2026

- New documentation covers Signal's AI security, data protection, and trust posture, including LLM architecture, data isolation, and compliance certifications.

## April 2026

Black Duck Signal was released for general availability. Capabilities include the following:

- **Signal Developer**: Scan your changes thru the Black Duck MCP, an IDE or Bridge CLI.
- **Signal Enterprise**: Scan an entire project in your pipeline to generate a SARIF report for Polaris or any platform that supports SARIF.

- See the [FAQ here](https://community.blackduck.com/s/article/Signal-FAQ).
- Read the overview in documentation.
