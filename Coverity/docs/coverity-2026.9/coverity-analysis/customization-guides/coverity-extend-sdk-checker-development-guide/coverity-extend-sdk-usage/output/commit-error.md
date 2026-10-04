---
title: "COMMIT_ERROR"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/commit_error.html"
content_id: "xxRQzxRG2a9gmdh17~~k4w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:54.551242+00:00"
---

# COMMIT_ERROR

You use `COMMIT_ERROR(t, tag, text)` to output a defect report that
contains all the events in the store that were previously associated with
`t` and one final, main event given by `tag` and
`text`:

- `tree t`: The expression tree with which events were
  previously associated through the use of `ADD_EVENT(t,...)`
  or `ADD_INPUTFILE_EVENT(t,...)`. It is an error if
  `t` does not have any associated events (in the current
  implementation, `COMMIT_ERROR` does nothing in this
  case).
- `tag/text`: These are the same as described in
  `ADD_EVENT` and are used to create one final event for
  the defect report (but this final event is not added to the store). If you
  pass the empty string (`""`) for both, no final event is
  created.
