---
title: "Specify the Coverity Connect Web URL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-the-coverity-connect-web-url.html"
content_id: "6HZ7bW4~bQdfwjm55teEjA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:27.993547+00:00"
---

# Specify the Coverity Connect Web URL

For any Coverity Connect instance, for integrations such as SAML (Security Assertion
Markup Language), Jira, and Bugzilla to work, you must specify the Coverity Connect Web
URL using the following `cnc` chart Helm key:
`cim.cimweb.webUrl`

Important: The Connect (cim) hostname portion of the URL
that you specify in `cim.cimweb.webURL` must not exceed 46 characters in
length. This restriction excludes the `https://` characters that are used
when you specify the URL, as well as any port specification.

For Helm key information, refer to cnc Helm chart: Helm keys.
