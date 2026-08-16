---
title: "Black Duck C/CPP Tool"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-c/cpp-tool.html"
content_id: "CMnVmEFQtMEgHU5KzvqEiA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:29.190222+00:00"
---

# Black Duck C/CPP Tool

C and C++ projects don't have a standard package manager or method for managing dependencies.
It is therefore more difficult to create an accurate BOM for these projects. This leaves
Software Composition Analysis tools fewer options than with other languages. The primary
options which are available in this context are: file system signatures. Black Duck has a variety of old and new signatures which can be used to
build a BOM. In order to effectively use signatures, the tool first needs to know which
files to take signatures from. In the past SCA tools have pointed a scanner at a build
directory, getting signatures from a subset of files within the directory sub-tree. The
problem with this approach is that there are many environmental variables, parameters
and switches provided to the build tools, which make reference to files outside of the
build directory to include as part of the build. Further, there are, commonly, files
within the build directory, which are not part of the build and can lead to false
positives within the BOM.

The new Black Duck C/CPP tool avoids the pitfalls described above by using a feature of
Coverity called Build Capture. Coverity Build Capture, wraps your build, observing all
invocations of compilers and linkers and storing the paths of all compiled source code,
included header files and linked object files. These files are then matched using a
variety of methods described in the section of this document called "The BOM".

This overview is an excerpt from the documentation that can be found in the [Black Duck C/CPP Tool Documentation Portal
page](https://docs.blackduck.com/access?ft:originId=d7a4b1f5a86f212be27e594dc02681c4473766e2b2ad3db9123e8a92e34e44e2) along with other details on how to use the Blackduck-C-CPP tool.
