---
title: "Analyzing more than one source file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-more-than-one-source-file.html"
content_id: "MNb02mDtjLon6yzkZQms4g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:49.145638+00:00"
---

# Analyzing more than one source file

To analyze multiple source files, the syntax in general is:

```
cov-run-forcheck [control-options] – [analysis-options] sourcefiles
```

e.g.:

```
cov-run-fortran --dir idir -l mylistfile -ff source1 source2
```

All options specified before the list of source files are global: they are effective for
the analysis of each source file and for the global analysis. Options specified within
the list of source files are local: they act only upon the immediately-following source
file. For example, in

```
cov-run-fortran --dir idir -- -l mylistfile -ff source1 -nff source2
```

`source1` is analyzed using free-form syntax rules while
`source2` is analyzed using fixed-form syntax.
