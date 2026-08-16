---
title: "proxy"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/proxy.html"
content_id: "u9exgvIZYDuPrkasn8m1ew"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:26.760187+00:00"
---

# proxy

## Bypass Proxy Hosts (Advanced)

```
--blackduck.proxy.ignored.hosts
```

A comma separated list of regular expression host patterns that should not use the proxy.

This property accepts Java regular expressions. For further information refer to [Java regular expression support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/javaregex%2Ehtml)

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `blackduck[0-9]+.mycompany.com` |

## NTLM Proxy Domain (Advanced)

```
--blackduck.proxy.ntlm.domain
```

NTLM Proxy domain.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## NTLM Proxy Workstation (Advanced)

```
--blackduck.proxy.ntlm.workstation
```

NTLM Proxy workstation.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Proxy Host (Advanced)

```
--blackduck.proxy.host
```

Hostname of the proxy server.

Schema/protocol is not accepted by this parameter.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--blackduck.proxy.host=<Proxy_IP/URL>` |

## Proxy Password (Advanced)

```
--blackduck.proxy.password
```

Proxy password.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Proxy Port (Advanced)

```
--blackduck.proxy.port
```

Proxy port number.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Proxy Username (Advanced)

```
--blackduck.proxy.username
```

Proxy username.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
