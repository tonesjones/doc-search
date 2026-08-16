---
title: "Troubleshooting for FlexNet licensing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-for-flexnet-licensing.html"
content_id: "s2CCBK~AvsFE3ghI_lC3ew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:56.978473+00:00"
---

# Troubleshooting for FlexNet licensing

You might encounter the following common issues with licensing of Coverity Analysis.

Note: FlexLM software is now called FlexNet Publisher. For more
information about FlexNet Publisher (including support contact information), visit the
FlexNet Publisher Community page at: <https://community.flexera.com/t5/FlexNet-Publisher/ct-p/FlexNet_Publisher>.

## I get an `lmutil not found` error when I run `generate-flexnet-hostid`.

**Solution:**

Depending on the platform, installing the Linux Standard Base (`lsb`
or `lsb-base` or `lsb-core`) package on your machine
will solve the problem.

For platforms where the Linux Standard Base package is not available (for example,
32-bit Debian12), follow these steps:

1. Verify that <INSTALL_ROOT>/bin/lmutil exists
2. Verify that running the command: <INSTALL_ROOT>/bin/lmutil
   --help generates an error message and no help text
3. Verify that the host machine *does not* have the file
   /lib/ld-lsb.so.3
4. Verify that the host machine *does* have the file
   /lib/ld-linux.so.2
5. If necessary, install the `patchelf` binary. On Debian,
   this might be done with apt install patchelf
6. Execute the following commands:

   ```
   patchelf --set-interpreter /lib/ld-linux.so.2 <INSTALL_ROOT>/bin/lmutil
   patchelf --set-interpreter /lib/ld-linux.so.2 <INSTALL_ROOT>/bin/lmgrd
   patchelf --set-interpreter /lib/ld-linux.so.2 <INSTALL_ROOT>/bin/covlicd
   ```
7. Repeat the command to generate the license ID

## A long message displays when I run the `lmgrd` command.

**Solution:** The following FlexNet marketing message displays when you run the
`lmgrd`command. Real error messages often proceed or follow it.
Make sure to scroll up to the top of your screen to read any error messages that
display. For the sake of brevity, this content is removed from the remaining
questions and solutions.

```
13:53:54 (lmgrd) -----------------------------------------------
13:53:54 (lmgrd)   Please Note:
13:53:54 (lmgrd) 
13:53:54 (lmgrd)   This log is intended for debug purposes only.
13:53:54 (lmgrd)   In order to capture accurate license
13:53:54 (lmgrd)   usage data into an organized repository,
13:53:54 (lmgrd)   please enable report logging. Use Macrovision's
13:53:54 (lmgrd)   software license administration  solution,
13:53:54 (lmgrd)   FlexNet Manager, to  readily gain visibility
13:53:54 (lmgrd)   into license usage data and to create
13:53:54 (lmgrd)   insightful reports on critical information like
13:53:54 (lmgrd)   license availability and usage. FlexNet Manager
13:53:54 (lmgrd)   can be fully automated to run these reports on
13:53:54 (lmgrd)   schedule and can be used to track license
13:53:54 (lmgrd)   servers and usage across a heterogeneous
13:53:54 (lmgrd)   network of servers including Windows NT, Linux
13:53:54 (lmgrd)   and UNIX. Contact Macrovision at
13:53:54 (lmgrd)   www.macrovision.com for more details on how to
13:53:54 (lmgrd)   obtain an evaluation copy of FlexNet Manager
13:53:54 (lmgrd)   for your enterprise.
13:53:54 (lmgrd) 
13:53:54 (lmgrd) -----------------------------------------------
```

## The `lmgrd` command uses a different port number than the one in my license.config file.

**Solution:** If you provide a port number in the
license.config file, use the port number of
`lmgrd`. In the following example, `lmgrd`
uses port 27000 and `covlicd` (the Coverity vendor daemon) uses
port 60185. Use the `lmgrd` port in the
license.config file.

