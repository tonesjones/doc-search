---
title: "Set the Scan Service storage retention period"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/set-the-scan-service-storage-retention-period.html"
content_id: "nwtji5WObx5F_Y8mtiyV9w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:41.013960+00:00"
---

# Set the Scan Service storage retention period

Scan Service storage retention period enables you to control how long scan artifacts are
kept in the Scan Service storage, thereby managing the cost of that storage space.

Scan Service can be configured to delete terminated jobs from Scan Service storage when a
defined retention time period is met. This time period begins when the job is completed,
failed or canceled, and ends when the retention period is met. When the retention period
is met, Scan Service deletes all scan artifacts for the job, including storage objects
used or produced by the job.

If you are installing Scan Service in the cloud, enable and set the retention period on
the Scan Service storage using the following Helm keys, one to enable retention period
and one to set retention period.

See the following excerpt from the `scan-services` chart >
`values.yaml` file:

```
scan-service:
  retention:
    enabled: true
    minutes: 43200
```

The default value is `43200` minutes = 30 days. The minimum retention
period is `4320` minutes (3 days). Black Duck recommends 30 days.

For further information, see:

- For Helm keys, see scan-services Helm subchart: Helm keys.
- For storage bucket sizing information, see .
