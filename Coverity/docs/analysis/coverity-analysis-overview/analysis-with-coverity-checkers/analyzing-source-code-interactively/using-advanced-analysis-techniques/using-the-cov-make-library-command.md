---
title: "Using the 'cov-make-library' command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-cov-make-library-command.html"
content_id: "gSt8bEm9RGcj~2ZJ1uaGgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:18.824416+00:00"
---

# Using the 'cov-make-library' command

The `cov-make-library` command behaves as follows:

- Uses mangled function names for C++ models, but not for C models.
- Uses a C++ extension for C++ models: .cpp,
  .cc, or .cxx.

Note: Typically, `cov-make-library` expects header
(.h) files to reside in same directory as the source files that use
them. If headers or other files to include reside in a different directory, use the
`cov-make-library`
`--compiler-opt` flag to specify additional include directories.

You can use the `cov-make-library` command to create custom models for
methods. For more information, see "Models and primitives" in Customizing Coverity.

C++ programs use `extern "C"` semantics to declare C functions, and those
semantics apply to the library models as well. Because library files are parsed only
(rather than compiled and built into executables), you can use external references to
undefined functions or types. Rather than relying on linkage, the analysis uses function
names to determine which models to use.

To create the model files, specify the following arguments to the
`cov-make-library` command:

- (Required) The list of source files that contain the stub library functions
- (Optional) The computed model’s output file name from the `-of`
  modulefile option of the `cov-make-library`
  command

  Note: If you do not specify the `-of`
  modulefile option, the output file goes into the default
  location.
- (Optional) The path to the XML configuration file (-c
  path/to/coverity_config.xml)

Note: In most cases, the default specifications for configuration and output files work
correctly.

For more examples, see the following sections that describe how to override and add
specific models for allocators and panic functions.

The `cov-make-library` command creates either the file
user_models.xmldb or the output file that you specified with
the `-of` option to the `cov-make-library` command. If
the output file already exists, the most current output is appended to it. The following
order of precedence determines the directory where the model file gets created:

1. The `-of` option, if you specified it
2. <install_dir>/config

The coverity_config.xml file contains an encoded version of the
models. The analysis reads these models and gives them precedence over other models. If
there is a conflict, the models the user explicitly specifies are always used. To
indicate to `cov-analyze` that it should read the
user_file.xmldb file, specify it on the
command line by using the `--user-model-file` option.

In this section:

- Determining which functions are analyzed and called
- Suppressing macro expansion to improve modeling
- Adding a prototype for a function