```
$ ./lmgrd -c coverity.lic
13:53:54 (lmgrd) -----------------------------------------------
...
13:53:54 (lmgrd) -----------------------------------------------
13:53:54 (lmgrd) FlexNet Licensing (v11.5.0.0 build 56285 amd64_re3) started on
bl-1-4 (linux) (4/3/2008)
13:53:54 (lmgrd) Copyright (c) 1988-2007 Macrovision Europe Ltd. and/or
Macrovision Corporation. All Rights Reserved.
13:53:54 (lmgrd) US Patents 5,390,297 and 5,671,412.
13:53:54 (lmgrd) World Wide Web:  http://www.macrovision.com
13:53:54 (lmgrd) License file(s): coverity.lic
13:53:54 (lmgrd) lmgrd tcp-port 27000
13:53:54 (lmgrd) Starting vendor daemons ... 
13:53:54 (lmgrd) Started covlicd (internet tcp_port 60185 pid 32023)
13:53:54 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285 amd64_re3
13:53:54 (covlicd) Server started on bl-1-4 for:        prevent.platform 
13:53:54 (covlicd) prevent.dotnet       prevent.java    prevent.ccpp
13:53:54 (covlicd) EXTERNAL FILTERS are OFF
13:53:54 (lmgrd) covlicd using TCP-port 60185
```

## The license server cannot verify my license.

**Solution:** The license.config file might be incorrectly
configured or empty. Verify that the license server in the
<install_dir>/bin/license.config file correctly
points to where the `lmgrd` command is running.

The DNS server might be down. If the DNS server is down, use an IP address in the
license.config file instead of a hostname.

The license server might not be running. If it is not running, use the
`lmgrd` command to start it.

The firewall on the license server might be blocking the `lmgrd`
port. If so, make sure that the server where the `lmgrd` command is
running does not block ports 27000 through 27009 for incoming TCP messages.

## The license manager cannot initialize.

**Solution:** If you use the `lmgrd` command without the
`-c` option, the command fails and displays an error message that
includes the text `Cannot find license file` at the top of the output
on the screen. Retry the `lmgrd` command using the
`-c` option.

```
$ ./lmgrd coverity.lic 
license manager: can't initialize: Cannot find license file.
The license files (or license server system network addresses) attempted are 
listed below.  Use LM_LICENSE_FILE to use a different license file,
or contact your software provider for a license file.
Filename:      /usr/local/flexlm/licenses/license.dat
License path:  /usr/local/flexlm/licenses/license.dat:
FlexNet Licensing error:-1,359.  System Error: 2 "No such file or directory"
For further information, refer to the FlexNet Licensing documentation,
available at "www.macrovision.com".
14:04:49 (lmgrd) -----------------------------------------------
...
14:04:49 (lmgrd) -----------------------------------------------
14:04:49 (lmgrd) Using license file "/usr/local/flexlm/licenses/license.dat"
```

## The license file is different than the one that you expect.

**Solution:** There are two reasons why the license file seems to be different
than the one that you expect.

If the date on the license server is incorrect, the following type of error displays
and likely causes confusion. Change the date on the license server to today's
date.

```
21:04:27 (lmgrd) -----------------------------------------------
...
21:04:27 (lmgrd) -----------------------------------------------
21:04:27 (lmgrd) FlexNet Licensing (v11.5.0.0 build 56285 i86_re3) started on
rh el3x86 (linux) (5/11/2007)
21:04:27 (lmgrd) Copyright (c) 1988-2007 Macrovision Europe Ltd. and/or
Macrovis ion Corporation. All Rights Reserved.
21:04:27 (lmgrd) US Patents 5,390,297 and 5,671,412.
21:04:27 (lmgrd) World Wide Web:  http://www.macrovision.com
21:04:27 (lmgrd) License file(s): coverity.lic
21:04:27 (lmgrd) lmgrd tcp-port 27000
21:04:27 (lmgrd) Starting vendor daemons ...
21:04:27 (lmgrd) Started covlicd (internet tcp_port 35916 pid 5362)
21:04:27 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285 i86_re3
21:04:27 (covlicd) Feature prevent.platform is not enabled yet, starts on
12-may -2008
21:04:27 (covlicd) Feature prevent.ccpp is not enabled yet, starts on
12-may-200 8
21:04:27 (covlicd) License server system started on rhel3x86
21:04:27 (covlicd) No features to serve, exiting
21:04:27 (covlicd) EXITING DUE TO SIGNAL 36 Exit reason 4
21:04:27 (lmgrd) covlicd exited with status 36 (No features to serve)
21:04:27 (lmgrd) covlicd daemon found no features.  Please correct
21:04:27 (lmgrd) license file and re-start daemons.
21:04:27 (lmgrd)
21:04:27 (lmgrd) This may be due to the fact that you are using
21:04:27 (lmgrd) a different license file from the one you expect.
21:04:27 (lmgrd) Check to make sure that:
21:04:27 (lmgrd) coverity.lic
21:04:27 (lmgrd) is the license file you want to use.
```

