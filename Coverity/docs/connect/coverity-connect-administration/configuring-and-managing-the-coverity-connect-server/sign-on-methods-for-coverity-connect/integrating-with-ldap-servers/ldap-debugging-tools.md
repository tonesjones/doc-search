---
title: "LDAP debugging tools"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ldap-debugging-tools.html"
content_id: "6ssDJBwmBfp5rTk4xTKwow"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:42.208666+00:00"
---

# LDAP debugging tools

To set up the LDAP environment, customers need to examine their internal LDAP
configuration in order to find and test values for Connection
Settings, User Search Settings, and
Group Search Settings. The following tools are suggested for
this purpose.

- `ldapsearch`
- `JXplorer` (see [JXplorer download page](http://jxplorer.org/downloads/).)
- `Apache Directory Studio` (see [Apache Directory Studio download page](https://directory.apache.org/studio/downloads.html).)

## Integrating Coverity Connect with the Azure Entra ID (AD) Global Catalog

The Global Catalog component of Azure Entra ID is accessed using 3268/3269, and the AD
server is accessed using ports 389/636. When connecting to the Global Catalog, the AD
attributes typically used by Coverity are not available, and Test Connection
Settings results in an error.

To avoid this error, edit the ldap.properties file in the
<install_dir>/server/base/webapps/ROOT/WEB-INF/classes/
directory, as follows:

1. Set the `ldap.ldapValidationEnabled` property to
   `false`. This will turn off LDAP validation on Coverity Connect and thus should suppress the error.

Note: Make sure to verify that you can import users and groups, by using Test
User Search Settings and Test Group Search
Settings.

To enable Test Connection Settings to work, do the following:

1. Edit the `ldap.connectFilter=(objectClass=classSchema)` line and
   replace the `classSchema` with a known attribute in your AD
   catalog.

Note: Use the tools mentioned above to inspect your AD catalog.
