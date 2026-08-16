---
title: "Regular expression (regex)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regular-expression-regex-.html"
content_id: "plKwnsWj8XUkKEIJtuGY7Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:30.922632+00:00"
---

# Regular expression (regex)

A regular expression (`regex`) denotes a potentially infinite set of strings. Another string is
said to "match" the `regex` if it is a member of its denoted set. In this file format,
regular expressions use the [Perl syntax](http://perldoc.perl.org/perlre.html),
except they must be written as JSON strings, which means you need to double backslashes and also put a backslash before certain other characters
such as a double-quote.
