---
title: "Required URLs for Proxy Access"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/required-urls-for-proxy-access.html"
content_id: "XbsDE_BP0_Vk8OjxWM5rOw"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:55.368047+00:00"
---

# Required URLs for Proxy Access

If your corporate security policy requires registration of specific URLs, connectivity
from your Black Duck server to Black Duck hosted
servers is limited to communications via HTTPS/TCP on port 443 with the following
server:

| Domain | IP Address(es) |
| --- | --- |
| <yourcompanyname>.blackduck.com | <IP address> |
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

Companies that wish to enhance the security of their Black Duck server
should configure their firewalls to block external communications on other ports or
to/from other machines outside their firewall.