If you created the license file coverity.lic by copying and
pasting from a Windows machine, the space character (ASCII 32) might be replaced
with a 160 character (hex 0xA0). To resolve this, replace all the 0xA0 characters in
the license file with spaces. In this case, the following message displays:

```
$ ./lmgrd -c coverity.lic                    
9:58:10 (lmgrd)
9:58:10 (lmgrd) -----------------------------------------------
...
9:58:10 (lmgrd) -----------------------------------------------
9:58:10 (lmgrd) 
9:58:10 (lmgrd) 
9:58:10 (lmgrd) FlexNet Licensing (v11.5.0.0 build 56285 amd64_re3) started on
bl-1-4 (linux) (4/23/2008)
9:58:10 (lmgrd) Copyright (c) 1988-2007 Macrovision Europe Ltd. and/or
Macrovision Corporation. All Rights Reserved.
9:58:10 (lmgrd) US Patents 5,390,297 and 5,671,412.
9:58:10 (lmgrd) World Wide Web:  http://www.macrovision.com
9:58:10 (lmgrd) License file(s): coverity.lic
9:58:10 (lmgrd) lmgrd tcp-port 27000
9:58:10 (lmgrd) Starting vendor daemons ... 
9:58:10 (lmgrd) Started covlicd (internet tcp_port 50476 pid 9281)
9:58:10 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285 amd64_re3
9:58:10 (covlicd) License server system started on bl-1-4
9:58:10 (covlicd) No features to serve, exiting
9:58:10 (covlicd) EXITING DUE TO SIGNAL 36 Exit reason 4
9:58:10 (lmgrd) covlicd exited with status 36 (No features to serve)
9:58:10 (lmgrd) covlicd daemon found no features.  Please correct
9:58:10 (lmgrd) license file and re-start daemons.
9:58:10 (lmgrd) 
9:58:10 (lmgrd) This may be due to the fact that you are using
9:58:10 (lmgrd) a different license file from the one you expect.
9:58:10 (lmgrd) Check to make sure that:
9:58:10 (lmgrd) coverity.lic 
9:58:10 (lmgrd) is the license file you want to use.
```

## The `lmutil lmdown` command cannot shut down the license server.

**Solution:** The license server is not running. The following message displays:

```
$ lmutil lmdown
lmutil - Copyright (c) 1989-2007 Macrovision Europe Ltd. and/or Macrovision
Corporation. All Rights Reserved.
Shutdown failed: Cannot connect to license server system. (-15,570:115
"Operation now in progress")
```

## The `lmutil lmdiag` command returns a start date of 1-jan-1990.

**Solution:** This is bug OA-002429 from Acresso (FlexNet). Although the start
date is incorrect, the `lmutil lmdiag` command works as expected.

```
$ lmutil lmdiag
"commit" v2008.03, vendor: covlicd
License server: localhost
floating license  starts: 1-jan-1990,   expires: 26-mar-2008
                    
This license can be checked out
```

## The clock difference is too large between the client and server systems.

**Solution:** If the time difference between the client and server systems is
larger than two days, the `cov-analyze`,
`cov-commit-defects`, and `cov-format-errors`
commands will not run because they cannot verify the license.

## The behavior of the following `lmutil lmdown` command query can cause confusion:

```
Are you sure (y/n)?
```

**Solution:** Any letter after `y` or `Y` is
ignored. If the first letter is not `y` or `Y`, the
following message displays:

```
"No server selected, exiting"
```

## The .flexlmrc file settings are not recognized.

**Solution:** Coverity command-line utilities do not use the
.flexlmrc file. Store license settings in the
<install_dir>/bin/license.config file.

## The /usr/tmp/.flexlm file cannot be created.

**Solution:** To resolve this, run the license server from a supported platform
and edit the <install_dir>/bin/license.config file to
point to the correct location of the license server. FlexNet on Linux is supported
on systems running Red Hat Enterprise Linux 3, Red Hat Enterprise Linux 4, or Red
Hat Enterprise Linux 5.

