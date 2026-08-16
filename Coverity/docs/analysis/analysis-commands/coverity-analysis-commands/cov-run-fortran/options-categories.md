---
title: "Options categories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-categories.html"
content_id: "F7o6Prv3we5gZ6bVEqz9tg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:17.149326+00:00"
---

# Options categories

The options accepted by `cov-run-fortran` fall into several categories as
summarized below.

Note: Each of the items below is linked to other sections in this document.
Many link to the relevant definition in this section, while common analysis options link
to corresponding entries in the `cov-analyze` section.

Analysis options
must follow all control options and are separated from control options by
`--`.

## Control options that select the compiler configuration

Configuration options are used to select the configuration file that controls
compiler emulation. The `--configuration` and
`--config-path` options can be used to select a configuration
file by name, including a user-supplied configuration file. The remaining
configuration options can be used to select from the matrix of pre-written
configuration files.

Configurations are filtered in the following order: `--platform`;
`--vendor`; `--version`; `--level`.
Very few configuration files provide platform information, so it does not make a
good selector. In most cases, it is sufficient to select the desired compiler
emulation using just the `--vendor` and `--version`
options. Where necessary, the `--platform` and
`--level` options can be used to refine this initial
selection.

- --configuration
- --config-path
- --level
- --list-configs
- --platform
- --vendor
- --version

## Control options used in other Coverity analysis tools

- --append
- --dir
- --strip-path
- --security-file

## Other control options

- --impact

## Analysis options that affect the analysis of individual program units

The following analysis options affect the kinds of defects that are
reported:

Note: Analysis options must be separated from control options by a
double-dash (`--`).

- -acqintf
- -allc
- -cntl
- -cond
- -cpp
- -declare
- -dp
- -externals
- -f03
- -f08
- -f18
- -f77
- -f90
- -f95
- -ff
- -i2
- -i4
- -i8
- -intent
- -intrinsic
- -obsolescent
- -r8
- -relax
- -save
- -specific
- -standard

## Analysis options that affect the analysis of whole programs

The following analysis options affect the kinds of defects that are reported:

Note: Analysis options must be separated from control options by a double-dash
(`--`).

- -ancmpl
- -anprg
- -anref

## Analysis options that affect additional outputs

The following analysis options do not affect any of the defects that are
reported:

Note: Analysis options must be separated from control options by a double-dash
(`--`).

- -l
- -plen
- -pwid
- -refstruct
- -moddep
- -shinc
- -shsub
- -shsrc
- -shsngl
- -shprg
- -shref
- -shcom
- -shmodtyp
- -shmodvar
- -shmoddep

## Analysis options used for library usage and maintenance

The following analysis options are used when generating or maintaining libraries:

- -create
- -include
- -library
- -update

## Miscellaneous analysis options

The following options (except for -idep, -log and -report) affect the kinds of
defects that are reported:

- -define
- -I
- -idep
- -informative
- -log
- -report
- -rigorous
- -truncate
- -warnings
