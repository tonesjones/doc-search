---
title: "Restarting Coverity Connect and verifying the new certificate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/restarting-coverity-connect-and-verifying-the-new-certificate.html"
content_id: "Q_PyMoziiDYDfopckTnd1w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:33.165589+00:00"
---

# Restarting Coverity Connect and verifying the new certificate

Important:
For any configuration changes to take effect, you must restart Coverity Connect.

1. Restart the Coverity Connect service.

   On Windows, start it via **Services** (net start "Coverity Connect" at the command prompt),
   or through the **Services** control panel.

   On Linux, use `systemctl start coverity` or an appropriate startup script provided by Coverity,
   such as `cov-start-im`.

Be alert for problems. If the service fails to start or it stops immediately, check the following:

- Check the Coverity logs for clues.

  Look at catalina.out and coverity.log to see if they contain error messages.
- Check the Tomcat logs, which are usually saved in <cc_install_dir>/server/logs/.

  Common issues can include:

  - A typo in server.xml (XML parse error).
  - A wrong keystore password (you'll see an error such as `"Keystore was tampered with, or password was incorrect"` in the log).
  - An incorrect path to the keystore: `file not found` exception.
  - A message saying `"keyAlias not found"`.

    This means the alias specified in server.xml doesn’t exist in your keystore:
    Either correct the alias in server.xml or import the certificate under the expected alias.

  If such errors appear, fix the server.xml contents accordingly.
  Tomcat will not restart until these errors are resolved.
