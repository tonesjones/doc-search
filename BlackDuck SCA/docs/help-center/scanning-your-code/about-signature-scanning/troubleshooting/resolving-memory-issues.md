---
title: "Resolving memory issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/resolving-memory-issues.html"
content_id: "3JGr95xUJoFfkbX2D71udw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:45.029044+00:00"
---

# Resolving memory issues

You may receive the following error when trying to run Signature Scanner:

```
ERROR: Insufficient memory <Value>
```

To resolve this error, increase the memory that is available for use by Signature Scanner. You can accomplish this by using the SCAN_CLI_OPTS
environment variable to increase the values for the initial and maximum heap size.

Note: The value you specify for the maximum heap size must be larger than that value shown in the
error message.

The instructions shown below describe how to use the command line to configure the
environment variable. These instructions can be adapted so you can create an alias
definition in Linux or Mac OS X or use the Control Panel in Windows.

To configure the SCAN_CLI_OPTS environment variable in Linux or Mac OS X:

1. Start a terminal session.
2. At the command line, type:

   ```
   export SCAN_CLI_OPTS="-Xms<Initial heap size> -Xmx<Maximum heap size>"
   ```

   For example, to set the minimum size to 1 GB and the maximum to 6 GB:

   ```
   export SCAN_CLI_OPTS="-Xms1g -Xmx6g"
   ```
3. Close the terminal session.

To configure the SCAN_CLI_OPTS environment variable in Windows :

1. At the command line, type:

   ```
   set SCAN_CLI_OPTS=-Xms<Initial heap size> -Xmx<Maximum heap size>
   ```

   For example, to set the minimum size to 1 GB and the maximum to 6 GB:

   ```
   set SCAN_CLI_OPTS=-Xms1g -Xmx6g
   ```

   Note: There are limits in the maximum scan size when scanning with a 32-bit system as the
   increase in addressable memory is restricted by the limitations of the 32-bit
   system.
