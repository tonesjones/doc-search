---
title: "Defaults"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defaults.html"
content_id: "QRz~MnC4Vnwei16zqdQvmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:17.502755+00:00"
---

# Defaults

```
-nallc -nacqintf -nancmpl -anprg -anref -nbatch -ncond -ncreate -ndecl -ndefine -ndp
-nexternals -nf77 -nf90 -nf95 -nf03 -nf08 -nf15 -nff -nI -nidep -ninclude -informative
-nintent -nintrinsic -ni2 -i4 -ni8 -nl -nlibrary -nlog -nmoddep -nobsolescent -plen 62 
-pwid 100 -nr8 -nrelax -nreport -nrefstruct -nrigorous -nsave -nshcom -shinc -shmoddep 
-nshmodvar -shprg -shref -shsngl -shsrc -shsub -nspecific -nstandard -ntruncate -nupdate 
-warnings
```

For files with a filename extension of .f90, .f95,
.f03, .f08, .F90,
.F95, .F03, or .F08,
the default source form is freeform `-ff`.

The default number of allowed continuation lines depends on the compiler emulation
chosen.

On the page headers in the listing file, the specified non-default analysis options will be
shown. You can override the default options by setting the environmental variable
`FCKOPT` to the default options of your choice. For example for the C
shell:

```
setenv FCKOPT "-plen 66 -pwid 100 -f77"
```

or for the Bourne or Korn shell:

```
export FCKOPT="-plen 66 -pwid 100 -f77"
```
