---
title: "The usage of analysis options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-usage-of-analysis-options.html"
content_id: "tebufveyoPvCSylOmLb0mA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:18.154663+00:00"
---

# The usage of analysis options

An analysis option starts with ”`-`”, or ”`--`”. To negate
an option, precede it by ”`n`”, or ”`no­`” for example
`-nwarnings`, or `--no-warnings`. Analysis options can
be truncated as long as they are unique. Option arguments (include directories, common
blocks, modules, defined meta symbols, roots, and program units) must be separated by a
”`;`”, a ”`:`”, or a ”`,`”, e.g.
`-I dir1:dir2`, `-shcom com1,com2` or `-shmod
mod1,mod2`. A double-dash ”`--`” can be used to signal the
end of the global options list.

The output options determine which information will be stored in the list file. You must
specify the `-l` option for these options to have any effect. When the
`-l` option has not been specified, or when certain sections of the
output are being suppressed by, for ex­ample, the `-nshsub` or
`-nshprg` options, all diagnostic and system messages generated
during this suppression will be sent to output file, which an be found in
output/forchk.log in the intermediate directory. During
program-unit analysis all syntax messages will be pre­ceded by the related
statement.

Options specified on the command line in front of the first filename are global and hold
for all input files. Options specified in front of a subsequent filename are local and
hold for that file only; they overrule the global setting temporarily.

For example:

```
cov-run-fortran --dir idir -l prg -f77 prg1 sub1 -relax sub2
```

will analyze `prg1.f`, `sub1.f`, `sub2.f`
and generate listings and cross references in `prg.lst`. All nonstandard
Fortran 77 syntax will be flagged. Type checking is relaxed while processing
`sub2.f`.

Since wildcards in filenames are expanded by the shell, local options apply only to the
first filename in the expanded list. Since the order in which filenames are substituted
is determined by the shell, this can lead to unstable or unexpected results. When using
local options, it is recommended to specify all source file names explicitly.
