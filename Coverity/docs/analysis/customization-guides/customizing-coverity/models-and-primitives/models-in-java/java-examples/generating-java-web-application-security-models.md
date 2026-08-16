---
title: "Generating Java Web application security models"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-java-web-application-security-models.html"
content_id: "2E~p1fviV2GnYynfigiztg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:00.663877+00:00"
---

# Generating Java Web application security models

To generate models for Web application security checkers only, and avoid the case
where the model overrides inferences that other kinds of checkers make about the method
being modeled, you can use the `--disable-default` and
`--webapp-security options` when you invoke
`cov-make-library`.

For example, the following command line restricts analysis to Web-app security checking
only:

```
> cov-make-library --output-file user_models --disable-default --webapp-security MyClass.java
```
