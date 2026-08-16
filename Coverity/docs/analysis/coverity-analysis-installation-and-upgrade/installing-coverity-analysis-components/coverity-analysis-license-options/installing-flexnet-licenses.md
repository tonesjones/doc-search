---
title: "Installing FlexNet licenses"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-flexnet-licenses.html"
content_id: "Je0PbImvBz~btlVA24~RmA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:56.226317+00:00"
---

# Installing FlexNet licenses

Coverity Analysis supports FlexNet licensing. FlexNet licensing is an alternative to the
default licensing process described in Coverity Analysis license options.

Note: FlexLM software is now called FlexNet Publisher. For more
information about FlexNet Publisher (including support contact information), visit the
FlexNet Publisher Community page at: <https://community.flexera.com/t5/FlexNet-Publisher/ct-p/FlexNet_Publisher>.

The following table lists how the Coverity Analysis commands map to FlexNet licensing
features. This information is helpful for troubleshooting purposes.

Table 1. Coverity commands mapped to FlexNet licensing features

| Coverity command | FlexNet licensing feature |
| --- | --- |
| `cov-analyze` | analysis.master and analysis.worker |
| `cov-commit-defects` | analysis.infrastructure |
| `cov-format-errors` | analysis.infrastructure |
| `cov-make-library` | analysis.master and analysis.worker |
| `cov-configure` | analysis.infrastructure |

There is one analysis.master for each analysis job.

There is one or more analysis.worker; one for each analysis worker.
The number of parallel analysis workers for `cov-analyze` is specified
in the `-j number-of-workers option`. There is exactly
one worker each for `cov-make-library`.

To set up FlexNet licensing for Coverity Analysis:

1. Verify that your platform is supported (see Supported platforms for Extend SDK and FlexNet licensing).
2. Run the `generate-flexnet-hostid` script and send the output to the support
   team. You can open a Support case by logging in to the
   [Black Duck Community site](https://community.blackduck.com/s/contactsupport).

   Note:
   The `generate-flexnet-hostid` script generates the MAC
   addresses of all NICs that will be used for FlexNet licensing.

   On Linux hosts, you must have the standard base `lsb` package
   installed on your machine in order to run
   `generate-flexnet-hostid`.

   On Solaris SPARC hosts, the FlexNet Publisher license manager cannot be configured on a
   non-global zone. This means that the license manager daemon
   (`lmgrd`) and the script that configures the daemon's
   initial setup ( `generate-flexnet-hostid`) must be installed
   on the global zone.

   Black Duck will send you, attached to an e-mail, a license file named
   coverity.lic.
3. Rename the sample-license.config file to
   license.config and put it in the
   <install_dir>/bin directory.

   Important:
   The <install_dir>/bin/license.config file must
   exist.

   If this file is empty, Coverity Analysis uses localhost for the
   default license server during the analysis and committing of defects.
4. Start the license server manager from the
   <install_dir>/bin directory by running the
   following command:

   ```
   > [nohup] lmgrd -c coverity.lic
   ```

   Important:
   For security reasons, the license server manager should be run as a user with limited privileges,
   and the host should only be accessible to authorized persons.

   The `lmgrd` command runs in the background. To run
   `lmgrd` in the foreground or to debug FlexNet license
   server problems on Windows, use the `-z` option. Avoid the
   `-z` option on UNIX or Linux systems because the
   `lmgrd` daemon cannot be stopped with Ctrl-C.

   To capture the output in a log file, use the `-l
   log-file` option.

   Note:
   On some UNIX or Linux
   systems, if you do not use the `nohup` command, it is not
   possible to log out of the license server from the shell where the
   `lmgrd` command ran. To avoid this, use the
   `nohup` command on UNIX or Linux systems.
5. Edit the
   <install_dir>/bin/license.config file to add your
   license server configuration information using the following
   syntax:

   `license-server [port1]@server1[,[port2]@server2 ... ]`

   Important:
   The license.config file that is used for FlexNet licensing needs to end with a newline character:
   that is, to end with a blank line.
   If it does not, cov-analyze will not recognize the last line of the file.

   Example:

   ```
   license-server @localhost
   ```

   Example:

   ```
   license-server 28000@flex1,28001@flex1,28000@flex2
   ```

For information about troubleshooting FlexNet licensing,
see Troubleshooting for FlexNet licensing.
