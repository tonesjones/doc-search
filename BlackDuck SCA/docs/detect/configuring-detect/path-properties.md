---
title: "Path properties"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/path-properties.html"
content_id: "iANJRYWc1NZpKcS6ubZ6tA"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:21.899473+00:00"
---

# Path properties

Each Detect property with a type of "Path" or "Optional Path" accepts a file path value.
(These properties also tend to have names that end with ".path".)
The file path value can be either absolute (e.g. /usr/bin/conan) or relative to the directory
from which Detect is executed (e.g. ../bin/conan).
The format of the file path (the directory separator character, whether or not a drive letter prefix is supported, etc.)
is dictated by the operating system on which Detect is running.

Path property value examples (applicable when executing the Detect .jar directly):

- Linux/Mac: --detect.conan.path="/usr/bin/conan"
- Windows: --detect.npm.path="C:\Program Files\nodejs\npm.cmd"

When running Detect using one of the scripts, remember to also apply quoting and escaping rules that
apply. For more information refer to Quoting and escaping shell script arguments.
