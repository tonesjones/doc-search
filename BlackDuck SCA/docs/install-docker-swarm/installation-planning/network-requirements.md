---
title: "Network requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/network-requirements.html"
content_id: "iyjiqk71PbkL8vDBg5EtTg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:30.049108+00:00"
---

# Network requirements

Black Duck SCA requires the following ports to be externally
accessible:

- Port 443 – Web server HTTPS port for Black Duck SCA via NGiNX
- Port 55436 – Read-only database port from PostgreSQL for reporting

If your corporate security policy requires registration of specific URLs, connectivity
from your Black Duck SCA installation to Black Duck Software
hosted servers is limited to communications via HTTPS/TCP on port 443 with the following
servers:

- updates.suite.blackducksoftware.com (to register your software)
- kb.blackducksoftware.com (access Black Duck KB data)
- https://auth.docker.io/token?scope=repository/blackducksoftware/blackduckregistration/pull&service=registry.docker.io
  (access to Docker Registry)

Note: If you are using a network proxy, these URLs must be configured as destinations in your
proxy configuration.

## Allow list addresses and IP ranges

Note: HTTPS is used for all traffic to Black Duck SCA. IPs that include a subnet
mask (for example, /22 in 103.21.244.0/22) represent a range of IPs, all of which
should be allow listed to ensure Black Duck SCA functions as
intended.

Ensure that the following addresses and IPs are on the allow list:

| Domain | IP Address(es) |
| --- | --- |
| kb.blackducksoftware.com | 34.160.126.173, 34.149.112.69, 34.111.46.24, 35.224.73.200, 35.242.234.51, 35.220.236.106 |
| updates.suite.blackducksoftware.com | 35.244.241.173 |
| scass.blackduck.com | 35.244.200.22 |
| na.scass.blackduck.com | 35.244.200.22 |
| na.store.scass.blackduck.com | 34.54.95.139 |
| eu.store.scass.blackduck.com | 34.54.213.11 |
| eu.scass.blackduck.com | 34.54.38.252 |
| repo.blackduck.com | 34.149.5.115 |
| production.cloudflare.docker.com | 173.245.48.0/20, 103.21.244.0/22, 103.22.200.0/22, 103.31.4.0/22, 141.101.64.0/18, 108.162.192.0/18, 190.93.240.0/20, 188.114.96.0/20, 197.234.240.0/22, 198.41.128.0/17, 162.158.0.0/15, 104.16.0.0/13, 104.24.0.0/14, 172.64.0.0/13, 131.0.72.0/22 |
| hub.docker.com | 44.219.3.189, 3.224.227.198, 44.193.181.103 |
| docker.io | 44.219.3.189, 3.224.227.198, 44.193.181.103 |
| auth.docker.io | 34.226.69.105, 54.196.99.49, 3.219.239.5 |
| registry-1.docker.io | 54.196.99.49, 3.219.239.5, 34.226.69.105 |
| github.com | 140.82.116.4 |
| static.cloud.coveo.com |  |
| search.cloud.coveo.com |
| platform.cloud.coveo.com |
| platformhipaa.cloud.coveo.com  (for HIPAA compliant deployments) |

Note:

Customers not utilizing the AI-assisted documentation search can still modify the
CSP headers by using environment variables for the
`blackduck-nginx` container:

```
HUB_CSP_HEADER=default-src 'none'; connect-src 'self'; object-src 'self'; script-src 'self'; 
img-src 'self' data: https://s3.amazonaws.com/cloud.ohloh.net/; style-src 'self' 'unsafe-inline'; 
font-src 'self'; frame-ancestors 'self'; frame-src 'self';
```

## Verifying connectivity

To verify connectivity, use the cURL command as shown in the following example.

```
curl -v https://kb.blackducksoftware.com
```

Tip: It's good to check connectivity on the Docker host but it's better to verify the
connectivity from within your Docker network.

## IPv4 and IPv6 networks

Black Duck SCA supports IPv4 and IPv6 for ingress and egress traffic. This
includes connectivity between Black Duck components, the KnowledgeBase, customer
systems, and internet-facing networking pods.

For deployments in IPv6-only environments, ensure that your networking configuration
supports IPv6 routing for all required communication paths.
