---
title: "Operational messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operational-messages.html"
content_id: "yk3PojzHhHP_3YUEQODJyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:27.623540+00:00"
---

# Operational messages

Operational messages are generated when a problem occurs during the operation of Coverity
Fortran Syntax Analysis. They are of the form `FCK-- ...`, for
example:

`FCK-- open error on input or include file`

For many operational messages an i/o status code is presented. This code is system
de­pendent, and is provided for debugging purposes only. When reporting problems to the
Coverity Fortran Syntax Analysis support team, please specify the message and the i/o
status code. Operational messages are sent to the report file and to your screen or log
file.
