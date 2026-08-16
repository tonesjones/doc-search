---
title: "Security checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-checkers.html"
content_id: "0wjb694nAJ~pKtnnpZ67WA"
version: "2026.6"
section: "SpotBugs™ Checker Reference"
scraped_at: "2026-08-12T03:21:05.177437+00:00"
---

# Security checkers

Note that all SpotBugs™ checkers are quality checkers. Some of them are also security
checkers. The table below lists the SpotBugs™ security checkers and their enablement
status.

| Security checker | Enabled by default | Notes |
| --- | --- | --- |
| FB.DMI_CONSTANT_DB_PASSWORD | No | Overlap with HARDCODED_CREDENTIALS |
| FB.DMI_EMPTY_DB_PASSWORD | No |
| FB.DM_EXIT | No | Overlap with DC.CODING_STYLE |
| FB.HRS_REQUEST_PARAMETER_TO_COOKIE | No | Deemed not useful by Coverity Security Research Laboratory: HTTP response splitting is not a vulnerability in modern servlet containers and is hence not worth reporting. |
| FB.HRS_REQUEST_PARAMETER_TO_HTTP_​HEADER | No |
| FB.IL_INFINITE_RECURSIVE_LOOP | Yes |  |
| FB.IS2_INCONSISTENT_SYNC | No | Overlap with GUARDED_BY_VIOLATION |
| FB.IS_FIELD_NOT_GUARDED | Yes |  |
| FB.IS_INCONSISTENT_SYNC | Yes |  |
| FB.PT_ABSOLUTE_PATH_TRAVERSAL | No | Overlap with PATH_MANIPULATION |
| FB.PT_RELATIVE_PATH_TRAVERSAL | No |
| FB.SQL_NONCONSTANT_STRING_PASSED_​TO_​EXECUTE | No | Overlap with SQLI |
| FB.SQL_PREPARED_STATEMENT_​GENERATED_​FROM_NONCONSTANT_STRING | No |
| FB.XSS_REQUEST_PARAMETER_TO_JSP_​WRITER | No | Overlap with XSS |
| FB.XSS_REQUEST_PARAMETER_TO_SEND_​ERROR | No |
| FB.XSS_REQUEST_PARAMETER_TO_SERVLET_​WRITER | No |
