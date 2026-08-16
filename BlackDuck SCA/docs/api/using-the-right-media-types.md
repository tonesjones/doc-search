---
title: "Using the right media types"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-the-right-media-types.html"
content_id: "zRk9wOsR8KO1K8cTRLmr2A"
version: "2026.7"
section: "Getting Started with the Black Duck API"
scraped_at: "2026-08-08T15:32:39.198255+00:00"
---

# Using the right media types

The Black Duck API uses **custom media types** to ensure stable
and versioned responses.

Specify the media type in the `Accept` and `Content-Type`
headers of your request. This ensures backward compatibility and consisten reponses.

Example:

```
Content-Type: application/vnd.blackducksoftware.user-4+json
Accept: application/vnd.blackducksoftware.user-4+json
```

Note: You can find the recommended media types listed next to each endpoint in the REST API
documentation.

## Why media types matter

Media types (also known as MIME types) are used in API requests and responses to
specify the format of the data being exchanged. In Black Duck,
media types serve an additional, important purpose: they ensure backward
compatibility and versioned stability of the API.

Each API endpoint may support one or more custom Black Duck
media types. By explicitly specifying a media type in your request headers, you
ensure that:

- You receive a predictable and structured response.
- Your integration continues to work even if the underlying API evolves.
- The correct version of a resource is returned, especially if multiple versions
  exist.

Failing to set the correct media type (e.g., using `application/json`
as a generic fallback) may result in unsupported behavior, incomplete data, or even
failed requests—especially for endpoints that return complex or versioned
resources.

Tip: You can find the correct media type for each endpoint in the REST API
documentation.

## Examples of using media types

Here are some practical examples of how to use media types when working with the Black Duck API.

**Example 1: Setting Accept and Content-Type headers**

When making a `PUT` or `POST` request with a request
body, you typically include both `Content-Type` and
`Accept` headers.

```
PUT /api/users/{userId}
Content-Type: application/vnd.blackducksoftware.user-4+json
Accept: application/vnd.blackducksoftware.user-4+json
```

This tells the server:

- The request body is formatted according to `user-4+json`
- You expect the response to also be in that format

**Example 2: GET request for a project**

```
curl -X GET \
    https://<your-black-duck-server>/api/projects
    -H "Accept: application/vnd.blackducksoftware.project-detail-7+json
    -H "Authorization: Bearer <your-bearer-token>
```

This returns a list of projects in a versioned, structured JSO format that the client
knows how to handle.

**Example 3: Receiving a BDIO ZIP**

Some endpoints, like those related to data import/export, return or accept binary
data (e.g., BDIO):

```
application/vnd.blackducksoftware.bdio+zip
```

You would use this media type when downloading or uploading BDIO scan archives.
