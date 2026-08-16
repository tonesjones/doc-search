---
title: "Downloading scan artifacts using the Coverity CLI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-scan-artifacts-using-the-coverity-cli.html"
content_id: "4MA4gmzBmsWXqUCFds0BBQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:38.811777+00:00"
---

# Downloading scan artifacts using the Coverity CLI

The Coverity CLI contains a `coverity scan-status` command that you can
use to download artifacts for a given scan. For help with this command, enter the
following help command:

```
coverity scan-status --help
```

You can use the following command options to download the desired scan artifacts:

- `--artifact-name`: Specifies the artifact to download. The default
  value is `execLog.zip`. Other values include
  `analyzed-idir.zip` and
  `analysis-output.zip`.
- `--output-file`: Specifies the filename to save the downloaded
  artifact as.
- `--job-id`: Specifies the scan job ID, and defaults to the latest
  job for the scan (as stored in the idir).
