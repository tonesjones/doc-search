---
title: "Frequently Recommended Black Duck Detect Properties"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/frequently-recommended-black-duck-detect-properties.html"
content_id: "jUzya4EilGNXAlpX4sMsHA"
version: "2026.7"
section: "Scanning Best Practices"
scraped_at: "2026-08-08T15:34:30.816822+00:00"
---

# Frequently Recommended Black Duck Detect Properties

Below are some of the more frequently used Black Duck Detect properties and their
use.

| Task | Property |
| --- | --- |
| Check for policy violations | - **--detect.policy.check.fail.on.severities**  A comma-separated list of policy violation severities that   will fail Black Duck Detect. If this is not set, Black Duck Detect will not fail due to policy   violations for full scans. - **--detect.timeout**  When using the policy check property above, you may need to   increase the timeout for larger, more complex projects. |
| Perform a Rapid Scan | - **--detect.blackduck.scan.mode=RAPID**  Use this property to run a package manager only, synchronous   scan, returning scan results to the command line, without   creating a BOM or saving results in Black Duck. Defaults to false. |
| Disable signature (also known as file system) scanning and rely on package manager scanning exclusively | - **--detect.tools=DETECTOR**  Runs the Detector tool only. |
| Include and exclude options to tune what gets analyzed by the Signature Scanner | - **--detect.blackduck.signature.scanner.exclusion.patterns**  Enables you to exclude the folder matching the absolute path   from the scanning target folder. - **--detect.blackduck.signature.scanner.exclusion.name.patterns**  Enables you to provide folder patterns to exclude. Black Duck Detect will search all folders inside the   scanning target and then exclude those matching the supplied   patterns. - **--detect.blackduck.signature.scanner.paths**  Enables you to specify that these paths and only these paths   will be scanned for full scanning. |
| Enable Correlated Scanning | - **--detect.blackduck.correlated.scanning.enabled**  When enabled, Black Duck Detect activates the   Black Duck SCA correlated scanning   capability to enhance match accuracy. The correlated   scanning capability must be present and enabled in your   Black Duck SCA server before you   enable the correlated scanning feature in Black Duck Detect. |
