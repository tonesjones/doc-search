---
title: "TaintKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taintkind.html"
content_id: "LzvwuVKAcEbj~XxcDkacBw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:39.072133+00:00"
---

# TaintKind

**Used by these directives:**
`dataflow_checker_name`, `method_returns_tainted_data`,
`simple_entry_point`, `tainted_data`

**Used by these objects:**
`InputAndAccessPathSpecifier`, `TaintKindGroup`

A `TaintKind` value describes a single taint kind. It has one of the
values listed in this section. `TaintKind` values are divided into
different groups that you can refer to collectively in some directives by using a
`TaintKindGroup`.

The following taint kinds are relevant to server-side Web applications and other
server-side applications:

- `cookie`: Data from HTTP cookies. See the
  `--trust-cookies` and `--distrust-cookies`
  options to the `cov-analyze` command.
- `command_line`: Data from the command line. See the
  `--trust-command-line` and
  `--distrust-command-line` options to the
  `cov-analyze` command.
- `console`: Data from the console. See the
  `--trust-console` and `--distrust-console`
  options to the `cov-analyze` command.
- `database`: Data from a database. See the
  `--trust-database` and `--distrust-database`
  options to the `cov-analyze` command.
- `environment`: Data from environment variables. See the
  `--trust-environment` and
  `--distrust-environment` options to the
  `cov-analyze` command.
- `filesystem`: Data read from a file. See the
  `--trust-filesystem` and
  `--distrust-filesystem` options to the
  `cov-analyze` command.
- `http`: Data from incoming HTTP requests. This does not include
  headers or cookies. See the `--trust-http` and
  `--distrust-http` options to the
  `cov-analyze` command.
- `http_header`: Data from HTTP headers. See the
  `--trust-http-header` and
  `--distrust-http-header` options to the
  `cov-analyze` command.
- `network`: Data from network connections. This does not include
  data from incoming HTTP requests or remote procedure calls. See the
  `--trust-network` and `--distrust-network`
  options to the `cov-analyze` command.
- `rpc`: Data returned from remote procedure calls (RPC). See the
  `--trust-rpc` and `--distrust-rpc` options to
  the `cov-analyze` command.
- `system_properties`: Data on system properties. See the
  `--trust-system-properties` and
  `--distrust-system-properties` options to the
  `cov-analyze` command.

The following taint kinds are relevant to client-side JavaScript code (that is,
JavaScript that runs in a Web browser):

`js_client_cookie`
:   Data from the JavaScript `document.cookie`. See the
    `--trust-js-client-cookie` and
    `--distrust-js-client-cookie` options to the
    `cov-analyze` command.

`js_client_external`
:   Data from the response to an `XMLHttpRequest` or similar. See
    the `--trust-js-client-external` and
    `--distrust-js-client-external` options to the
    `cov-analyze command`.

`js_client_html_element`
:   Data from user input on HTML elements such as `textarea` and
    `input` elements. See the
    `--trust-js-client-html-element` and
    `--distrust-js-client-html-element` options to the
    `cov-analyze` command.

`js_client_http_referer`
:   Data from the `referer` HTTP header (from
    `document.referrer`). See the
    `--trust-js-client-http-referer` and
    `--distrust-js-client-http-referer` options to the
    `cov-analyze` command.

`js_client_http_header`
:   Data from the HTTP response header of the response to an
    `XMLHttpRequest` or similar. See the
    `--trust-js-client-http-header` and
    `--distrust-js-client-http-header` options to the
    `cov-analyze` command.

`js_client_other_origin`
:   Data from content in another frame or from another origin, for instance, from
    `window.name`. See the
    `--trust-other-origin` and
    `--distrust-other-origin` options to
    the `cov-analyze` command.

`js_client_url_query_or_fragment`
:   Data from the query or fragment part of the URL, for instance,
    `location.hash` or `location.query`. See
    the `--trust-url-query-or-fragment` and
    `--distrust-url-query-or-fragment` options to the
    `cov-analyze` command.

The following taint kinds are relevant to mobile applications:

`mobile_other_app`
:   Data received from any mobile application that does not require a permission
    to communicate with the current application component. See the
    `--trust-mobile-other-app` and
    `--distrust-mobile-other-app` options to the
    `cov-analyze` command.

`mobile_same_app`
:   Data received from the same mobile application. See the
    `--trust-mobile-same-app` and
    `--distrust-mobile-same-app` options to the
    `cov-analyze` command.

`mobile_user_input`
:   Data obtained from user inputs into a mobile application. See the
    `--trust-mobile-user-input` and
    `--distrust-mobile-user-input` options to the
    `cov-analyze` command.

`mobile_other_privileged_app`
:   Data received from any mobile application that requires a permission to
    communicate with the current application component. See the
    `--trust-mobile-other-privileged-app` and
    `--distrust-mobile--other-privileged-app` options to the
    `cov-analyze` command.

The following taint kinds represent sensitive data, rather than data controlled by an
attacker:

`decrypted`
:   Decrypted data

`password`
:   A password

`token`
:   An authentication token

`session_id`
:   A session ID

`mobile_id`
:   A mobile device ID

`user_id`
:   An application user ID

`national_id`
:   A national ID

`persistent_secret`
:   Persistent secret data, such as an encryption key

`transient_secret`
:   Transient secret data, such as a TLS ticket

`seed`
:   A seed for a randomization algorithm

`cardholder_data`
:   Payment cardholder data

`account`
:   Account data

`transaction`
:   Transaction data

`medical`
:   Medical data

`biometric`
:   Biometric data

`geographical`
:   Sensitive geographical data

`exception`
:   Information about an application exception

`source_code`
:   Application source code

`configuration`
:   Configuration data

`bug`
:   Information about a bug in the application

`file path`
:   A path on the filesystem

`directory_listing`
:   A directory listing

`system_memory`
:   Information about system memory usage

`system_user`
:   System user data

`platform`
:   Information about the runtime platform
