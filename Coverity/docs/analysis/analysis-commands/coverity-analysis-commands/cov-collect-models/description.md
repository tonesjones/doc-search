---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "PKgJgPPbDrKJ0ccD2phjYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:07.971760+00:00"
---

# Description

The `cov-collect-models` command gathers all of the function models from
a C/C++ intermediate directory previously analyzed with `cov-analyze`
and collects them into a single output model file. This model file can be subsequently
passed to `cov-analyze` with the `--model-file` option.
The models generated are derived models. For more information about the model kinds and
their impact, see Model search order" in Customizing Coverity.

The primary purpose of `cov-collect-models` is to allow interprocedural
information from a full analysis run to be used when analyzing only a small portion of
the code base. This usually results in finding some interprocedural errors even when
only a small portion of the code base is analyzed, and it also usually helps lower the
false positive rate.

Warning:
While the `cov-collect-models` command can accept C# and Java source, this is not a recommended practice.
It is more reliable simply to pass the C# or Java bytecode directly to `cov-analyze`.

Note:
To use the derived model file on a Windows SMB network shared drive (for example, when
running Coverity Desktop local analyses that use derived models), it is necessary to
generate the file on a physical disk, then copy it to the shared drive for read-only
access by other processes.
