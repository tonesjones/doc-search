---
title: "Redefinition and suppression of messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/redefinition-and-suppression-of-messages.html"
content_id: "BfnlhCVVkZKtuiwfEh5Efg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:29.578296+00:00"
---

# Redefinition and suppression of messages

This section describes how to redefine the severity level flag of Coverity Fortran Syntax
Analysis’s analysis messages. To suppress them temporary see the next section.

If you use a private configuration file for a specific compiler emulation or set of
language extensions you can add records (using an editor) consisting of the number of
the message to be redefined along with the severity level flag that you want Coverity
Fortran Syntax Analysis to present. The lines with the messages to be redefined must be
placed in the section ”`[MESSAGES]`”.

The numbers and default severity level flags of the messages can be found in Message summary. If you specify a level flag’ ’ (blank) then the message
will be suppressed fully, and will not be counted either. For example:

`335 ’I’`

`53 ’ ’`

These configuration file records specify that the analysis message ”type conflict” now
will be presented as Informative message and ”tab(s) used” will neither be presented nor
counted.

To present specific messages only you can suppress all analysis messages by placing the
following line in this section:

`suppress = ’all’`

and subsequently list all messages that must be presented with its severity level. To
activate this configuration file see The usage of language extensions.
