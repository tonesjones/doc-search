---
title: "Updating TLS/SSL: Additional tips, warnings, and information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/updating-tls/ssl-additional-tips-warnings-and-information.html"
content_id: "VULsCddtCSFjpfuccPap9w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:33.817788+00:00"
---

# Updating TLS/SSL: Additional tips, warnings, and information

- **Keep private keys secure:**

  Whether you keep the private key for your certificate in the keystore or in a separate file, it must be kept secret.
  Never share the keystore or .key file publicly.
  Treat the keystore file with the same care as you would a password: It grants access to your server.
- **Use strong passwords:**

  In examples, we used the default password `Coverity` for simplicity, but in a real environment you shouild use a stronger keystore password,
  preferably a longer one.
  If you change the password from the default, remember to update server.xml accordingly.

  Remember:
  The default Java keystore password is `changeit`. This is widely known and *should be changed*.
- **Back up the keystore and certificate files:**

  Keep backups of your working keystore and certificate files.
  This way, if something should go wrong or if you need to roll back to a previous certificate, you can do so quickly.
  Also, when your certificate is nearing expiry next time, you already have these steps and the backups to help renew your certification.
- **Distribute trust for internal Certificate Authorities:**

  If your new certificate is issued by a private or an internal Certificate Authority, as opposed to a public one, then client systems such as
  web browsers, Coverity users' machines, and so on) must trust that Certificate Authority.

  Usually this means installing the CA's root certificate in the clients' trusted certificate store.
  In the context of Coverity, any Coverity Analysis tools or integrations—such as commit hooks or the
  Coverity Command-Line Interface (CLI) tools—that connect to the Coverity Connect server need to trust its certificate.
  The Coverity installation provides a bundle of trusted CAs in the file certs/ca-certs.pem.
  You might need to add your internal CA's certificate to that trust store on each analysis machine so that it can trust the
  Coverity Connect server.

  To do so, open ca-certs.pem and append your CA's PEM-formatted certificate to the file.
  This ensures that Coverity tools don't throw `"untrusted certificate"` errors when connecting.

  This step is not required for publicly trusted certificates, as those are already in the trust store.
- **Include intermediate certificates:**

  Always remember to include intermediate certificates.
  Without them, users might get trust warnings even if your server certificate is valid.
  The keystore approach we showed earlier handles this situation by importing the intermediate certificate into the chain.
- **Plan for future renewals:**

  Whenever you need to update the certificate again (say, after a year or two when the certificate expires),
  you can follow a process similar to the previously described scenarios.

  - If you reuse the key again, this process will be similar to Scenario 1.

    Mark your calendar to start the renewal process before the certificate expires to avoid any downtime.
