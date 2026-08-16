---
title: "Java regular expression support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/java-regular-expression-support.html"
content_id: "MxYfQG3Q6K2WdyP7YW0TSQ"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:23.122042+00:00"
---

# Java regular expression support

The values of the following Detect property can utilize Java regular expressions described below:

- blackduck.proxy.ignored.hosts

A few of the supported wildcards and their effect are:

- A period (.) matches any single character
- An asterisk (*) matches a sequence of zero or more of the preceding character
- A backslash (\) preceding a special regular expression character (such as . or *) causes that character to be treated as the literal character

For example:

- .*-proxy01\.dc1\.lan matches qa-ssl-proxy01.dc1.lan and prod-proxy01.dc1.lan, but not qa-ssl-proxy02.dc1.lan
- qa-ssl-proxy..\.dc1\.lan matches qa-ssl-proxy01.dc1.lan and qa-ssl-proxy02.dc1.lan

Detect uses the [Java Pattern class](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) to determine whether a string matches the given pattern.
