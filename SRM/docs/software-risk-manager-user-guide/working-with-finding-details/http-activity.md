---
title: "HTTP Activity"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/http-activity.html"
content_id: "wadlNWEAKARS6Zfk~OGCTg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:25.765837+00:00"
content_hash: "85a3055e24b5b2d71ea8205dbc2d1d600ec2a9e6808912f1ae46817381bb9b67"
---

# HTTP Activity

The *Http Activity* section shows any detail Software Risk Manager knows about the
HTTP request and response associated with a DAST result.

[image: image]

The table at the top of the *HTTP Activity* section enumerates the "variants" of
request/response that were reported with the result. Some tools will attack the same URL
with different variations of query parameters and form parameters to try and find
vulnerabilities, then report each variant as part of the same result. Other tools will
report each variation as its own result, but if Software Risk Manager sees that
everything else is the same, it may join them together under a single result. Often
times, there is only one variant reported, as is the case in the screenshot above. In
cases where there are multiple variants, click on the different rows of the variants
table to show the details for that variant in the sections below.

For each variant, the details are described in the sections that follow.

## Request Tab

The details of the HTTP request are broken down here:

- **Query Params** will show any applicable query parameters (i.e. parts of the
  URL after the `?`, e.g. `?foo=1&bar=2`)
- **Request Headers** shows each of the headers sent with the HTTP request, as
  a table.
- **Request Body** shows the body data sent with the request, if applicable.
  This is where form parameters go, or any other arbitrary content being sent to
  the server.
- **Raw Request Data** shows the raw, un-parsed version of the request. Note
  that some tools don't report this, instead reporting specific details of the
  request. In these cases, the raw request will be reconstructed automatically.

## Response Tab

The details of the HTTP response are broken down here:

- **Response Headers** shows each of the headers sent with the HTTP response,
  as a table.
- **Response Body** shows the body data sent with the response, if applicable.
  Expanding it will show a text view of the raw response data. Note that response
  bodies are typically rather large, and are sometimes non-text data, which may
  make this view difficult to use. Software Risk Manager will not attempt to
  render whatever the data represents, since the assumption is that the response
  contained some vulnerability like cross-site scripting, or a malicious file.

## Metadata Tab

Some tools will report extra "metadata" with their HTTP activity. When applicable,
this data will be shown in the *Metadata Tab* as a table.
