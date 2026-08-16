---
title: "Temporary suppression of messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/temporary-suppression-of-messages.html"
content_id: "xtzCaaqRt_irUXf4sVfSZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:30.232026+00:00"
---

# Temporary suppression of messages

To suppress analysis messages temporarily, you can insert Coverity Fortran Syntax
Analysis directives in your source code. First you have to define the mnemonic of the
directive of your choice, beginning with an ’!’. You specify this directive string on
the ”compiler directive” line of the ”GENERAL” section of the configuration file to use.
For example:

```
’!DEC$’ ’!fck’                           ’compiler directive strings’
```

To define ’`!fck`’ as directive in addition to the ’`!DEC$`’
compiler directive.

Now you can use this directive to disable and enable Coverity Fortran Syntax Analysis
analysis messages in the source code. You can either suppress messages for a block of
code or in a single statement. To suppress messages in a block of code add a line with
the directive followed by a list of the message numbers which you want to suppress, each
message number preceded by a minus sign. To enable messages again, add a line with the
directive followed by a list of message numbers, each preceded by a plus sign. You can
add online comment after the list of messages. For example:

```
	CHARACTER*120 CH1, CH2
      DATA CH1,CH2/2*’ ’/
!fck -313 -384      !suppress "possibly no value assigned" and "truncation"
	CH1 = ’123’
	CH2 = ’ab’
!fck +313 +384
```

To suppress messages for a single, compound, or line with a list of statements only, add
the directive with the list of messages you want to suppress, each preceded by a minus
sign, after the first line of the statement. For example:

```
	CHARACTER CH*120 
	DATA CH/’ ’/
	IF (.TRUE.) CH = ’123’ 		!fck -384 -314
```
