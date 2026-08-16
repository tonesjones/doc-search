---
title: "Connecting to Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connecting-to-coverity-connect.html"
content_id: "GERByTQwaqwcp9QyXin64w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:50.179034+00:00"
---

# Connecting to Coverity Connect

Before you can configure and generate a report, you must set up a connection to your
instance of Coverity Connect, which stores the information that is included in the
report. Follow these steps to create your connection:

1. Locate the application executable, `cov-misra-report`, in
   <installation-directory>/bin
2. Double-click on the application icon to launch it. It starts in New
   Configuration mode. (Alternatively, double-click on a
   previously-created configuration file to launch the application with that
   configuration.)
3. On the Connection tab, enter the Host
   Name and Port Number. If your Coverity
   Connect administrator has enabled SSL, enter the HTTPS port number associated
   with your Coverity Connect host. The default HTTPS port is 8443.

     
    [image: image]
4. Check the Coverity Connect URL to make sure it is correct.
5. If SSL is used with the connection, select Secured using
   SSL.

   Note: If an additional CA certificate is needed, select Use Extra CA
   Certificate, and click Browse to identify
   the file.
6. Enter the Username and Password for
   Coverity Connect. The password is *not* stored in the configuration
   file.
7. Click Check Connection to test the connection to Coverity
   Connect.

If you want to regenerate a report using the same input data, you do not have to
reconnect to Coverity.
