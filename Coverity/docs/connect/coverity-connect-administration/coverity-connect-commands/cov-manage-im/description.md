---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "YQVaDftFU8Juf0cJzBmxxg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:31.972527+00:00"
---

# Description

Important: If Coverity Connect is deployed in the cloud, refer
to the section Coverity tools in a Coverity cloud deployment in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on using the
`cov-manage-im` command in the cloud deployment.

The `cov-manage-im` command modifies and queries information for
defects, projects, and streams in Coverity Connect. This command also outputs logging
information to <install_dir>/logs/cim.log.

This command has the following modes of operation:

- Defects mode
- Projects mode
- Streams mode
- Triage mode
- MOTD mode
- Commit mode
- Notification mode
- Authentication key mode

The `cov-manage-im` command can operate on (update or delete) the set of
objects that were matched by a query within a single command line.

Each `cov-manage-im` mode accepts CONNECTION
options that allow you specify connection settings such as host name, port
number, and so forth, on the command line.

Alternatively, you can use the
coverity_config.xml file, which is a configuration file that
you can edit to store connection options for `cov-manage-im`. If you
run the `cov-manage-im` command from a Coverity Analysis or Coverity
Analysis package, you can create a default version of this file at
<install_dir>/config/coverity_config.xml by running
the `cov-configure` command. After you run the
`cov-configure` command, you must add the elements as in the
example that follows, if you want to include connection options in the configuration
file instead of on the command line. If you run the `cov-manage-im`
command from a Coverity Connect package, you must manually create the default
coverity_config.xml file, and move it to
<install_dir>/config/coverity_config.xml.

The following example element in the coverity_config.xml file
defines connection options for Coverity Connect:

```
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>
  <config>
    <cim>
      <url>cim.company.com:8443</url>
      <client_security>
         <user>test</user>
         <password>secret</password>
         <ssl>yes</ssl>
         <certs>/pathto/.certs</certs>
      </client_security>
    </cim>
  </config>
</coverity>
```

Note: Glob arguments are patterns used for filter expressions. In glob patterns,
`*` matches zero or more characters, and `?` matches
exactly one character.

You can configure this command to use a forward proxy when communicating with the Coverity
Connect server. The setup is the same as with the `cov-commit-defects`
command. For more information on this topic, see Using a forward proxy in
the `cov-commit-defects` section.
