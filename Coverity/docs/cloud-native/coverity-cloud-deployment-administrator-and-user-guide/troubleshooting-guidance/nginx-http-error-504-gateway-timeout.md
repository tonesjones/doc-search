---
title: "NGINX HTTP error 504: Gateway Timeout"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nginx-http-error-504-gateway-timeout.html"
content_id: "jKF~AC7vO~mydS7ykZAh1w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:47.375651+00:00"
---

# NGINX HTTP error 504: Gateway Timeout

If the Coverity cloud deployment uses NGINX for ingress, and if Coverity Connect Web
users who request 'Users and Groups' data begin to experience [504 Gateway
Timeout](https://http.dev/504) errors, the Coverity cloud administrator can try the solutions
described within the following sections to resolve the timing issue.

This issue might occur if you have a very large Connect PostgreSQL database. If Coverity
Connect Web users who request data begin to experience 504 Gateway Timeout errors,
perform one of the following procedures to change the NGINX ingress proxy timeout
values:

**Recommended procedure: Change the NGINX ingress proxy timeout Helm key values**

1. If you are deploying only Connect in the cloud, disable TLS sidecar on the
   `cim-web` pod. See Disable TLS sidecar on the cim-web pod.
2. In the `cnc` Helm chart, edit the
   `cim.cimweb.tlsSidecar.nginxConfig.proxy_..._timeout` key
   value(s) as needed with larger timeout values that override the default NGINX
   proxy timeout values. See Change the NGINX ingress proxy timeout Helm key values.
3. Re-deploy Coverity cloud (cnc) to apply the Helm chart annotations. See NGINX redeploy Coverity cloud.
4. The steps above should solve the immediate timeout issue. Next, to improve response
   time and prevent future timeouts, it is important to maintain PostgreSQL database
   size and integrity. Once you optimize the database size, you can then reset the
   timeout annotations to a smaller value. To optimize and maintain the database,
   see:
   - For a short list of important database optimization procedures, see Managing database size and integrity.
   - For a complete list of database optimization procedures, see Managing Connect PostgreSQL database size and integrity.

**Alternate procedure: Create NGINX ingress proxy timeout annotations**

1. If you are deploying only Connect in the cloud, disable TLS sidecar on the
   `cim-web` pod. See Disable TLS sidecar on the cim-web pod.
2. In the `cnc` Helm chart, Create NGINX ingress proxy timeout
   annotations with larger timeout values that override the default NGINX proxy timeout
   values. See Create NGINX ingress proxy timeout annotations.
3. Re-deploy Coverity cloud (cnc) to apply the Helm chart annotations. See NGINX redeploy Coverity cloud.
4. The steps above should solve the immediate timeout issue. Next, to improve response
   time and prevent future timeouts, it is important to maintain PostgreSQL database
   size and integrity. Once you optimize the database size, you can then reset the
   timeout annotations to a smaller value. To optimize and maintain the database,
   see:
   - For a short list of important database optimization procedures, see Managing database size and integrity.
   - For a complete list of database optimization procedures, see Managing Connect PostgreSQL database size and integrity.

**Alternate procedure: Set proxy timeouts in the NGINX configMap**

1. If you are deploying only Connect in the cloud, disable TLS sidecar on the
   `cim-web` pod. See Disable TLS sidecar on the cim-web pod.
2. In an NGINX configMap file, add NGINX ingress proxy timeout configurations with
   larger timeout values. See Alternate method: Set proxy timeouts in the NGINX configMap.
3. Restart the `cim` web pod to apply the configMap change. See Restart the cim-web pod.
4. The steps above should solve the immediate timeout issue. Next, to improve response
   time and prevent future timeouts, it is important to maintain PostgreSQL database
   size and integrity. Once you optimize the database size, you can then reset the
   timeout annotations to a smaller value. To optimize and maintain the database,
   see:
   - For a short list of important database optimization procedures, see Managing database size and integrity.
   - For a complete list of database optimization procedures, see Managing Connect PostgreSQL database size and integrity.
