---
title: "Black Duck C/CPP tool overview"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool-overview.html"
content_id: "czazY~fEsIGqBzRimoHsxA"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:51.541416+00:00"
---

# Black Duck C/CPP tool overview

The Black Duck C/CPP tool allows you to generate a BOM report for projects written in
C/C++ by building the project, capturing the source and binary files involved, and then
delivering a BDIO and signatures to Black Duck SCA.

C and C++ projects don't have a standard package manager or method for managing
dependencies. It is therefore more difficult to create an accurate BOM for these
projects. This leaves Software Composition Analysis tools fewer options than with other
languages.

The new Black Duck C/CPP tool avoids this pitfall by using a feature of Coverity called
Build Capture. Coverity Build Capture, wraps your build, observing all invocations of
compilers and linkers and storing the paths of all compiled source code, included header
files and linked object files. These files are then matched using a variety of methods
described in the section of this document called "The
BOM".

The Black Duck C/CPP tool can be run in two ways:

- Using command line
  options.
- Configuring and using a yaml file contaning
  the desired options.

As decribed above, once the scan is completed, the tool sends the results to Black Duck
SCA as a BOM.

## blackduck-c-cpp 2.0.0

blackduck-c-cpp 2.0.0 now uses cov-cli instead of cov-build by default. Coverity cli
uses cov-build under the hood. It is a layer of automation on top of cov-build and
other tools. Instead of the user having to figure out the correct cov-configure
options, Coverity CLI guesses at the right options and runs the tools
automatically.

It doesn't always work correctly, so there are options to fix things where needed.
You can also choose to run cov-build by setting following option in yaml file:

```
set_coverity_mode: 'cov-build'
```

Starting with Coverity build capture 2022.12.0, `glibc_2.18` is a
requirement. Please note for customers using CentOS7, the latest version of glibc
supported in CentOS7 is `glibc_2.17`. The blackduck-c-cpp tool will
attempt to download an older version of Coverity, 2022.9, on Linux platforms with
`glibc_2.17` or older. However, if this process fails, you can
forcefully download an older version by specifying following parameter in yaml file:

```
force_pull_coverity_vers: 'old'
```