```
23:41:25 (lmgrd) -----------------------------------------------
...
23:41:25 (lmgrd) -----------------------------------------------
23:41:25 (lmgrd)
23:41:25 (lmgrd) The license server manager (lmgrd) running as root:
23:41:25 (lmgrd)        This is a potential security problem
23:41:25 (lmgrd)        and is not recommended.
23:41:25 (lmgrd) Can't make directory /usr/tmp/.flexlm, errno: 2(No such file
or directory)
23:41:25 (lmgrd) Can't make directory /usr/tmp/.flexlm, errno: 2(No such file
or directory)
23:41:25 (lmgrd) Can't open /usr/tmp/.flexlm/lmgrdl.29777, errno: 2
license manager: can't initialize: 
For further information, refer to the FlexNet Licensing End User Guide,
available at "www.macrovision.com".
23:41:25 (lmgrd) Can't remove statfile /usr/tmp/.flexlm/lmgrdl.29777: errno No
such file or directory
```

## The `lmgrd -z` option leaves `lmgrd` in the foreground on UNIX and Linux systems.

**Solution:** If you used the `lmgrd -z` option on UNIX or Linux
systems, Ctrl-C does not terminate the license server. To terminate the license
server, manually terminate all `lmgrd` and
`covlicd` processes.

## The `covlicd` command exits unexpectedly.

**Solution:** If the `lmgrd` and `covlicd`
commands run on an unsupported platform, the following error message displays:

```
./lmgrd -c coverity.lic
18:20:04 (lmgrd) -----------------------------------------------
...
18:20:04 (lmgrd) -----------------------------------------------
18:20:04 (lmgrd)
18:20:04 (lmgrd)
18:20:04 (lmgrd) FlexNet Licensing (v11.4.100.0 build 50818 i86_re3) started on
lee-linux (linux) (4/26/2008)
18:20:04 (lmgrd) Copyright (c) 1988-2007 Macrovision Europe Ltd. and/ or
Macrovision Corporation. All Rights Reserved.
18:20:04 (lmgrd) US Patents 5,390,297 and 5,671,412.
18:20:04 (lmgrd) World Wide Web:  http://www.macrovision.com
18:20:04 (lmgrd) License file(s): coverity.lic
18:20:04 (lmgrd) lmgrd tcp-port 27000
18:20:04 (lmgrd) Starting vendor daemons ...
18:20:04 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285
i86_re3
18:20:04 (covlicd) lmgrd version 11.4, covlicd version 11.5
18:20:04 (lmgrd) Started covlicd (internet tcp_port 35481 pid 22149)
coverity@lee-linux:~/prevent-linux-4.0.0.beta1/bin$ 18:20:04
(covlicd) Server started on lee-linux for: prevent.platform
18:20:04 (covlicd) prevent.ccpp
18:20:04 (covlicd) EXTERNAL FILTERS are OFF
18:20:04 (lmgrd) covlicd using TCP-port 35481
18:20:04 (lmgrd) covlicd exited with status 0 signal = 17
18:20:04 (lmgrd) Since this is an unknown status, license server
18:20:04 (lmgrd) manager (lmgrd) will attempt to re-start the vendor daemon.
18:20:04 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285
i86_re3
18:20:04 (covlicd) lmgrd version 11.4, covlicd version 11.5
18:20:04 (lmgrd) REStarted covlicd (internet tcp_port 43652 pid 22155)
18:20:04 (covlicd) Server started on lee-linux for:     prevent.platform
18:20:04 (covlicd) prevent.ccpp
18:20:04 (covlicd) EXTERNAL FILTERS are OFF
18:20:04 (lmgrd) covlicd using TCP-port 43652
18:20:04 (lmgrd) covlicd exited with status 0 signal = 17
18:20:04 (lmgrd) Since this is an unknown status, license server
18:20:04 (lmgrd) manager (lmgrd) will attempt to re-start the vendor daemon.
18:20:04 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285
i86_re3
18:20:04 (covlicd) lmgrd version 11.4, covlicd version 11.5
18:20:04 (lmgrd) REStarted covlicd (internet tcp_port 55809 pid 22161)
18:20:04 (covlicd) Server started on lee-linux for:     prevent.platform
18:20:04 (covlicd) prevent.ccpp
18:20:04 (covlicd) EXTERNAL FILTERS are OFF
18:20:04 (lmgrd) covlicd using TCP-port 55809
18:20:04 (lmgrd) covlicd exited with status 0 signal = 17
18:20:04 (lmgrd) Since this is an unknown status, license server
18:20:04 (lmgrd) manager (lmgrd) will attempt to re-start the vendor daemon.
18:20:04 (covlicd) FlexNet Licensing version v11.5.0.0 build 56285
i86_re3
18:20:04 (covlicd) lmgrd version 11.4, covlicd version 11.5
18:20:04 (covlicd) Cannot open lock file. errno=11 (/var/tmp/
lockcovlicd): Resource temporarily unavailable
18:20:04 (covlicd) EXITING DUE TO SIGNAL 41 Exit reason 9
18:20:04 (lmgrd) REStarted covlicd (internet tcp_port 56164 pid 22167)
18:20:04 (lmgrd) covlicd exited with status 41 (Exited because another server
was running)
18:20:04 (lmgrd) MULTIPLE "covlicd" license server systems running.
18:20:04 (lmgrd) Please kill, and run lmreread
18:20:04 (lmgrd)
18:20:04 (lmgrd) This error probably results from either:
18:20:04 (lmgrd)   1. Another copy of the license server manager  
(lmgrd) is running.
18:20:04 (lmgrd)   2. A prior license server manager (lmgrd) was  
killed with "kill -9"
18:20:04 (lmgrd)       (which would leave the vendor daemon running).
18:20:04 (lmgrd) To correct this, do a "ps -ax | grep covlicd"
18:20:04 (lmgrd)   (or equivalent "ps" command)
18:20:04 (lmgrd) and kill the "covlicd" process.
```

