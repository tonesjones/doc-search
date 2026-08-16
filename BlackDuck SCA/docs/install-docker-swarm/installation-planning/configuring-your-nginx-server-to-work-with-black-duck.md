---
title: "Configuring your NGiNX server to work with Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-your-nginx-server-to-work-with-black-duck.html"
content_id: "q5D4FUr0IclNx5Pn_vGGGg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:32.871707+00:00"
---

# Configuring your NGiNX server to work with Black Duck

[HUB-5055, HELPDESK-18723]If you have
an NGINX server acting as an HTTPS server/proxy in front of Black Duck,
you must modify the NGINX configuration file so that the NGINX server passes the correct
headers to Black Duck. Black Duck then
generates the URLs that use HTTPS.

Note: Only one service on the NGINX server can use https port 443.

To pass the correct headers to Black Duck, edit the
`location` block in the nginx.config configuration file to:

```
location / {
client_max_body_size 1024m;
proxy_pass http://127.0.0.1:8080;
proxy_pass_header X-Host;
proxy_set_header Host $host:$server_port;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
}
```

If the X-Forwarded-Prefix header is being specified in a proxy server/load balancer
configuration, edit the `location` block in the
`nginx.conf` configuration file:

```
location/prefixPath {
proxy_set_header X-Forwarded-Prefix "/prefixPath";
}
```

To scan files successfully, you must use the **context** parameter when using the
command line or include it in the **Black Duck Server URL** field in
the Black Duck Scanner.

Note: Although these instructions apply to an NGINX server, similar configuration changes would
need to be made for any type of proxy server.

If the proxy server will rewrite requests to Black Duck, let the proxy
server administrator know that the following HTTP headers can be used to preserve the
original requesting host details.

|  |  |
| --- | --- |
| **HTTP Header** | **Description** |
| X-Forwarded-Host | Tracks the list of hosts that were re-written or routed to make the request. The original host is the first host in the comma-separated list.  **Example:**   ``` X-Forwarded-Host: "10.20.30.40,my.example, 10.1.20.20" ``` |
| X-Forwarded-Port | Contains a single value representing the port used for the original request.  **Example:**   ``` X-Forwarded-Port: "9876" ``` |
| X-Forwarded-Proto | Contains a single value representing the protocol scheme used for the original request.  **Example:**   ``` X-Forwarded-Proto: "https" ``` |
| X-Forwarded-Prefix | Contains a prefix path used for the original request.  **Example:**   ``` X-Forwarded-Prefix: "prefixPath" ```   To successfully scan files, you must use the **context** parameter |
