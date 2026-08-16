---
title: "Enable Web application security"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enable-web-application-security.html"
content_id: "qQ2rH1WohbqH0vg8axFUeg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:56.824949+00:00"
---

# Enable Web application security

The following configuration specifies that audit-mode checkers should be enabled (`audit: true`)
and that the Web application security checkers should be enabled with an aggressiveness level of
`high`.

The configuration also specifies, in the `directives` section, some security modeling directives
to designate Java methods that received untrusted data.

```
capture:
  build:
    clean-command: mvn clean
    build-command: mvn install

analyze:
  directives:
    - config:
        language: Java
        directives:
          - simple_entry_point:
              and:
                - implemented_in_class:
                    with_annotation:
                      named: annot.Controller
                - matching: ".*\\.get.*"
            taint_kinds: [http]
  checkers:
    audit: true
    webapp-security:
      aggressiveness-level: high

commit:
  connect:
    stream: WebGoat
    url: https://connect.example.com
```
