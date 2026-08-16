---
title: "Using the <cim> tag to specify commit options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-cim-tag-to-specify-commit-options.html"
content_id: "tyTj~tk5wCg0LDuCikvVFw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:00.688277+00:00"
---

# Using the <cim> tag to specify commit options

You use the `cov-commit-defects` command to send analysis results to Coverity
Connect. You can use its `--config` option to pass many Coverity
Connect-specific options that are specified in the master configuration file (typically,
coverity_config.xml). Note, however, that if the same option is
specified both on the command line and in an XML configuration file, the command line
takes precedence.

Note: For an example of the master configuration file, see The configuration.

The following `<cim>` tags are available. The `<cim>` tag
is nested under the `<coverity>` and `<config>`
elements (see example).

Table 1. Options under the cim tag in coverity_config.xml

| Tag | Description | Equivalent `cov-commit-defects` option |
| --- | --- | --- |
| `<certs>` | Set of CA certificates specified in the given `filename` that are in addition to CA certificates obtained from other truststores. A child of the `<client_security>` tag. | `--certs <filename>` |
| `<host>` | Name of the Coverity Connect server host to which you are sending the results of the analysis. Used along with the `<port>` tag. A child of the `<cim>` tag. | `--host <server_name>` |
| `<password>` | The password for the user specified with the `<user>` tag. A child of the `<client_security>` tag. If you put your password into this file, consider taking precautions to set the file permissions so that it is readable only by you. | `--password <password>` |
| `<port>` | The HTTP port on the Coverity Connect host. Used along with the <host> tag. A child of the `<cim>` tag.   - `<cim>/<port>` is equivalent to `--port` - `<cim>/<commit>/<port>` is equivalent to `--data   port` | `--port <port_number>` |
| `<user>` | The user name that is shown in Coverity Connect as having committed the analysis results (in a Coverity Connect snapshot). A child of the `<client_security>` tag. | `--user <user_name>` |
| `<source-stream>` | The Coverity Connect stream name into which you intend to commit these defects. A child of the `<commit>` tag. The stream must exist in Coverity Connect before you can commit data to it. | `--stream <stream_name>` |
| `<ssl>` | Indicator that TLS/SSL is to be used for both HTTPS port and data port connections. A child of the `<client_security>` tag. | `--ssl` |

The following example shows how to use the tags described in
Table 1:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>
  <cit_version>1</cit_version>
  <config>
    <cim>
      <host>cim.company.com</host>
      <port>8443</port>
      <client_security>
         <user>admin</user>
         <password>1256</password>
         <ssl>yes</ssl>
         <certs>/path/to/.certs</certs>
      </client_security>
      <commit>
        <source-stream>myStream</source-stream>
      </commit>
    </cim>
  </config>
</coverity>
```
