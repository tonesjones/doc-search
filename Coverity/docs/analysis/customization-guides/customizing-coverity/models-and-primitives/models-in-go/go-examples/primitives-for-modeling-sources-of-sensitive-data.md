---
title: "Primitives for modeling sources of sensitive data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/primitives-for-modeling-sources-of-sensitive-data.html"
content_id: "f378rhhoTeRdTcpd718kAg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:52.020355+00:00"
---

# Primitives for modeling sources of sensitive data

Detecting unsafe uses of sensitive data is built in to Coverity Analysis, but you can add models of additional,
application-specific sources in order to detect additional, and possibly more accurate,
defects.

The analysis reports defects—such as `SENSITIVE_DATA_LEAK` or
`WEAK_PASSWORD_HASH`—when it detects unsafe uses of sensitive
data.

Methods that return sensitive data can be modeled by using the
`SensitiveDataSource()` primitive, described in Go security primitives.

For example, the following model indicates that the `GetUsername()` method
returns a sensitive user identifier:

```
func GetLoginInfo() string {
    var ret string
    ret = SensitiveDataSource(SensitiveTypes.UserId).(string)
    return ret
}
```

The following model indicates that `GetSessionId()` writes a sensitive
session identifier into its byte array parameter:

```
func GetSessionId() []byte {
    var ret_0 []byte = Unknown().([]byte)
    ret_0 = SensitiveDataSource(PersistentSecret).([]byte)

    return ret_0
}
```
