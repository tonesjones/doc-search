---
title: "I see the message: #error No Architecture defined"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/i-see-the-message-error-no-architecture-defined.html"
content_id: "G7stFHl3dIU6isRkYTgRIg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:24.086328+00:00"
---

# I see the message: #error No Architecture defined

Macros are not defined. Some compilers have to be explicitly probed for particular
macros. There are a number of reasons why this needs to be done, for instance:

- The compiler can support a number of OS architectures.

  The compiler needs to know a
  particular variant of the processor.
- A particular macro definition causes the inclusion of particular header files that define a
  number or related macros.

The probing of the compiler by the `cov-configure` program may require a
specific option to be defined on the command line. For example, the Greenhills compiler
toolchain uses the -bsp option to determine what directory to use
`#include` files from. To add this option to the
`cov-configure` process, you would need to use the "--" option, for
example:

`cov-configure -co ccintppc.exe -pgreen_hills -- -bsp SLS_Debug -os_dir
...`

Options that are put after the `--` are then put into the
comp_require tag by the `cov-configure` program.
This ensures that you can configure the same compiler for more than one usage.

If the compiler will only tell you about a macro if you already know about it, then you
will need to trawl through the manual for the compiler and add the macros using the
macro_candidate tag.

Some compilers can be told to give all the macros that they have defined internally to the
standard output. For example, the gcc compiler will do this if it is given the option
`-dM` when you are preprocessing a file (-E). If the compiler is
capable of doing this, then `cov-configure` can make use of it to find
more macros. If you have the manual for the compiler, find the option(s) that have the
desired effect and add them to the configuration file using the
dump_macros_arg tag. For example, for gcc:

```
<options>              
     <dump_macros_arg>-dM</dump_macros_arg>                
     <dump_macros_arg>-E</dump_macros_arg>                   
<options>
```
