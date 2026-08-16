---
title: "Increasing the timeout duration for a custom defect handler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/increasing-the-timeout-duration-for-a-custom-defect-handler.html"
content_id: "OJSxBatG8jzsEnkyjAPh5g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:06.084349+00:00"
---

# Increasing the timeout duration for a custom defect handler

For an export handler, the default timeout duration is 8 seconds. It is possible to
customize this value so the duration is longer.

To increase the timeout duration, edit the file
<platform>/server/base/webapps/ROOT/WEB-INF/cov-server-servlet.xml.
Locate the following section of XML code:

```
<bean id="exportHandler" class="com.coverity.ces.web.service.DefectHandlerServiceImpl">
    <property name="commandLocation" value="bin/export-defect-handler"/>
    <property name="handlerTimeoutSeconds" value="8"/>
</bean>
```

Increase the `value` of `handlerTimeoutSeconds`; for
example, you might prefer the timeout to last 30 seconds rather than 8.

After you edit and save the XML file, you must restart your Coverity Connect server for this change to take effect.

Whenever your Coverity Connect instance is upgraded (including in-place
upgrades) and whenever a database is imported into a new Coverity Connect
installation, you will have to make your change to the XML file again.
