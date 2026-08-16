---
title: "Categories of tainted data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/categories-of-tainted-data.html"
content_id: "n87cRkdoe9NNg4nejcW9_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:22.499532+00:00"
---

# Categories of tainted data

Tainted data can be grouped into several categories, depending on where the data
originates.

These are the main categories of tainted data:

- Server-side applications
- Web-browser applications
- Mobile applications

Note: Another source of tainted data might be the code base itself, that you are scanning. You
cannot use command-line options to manage the detection of this taint source type.
See Taint sources in the code base for more information.

For examples of handling tainted data, see the code samples in "Options: Web and
mobile application security", part of the `cov-analyze` section in Coverity 2026.6.0 Command Reference.

Important: Tainted data checkers are not always concerned with taint kinds from all of these
categories. For example, the ANGULAR_EXPRESSION_INJECTION checker reports a defect
in code that uses an untrusted value as part of an AngularJS expression. It examines
Web-browser-based and mobile taint kinds but *does not* examine server-side
taint kinds.

The tables that follow sort the various taint kinds according to the
category of the potentially tainted data.

For the default values of individual taint kinds by checker, see the "Checker Enablement and Option Defaults by Language" table
in the Coverity 2026.6.0 Checker Reference (HTML only).

## Server-side taint sources

The taint kinds in this table are relevant to server-side Web applications and other
server-side applications.

Table 1. Server-side applications

| Taint kind | Description |
| --- | --- |
| `cookie` | Data from HTTP cookies |
| `command_line` | Data from the command line |
| `console` | Data from the console |
| `database` | Data from a database |
| `environment` | Data from environment variables |
| `filesystem` | Data read from a file |
| `http` | Data from incoming HTTP requests |
| `http_header` | Data from HTTP headers |
| `llm` | Data from Large Language Model (LLM) output |
| `network` | Data from network connections. This *does not* include data from incoming HTTP requests or remote procedure calls. |
| `rpc` | Data returned from remote procedure calls (RPCs) |
| `system_properties` | Data on system properties |

## Browser application taint sources

The taint kinds in this table are relevant to client-side JavaScript code (that is,
JavaScript that runs in a Web browser).

Table 2. Web-browser-based applications

| Taint kind | Description |
| --- | --- |
| `js_client_cookie` | Data from the JavaScript `document.cookie` Note: This category was originally called `client_cookie`. |
| `js_client_external` | Data from the response to an `XMLHttpRequest` or similar request Note: This category was originally called `external`. |
| `js_client_html​_element` | Data from user input on HTML elements such as text area and input elements |
| `js_client_http​_referer` | Data from the "referer" HTTP header (from `document.referrer`) |
| `js_client_http_header` | Data from the HTTP response header of the response to an `XMLHttpRequest` or similar request |
| `js_client_other​_origin` | Data from content in another frame or from another origin; for example, from `window.name` |
| `js_client_url_query​_or_fragment` | Data from the query or fragment part of the URL; for example, from `location.hash` or `location.query` |

## Mobile application taint sources

The taint kinds in this table are relevant to mobile applications.

Table 3. Mobile applications

| Taint kind | Description |
| --- | --- |
| `mobile_other_app` | Data received from any mobile application that does not require a permission to communicate with the current application component |
| `mobile_other​_privileged_app` | Data received from any mobile application that requires a permission to communicate with the current application component |
| `mobile_same_app` | Data received from the same mobile application |
| `mobile_user_input` | Data obtained from user inputs into a mobile application |
