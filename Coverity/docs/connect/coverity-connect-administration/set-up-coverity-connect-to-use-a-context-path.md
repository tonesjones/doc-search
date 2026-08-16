---
title: "Set up Coverity Connect to use a context path"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/set-up-coverity-connect-to-use-a-context-path.html"
content_id: "5kdyxw2uIncYBsfTpPX14A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:28.492265+00:00"
---

# Set up Coverity Connect to use a context path

Note: If Coverity Connect is deployed in the cloud, this section does not apply. Context
path is not supported.

These are the steps to set up a context path for the Coverity Connect Web
application.

Important: Before you make any of the following changes, make sure that Coverity
Connect is *no longer running*.

1. **Rename ROOT.war.**

   1. Go to the directory server/base/webapps/, and then
      delete the ROOT/ subdirectory.
   2. Rename ROOT.war to
      myContextPath.war.

      The string myContextPath.war
      represents the context path itself. For example,
      newPath.war locates Coverity Connect at
      localhost:8080/newPath/. Tomcat will unpack the
      new .war file and create a Web service that uses
      the new path name.

      Note: The default value of ROOT.war is simply
      /.
2. **Modify context.xml.**

   1. Locate context.xml. It should be in the directory
      server/base/conf/.
   2. Open context.xml in a text or code editor.
   3. In context.xml, locate the `Context`
      record.

      The `Context` record will look something like the
      following code:

      ```
      <Context sessionCookieName="COVJSESSIONID11171NR" sendRedirectBody="true">
          .
          .
          .
      </Context>
      ```
   4. Add a `docBase` entry to the `Context`
      record.

      Set the value of `docBase` to the same string you used to
      name the .war file.

      For example, the opening of the `Context` record should
      now appear something like this:

      ```
      <Context sessionCookieName="COVJSESSIONID11171NR" sendRedirectBody="true" docBase="newPath">
      ```
   5. Save the change.
3. **Update web.properties.**

   1. Locate web.properties. It should be in the directory
      config/.
   2. Open web.properties in a text or code
      editor.
   3. Locate the `web.url` property.

      This property is set to the server's IP address.
   4. Append the context path to the value of the `web.url` property:

      For example, if your context path is `newPath`, your
      edited `web.url` property will look similar to the
      following:

      ```
      web.url=http\://ccserver_hostname\:8080/newPath
      ```

      For an HTTPS-only Coverity Connect server, your edited
      `web.url` property will look similar to this:

      ```
      web.url=https\://ccserver_hostname\:443/newPath
      ```
   5. Save the change.
4. **Restart Coverity Connect.**

   - Now you will access Connect at the */<myContextPath>* link; for example, /newPath.
