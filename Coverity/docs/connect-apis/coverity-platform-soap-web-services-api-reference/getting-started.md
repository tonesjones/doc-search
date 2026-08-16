---
title: "Getting started"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/getting-started.html"
content_id: "9AAHRAaYoJ7JMQCtQ4ns2w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:21.343491+00:00"
---

# Getting started

**To get started with the API**:

1. Use the free **SoapUI** software ([http:www.soapui.org](http://www.soapui.org) or <http://www.smartbear.com>) to download the WSDL files and create test
   suites with query templates for the calls. You can also use this software for
   checking the return XML results. The URLs for the WSDL files are as follows:
   - Configuration service:

     ```
     http://<cov_connect_server>.<domain>:<port>/ws/v9/configurationservice?wsdl
     ```

     (for example, http://my.cov_connect.domain:8080/ws/v9/configurationservice?wsdl)
   - Defect service:

     ```
     http://<cov_connect_server>.<domain>:<port>/ws/v9/defectservice?wsdl
     ```

     (for example: http://my.cov_connect.domain:8080/ws/v9/defectservice?wsdl)
2. Write your own scripts in the scripting language of your choice, and use the appropriate
   libraries or modules for handling the data objects and calls. The scripts need
   to use a SOAP library (for example, SOAP::Lite with Perl or
   suds with Python).Working examples with source code are provided in the example
   directory, in Python, Perl, and Java. Each zip file contains a
   Readme file with information on how to run (and build,
   if necessary) these examples.

   Note: Coverity Connect uses WSSE for authentication, not
   simple HTTP authentication.
