---
title: "Date and time format"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/date-and-time-format.html"
content_id: "ZWhMytvJ89CZfdYkLyRhxQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:32.842770+00:00"
---

# Date and time format

By default, Coverity Fortran Syntax Analysis presents the date and time according to the ISO
standard. You can change this by adding a `date format` or `time
format` option line to the configuration file in the [VARIOUS] section of
the configuration file. The lines to be added have the form `date format =
’format’` and `time format = ’`format`’`, in
which format is a template for the presentation of the date and time respectively.

In the template for the date the day must be specified by dd, the month by `mm`
or `mmm` (which causes a three letter mnemonic of the month to be
displayed), the year by `yy` or `yyyy`. The year, month
and day codes must be separated by a character of your own choice which will be used as
separator in the actual presentation.

In the template for the time the hours must be specified by `hh` or
`h` (which causes hours below 10 to be displayed with one digit), the
minutes by `mm`, and the seconds by `ss`. The hour,
minutes and seconds codes must be separated by a character of your own choice which will
be used as separator in the actual presentation. For example:

```
date format = ’yyyy-mm-dd’
date format = ’mmm-dd-yy’ 
date format = ’dd/mm/yyyy’ 
time format = ’hh:mm:ss’ 
time format = ’h:mm:ss’
```

If you use an x as the format character, the date and/or time will be suppressed in the
listings. This can be useful if you want to compare listings of different Coverity
Fortran Syntax Analysis runs. For example:

```
date format = ’xx xx xx’ 
time format = ’xx xx xx’
```
