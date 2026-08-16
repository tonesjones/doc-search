---
title: "Understanding database information in the cim.properties file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/understanding-database-information-in-the-cim.properties-file.html"
content_id: "zJ97NF~wNxNOoW7YuB5b8w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:58.868031+00:00"
---

# Understanding database information in the cim.properties file

To edit the <install_dir>/config/cim.properties file:

1. Stop Coverity Connect:

   Linux:

   ```
   > cd <install_dir>/bin
   > ./cov-im-ctl stop
   ```

   Windows:

   Go to
   <install_dir>\bin and double click the
   `cov-stop-im` program.
2. Check and, if necessary, edit the properties as follows:
   - `embeddedDatabase=false`

     This property is set to `true` when Coverity Connect uses
     an embedded database. However, after you have installed Coverity Connect
     with an external database, you cannot just change this value to
     `true` to change to an embedded database.
   - `maindb.name=database_name`
   - `maindb.user=ROLE_name`
   - `maindb.url =
     jdbc\:postgresql\://database_server_name\:port_number/database_name`

     This property value takes the form of a JDBC URL.

     To configure an
     SSL connection to the external database, append the following query
     parameters to this property value and set them as described:

     - `sslmode=disable | allow | prefer | require | verify-ca |
       verify-full`
     - `sslrootcert=`
       *absolute path to SSL root certificate*
       `sslcert=`
       *absolute path to client certificate*
     - `sslkey=`
       *absolute path to client certificate key*
     - `sslpassword=`
       *password for SSL key*

   The following example, shows how to configure an SSL connection to an
   external database with the SSL mode set to `verify-full` and
   using the SSL root certificate `/tmp/root.cert` for server
   authentication, and the client certificate `/tmp/client.cert`,
   the certificate key `/tmp/client.pk8`, and the password
   `123456` for client authentication:

   ```
   #Mon Sep 14 11:13:39 PDT 2009
   embeddedDatabase=false
   maindb.name=jdoe_main
   db.driver=org.postgresql.Driver
   db.dialect=org.hibernate.dialect.PostgreSQLDialect
   maindb.password=afy687
   maindb.user=jdoe
   maindb.url=jdbc\:postgresql\://t-postgres-03\:5432/jdoe_main?sslmode=verify-full&sslrootcert=/tmp/root.cert&sslcert=/tmp/client.cert&sslkey=/tmp/client.pk8&sslpassword=123456
   dir.log=/usr/local/jdoe/CIM/server/base/logs
   commitPort=9090
   dir.temp=/usr/local/jdoe/CIM/server/base/temp
   ```

You must restart Coverity Connect for your changes to take effect.
