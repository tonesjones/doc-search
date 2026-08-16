---
title: "Configuring the browser"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-browser.html"
content_id: "V9150u9ovnUxt6dOdn5w~A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:45.348362+00:00"
---

# Configuring the browser

Browsers must be configured to use Kerberos. The procedure varies by browser and
operating system. It may be necessary to obtain a Kerberos ticket for the browser as
well.

Note: In some networks, a server may be configured to share login credentials with other
servers. This is called "credential delegation." Credential delegation can expose the
credentials to third parties, which in theory is a security vulnerability. The
procedures for configuring browsers for Kerberos include a step for enabling credential
delegation. Coverity Connect does not use credential delegation, so unless otherwise
needed, consider refraining from enabling credential delegation. The specific settings
are indicated in the respective procedures.

## Configuring the Firefox browser on Linux and Mac OS

To configure the Firefox browser to use Kerberos:

1. Enter `about:config` in the address bar.
2. In Filter, enter `negotiate`.
3. Double-click network.negotiate-auth.trusted-uris.
4. Enter the Coverity Connect domain name.
5. Repeat the procedure for the
   network.negotiate-auth.delegation-uris entry,
   using the same domain.

   Note: This setting enables credential delegation. It is optional.
6. Double-click network.negotiate-auth.allow-non-fqdn to
   change the Value to true.

## Configuring the Chrome browser on Linux and Mac OS

To configure the Chrome browser to use Kerberos, start the browser from the command
line with the following arguments:

`--auth-server-whitelist="*.example.com"
--auth-negotiate-delegate-whitelist="*.example.com"`

Replace the `"*.example.com"` with the domain used in your
organization.

Note: The setting `--auth-negotiate-delegate-whitelist` enables
credential delegation. It is optional.

## Obtaining an initial Kerberos ticket

If the client is not in a Windows Azure Entra ID network, then it is necessary to
obtain an initial Kerberos Ticket Granting Ticket (TGT). This ticket provides
evidence that the client (browser) is authenticated in the network. This procedure
will work if the client is in a Kerberos realm.

1. In a command shell, type `kinit` and enter the user password.
   This retrieves the Kerberos ticket from the KDC.
2. To view the Kerberos tickets on the client, enter `klist`.
