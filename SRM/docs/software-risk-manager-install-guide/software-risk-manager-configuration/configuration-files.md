---
title: "Configuration Files"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuration-files.html"
content_id: "ySICqz5Mq1XaOOGQWALWOw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:19.118076+00:00"
content_hash: "8dfe06760521a4dc3b2b02b9790d8746a1165ea33f27256b7378eb963e963759"
---

# Configuration Files

## Log Configuration File

Software Risk Manager uses [Logback](http://logback.qos.ch) for logging. A sample
`logback.xml` file is provided in the appdata directory. For more
information about the logging configuration, consult the [Logback manual](http://logback.qos.ch/manual/configuration.html).

### Automatic Log Deletion

For fresh installations of Software Risk Manager, the Logback configuration file
will specify a default retention period of seven days. To change the default,
replace the value of `maxHistory` in the
`logback.xml` file with the desired number of days to retain
a log file. Log files outside of this period will be deleted.

Existing installations may achieve this same behavior by adding the following
within the `<rollingPolicy>` block in the
`logback.xml` configuration file.

```
<!-- keep 7 days worth of history -->
<maxHistory>7</maxHistory>
```

After making any changes, it is recommended that you delete the log files—except
`codedx.log`—from the `log-files` directory to
avoid unexpected behavior. Problems may occur because existing installations
will likely exceed the maximum number of log files Logback will delete at a
time.

**Note:** With this configuration change, eligible log files are deleted with
each rollover period (which is daily for the default Software Risk Manager
Logback configuration). If you also want log files to be deleted when the
Software Risk Manager server is started, add the code shown below just after
`maxHistory`.

```
<cleanHistoryOnStart>true</cleanHistoryOnStart>
```

You must restart the Tomcat server after you've completed your revisions. This
can be done by launching the Software Risk Manager application's Manager Tool,
clicking the Manage Servers tab, selecting Tomcat server, and then clicking
Restart.

## Software Risk Manager Properties File

The most important configuration file is `codedx.props`, also referred
to in this guide as the "props" file. Located in the appdata directory, the props
file configuration determines a variety of settings, including the database
connection information, the analysis behavior, and Active Directory integration.

The props file is formatted as a [.properties file](http://en.wikipedia.org/wiki/.properties), using key-value pairs to set
configuration fields.

When changing this file, remember to delete the comment designation
(`#`) at the beginning of the line.

You must restart the Tomcat server after you've completed any revisions. This can be
done by launching the Manager Tool, clicking the Manage Servers tab, selecting
Tomcat server, and then clicking Restart.
