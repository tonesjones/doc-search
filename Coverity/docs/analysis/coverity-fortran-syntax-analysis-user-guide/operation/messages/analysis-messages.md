---
title: "Analysis messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-messages.html"
content_id: "e5eJRenBKLsJf7KDK~IINQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:28.276901+00:00"
---

# Analysis messages

Those analysis messages flagged with an ‘`I`’ are informative, with a
‘`W`’ are warnings, those flagged with an ‘`E`’ are
errors.

Informative messages hold no conflicts with the Fortran standard. Warnings indicate the
usage of extensions to the standard. Error messages will arise when the Fortran standard
has been violated.

The distinction between warnings and error messages, however, is not principal. In
general we can say that warnings indicate constructions which, if accepted by your
compiler, impose no risk to the proper execution of the program, while errors indicate
constructions which may influence the proper execution.

All analysis messages have a number. In Message summary you will find a list
of all messages with explanation for those messages which are not self-explanatory.
During program unit analysis a message is preceded by the file name and line number to
be able to locate the problem in the source file easily. To use this feature you should,
however, not change the method of line or statement numbering as described in Line or statement numbering.

The following remarks can be made on the presentation of analysis messages:

- Only the first 6 analysis messages in a statement are presented, unless the
  `-rigorous` option has been specified. The number can be changed
  by specifying `max msg = n` in the [VARIOUS] section of the
  configuration file.
- Only the first 6 problems encountered in an argument list or common block are
  presented, unless the `-rigorous` option has been specified. The
  number can be changed by specifying `max msg = n` in the [VARIOUS]
  section of the configuration file.

Analysis messages are sent to the report file and to the listing file if specified, or to the
forchk.log file otherwise.
