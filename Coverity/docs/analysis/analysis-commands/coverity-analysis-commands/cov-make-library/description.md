---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "Htky9zRMDpuyZT3zanNYWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:41.388705+00:00"
---

# Description

The `cov-make-library` command creates user model files from source files.
User model files contain information that overrides what `cov-analyze`
can derive for itself. See "Model search order" in Customizing Coverity
for more information about model kinds, their
impact, and how to model source files. See also the examples in the
<install_dir>/library directory.

Note: The files in the <install_dir>/library directory should not
be provided as arguments to `cov-make-library`. You should instead
create your own new files for models. Using the existing files creates duplicate,
identical user models and Coverity default models.

The file is appended if it already exists, and created if it does not exist. The search
order used to determine where to create the model file is the filename specified by
`-of` or a default value of
<install_dir>/config/user_models.xmldb.

The `cov-make-library` command works by calling
`cov-emit` to parse and emit the source files, followed by
`cov-analyze`, and then `cov-collect-models` to
collect the analyzed models.

Default behavior
:   For C, C++, Objective-C, Objective-C++, and Go, the default behavior of this
    command is to generate models for checkers that are enabled by default.

    For Java, C#, and Visual Basic, the default behavior of this command is to
    generate a model for use by all checkers, quality and security. Some of the
    command line options allow you to limit the generation of models to those
    used by groups of checkers.

Source files are compiled as C, C++, Objective-C, Objective-C++, C#, Go, Java, or Visual
Basic, depending on their file extension:

- Compiled as C code: .c extension
- Compiled as Objective-C code: .m extension
- Compiled as C++ code: .cc, .CC,
  .cp, .cpp,
  .cxx, .c++, and *with the
  exception of Windows*, .C extensions
- Compiled as Objective-C++ code: .mm extension
- Compiled as C# code: .cs extension
- Compiled as Go code: .go extension
- Compiled as Java code: .java extension
- Compiled as Visual Basic code: .vb extension

Note: This command no longer supports a Swift user model. Swift is supported by SIGMA.*
checkers as of 2021.9.0.
