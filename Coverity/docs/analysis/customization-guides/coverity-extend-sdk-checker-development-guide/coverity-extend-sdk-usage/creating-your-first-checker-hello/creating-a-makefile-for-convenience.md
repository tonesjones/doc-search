---
title: "Creating a Makefile for convenience"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-makefile-for-convenience.html"
content_id: "VlG7k8Cn3JvZtB3iV~T4VQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:26.918287+00:00"
---

# Creating a Makefile for convenience

When creating your own checkers, you can adapt the Hello makefile
(<install_dir>/sdk/samples/hello/Makefile) and the
checker.mk file that it includes:
checker.mk and include.mk.

**Makefile for the hello sample checker:**

```
# hello/Makefile
# Makefile for the 'hello' Extend checker
# name of the checker
include checker.mk
# default target
all: $(CHECKER)
# rules shared by the example checkers
include ../include.mk
# EOF
```

**The checker.mk file for the hello sample
checker:**

```
# hello/checker.mk
# set CHECKER to 'hello'
# This fragment is separated into its own file so that it can
# be used by the Makefile in this directory, as well of those
# in the test subdirectories.
CHECKER := hello
# EOF
```
