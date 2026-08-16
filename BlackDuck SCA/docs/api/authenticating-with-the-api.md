---
title: "Authenticating with the API"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authenticating-with-the-api.html"
content_id: "dRQZ8kbNy06MPUwhy3g6_Q"
version: "2026.7"
section: "Getting Started with the Black Duck API"
scraped_at: "2026-08-08T15:32:38.619296+00:00"
---

# Authenticating with the API

Black Duck uses API tokens for authentication. This approach improves
security and makes it easier to integrate with external tools.

## Step 1: Generate an API token

1. Log into the Black Duck UI.
2. From the top-right menu, select **System** → **Access Tokens**.
3. Click **Create New Token** and follow the prompts.

   - Name the token
   - (Optional) Add a description
   - Choose **Read Access Only** or **Read and Write Access**
   - Click **Create**.
4. Save the token somewhere safe. For security reasons, it will only be shown once.

## Step 2: Exchange the token for a bearer token

Make an HTTP `POST` request to:

```
/api/tokens/authenticate
```

Include your API token in the Authorization header:

```
curl -X POST \
    https://<your-black-duck-server>/api/tokens/authenticate \
    -H "Accept: application/vnd.blackducksoftware.user-4+json" \
    -H "Authorization: token <your-api-token>"
```

This returns a **Bearer token**, which you use to authorize all subsequent API
requests.

## Step 3: Use the Bearer token in your requests

Example:

```
curl -X GET \
    https://<your-black-duck-server>/api/projects/ \
    -H "Authorization: Bearer <your-bearer-token> \
    -H "Accept: application/vnd.blackducksoftware.project-detail-4+json" \
```

## Changing the expiration time for a bearer token

To extend the expiration time of a bearer token used in REST API, use the
`docker-compose.local-overrides.yml` file to override the
default setting by configuring the
`HUB_AUTHENTICATION_ACCESS_TOKEN_EXPIRE` environment variable
with the new expiration value in seconds.

The `HUB_AUTHENTICATION_ACCESS_TOKEN_EXPIRE` property is the
number of seconds that the access tokens take to expire.

Note: The expiration configuration change only works for API tokens that are created after you
change the setting in the `docker-compose.local-overrides.yml`
file. The expiration time that you configure isn't updated for existing database
records/API tokens when the setting is changed and the service is
restarted.
