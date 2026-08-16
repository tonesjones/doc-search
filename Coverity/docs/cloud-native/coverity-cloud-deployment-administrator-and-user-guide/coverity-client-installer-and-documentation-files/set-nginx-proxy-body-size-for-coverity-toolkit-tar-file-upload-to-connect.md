---
title: "Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/set-nginx-proxy-body-size-for-coverity-toolkit-tar-file-upload-to-connect.html"
content_id: "iFhwAp4MGS2nZGYV5Iejhg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:35.186615+00:00"
---

# Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect

If you will be deploying Scan Service, then you must set the following NGINX variable to
successfully upload a Coverity toolkit tar file to Coverity Connect. You do this by
changing the `proxy-body-size` value to the size (or greater) of the
Coverity toolkit tar file that you need to upload to Connect. The default
`proxy-body-size` value is 1 MB.

Having `proxy-body-size` set to any value that is smaller than a file
being uploaded returns an error 413 (Request Entity Too Large) and the file transfer
fails.

To set the `proxy-body-size` value, after you have downloaded the Coverity
toolkit tar file from the Black Duck registry:

1. Look up the size of the `coverity-all-platforms-2026.6.0.tar.gz` Coverity toolkit tar file that you downloaded from the Black Duck
   registry.
2. Create an annotation in the `cim.ingress.annotations` Helm key to
   define the `proxy-body-size` value. For information on the
   `cim.ingress.annotations` Helm key, see cim.ingress Helm keys.

   The annotation syntax is:

   ```
   nginx.ingress.kubernetes.io/proxy-body-size: <fileSize>
   ```

   Setting `proxy-body-size` to `<fileSize>` allows
   you to transfer files as large as `<fileSize>` through the
   ingress port.

For example, if the `coverity-all-platforms-2026.6.0.tar.gz` file is 7.6 GB, you might set `proxy-body-size` to
`8g` as an annotation in the `values.yaml` file or
equivalent:

```
cim:
  ingress:
    annotations:
      nginx.ingress.kubernetes.io/proxy-body-size: 8g
```

Optionally, you can set `proxy-body-size` to `0` to disable
checking of the client request body size.
