---
title: "Configuring user session timeout"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-user-session-timeout.html"
content_id: "7EhVtCw27nUCj_YrXxcm~g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.053629+00:00"
content_hash: "96ecabc31bf13a8cb2e6ca2ab9cdf9d310d3d6b1d3978c7f9d4df4ac9dc69a5b"
---

# Configuring user session timeout

Configure the user session timeout value to automatically log out users from the Black Duck server, and align with your corporate security policy.

1. To view the current timeout value, make the following GET request:

   `GET https://<Black-Duck-server>/api/system-oauth-client`

   Note: Users must have read permission for the OAuth Client to use the GET method.
2. To change the current timeout value, make the following PUT request with the PUT request body.

   `PUT https://<Black-Duck-server>/api/system-oauth-client`

   [image: image]

   Note: Users must have permission to update the OAuth Client to use the PUT method for this task. The system administrator role includes the required permissions.

   The value that you type in the PUT request body is the new timeout value.

   Timeout values between 30 minutes (1800 seconds) and 24 hours (86400) are accepted.

The following media types are accepted:

```
application/vnd.blackducksoftware.user-4+json application/json
```

Here's an example in Postman:

  
 [image: image]   

In the following example, you change the timeout value from 7200 to 8000 seconds.

  
 [image: image]
