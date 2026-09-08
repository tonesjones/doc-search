---
title: "Cookie Config"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/cookie-config.html"
content_id: "h7IBfJg2L5vdqDnsVTtvJQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:25.517412+00:00"
content_hash: "44cd4f852f3009d03eda342c4d9aa9ac4292cded84b77ffed47e8a854324e9ef"
---

# Cookie Config

For SRM 2023.12.5 and later, the prop `auth.cookie.secure` is available and gives control for setting the secure flag on the session cookie used by SRM.
Native HTTP installs will have this prop set to `false` and HTTPS installs will have this set to `true`.
If not using a native install, and HTTPS is being used between the client and SRM, this attribute will need to be manually set to `true` in the props file.

- `auth.cookie.secure` - [default: false] When SRM is communicating over HTTPS, the secure flag on the session cookie will always be set regardless of the value of this prop.
  When SRM is communicating over HTTP, the value of this prop controls if the session cookie has this flag set. Where `true` means the secure flag is set.
