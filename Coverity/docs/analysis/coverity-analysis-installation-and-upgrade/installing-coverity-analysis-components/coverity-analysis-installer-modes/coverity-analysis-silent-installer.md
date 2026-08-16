---
title: "Coverity Analysis silent installer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-silent-installer.html"
content_id: "sz7Y7lVdnVlgu30yJNTdhw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:53.603867+00:00"
---

# Coverity Analysis silent installer

The Coverity Analysis silent installer allows you to specify all of the installation
configuration details on the command line so you do not need to run the "step-through"
process either through the command line (`-c`) or the graphical
(`-g`) installer modes.

To run the silent installer, specify the installation utility with the
`-q` option, followed by the installation parameters. The
`-q` option and the installation parameters must all be on the same
command line. The following example installs Coverity Analysis version 2026.6.0 to the home/cov-analysis-linux64-2026.6.0 directory.

```
./cov-analysis-linux64-2026.6.0.sh -q \
--installation.dir=cov-analysis-linux64-2026.6.0 \
--license.region=0 \
--license.agreement=agree \
--license.type.choice=0 \
--license.cov.path=/tmp/license.dat \
```

If you are installing on Windows, use the `-q -console` options preceded
by a `start /wait` command. If the executable filename contains spaces,
precede it with empty double quotes, even if the filename itself is double-quoted, for
example:

```
> start /wait "" "<my executable name>" -q -console
```

Note: You can include the empty double quotes whether or not the executable name contains
spaces.

The silent installer accepts the following options. Note that not all of the options are
required. If you use any of the following parameters, you should provide specifically
assigned values. Some values, if left blank, will accept the default value, but this is
not a recommended practice. For more information about the installation options, see
Installing Coverity Analysis components.

## Installer command line options

Note: Do not use the `-V` prefix with these options:

| Option | Description |
| --- | --- |
| `-q` | **Required.** Enables the silent installer. |
| `-console` | **Required on Windows.** Displays status messages in the console from which you invoked the silent installer. |
| `--installation.dir=directory-path` | **Required.** This option sets the location to which the Coverity Analysis product is installed. The default value on Linux is `cwd/cov-analysis-platform-version`.  The default value on Windows is `%ProgramFiles%\Coverity\Coverity Static Analysis` if the installer has administrative privileges, or `%LOCALAPPDATA%\Programs\Coverity\Coverity Static Analysis` if it does not. |

## General parameters

| Parameter | Description |
| --- | --- |
| `--create.program.group=true | false` | Grants the user who is running the installer permission to create all program group actions that rely on a default program group. This parameter is optional and valid only on Windows. Default value is `true`. |
| `--desktop.link=true | false` | Creates a desktop icon for Coverity Analysis. This option is valid only on Windows. Default value is `false`. |
| `--license.agreement =agree` | **Required.** Confirms agreement to the terms of the license. |
| `--license.region=0 | 1 | 2 | 3 | 4 | 5 | 6` | **Required.** Specifies the region of the End User License and Management Agreement (EULM). It used to select the correct product license. The available values (and representative region) are as follows:  - 0 - Americas, Africa, and Israel - 1 - Japan - 2 - Taiwan - 3 - China Mainland - 4 - Korea - 5 - International license (for any countries not mentioned   in 0-4) - 6 - Evaluation Only. This installation is being used solely   for evaluation purposes, and is not for production use |
| `--license.type.choice=0 | 1 | 2 | 3` | Specifies the type of license.  - 0 - coverity.dat license file. - 1 - FlexNet config.file license file. - 2 - Obtain license file from server (in Desktop mode). - 3 - Keygen license.json license file (internal use only). Important: Keygen is   Black Duck internal use   only. Do NOT use Keygen.   If not specified, the default value is `0`. |
| `--program.group.all.users=`true | false | Specifies whether the program group is created for all users. This parameter is optional and valid only on Windows. Default value is `false`. |
| `--program.group.name=`directory path | Specifies the name for the program group that appears in the Windows Start menu and the subpath in which the program group files are installed (this subpath is appended to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\). This parameter is optional and valid only on Windows. Default value is `Coverity Analysis` release version number, for example, Coverity Analysis 2022.9.0. |

