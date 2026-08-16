---
title: "Polaris IP ranges"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-ip-ranges.html"
content_id: "1Lm9ndys1q8mb6062A~EMQ"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:55.866654+00:00"
content_hash: "3b3380bee1558732607e0ae759c22a59fe05cfc98fa635059fe4696ed44645c0"
---

# Polaris IP ranges

Add the IPs on this page to your allow list.

Note: HTTPS is used for all traffic to Polaris. IPs that include a subnet mask (for example, /22 in 103.21.244.0/22) represent a range of IPs, all of which should be allow listed to ensure Polaris functions as expected.

## The Polaris user interface and APIs

### North American and European instances

The user interface and APIs for American and European instances of Polaris are domain-fronted by CloudFlare.

- 103.21.244.0/22
- 103.22.200.0/22
- 103.31.4.0/22
- 104.16.0.0/13
- 104.24.0.0/14
- 108.162.192.0/18
- 131.0.72.0/22
- 141.101.64.0/18
- 162.158.0.0/15
- 172.64.0.0/13
- 173.245.48.0/20
- 188.114.96.0/20
- 190.93.240.0/20
- 197.234.240.0/22
- 198.41.128.0/17

Note: Find Cloudflare IP ranges (IPv4) here: <https://www.cloudflare.com/ips>.

### Saudi Arabian instance

The user interface and APIs for the Saudi Arabian instance of Polaris are domain-fronted by Google Cloud Armor.

- 34.1.59.210

## Black Duck Support

Request support (and monitor your support cases) in the Black Duck Community: <https://community.blackduck.com>.

- 34.226.36.53

## Artifacts

Black Duck artifacts (like Bridge CLI) are stored at <https://repo.blackduck.com> (formerly, <https://sig-repo.synopsys.com>).

- 34.149.5.115

Important: To ensure Polaris continues to function as expected, keep <https://sig-repo.synopsys.com> (34.110.245.127) on your allow list until September 30, 2025.

## Storage service

Test artifacts are sent to a Polaris storage service using IPs that vary between Polaris instances.

Table 1. IPs for storage services

| Polaris instance | DNS | IPs |
| --- | --- | --- |
| America, production | <https://store.polaris.blackduck.com> (formerly, <https://store.polaris.synopsys.com>) | - 34.120.169.184 |
| America, POC | <https://store-poc.polaris.blackduck.com> (formerly, <https://store-poc.polaris.synopsys.com>) | - 34.49.227.145 |
| European Union, production | <https://store-eu.polaris.blackduck.com> (formerly, <https://store-eu.polaris.synopsys.com>) | - 34.36.5.64 |
| Kingdom of Saudi Arabia, production | <https://store-ksa.polaris.blackduck.com> | - 34.102.191.134 |

Important: <https://store.polaris.synopsys.com> (34.110.190.234), <https://store-poc.polaris.synopsys.com> (34.95.76.31), and <https://store-eu.polaris.synopsys.com> (34.120.192.89) will continue to function until September 30, 2025. Update your allow list before September 30, 2025 to avoid issues.

## Integrations

Polaris integrations (including SCM integrations) rely on IPs that vary between Polaris instances.

Table 2. Integration IPs

| Polaris instance | IPs (outbound) |
| --- | --- |
| America, production | - 35.225.126.189 - 35.193.82.82 - 34.136.219.177 - 34.170.207.134 - *34.73.103.42* - *34.148.68.248* - *34.74.71.40* - *34.148.196.234* |
| America, POC | - 34.69.14.244 - 34.67.166.17 - 34.132.152.19 - 104.197.46.146 |
| European Union, production | - 34.159.207.114 - 34.141.42.119 - 35.242.204.246 - 35.242.235.223 - *35.241.205.168* - *34.76.231.77* - *35.205.114.247* - *130.211.71.188* |
| Kingdom of Saudi Arabia, production | - 34.166.64.192 - 34.166.137.13 - 34.166.160.6 - 34.166.121.67 |

Note: If a large-scale outage occurs, traffic for production instances is redirected via *disaster recovery IPs*. Redirection is only available for the American and European production instances.

## Monitoring

Polaris is monitored via <https://rum-http-intake.logs.datadoghq.com>.

- 3.233.144.0/20

Note: You can find regional Datadog IP ranges here: <https://ip-ranges.datadoghq.com/synthetics.json>.

## fAST Dynamic (DAST)

To run DAST tests, Polaris communicates with your web-accessible applications using IPs that vary between Polaris instances.

Table 3. fAST Dynamic (DAST) IPs

| Polaris instance | IPs (outbound) |
| --- | --- |
| America, production | - 192.231.134.0/24 |
| America, POC |
| European Union, production | - 162.244.5.0/26 |
| Kingdom of Saudi Arabia, production | - 162.244.5.80/28 |

Important: The IP addresses for the Kingdom of Saudi Arabia instance (162.244.5.80/28) are located within the KSA region. Geolocation data may suggest otherwise, as these are egress-only IP addresses.

To run DAST tests against internally-hosted applications, the IPs for Polaris Secure Tunnel must also be allow listed. See Polaris Secure Tunnel for more information.

## System status

The status of Polaris and other Black Duck products is available at <https://status.blackduck.com>.

Note: To find the IPs for the status page, go to <https://ip-ranges.atlassian.com/tool.html>. Then, under Products, select statuspage.

## SendGrid

SendGrid is used as an simple mail transfer protocol (SMTP) relay for Polaris. To work with Polaris, you must accept emails from noreply@blackduck.com (formerly, noreply@synopsys.com).
