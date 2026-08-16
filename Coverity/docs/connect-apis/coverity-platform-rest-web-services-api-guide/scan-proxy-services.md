---
title: "Scan Proxy Services"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-proxy-services.html"
content_id: "8W9WJqyXuVTw28_hkXYCzg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:43.344634+00:00"
---

# Scan Proxy Services

The Coverity REST Scan Proxy Services API allows you to send requests
to Coverity Connect and receive responses from it.

You can find usage examples for all API operations in this section, grouped by
resource.

These proxy services are available only when scan-services is enabled.

- Get a scan list
- Update a scan resource
- Get a scan status
- Get the job details associated with a scan

## How to Access the Coverity Scan Proxy Service API Swagger Doc

You can access detailed reference documentation for Scan Proxy API operations at the following
URL:

```
<scheme>://<my_connect_host>:<port>/swagger/scan/index.html
```

where `<scheme>` is either `http` or
`https`, depending on how you configured your Coverity Connect
server, and `<my_connect_host>:<port>` are the host and
port of your Coverity Connect server.

The reference documentation is written to the [OpenAPI Specification (OAS) format, version 3](https://swagger.io/specification/v3/), and describes the URI
formats, input parameters, request schemas, and response schemas of the
operations.

You can access the OAS YAML file (from which the `index.html` file is
generated) at the following URL:

```
<scheme>://<my_connect_host>:<port>/swagger/scan/openapi.yaml
```

Note: See also: Coverity Platform REST Scan Proxy Services API (v2)

You can access a JSON transformation of this YAML file at the following URL:

```
<scheme>://<my_connect_host>:<port>/swagger/scan/openapi.json
```

## Get a Scan List

Attention: Long response times may occur when filtering large sets of scan data from this request.

Example GET request to retrieve a scan list.

Example usage:

- Filter scans by state
- Filter scans by project name
- Filter scans by stream name
- Filter scans by username

**cURL Request**

```
curl --location '<url>/api/v2/scans?state=RUNNING&offset=0&project=Test&stream=Test&user=admin&limit=3' \
     --user my_username:my_password
```

**Response Body**

```
{
  "scans": [
    {
      "scanId": "string",
      "failureInfo": "string",
      "progress": 0,
      "priority": 0,
      "state": "RUNNING",
      "createdAt": "string",
      "version": "string",
      "labels": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "meta": {
    "limit": 0,
    "offset": 0,
    "totalCount": 0
  }
}
```

## Update a Scan Resource

Example PATCH request to update a scan resource.

Example usages:

- Cancel a scan in the QUEUED or RUNNING state.
  - Only the CANCELLED
    state is allowed in the request body.
- Update the priority of a scan in the QUEUED state.
  - Set priority
    between 1 and 4 in the request body. By default, a QUEUED scan has
    priority 4. Setting priority to 1 will dispatch the scan before
    those with priority 4.

**cURL Request**

```
curl --location --request PATCH '<url>/api/v2/scans/<id>' \
     --header 'Content-Type: application/json' \
     --user my_username:my_password \
     --data '{
         "scan": {
             "priority": 4,
             "state": "CANCELLED"
         }
    }'
```

**Response Body**

There is no response body for this request, which returns the status code 204
(No Content).

## Get a Scan Status

Example GET request to retrieve the status of a scan.

**cURL Request**

```
curl --location '<url>/api/v2/scans/<id>/status' \
     --user my_username:my_password
```

**Response Body**

```
{
  "scanId": "string",
  "failureInfo": "string",
  "progress": 0,
  "priority": 0,
  "state": "QUEUED",
  "createdAt": "string",
  "version": "string",
  "labels": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```

## Get the Job Details Associated with a Scan

Example GET request to retrieve the details of a scan.

Example usages:

- Correlate the snapshot ID with the scan ID by checking metadata in the
  details section after scan completion.
- Check artifacts linked to the scan ID

**cURL Request**

```
curl --location '<url>/api/v2/scans/<id>/jobs' \
     --user my_username:my_password
```

**Response Body**

```
[
  {
    "jobId": "string",
    "scanId": "string",
    "config": {
      "jobType": "string",
      "toolConfig": {
        "analysisConfig": {
          "storageId": "string",
          "toolVersion": "string"
        },
        "connectConfig": {
          "endpoint": "string",
          "streamId": "string"
        }
      }
    },
    "state": "QUEUED",
    "errorInfo": {
      "osProcessInfo": {
        "commandArguments": [
          "string"
        ],
        "executable": "string",
        "exitCode": 0
      },
      "errorMsg": "string"
    },
    "progress": 0,
    "details": {
      "analysis": {
        "summary": {
          "auditSeverity": 0,
          "highSeverity": 0,
          "lowSeverity": 0,
          "mediumSeverity": 0
        },
        "outputStorage": {
          "analyzedIdir": "string",
          "execLog": "string"
        },
        "metadata": {
          "snapshotId": "string"
        }
      }
    },
    "lastUpdatedAt": "string",
    "createdAt": "string",
    "artifactInfo": [
      {
        "id": "string",
        "name": "string",
        "isGenerated": true,
        "createdAt": "string"
      }
    ]
  }
]
```
