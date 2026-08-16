---
title: "Sensitive data source types"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sensitive-data-source-types.html"
content_id: "ySeIjAEz1kXm4QiZ6hykBQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:24.611114+00:00"
---

# Sensitive data source types

There are various categories of sensitive data.
The category of the data can be a factor in how a program
should handle that data.

The following table shows the sensitive data categories.

Table 1. Sensitive data source types

| C, C++, Java `SensitiveDataType enum` value | JavaScript sensitive data `"taint_kind"` | C# and Visual Basic `SensitiveDataType enum`value | Description |
| --- | --- | --- | --- |
| `SDT_ACCOUNT` | `"account"` | `Account` | Financial account information; for example, a bank account number |
| `SDT_BIOMETRIC` | `"biometric"` | `Biometric` | Biometric information; for example, fingerprints, DNA, or a retinal scan |
| `SDT_BUG` | `"bug"` | `Bug` | A known bug |
| `SDT_CARDHOLDER_DATA` | | | |
|  | `"cardholder_data"` | `CardholderData` | Credit card information; for example, a credit card number or a primary account number (PAN) |
| `SDT_CONFIGURATION` | `"configuration"` | `Configuration` | A configuration; for example, a configuration property |
| `SDT_DECRYPTED` | `"decrypted"` | `Decrypted` | Data that was decrypted |
| `SDT_DIRECTORY_LISTING` | | | |
|  | `"directory_listing"` | `DirectoryListing` | A directory listing |
| `SDT_EXCEPTION` | `"exception"` | `Exception` | A message generated from an exception |
| `SDT_FILEPATH` | `"filepath"` | `Filepath` | A path in a filesystem |
| `SDT_GEOGRAPHICAL` | `"geographical"` | `Geographical` | Geographical information; for example, GPS, IP, or cell tower information |
| `SDT_MEDICAL` | `"medical"` | `Medical` | General medical information; for example, lab results or medical history |
| `SDT_MOBILE_ID` | `"mobile_id"` | `MobileId` | The ID of a mobile device |
| `SDT_NATIONAL_ID` | `"national_id"` | `NationalId` | The ID of a person; for example, in the U.S., a social security number |
| `SDT_PASSWORD` | `"password"` | `Password` | A typical password |
| `SDT_PERSISTENT_SECRET` | | | |
|  | `"persistent_secret"` | `PersistentSecret` | An internal secret; for example, private keys |
| `SDT_PLATFORM` | `"platform"` | `Platform` | Information about the runtime platform |
| `SDT_SEED` | `"seed"` | `Seed` | A seed; for example, a value for use by a cryptographic pseudo-random number generator (CPRNG) |
| `SDT_SESSION_ID` | `"session_id"` | `SessionId` | A session ID |
| `SDT_SOURCE_CODE` | `"source_code"` | `SourceCode` | Information about source code; for example, a stack trace |
| `SDT_SYSTEM_MEMORY` | `"system_memory"` | `SystemMemory` | Information about system memory usage |
| `SDT_SYSTEM_USER` | `"system_user"` | `SystemUser` | System user data |
| `SDT_TOKEN` | `"token"` | `Token` | A generated password; for example, from a token |
| `SDT_TRANSACTION` | `"transaction"` | `Transaction` | Transaction information; for example, bank-account statements |
| `SDT_TRANSIENT_SECRET` | | | |
|  | `"transient_secret"` | `TransientSecret` | A temporary secret; for example, salts, nonces, and init vectors |
| `SDT_USER_ID` | `"user_id"` | `UserId` | The ID of a system user |
