---
title: "Specify where to commit scan results"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-where-to-commit-scan-results.html"
content_id: "KwirjOuM9YZKtxvwisPHQA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:51.610746+00:00"
---

# Specify where to commit scan results

The following command generates a help file.
The new file contains configuration settings that specify the stream, `test1`, in which to save scan results:

```
coverity help config --setting url -o commit.connect.stream=test1
```

This command produces YAML output that appears like the following:

```
# Coverity configuration file.
# The schema is available here: <install-dir>/doc/configuration-schema.json
# For help on individual settings:      coverity help config --setting <setting>
# For a complete example configuration: coverity help config --show-all
# For help on configuration syntax:     coverity help config --syntax

# Specifies where the analysis results should be sent.
commit:

  # Coverity Connect configuration to use when committing defects to Coverity
  # Connect.
  connect:

    # The name of the stream to commit the results to.
    stream: test1

    # Absolute URL of where to commit the Coverity Connect results.
    ##url: <value>
```

- The schema at <install-dir>/doc/configuration-schema.json describes all configurable settings.
- `coverity help config --setting <setting>` will display help on a particular setting.
- `coverity help config --show-all` will display help on the complete configuration.
- Invoke `coverity help config --syntax` to see an explanation of how to represent setting values in the YAML and JSON formats.
- The stream location is specified by `commit: connect: stream: test1`.
- A location field for the analysis data is commented out: This location *is not* specified here.

Note:

- Comments begin with a single "`#`" character followed by a space.
- Commented-out configuration settings begin with "`##`" and no following space.

Output can also be in JSON format, as produced by the following command:

```
coverity help config --format json --setting url -o commit.connect.stream=test1
```

Here is the resulting JSON output:

```
{
    "_comment_configuration": "Coverity configuration file.\n
    The schema is available here: <install-dir>/doc/configuration-schema.json\n
    For help on individual settings:      coverity help config --setting <setting>\n
    For a complete example configuration: coverity help config --show-all\n
    For help on configuration syntax:     coverity help config --syntax",
    "_comment_commit": "Specifies where the analysis results should be sent.",
    "commit": {
        "_comment_connect": "Coverity Connect configuration to use when committing defects to Coverity Connect.",
        "connect": {
            "_comment_stream": "The name of the stream to commit the results to.",
            "stream": "test1",
            "_comment_url": "Absolute URL of where to commit the Coverity Connect results.",
            "__url": "<value>"
        }
    }
}
```

JSON does not directly support comments, so for the JSON output,
comments consist of the prefix `_comment_`, followed by the name of the
setting to which the comment refers. Commented-out configuration settings begin with
`__`.

- If a setting is requested that occurs at more than one location within the
  schema (such as `file`), then all such locations are
  included.
- A non-leaf-level setting includes everything under that setting. For example,
  `--setting commit` would show the entire
  `commit` section of the configuration.
- If any item under a specified non-leaf-level setting is a map (such as
  `checker-config`, whose keys are checker names, or
  `trust`, whose keys are trust properties), then every setting
  below that level is commented out and `<name>` is used as the
  (commented-out) key.
