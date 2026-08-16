---
title: "Retrieve all supported locales"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-supported-locales.html"
content_id: "UfG5RuGnS18NPzYMJtic_w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:15.890807+00:00"
---

# Retrieve all supported locales

Example GET request to retrieve codes for all supported locales.

**cURL Request**

```
curl --location --request GET "http://my_connect_host:8080/api/v2/locales" \
--user  my_username:my_password \
--header 'Accept: application/json'
```

**Response body**

```
[
  {
    "code": "en_us",
    "label": "English",
    "selfLabel": "English"
  },
  {
    "code": "ja_jp",
    "label": "Japanese",
    "selfLabel": "日本語"
  },
  {
    "code": "ko_kr",
    "label": "Korean",
    "selfLabel": "한국어"
  },
  {
    "code": "zh_cn",
    "label": "Simplified Chinese",
    "selfLabel": "简体中文"
  }
]
```
