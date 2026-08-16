---
title: "Preprocessing source files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preprocessing-source-files.html"
content_id: "q~~PLUhItrt2h_F_UMXUlQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:02.251529+00:00"
---

# Preprocessing source files

The first step in debugging many parsing problems is to run the source file through the
preprocessor to expand macros and include files. This process reveals the text of the
entire translation unit that the compiler actually sees.

The `cov-preprocess` command can automatically preprocess an already
emitted file. The syntax is:

```
> cov-preprocess [--diff] <file_to_preprocess>
```

The name of the file to preprocess can be a full path or just a file name. If you only
specify a file name, the command looks for it in the intermediate directory, and
preprocesses it if it is unique. Otherwise, it outputs a list of possible candidates. If
the file name is an absolute path, the command will only preprocess the given file if it
exists. This can be much faster when there is a large amount of intermediate data. The
resulting preprocessed file is stored in:

<intermediate_directory>/output/preprocessed/file.i

If you use the `--diff` option, the program tries to preprocess the file
with the compiler originally used to compile it, by adding -E to the command line.
After, it will try to identify if the files differ, and notably if the order in which
files are included is different.

If the preprocessing program does not work for you, you can also manually preprocess a source
file by looking in build-log.txt for the invocation of
`cov-emit` for the file of interest. Above this line is a line that
includes `CWD=<dir>` which is the directory to change into when
running the preprocessing command. Take the `cov-emit` command line for
the file and remove the `--emit <dir>` option. Next, add the
`-E` option before the source-file name; leave the source-file name
as the last argument to `cov-emit`. Run the command, with a redirect to
a file that is to contain the preprocessed output:

```
> cd src_dir
> cov-emit <args...> -E file.c > file.i
```

Inspect the output file file.i to see if the location where the
parse error occurs appears to be different from the original source file.
