---
title: "Taint enumerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taint-enumerations.html"
content_id: "guvgdhYHXeTh04LDD1sYzA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:29.220390+00:00"
---

# Taint enumerations

The primitives.h header file provides a couple of enumerations to use
when invoking primitives that manage tainted data.

## ‘TaintType’

```
enum TaintType {
    TAINT_TYPE_HTTP,
    TAINT_TYPE_NETWORK,
    TAINT_TYPE_FILESYSTEM,
    TAINT_TYPE_DATABASE,
    TAINT_TYPE_CONSOLE,
    TAINT_TYPE_ENVIRONMENT,
    TAINT_TYPE_COMMAND_LINE,
    TAINT_TYPE_SYSTEM_PROPERTIES,
    TAINT_TYPE_RPC,
    TAINT_TYPE_HTTP_HEADER,
    TAINT_TYPE_COOKIE,
            
    WEAK_GUARD_IP_ADDRESS,
    WEAK_GUARD_DNS,
    WEAK_GUARD_HTTP_REFERER,
    WEAK_GUARD_PRINCIPAL_NAME,
    WEAK_GUARD_OS_LOGIN,

    UNENCRYPTED_DATA_UNENCRYPTED_SOCKET,
    UNENCRYPTED_DATA_UNENCRYPTED_URL_CONNECTION,

    SDT_DECRYPTED,
    SDT_PASSWORD,
    SDT_TOKEN,
    SDT_SESSION_ID,
    SDT_MOBILE_ID,
    SDT_USER_ID,
    SDT_NATIONAL_ID,
    SDT_PERSISTENT_SECRET,
    SDT_TRANSIENT_SECRET,
    SDT_SEED,
    SDT_CARDHOLDER_DATA,
    SDT_ACCOUNT,
    SDT_TRANSACTION,
    SDT_MEDICAL,
    SDT_CONTACT_INFO,
    SDT_BIOMETRIC,
    SDT_GEOGRAPHICAL,
    SDT_PRIVATE_CONTENT,
    SDT_EXCEPTION,
    SDT_SOURCE_CODE,
    SDT_CONFIGURATION,
    SDT_BUG,
    SDT_FILEPATH,
    SDT_DIRECTORY_LISTING,
    SDT_SYSTEM_MEMORY,
    SDT_SYSTEM_USER,
    SDT_PLATFORM,
};
```

## ‘TaintSinkType’

```
// Used by TAINTED_SCALAR, and TAINTED_STRING and subclasses
// Roughly determines which checker reports a defect
enum TaintSinkType {

    // SAT-26837 TAINTED_SCALAR sinks
    TAINTED_SCALAR_GENERIC,
    LOOP_BOUND_LOWER, // needs a lower bound check before being passed to this function
    LOOP_BOUND_UPPER, // needs upper bound
    ALLOCATION,
    OVERRUN,

    // SAT-26837 TAINTED_STRING sinks
    GENERIC,
    ENVIRONMENT,
    REGISTRY,

    // SAT-26837 sinks for TAINTED_STRING spin-offs
    OS_CMD_ONE_STRING,
    OS_CMD_ARRAY,
    OS_CMD_FILENAME,
    OS_CMD_ARGUMENTS,
    PATH,
    SQL,
    XPATH,
    URL,
    HTTP,
    SCRIPT_CODE,  // SAT-32622  for tainted executable code
    HTTP_HEADER,  // HEADER_INJECTION sink type
    FORMAT_STRING,

    // SENSITIVE_DATA_LEAK sink types (see SAT-31512)
    // Additionally, SENSITIVE_DATA_LEAK should report
    // on leaks to REGISTRY sinks.
    COOKIE,
    DATABASE,
    FILESYSTEM,
    LOGGING,
    TRANSIT,
    UI,
};
```
