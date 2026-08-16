---
title: "Concurrent execution"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/concurrent-execution.html"
content_id: "jjxFDWLQC976B4nur4bgFg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:36.408917+00:00"
---

# Concurrent execution

Concurrent execution of Black Duck® SCA by the same user can result in collisions as the Detect script,
the Detect .jar, the Detect inspectors, and the Black Duck Signature Scanner
are each downloaded to the same default location during execution. There are also potential race conditions that
can occur when multiple concurrent runs of Detect create or update the same Black Duck SCA
project/version or codelocation.

Concurrent execution of Detect runs that include Docker image inspection involves additional
challenges. For that scenario, we recommend engaging Professional Services for a solution tailored to your environment.
The rest of this page addresses scenarios that do not involved inspecting Docker images.

The recommended way for a single user to execute multiple Detect runs concurrently and
avoid the collisions mentioned above is to:

1. Run Detect using the air gap capability. This avoids downloading the Detect script, .jar, or inspectors during execution.
2. Manually download and install the Black Duck Signature Scanner, and point Detect to it. This avoids downloading the Black Duck Signature Scanner during execution.
3. Ensure that concurrent runs do not attempt to create or update the same Black Duck SCA project/version, or the same codelocation.

To accomplish the first two:

1. Log into Black Duck SCA, and under Tools > Legacy Downloads, download and unzip the Black Duck Signature Scanner.
2. Download the Detect "no docker" air gap zip from the location specified in download locations, and unzip it. More details on using air gap mode can be found on the air gap page.
3. Run Detect as shown in this example:

```
java -jar {airgap dir}/detect-{version}.jar --detect.blackduck.signature.scanner.local.path={scan.cli-yourBlackDuckVersion dir}
```