Make sure that the platform, upon which the `lmgrd` and
`covlicd` commands run, is supported by Coverity.

## The `lmutil lmhostid --help` command does not display the -ether option.

**Solution:** The `lmutil lmhostid -ether` command generates the
MAC addresses of all NICs that are used for FlexNet licensing.

The Ethernet address term in the FlexNet
documentation is incorrect. An accurate term is MAC address.

## The message `(covlicd) UNSUPPORTED: "prevent.ccpp" (PORT_AT_HOST_PLUS )` displays.

**Solution:** The following message might display if a specified feature is not
listed in the license file. The message is benign; Coverity Analysis will attempt to
use the "prevent.analysis" feature instead. If neither feature is present in the
FlexNet license file, Coverity Analysis will not run.

```
(covlicd) UNSUPPORTED: "prevent.ccpp" (PORT_AT_HOST_PLUS )
email_address@domain.com
(License server system does not support this feature. (-18,327))
```

## License failure for systems configured to use IPv6.

**Solution:** Systems configured to use IPv6, which is now standard
for some Linux distributions, can have problems using FlexNet licensing with either
Coverity Analysis for C/C++ or Coverity Analysis for Java. If the server pointed to in
the license.config file is `@localhost` you might
get one of these errors:

*For Coverity Analysis for C:*

```
cov-analyze --dir 'data'
[FATAL] Licensing failure.
[FLEXlm] License server machine is down or not responding.
[FLEXlm] See the system adminstrator about starting the license server system, or 
[FLEXlm] make sure you're referring to the right host (see LM_LICENSE_FILE).
[FLEXlm] Feature: prevent.analysis
[FLEXlm] Hostname: localhost
[FLEXlm] License path: 27000@localhost:
```

*For Coverity Analysis for
Java:*

```
cov-analyze --max-mem 1024 --dir data junit-4.1.jar --findsource src

Coverity Static Analyzer for Java
Version 5.0.0 (pj5.0dev-push-2255)
using Java 1.6.0_07 (Sun Microsystems Inc.)

License check failed.
Could not get FlexNet License
[ERROR] Could not verify the license.
FlexlmException: Can't Connect to License Server (-15,3002) (Connection refused)
```

If
you get one of the preceding error messages, check that the license server is
running with `lmutil lmdiag -c <license>`. If it is running,
try changing the license.config file to use
`@127.0.0.1` instead of `@localhost`. Next, rerun
`cov-analyze`.

## cov-analyze will not recognize the last line of the file.

**Solution:** The license.config file that is used for
FlexNet licensing needs to end with a newline character - that is - end with a blank
line. If it does not, cov-analyze will not recognize the last
line of the file. Leave a blank line at the end of the
license.config file.

## On Linux environments, the FlexNet licensing does not work with Ethernet devices that have the LAN port mapped to anything other than **eth0**.

**Solution:** The FlexNet licensing manager (FLEXlm), expects to get the MAC
address only from the **eth0** device. If the licensing machine LAN port is
mapped to **eth1** or higher, it will not get the correct MAC address. The
solution is to map the LAN to **eth0**.
