---
title: "Setting up TLS and certificates for analysis in the cloud"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-tls-and-certificates-for-analysis-in-the-cloud.html"
content_id: "rn2ocA8j6Ftol7ih_XHSiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:32.407581+00:00"
---

# Setting up TLS and certificates for analysis in the cloud

When you perform analyses in the cloud using Coverity Scan Service, you must enable TLS
(SSL) since the source code to be analyzed might be uploaded through a public network.
Follow these steps to enable TLS:

1. In the `coverity.yaml` configuration file, specify
   `https` in the Coverity Connect URL.
2. Set the Coverity CLI configuration value `on-new-cert` to
   distrust.

   For more information on this setting, refer to "Connect configuration"
   in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

The following excerpt from a sample `coverity.yaml` configuration file
shows how to configure these settings when performing an analysis in the cloud. Some
significant values are in bold.

```
analyze:
  # The following specifies that the analysis is done in the cloud.
  location: connect

commit:
  connect:
    # The following specifies the results stream.
    stream: my-stream

    # The following specifies the location of the Coverity Connect instance.
    # "https" indicates that TLS should be used.
    url: https://name.connect.com

    # The following specifies that unrecognized certificates should not be trusted.
    on-new-cert: distrust
```

For further information on editing the configuration file, refer to "Performing an
analysis in a Coverity Cloud deployment" in the Coverity Analysis 2026.6.0 User and Administrator Guide.
