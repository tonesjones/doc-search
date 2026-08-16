---
title: "Producing a source listing with cross-references"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/producing-a-source-listing-with-cross-references.html"
content_id: "q9Ga5ic03ADzn3kLnil3Cg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:48.497757+00:00"
---

# Producing a source listing with cross-references

A listing file is produced by the option `-l`, for example:

```
cov-run-fortran --dir idir -- -l mylistingfile mysourcefile.f
```

A listing filename consisting of a single ”`-`” denotes
`stdout`, so

```
cov-run-fortran --dir idir -- -l - mysourcefile.f
```

produces a listing in the log file. The log file can be found in the file
output/forchk.log relative to the root of the specified
intermediate directory.

Some tuning may be required to analyze the code and produce defects consistent with your
needs. The available options and their effects on analysis are describe in Operation. Advanced users can also control the analysis in great
detail by creating and using a custom configuration file.
