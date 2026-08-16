---
title: "Polaris IP ranges for Bridge CLI"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-ip-ranges-for-bridge-cli.html"
content_id: "~yN_fpU5QAib9FJLTHKk5g"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:56.590961+00:00"
content_hash: "41288cc69d4a9a5701cce790ea79ef760ab1934f6589691a2a6588e4f951fe7a"
---

# Polaris IP ranges for Bridge CLI

When you run Bridge in a pipeline (including the Bridge CLI, Black Duck Security Scan Extension for Azure DevOps, Black Duck Security Scan Action, Black Duck Security Scan Template, Black Duck Security Scan Plugin for Jenkins), it interacts with several services, along with Polaris (<https://polaris.blackduck.com>, <https://poc.polaris.blackduck.com>, <https://eu.polaris.blackduck.com>, <https://ksa.polaris.blackduck.com>).

Note: HTTPS is used for all traffic to Polaris. IPs that include a subnet mask (for example, /22 in 103.21.244.0/22) represent a range of IPs, all of which should be allow listed to ensure Bridge and Polaris function as expected.

## Polaris APIs

### North American and European instances

APIs for the American and European instances of Polaris are domain-fronted by CloudFlare.

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

APIs for the Saudi Arabian instance of Polaris are domain-fronted by Google Cloud Armor.

- 34.1.59.210

## Tools

Tools to run tests are downloaded from <https://tool-download.polaris.blackduck.com> (formerly, <https://tool-download.polaris.synopsys.com>).

- 34.54.106.228

Important: <https://tool-download.polaris.synopsys.com> (34.102.175.248) will continue to function until September 30, 2025. Update your allow list to avoid issues.

## Bridge CLI

The Bridge CLI is downloaded from <https://repo.blackduck.com> (formerly, <https://sig-repo.synopsys.com>).

- 34.149.5.115

Important: To ensure the Bridge CLI continues to function as expected, keep <https://sig-repo.synopsys.com> (34.110.245.127) on your allow list until September 30, 2025.

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

## Polaris Secure Tunnel

Polaris Secure Tunnel orchestrates secure communication for DAST tests you run against internally-hosted applications, and uses IPs that vary between Polaris instances.

Table 2. IPs for Polaris Secure Tunnel

| Polaris instance | DNS | IPs |
| --- | --- | --- |
| America, production | <https://securetunnel.blackduck.com> | - 34.27.215.249 |
| America, POC | <https://poc.securetunnel.blackduck.com> | - 34.27.215.249 |
| European Union, production | <https://eu.securetunnel.blackduck.com> | - 35.246.130.181 |
| Kingdom of Saudi Arabia, production | <https://ksa.securetunnel.blackduck.com> | - 34.166.29.196 |
