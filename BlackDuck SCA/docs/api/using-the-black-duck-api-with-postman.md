---
title: "Using the Black Duck API with Postman"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-the-black-duck-api-with-postman.html"
content_id: "T4UU1XLaJr1yqgqJP11Khw"
version: "2026.7"
section: "Getting Started with the Black Duck API"
scraped_at: "2026-08-08T15:32:39.758419+00:00"
---

# Using the Black Duck API with Postman

Postman is a popular tool for exploring and testing APIs without writing any code. Black Duck provides an official Postman collection that you can
import and use to try out API endpoints with your own instance.

## Why use Postman?

Postman makes it easy to:

- Explore and test API endpoints in a visual interface
- Authenticate using API tokens
- Send requests and view responses without writing scripts
- Save common requests as part of a reusable collection

It's especially helpful if you're new to the API or just want to experiment with
functionality before automating anything.

## Importing the Black Duck Postman collection

1. Open a browser and log in to your Black Duck instance.
2. Navigate to the following URL, replacing the server name as needed:

   ```
   https://<your-black-duck-server>/api-doc/postman-collection-public.json
   ```
3. Right-click anywhere on the page and Save As
   `postman-collection-public.json`.
4. Open Postman and import the saved file:

   - Clicking Import int he top-left corner of Postman.
   - Choose the file you just saved.
5. The collection will now appear in your Postman sidebar, organized into
   folders by endpoint category.

## Setting up authentication in Postman

To use the API, you'll need to authenticate using an API token. This process involves
generating a bearer token and using
it in your requests.

In Postman, create a new request:

- Method: `POST`
- URL:
  `https://<your-black-duck-server>/api/tokens/authenticate`
- Headers:

  - `Accept:
    application/vnd.blackducksoftware.user-4+json`
  - `Authorization: token <your-api-token>`

Copy the `bearerToken` from the response. You can now use the token
for all future API calls:

- In Postman, go to your collection or request.
- Under the Authorization tab, set:

  - Type: `Bearer Token`
  - Token: Paste your bearer token

Alternatively, use the `Authorization: Bearer <token>` header
manually in each request.

## Making your first API request

With authentication configured, try a simple request like retrieving all
projects:

- Method: `GET`
- URL: `https://<your-black-duck-server>/api/projects`
- Header: `Accept:
  application/vnd.blackducksoftware.project-detail-7+json`

Hit **Send**, and you should see the response from your Black Duck instance in the lower pane.

Fastpath:

For more information on how to authenticate, see Authenticating with the API.

To dive deeper into request structure, see Using
the right media types.
