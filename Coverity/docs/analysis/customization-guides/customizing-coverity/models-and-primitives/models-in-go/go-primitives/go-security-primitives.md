---
title: "Go security primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/go-security-primitives.html"
content_id: "dt1STPBQ~a1MHf3mD61IGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:53.329822+00:00"
---

# Go security primitives

These primitives deal with security issues, chiefly involving potential sources or
sinks of tainted data.

## `ConnectionStringSink( i interface{} )`

Marks its parameter as flowing into a method that consumes it as a connection string.
The HARDCODED_CREDENTIALS checker reports a defect if a constant string is used as
the password in the connection string.

**Parameters:**

`i`
:   The interface that contains the credentials

## `CryptoSink( i interface{} )`

Marks its parameter as flowing into a method that consumes it as a cryptographic key.
The HARDCODED_CREDENTIALS checker reports a defect if a source-code-embedded
constant string is passed to it.

**Parameters:**

`i`
:   The interface that contains the credentials

## `HeaderSink( i interface{} )`

Marks a method parameter as being used to construct an HTTP header. The
HEADER_INJECTION checker reports a defect if an unsafe, user-controllable string is
passed to this method.

**Parameters:**

`i`
:   The interface that contains the value for the HTTP header

## `HttpRedirectSink( i interface{} )`

Marks a method parameter as being used as an HTTP address to redirect to. The
OPEN_REDIRECT checker reports a defect if an unsafe, user-controllable string is
passed to this method.

**Parameters:**

`i`
:   The interface that contains the password

## `NoSqlSink( i interface{} )`

Marks a method parameter as being used to construct a NoSQL query. The
NOSQL_QUERY_CHECKER checker reports a defect if an unsafe, user-controllable string
is passed to this method.

**Parameters:**

`i`
:   The interface that contains the NoSQL query

## `OsCmdInjectionSink( i interface{} )`

Marks its parameter as flowing into a method that treats the parameter as a command,
or command argument, to be executed by the local operating system (OS). The
OS_CMD_INJECTION checker reports defects when tainted data flows into this
primitive.

**Parameters:**

`i`
:   The interface that contains the command to be executed, or that contains an
    argument to a command to be executed

## `PasswordSink( i interface{} )`

Marks its parameter as flowing into a method that consumes the parameter as a
password. The HARDCODED_CREDENTIALS checker reports a defect if a
source-code-embedded constant string is passed to this method.

**Parameters:**

`i`
:   The interface that contains the password

## `PathSink( i interface{} )`

Marks a method parameter as being used as a file name or as a filesystem path. The
PATH_MANIPULATION checker reports a defect if an unsafe, user-controllable string is
passed to this method.

**Parameters:**

`i`
:   The interface that contains the path

## `SensitiveDataSource( types ...SensitiveDataType )`

Returns an object of arbitrary type that the analysis treats as sensitive data. Use
this primitive to model a method that returns sensitive data.

**Parameters:**

`types`
:   The specific kinds of sensitive data

## `SqlSink( i interface{} )`

Marks its parameter as flowing into a method that treats the parameter as an SQL,
HQL, or JPQL query. The SQLI checker reports a defect when tainted data flows into
this primitive.

**Parameters:**

`i`
:   The interface that contains the query

## `TaintedEnvironmentSink( i interface{} )`

Marks a method parameter as being used to set an environment variable. The
TAINTED_ENVIRONMENT_WITH_EXECUTION checker reports a defect if an unsafe,
user-controllable string is passed to this method.

**Parameters:**

`i`
:   The interface that contains the value of the environment variable being
    set

## `TaintSource( types ...TaintSourceType )`

Returns an object of arbitrary type that the analysis treats as tainted data. Use
this primitive to model a method that returns tainted data.

**Parameters:**

`types`
:   The specific kinds of taint

## `TemplateSink( i interface{} )`

Marks a method parameter as being used to construct a template. The
TEMPLATE_INJECTION checker reports a defect if an unsafe, user-controllable string
is passed to this method.

**Parameters:**

`i`
:   The interface that contains the template

## `TokenSink( i interface{} )`

Marks its parameter as flowing into a method that consumes the parameter as a
security token. The HARDCODED_CREDENTIALS checker reports a defect if a
source-code-embedded constant string is passed to the method.

**Parameters:**

`i`
:   The interface that contains the credentials

## `UrlSink( i interface{} )`

Marks a method parameter as being used to construct a URL. The URL_MANIPULATION
checker reports a defect if an unsafe, user-controllable string is passed to this
method.

**Parameters:**

`i`
:   The interface that contains the URL

## `XssSink( i interface{} )`

Marks a method parameter as being used to construct an executable script on the
client side. The XSS (cross-site scripting) checker reports a defect if an unsafe,
user-controllable string is passed to this method.

**Parameters:**

`i`
:   The interface that contains the executable script
