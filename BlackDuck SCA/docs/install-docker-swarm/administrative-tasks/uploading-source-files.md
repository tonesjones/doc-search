---
title: "Uploading source files"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uploading-source-files.html"
content_id: "hznLOzBHgLVHqmsNkNcnsw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:56.514672+00:00"
---

# Uploading source files

BOM reviewers need to be able to easily confirm the results of a scan by confirming
matches and investigating false negatives. When reviewing snippet matches, seeing a
side-by-side comparison of the source file to the match can help in the evaluation and
review of the match.

Black Duck provides the ability for you to upload your source files so
that BOM reviewers can see the file contents from within the Black Duck
UI.

When you enable deep license data detection or copyright text search during scanning,
uploading source files enables BOM reviewers to view discovered license or copyright
text from within the Black Duck UI. When files are uploaded, Black Duck provides a list
of embedded licenses and copyright text and displays the highlighted text in the
file.

For a BOM reviewer to view file content from within the Black Duck UI:

1. Administrators must enable the upload of source files.

   1. The administrator enables the feature using an environment variable.
   2. The administrator optionally configures secrets encryption. Source code
      uploads for hosted customers are always encrypted.
2. The scan client sends the source file contents to the Black Duck instance via
   SSL/TLS-secured endpoint(s) and with the proper authorization token.

   The files are then encrypted. Uploaded
   files are stored using their associated scan identifier and file signature and
   not by their file name.

   In the Black Duck UI, the source file is transmitted via HTTPS
   over the network.

Note the following:

- Ensure that you have enough disk space for file uploads.
- The maximum total source size that you can upload at one time is 4 GB (4000 MB).
  This value is configurable.
- Uploaded files are deleted after 180 days. This value is configurable.
- Files are deleted when the upload service reaches 95% of the maximum disk
  setting.

  The service deletes the oldest files until the disk space is equal to 90% of the
  maximum disk setting.

## Enabling file upload

To enable file upload, set the `ENABLE_SOURCE_UPLOADS` environment variable In
the `blackduck-config.env` file located in the
`docker-swarm` directory, to true:

```
ENABLE_SOURCE_UPLOADS=true
```

## Enabling encryption of source code

To enable encryption of source code uploaded along with other sensitive data managed by the
storage service `BLACKDUCK_CRYPTO_ENABLED` must be set. See Configuring secrets encryption in Black
Duck for more information on secrets encryption.

Note: Source code uploads for hosted customers are always encrypted.