## Included component parameters

The following optional parameters specify which components will be included in the Coverity
Analysis installation. If unspecified, only Coverity Analysis will be installed.

| Parameter | Description |
| --- | --- |
| `--component.cov_pns=true | false` | Installs the Coverity Point and Scan component. Default value is `true`. |
| `--component.sdk=true | false` | Installs the Coverity Extend SDK. This option is valid only for platforms that support Extend SDK. Default value is `false`. |
| `--component.skip.documentation=true | false` | Skips all documentation components. This option overrides all individual documentation component options. Default value is `false`. |
| `--component.en_doc=true | false` | Installs the English documentation component. This option is ignored if `--component.skip.documentation=true`. Default value is `true`. |
| `--component.ja_doc=true | false` | Installs the Japanese documentation component. This option is ignored if `--component.skip.documentation=true`. Default value is `true`. |
| `--component.ko_doc=true | false` | Installs the Korean documentation component. This option is ignored if `--component.skip.documentation=true`. Default value is `true`. |
| `--component.zh-cn_doc=true | false` | Installs the Chinese Simplified documentation component. This option is ignored if `--component.skip.documentation=true`. Default value is `true`. |

## Coverity licensing parameters

The following parameters are optional configurations using the Coverity license. To use these
options, the `--license.type.choice` option must be set to
`0`.

| Parameter | Description |
| --- | --- |
| `--license.cov.path=path` | Required. Specifies the full directory path of a Coverity license.dat file. This option is valid if the `--license.type.choice` option is set to a `0`. |

## FlexNet licensing parameters

The following parameters are optional configurations using FlexNet licensing. To use these
options, the `--license.type.choice` option must be set to
`1`.

| Parameter | Description |
| --- | --- |
| `--license.flex.choice=0 | 1 | 2` | Specifies your FlexNet license server type. You can set the value to one of the following:  - 0 - Basic, single license server - 1 - Advanced, redundant triad of license servers - 2 - Existing license.config file.   Otherwise, the default value is 0. |

## Basic FlexNet licensing parameters

Basic FlexNet licensing parameters (where the `--license.flex.choice`
value is `0`) have the following configurations available:

| Parameter | Description |
| --- | --- |
| `--license.flex.basic.host=host-name` | Specifies the host name of your FlexNet server. This option is required if you are using a basic FlexNet server or if the `--license.flex.choice` option is set to `0`. |
| `--license.flex.basic.port=port` | Specifies the port number of your FlexNet server. This option is required if you are using a basic FlexNet server or if the `--license.flex.choice` option is set to `0`. |

## Advanced FlexNet licensing parameters

Advanced FlexNet licensing parameters (where the
`--license.flex.choice` value is `1`) have the
following configurations available:

| Parameter | Description |
| --- | --- |
| `--license.flex.advanced.triad=triad` | A FlexNet server triad is specified by a comma-separated list of three *port@host-name* values. For example, `28000@flex1,28001@flex2,28002@flex3`. This option is required if the `--license.flex.choice` option is set to `1`. |

## Existing FlexNet licensing parameters

Existing FlexNet licensing parameters (where the
`--license.flex.choice` value is `2`) have the
following configurations available:

| Parameter | Description |
| --- | --- |
| `--license.flex.config.path=path` | Specifies the full directory path to the license.config file. The license.config filename must be included at the end of the path. This option is required if the `--license.flex.choice` option is set to `2`. |

## Keygen licensing parameter

Sets the path for a Keygen license.json file. This option is required
when the `--license.type.choice` option is set to
`3`.

Important: Keygen is Black Duck internal use only. Do NOT use Keygen.

| Option | Description |
| --- | --- |
| `--license.keygen.path=path` | Specifies the full directory path of a Keygen license.json file. This option is valid if the `--license.type.choice` option is set to `3`.  Important: Keygen is Black Duck internal use only. Do NOT use Keygen. |
