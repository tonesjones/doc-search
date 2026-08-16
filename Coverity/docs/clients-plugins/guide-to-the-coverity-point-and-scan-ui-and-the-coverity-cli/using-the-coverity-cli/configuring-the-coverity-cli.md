---
title: "Configuring the Coverity CLI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-coverity-cli.html"
content_id: "54Uqc2xYe2k2OLbzh4xinA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:49.617451+00:00"
---

# Configuring the Coverity CLI

You can configure Coverity CLI actions using a configuration file in YAML or
JSON format and by using options on the `coverity` command line.
Configuration can be helpful if you need to support CI/CD or if you want to customize
your scans and retain that customization. The schema for this configuration format is
described in Options reference.

Configuration settings allow you to do things like the following:

- Customize build and capture actions.
- Customize the checkers and coding standards used to analyze your build.
- Reference special-purpose configuration files such as CodeXM checker configuration or security directives.
- Specify information about Coverity Connect deployment and security.

At a minimum, the configuration file that you create manually or by using the `coverity setup` command
must specify the stream to use and the location of the Coverity Connect server where you want to save results.

For example:

```
commit:
  connect:
    stream: commons-cli
    url: https://connect.example.com
```

For reference information about the configuration schema, see
Options reference.

Additional settings and setup overrides can also be provided to the `setup` subcommand.

For example:

```
> setup -o analyze.location=connect -o commit.connect.stream=setup-comms-cli
```

See Editing configuration settings
