---
title: "logging"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/logging.html"
content_id: "rMnDdqIWu1CvY0kGL79f6A"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:23.782547+00:00"
---

# logging

## Logging Level

```
--logging.level.detect=OFF,ERROR,WARN,INFO,DEBUG,TRACE
```

The logging level of Detect.

To keep the log file size manageable, use INFO level logging for normal use and DEBUG or TRACE for troubleshooting.

Detect logging uses Spring Boot logging, which uses Logback (https://logback.qos.ch). The format of this property name is *logging.level.{package}[.{class}]*. The property name shown above specifies package *com.blackduck.integration* because that is the name of Detect's top-level package. Changing the logging level for that package changes the logging level for all Detect code, as well as Black Duck SCA integration libraries that Detect uses. Non-Black Duck SCA libraries that Detect uses are not affected. However, you can use this property to set the logging level for some of the non-Black Duck SCA libraries that Detect uses by using the appropriate package name. For example, *logging.level.org.apache.http=TRACE* sets the logging level to TRACE for the Apache HTTP client library.

For log message format, a default value of *%d{yyyy-MM-dd HH:mm:ss z} ${LOG_LEVEL_PATTERN:%-6p}[%thread] %clr(---){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:%wEx}* is used. You can change your log message format by setting the Spring Boot *logging.pattern.console* property to a different pattern.

Refer to the Spring Boot logging and Logback Project documentation for more details.

| Details |  |
| --- | --- |
| Added | 5.5.0 |
| Type | LogLevel |
| Default Value | INFO |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | OFF, ERROR, WARN, INFO, DEBUG, TRACE |
| Strict | Yes |
