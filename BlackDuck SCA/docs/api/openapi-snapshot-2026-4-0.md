---
title: "Black Duck SCA 2026.4.0 public OpenAPI snapshot"
source_url: "/api-doc/openapi3-public.json"
source_type: "server-generated OpenAPI specification"
version: "2026.4.0"
captured_at: "2026-09-03T12:33:53-07:00"
sha256: "75860E37AB7F77D9102D682C0205AFCD73079380F1BC131B2422D2B0D3316E56"
---

# Black Duck SCA 2026.4.0 public OpenAPI snapshot

The raw specification is stored at:

`sources/openapi/2026.4.0/openapi3-public.json`

It identifies itself as OpenAPI 3.0.1 for Black Duck REST API version 2026.4.0.
It was downloaded from the public API-documentation endpoint of a Black Duck SCA
server. The saved file is 1,504,928 bytes.

## How to use this source

Use the snapshot for exact, version-specific REST details such as:

- endpoint paths and HTTP methods;
- accepted request and response media types;
- request and response examples;
- constraints explicitly stated in examples.

Use the narrative Markdown corpus for concepts, workflows, configuration, and
behavioral explanations. When the snapshot and the pinned 2026.7 documentation
are used together, disclose the version difference.

The specification frequently references a generic object schema and may list only
successful responses. Do not infer undocumented request fields, status-code meanings,
validation behavior, or algorithm details.

## Confirmed `/api/snippet-matching` details

The OpenAPI path is `/snippet-matching`; the declared server base is `/api`, making
the effective endpoint `POST /api/snippet-matching`.

The operation accepts:

- `text/plain` containing between 300 and 50,000 non-whitespace characters; or
- `application/vnd.blackducksoftware.bill-of-materials-6+json` containing fingerprints.

A successful response uses
`application/vnd.blackducksoftware.bill-of-materials-6+json`. The example groups
matches by license family and includes project, release, license, matched file path,
and source/matched line regions.

The snapshot documents only a `200` response for this operation. It does not explain
HTTP 412, similarity thresholds, fuzzy-matching sensitivity, or a line-count limit.
