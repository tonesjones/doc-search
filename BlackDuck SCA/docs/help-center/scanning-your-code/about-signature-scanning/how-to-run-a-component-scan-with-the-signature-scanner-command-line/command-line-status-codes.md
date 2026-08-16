---
title: "Command Line Status Codes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/command-line-status-codes.html"
content_id: "r4Tz~iWZ1hMTPI6HsLRL_Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:38.686561+00:00"
---

# Command Line Status Codes

When a signature scan completes, it returns one of
the following status codes to indicate the result.

## Success Codes

| Code | Name | Description |
| --- | --- | --- |
| 0 | SUCCESS | The scan completed successfully. |

## Execution Status Codes

| Code | Name | Description |
| --- | --- | --- |
| 1 | FAILURE | Generic failure. |
| 2 | NOT_EXECUTED | Scan was not executed because the minimum scan interval was not exceeded. See the `--min-scan-interval` parameter. |

## Command Usage Codes

| Code | Name | Description |
| --- | --- | --- |
| 64 | USAGE | Incorrect command usage (wrong arguments or syntax). |
| 65 | DATA_ERROR | Input data was incorrect. |
| 78 | CONFIGURATION | System found in an unconfigured or misconfigured state. |

## Resource Access Codes

| Code | Name | Description |
| --- | --- | --- |
| 66 | NO_INPUT | Input file does not exist or is not readable. |
| 67 | NO_USER | Specified user does not exist. |
| 68 | NO_HOST | Specified host does not exist. |
| 73 | CANNOT_CREATE | Cannot create output file. |
| 77 | NO_PERMISSION | Insufficient permission to perform the operation. |

## System Error Codes

| Code | Name | Description |
| --- | --- | --- |
| 69 | UNAVAILABLE | A service is unavailable. |
| 70 | SOFTWARE | Internal software error detected. |
| 71 | OS_ERROR | Operating system error detected. |
| 72 | OS_FILE | System file error (missing, cannot open, or has syntax error). |
| 74 | IO_ERROR | Input/output error on a file. |
| 75 | TEMPORARY_FAILURE | Temporary failure. |
| 76 | PROTOCOL | Remote system returned an unexpected response during protocol exchange. |
| 79 | NO_REGISTRATION | Registration to Black Duck is not valid. |

You can also find more information about these exit codes [here](https://www.freebsd.org/cgi/man.cgi?query=sysexits&apropos=0&sektion=0&manpath=FreeBSD+4.3-RELEASE&format=html).
