---
title: "Configuration syntax help"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuration-syntax-help.html"
content_id: "_xCOcN8I7yiEWB6pl0CZbQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:34.268107+00:00"
---

# Configuration syntax help

This topic shows the contents of the configuration-syntax.txt file,
which are output when you invoke `help config --syntax`.

The rule of thumb for which configuration format to specify depends on which Coverity server is in use:

- Coverity on Polaris

  When the server is Coverity on Polaris, the configuration
  file is a YAML file named polaris.yml. For further
  information about polaris.yml, please see ["Configuration File
  Overview"](https://docs.blackduck.com/r/cov_polaris/latest/coverity-on-polaris/coverity-on-polaris-configuration-file-overview.html) in the [Coverity on Polaris Help](https://docs.blackduck.com/r/cov_polaris/latest/coverity-on-polaris/understanding-coverity-on-polaris.html).
- Coverity Connect

  When the server is a Coverity Connect server, the configuration file is a JSON file named coverity.conf.
  For further information about coverity.conf, please see
  "coverity.conf file format" in the Coverity
  Desktop Analysis
  2026.6.0 User Guide.

```
Coverity configuration file syntax
==================================

The Coverity configuration file is created when you run "coverity scan" for the
first time for a given project, or when you run "coverity setup" for a project.
The file format is either YAML (the default) or JSON, and so must conform to
the syntax standards for these formats.  Some subtleties are discussed below.

If you already have a configuration file (e.g., coverity.yaml), you can invoke
"coverity help config -c coverity.yaml" to produce an annotated version of the
file, including comments on the purpose of each section and setting.  The
output of this command uses a standard format which may differ from what you
had originally, but will be equivalent.

YAML considerations
===================

Generally, setting values can be expressed directly, with no need for quoting
or escaping.  This is true even if a value contains spaces, quotes (other than
leading quotes), and/or backslash characters, as in the following example:

    analyze:
      model-file: C:\Users\me\Kim's very "best" models\foo.xmldb

For a build command or clean command, spaces are used to separate an executable
name and arguments from each other.  Consequently, if any of these contains a
space character, quoting is necessary, as in the following examples:

    capture:
      build:
        build-command: make "NAME=Kim Johnson" all

    capture:
      build:
        build-command: "\"/home/me/my tools/build\" -n 24 all"

Quoting is also required if any argument starts with a "*" character or ends
with a ":" character, as in the following examples:

    capture:
      files:
        exclude-glob: "*_test.php"

    capture:
      build:
        build-command: "build-all -drive C: -project foo"

YAML supports both single-quotes and double-quotes, but there are differences
in how these are interpreted:

  * A value surrounded by single-quotes does not support escaping within the
    string, with the one exception being the use of a pair of single-quotes to
    represent a single-quote within the string, as in the following example:

        analyze:
          model-file: 'C:\Users\me\Kim''s very "best" models\foo.xmldb'

  * A value surrounded by double-quotes uses the backslash character as an
    escape character.  Double-quotes and backslashes within the string must
    be escaped, as in the following example:

        analyze:
          model-file: "C:\\Users\\me\\Kim's very \"best\" models\\foo.xmldb"

If a setting value begins with a quote character, then the entire string must
be quoted and the inner quotes escaped if necessary.  The following two
examples are equivalent:

    capture:
      build:
        build-command: '"C:\Users\me\my tools\build.exe" -n 24 all'

    capture:
      build:
        build-command: "\"C:\\Users\\me\\my tools\\build.exe\" -n 24 all"

Settings whose values are lists can be specified with either a short form or a
long form.  For the short form, values are separated by commas.  The following
two examples are equivalent:

    capture:
      languages:
        include: [java, javascript]

    capture:
      languages:
        include:
        - java
        - javascript

Comments begin with a "#" character, either at the beginning of a line or
following a space character.  By convention, the coverity.yaml file uses a "#"
character followed by a space to introduce an explanatory comment, and two "#"
characters with no following space to indicate a commented-out setting, as in
the following example:

    analyze:
      # File containing function models.
      ##model-file: C:\Users\me\Kim's very "best" models\foo.xmldb

JSON considerations
===================

JSON values are always surrounded by double-quotes.  Within the value string,
double-quotes and backslashes must be escaped, as in the following example:

    {
      "analyze": {
        "model-file": "C:\\Users\\me\\Kim's very \"best\" models\\foo.xmldb"
      }
    }

JSON does not support comments.  However, the Coverity CLI treats settings
whose names begin with "_comment_" or "__" as though they were comments.
"_comment_" is used to introduce an explanatory comment and "__" is used to
indicate a commented-out setting, as in the following example:

    {
      "analyze": {
        "_comment_model-file": "File containing function models.",
        "__model-file": "C:\\Users\\me\\Kim's very \"best\" models\\foo.xmldb"
      }
    }

Glob patterns
=============

Glob patterns are used for file-name matching by some configuration settings
(e.g., capture.files.exclude-glob) and some command-line arguments (e.g.,
--file-exclude-glob).  A simple glob pattern can be used to match a file name
regardless of the directory in which it appears, or can be more complicated,
including directory components as well.

A glob pattern with directory components is matched against the deepest
subdirectory level.  For example, if the project directory is /home/me/proj,
then the following apply.

The glob pattern "test*/t*" matches the following files:

    /home/me/proj/main/testing/test1.js
    /home/me/proj/main/extra/testing/thing.js
    /home/me/proj/other/tests/trial.php

but does not match the following files:

    /home/me/proj/main/prod/title.js
    /home/me/proj/main/testing/tech/take2.js

The glob pattern "main/*/t*" matches the following files:

    /home/me/proj/main/prod/title.js
    /home/me/proj/main/testing/test1.js

but does not match the following files:

    /home/me/proj/main/extra/testing/thing.js
    /home/me/proj/main/testing/tech/take2.js
    /home/me/proj/other/tests/trial.php

Glob patterns support "*" but not "**", so more complex file matching must use
regex instead of glob.

Regular expressions
===================

Regular expressions are used for file-name matching by some configuration
settings (e.g., capture.files.exclude-regex) and some command-line arguments
(e.g., --file-exclude-regex).  Regular expressions are always matched against
the entire path relative to the project directory but are not implicitly
anchored against the start and end of the path.  For example, if the project
directory is /home/me/proj, then the following apply.

The regex "tests/" is equivalent to "^.*tests/.*$" and matches the following
files (including some you might not intend):

    /home/me/proj/main/tests/test1.js
    /home/me/proj/main/tests/subdir/test2.js
    /home/me/proj/tests/test3.php
    /home/me/proj/contests/src/foo.php

The regex "/tests/" matches the following files:

    /home/me/proj/main/tests/test1.js
    /home/me/proj/main/tests/subdir/test2.js

but does not match the following files (including some you might intend):

    /home/me/proj/tests/test3.php
    /home/me/proj/contests/src/foo.php

To match all files at any depth under any directory named "tests" or "testing",
including at the top level of the project and including path separators on both
Unix and Windows, use a regex like the following:

    (^|[/\\])(tests|testing)[/\\]
```
