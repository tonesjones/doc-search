---
title: "Analyze Connect configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyze-connect-configuration.html"
content_id: "nAbro3MR4yTqRfkFFWK5dA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:11.980562+00:00"
---

# Analyze Connect configuration

Use these values to define the Coverity Connect configuration.

| Key | Type | Description |
| --- | --- | --- |
| `auth-key-file` | string | The authentication key file to use when authenticating to Coverity Connect to perform analysis. Default: $HOME/.coverity/ak-hostname-port |
| `ca-certs-file` | string | The name of a file that contains additional certificates to trust in addition to the ones in the system certificate store and the Coverity TFT (Trust First Time) store. Default: system CA certificates |
| `proxy-client-cert-file` | string | Specifies the file containing the client certificate in PEM format, that should be presented to the proxy when making a request. |
| `proxy-client-key-file` | string | Specifies the file containing the client certificate private key in PEM format , for the `proxy-client-cert-file`. |
| `proxy-url` | string | A URL for a forward proxy to use when communicating with Coverity Connect. This must be a secure `https` scheme. If not specified, no proxy is used. You can also specify the proxy server URL by using the environment variable `HTTPS_PROXY` (or its lowercase equivalent `https_proxy`).  **Proxies and WebSocket requests:** The proxy server must support the use of WebSocket requests. To determine whether your server supports proxying WebSocket requests, refer to the server's documentation; if it does, use the documentation to learn how this can be configured. |
| `upload-artifacts` | string | Specifies artifacts to upload following analysis when the analysis location is Connect. Valid values are `"All"` (the default), `"LogsOnly"`, `"None"`, and `"OnFailure"`. |
| `url` | string | **Required**: The absolute URL of the Coverity Connect instance where you want to perform the analysis. |
