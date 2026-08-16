---
title: "Input file macros"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/input-file-macros.html"
content_id: "K542DtUuv3iKCTygM64CMQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:01.088247+00:00"
---

# Input file macros

## FOREACH_MATCHING_INPUTFILE(f, suffix_utf8)

This macro iterates over the input files (including source and application archives)
when the filesystem path matches the specified suffix.

- `f` is of type `extend_inputfile_t` and will be
  set in each iteration.
- `suffix_utf8` is of type `const char *`, which is
  interpreted as a NUL-terminated UTF-8 sequence.

Arguments to the function declarations in the remaining macros (below) share the
following characteristics:

- `f` is of type `extend_inputfile_t`.
- `line` is a positive integer line number on which to report the
  event.
- `tag` and `text_utf8` are of type `const
  char *`, which is interpreted as a NUL-terminated UTF-8 sequence.

## ADD_INPUTFILE_ONLY_EVENT(/*extend_inputfile_t*/ f, line, tag, text_utf8)

Queue an event (in an input file) to report at the next use of
COMMIT_INPUTFILE_ONLY_ERROR. This macro is useful when
reporting events that are entirely inside input files. It is most appropriate to use
this macro inside CHECKER_INIT or CHECKER_FINAL.

## COMMIT_INPUTFILE_ONLY_ERROR(/*extend_inputfile_t*/ f, line, tag, text_utf8)

Report an error in an input file. This macro will include only events previously
queued through ADD_INPUTFILE_ONLY_EVENT. This is useful when
reporting events that are entirely inside input files.

It is most appropriate to use this macro inside CHECKER_INIT
or CHECKER_FINAL.

## ADD_INPUTFILE_EVENT (tree, /*extend_inputfile_t*/ f, line, tag, text_utf8)

Create an event in input file
`f`, and add it to the set of events in the store for
`tree`. A subsequent use of COMMIT_INPUTFILE_ERROR(tree,
...) or COMMIT_ERROR(tree, ...) will include this event
in the defect report it produces. This macro is for reporting events in input files in
the context of a flow-sensitive checker; it allows mixing events in source code and
input files.

Use this macro inside any ANALYZE_* or
FUNCTION_INIT handler.

Note that subsequent use of
COMMIT_INPUTFILE_ERROR or COMMIT_ERROR
will include this event in the defect it creates.

For related information, see
Reporting events and defects on input files.

## COMMIT_INPUTFILE_ERROR (tree, /*extend_inputfile_t*/ f, line, tag, text_utf8)

Report the error in an input file using the events from `tree`, an AST
node.

This macro is for use with a flow-sensitive checker and allows mixing events in
source code and input files.

Use this macro inside any ANALYZE_* or
FUNCTION_INIT handler.

For related information, see Reporting events and defects on input files.
