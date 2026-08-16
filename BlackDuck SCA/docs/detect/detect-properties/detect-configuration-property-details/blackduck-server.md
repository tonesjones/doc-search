---
title: "blackduck-server"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/blackduck-server.html"
content_id: "RwliZJf3R0RX~49dctaC1w"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:17.112262+00:00"
---

# blackduck-server

## Black Duck SCA API Token

```
--blackduck.api.token
```

The access token used to authenticate with the Black Duck SCA Server.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Black Duck SCA URL

```
--blackduck.url
```

URL of the Black Duck SCA server.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `https://blackduck.mydomain.com` |

## Detect Timeout

```
--detect.timeout=300
```

The amount of time in seconds Detect will wait for network connection, for scans to finish, and to generate reports (i.e. risk and policy check). When changing this value, keep in mind the checking of policies might have to wait for scans to process which can take some time.

Note that timeout will exit with FAILURE_TIMEOUT (2) code.

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Long |
| Default Value | 300 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `600` |

## Force Offline BDIO Generation

```
--blackduck.offline.mode.force.bdio=false
```

This property will force Detect in offline mode to generate a BDIO even if no code locations were identified.

| Details |  |
| --- | --- |
| Added | 8.5.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Offline Mode

```
--blackduck.offline.mode=false
```

This can disable Black Duck SCA communication - if set to true, Detect will not upload BDIO files, or check policies, and it will not download and install the signature scanner. Note that the path to a local instance of the scanner can be provided using the -detect.blackduck.signature.scanner.local.path parameter.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Test Connection to Black Duck SCA

```
--detect.test.connection=false
```

Test the connection to Black Duck SCA with the current configuration.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detect Scan Mode (Advanced)

```
--detect.blackduck.scan.mode=RAPID,STATELESS,INTELLIGENT
```

Set the Black Duck SCA scanning mode of Detect.

Set the scanning mode to control how Detect will send data to Black Duck SCA. RAPID will not persist the results and disables select Detect functionality for faster results. INTELLIGENT, referred to as 'Full' scan mode in Black Duck SCA, persists the results and permits all features of Detect.

| Details |  |
| --- | --- |
| Added | 6.9.0 |
| Type | BlackduckScanMode |
| Default Value | INTELLIGENT |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | RAPID, STATELESS, INTELLIGENT |
| Strict | Yes |

## Trust All SSL Certificates (Advanced)

```
--blackduck.trust.cert=false
```

If true, automatically trust the certificate for the current run of Detect only.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
