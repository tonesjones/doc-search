---
title: "Managing artifact upload to storage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-artifact-upload-to-storage.html"
content_id: "UX8cQe5nB~Hlkh~5j5gRiw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:41.663924+00:00"
---

# Managing artifact upload to storage

Coverity Analysis jobs upload a compressed (zip) copy of the analyzed intermediate
directory (idir), analysis output, `analysis-output.zip`, and execution
logs, `execLog.zip`, to storage service storage (bucket, blob). These
artifacts appear in the scan dashboard within the Connect UI. You can then download the
uploaded artifacts from the scan dashboard to assist in debugging and verifying a
scan.

If you are scanning a very large codebase, the compression and upload of the artifacts
can consume significant resources and time. A very large intermediate directory can take
many (40 +/-) minutes to upload. If you have very large projects, to save time and
reduce overall scan time, you can optionally prevent artifact uploads.

Within the Kubernetes cluster, a job runner performs the analysis and generates all of
the following artifacts:

- analyzed-idir.zip - Contains both the analysis output and the analyzed idir.
- analysis-output.zip - Contains the analysis output.
- execLog.zip - Contains the execution logs.

Using the following Helm key, located in the `scan-services` Helm
subchart, you can specify which artifacts are uploaded to the storage bucket and when
they are uploaded.

```
scan-service:
  jobRunner:
    uploadArtifacts: "None | OnFailure | LogsOnly | All"
```

For information on this Helm key, also see scan-service.jobRunner Helm keys.

Four options enable you to determine which artifacts are uploaded to storage service
storage (bucket, blob) and when they are uploaded. The options are:

- `All` - Default value. Upload all scan artifacts
  (`analyzed-idir.zip`, `analysis-output.zip`, and
  `execLog.zip`) to the storage bucket/blob, in both success and
  failure scenarios.
- `OnFailure` - If a scan completes without failure, do NOT
  upload any artifacts to the storage bucket. If a scan failure occurs, upload the
  artifacts `analyzed-idir.zip` and `execLog.zip` to the
  storage bucket/blob.
- `LogsOnly` - Upload execution logs,
  `execLog.zip` and analysis output,
  `analysis-output.zip`, to the storage bucket/blob. This is true
  for successful and failed scans.
- `None` - Upload nothing to the storage bucket/blob. This
  option saves time, However, it does not provide any information to help troubleshoot
  a potential scan issue.

Example: To upload the `analyzed-idir.zip` and
`execLog.zip` artifacts only when a scan fails. For a very large
codebase, this allows a successful scan to upload quickly, :

```
scan-service:
  jobRunner:
    uploadArtifacts: "OnFailure"
```
