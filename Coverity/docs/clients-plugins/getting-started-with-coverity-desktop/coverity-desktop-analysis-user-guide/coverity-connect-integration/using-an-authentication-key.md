---
title: "Using an authentication key"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-an-authentication-key.html"
content_id: "7HRk3qw2mDXaCCPMt5oSuw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:50.180038+00:00"
---

# Using an authentication key

It is recommended that you create an authentication key to provide your Coverity Connect
credentials to `cov-run-desktop`. The authentication key allows you to
run Desktop Analysis without having to specify your password each time. To create an
authentication key, run the following command:

```
> cov-run-desktop --create-auth-key
```

The command above gets the Coverity Connect host information from
coverity.conf, prompts for your Coverity Connect password, and
writes the authentication key to a default directory:

- Windows directory: %APPDATA%/Coverity/authkeys
- Unix directory: $HOME/.coverity/authkeys

The `cov-run-desktop --setup` command will create an
authentication key if one has not already been created.

Once it has been created, every `cov-run-desktop` invocation that needs an
authentication key will get it from that location.

Note: The ability to create an
authentication key is not supported on the FreeBSD platform. As a workaround, it is
possible to create the key on another platform and then copy the authentication key
file to a different machine.
