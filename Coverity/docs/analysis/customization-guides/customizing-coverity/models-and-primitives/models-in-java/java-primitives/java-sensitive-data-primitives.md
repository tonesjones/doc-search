---
title: "Java sensitive-data primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-sensitive-data-primitives.html"
content_id: "fjM8VF1NAyZOju3oqR6M9g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:03.595448+00:00"
---

# Java sensitive-data primitives

Primitives to categorize sensitive data.

## `enum SensitivePrimitives.SensitiveDataCategory`

Represents various categories of sensitive data.

The following values are defined:

| Name | Description |
| --- | --- |
| `SDC_APPLICATION` |  |
| `SDC_CREDENTIAL` |  |
| `SDC_CRYPTOGRAPHY` |  |
| `SDC_FILESYSTEM` |  |
| `SDC_FINANCIAL` |  |
| `SDC_GENERIC` |  |
| `SDC_HEALTH` |  |
| `SDC_IDENTIFIER` |  |
| `SDC_PERSONAL` |  |
| `SDC_SYSTE` |  |

## `enum SensitivePrimitives.SensitiveDataType`

Represents various possible types of sensitive data.

The following values are defined:

| Name | Description |
| --- | --- |
| `SDT_ACCOUNT` |  |
| `SDT_BIOMETRIC` |  |
| `SDT_BUG` |  |
| `SDT_CARDHOLDER_DATA` |  |
| `SDT_CONFIGURATION` |  |
| `SDT_CONTACT_INFO` |  |
| `SDT_DECRYPTED` |  |
| `SDT_DIRECTORY_LISTING` |  |
| `SDT_EXCEPTION` |  |
| `SDT_FILEPATH` |  |
| `SDT_GEOGRAPHICAL` |  |
| `SDT_MEDICAL` |  |
| `SDT_MOBILE_ID` |  |
| `SDT_NATIONAL_ID` |  |
| `SDT_PASSWORD` |  |
| `SDT_PERSISTENT_SECRET` |  |
| `STD_PLATFORM` |  |
| `SDT_PRIVATE_CONTENT` |  |
| `SDT_SEED` |  |
| `SDT_SESSION_ID` |  |
| `SDT_SOURCE_CODE` |  |
| `SDT_SYSTEM_MEMORY` |  |
| `SDT_SYSTEM_USER` |  |
| `SDT_TOKEN` |  |
| `SDT_TRAMSACTION` |  |
| `SDT_TRANSIENT_SECRET` |  |
| `SDT_USER_ID` |  |

## `SensitivePrimitives.SensitiveDataCategory valueOf( java.lang.String name )`

Returns the `enum` constant of this type with the specified name.

## `SensitivePrimitives.SensitiveDataType valueOf( java.lang.String name )`

Returns the `enum` constant of this type with the specified name.

## `SensitivePrimitives.SensitiveDataCategory[] values()`

Returns an array containing the constants of this `enum` type, in the order they are declared.
This method can be used to iterate over the elements; for example:

```
for ( SensitivePrimitives.SensitiveDataCategory c : SensitivePrimitives.SensitiveDataCategory.values() )
    System.out.println( c );
```

## `SensitivePrimitives.SensitiveDataType[] values()`

Returns an array containing the constants of this `enum` type, in the order they are declared.
This method can be used to iterate over the elements; for example:

```
for ( SensitivePrimitives.SensitiveDataType c : SensitivePrimitives.SensitiveDataType.values() )
    System.out.println( c );
```
