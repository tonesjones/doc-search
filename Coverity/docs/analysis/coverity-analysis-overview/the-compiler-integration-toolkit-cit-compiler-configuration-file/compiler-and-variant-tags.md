---
title: "<compiler> and <variant> tags"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-and-variant-tags.html"
content_id: "i3rKM_A6hqIHQ2Cd6WFJWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:11.686309+00:00"
---

# <compiler> and <variant> tags

The Compiler Integration Toolkit (CIT) allows you to generate multiple configurations for a
single compiler binary. This is done using the `<variant>` tags.
Everything defined inside of the `<variant>` tags is specific to a
particular configuration. Everything that is not included in the
`<variant>` tags is common to all variants. For example, the
following configuration will generate C and C++ configurations for a single binary (note
how the `<comp_next_type>` points to the next variant):

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>  
    <cit_version>1</cit_version>
    <config>  
       <build>
         <variant>
           <compiler>
             <comp_translator>multi</comp_translator>
             <comp_desc>UNIX like, standards compliant, C compiler</comp_desc>
             <comp_lang>C</comp_lang>
             <comp_next_type>multi_cxx</comp_next_type>
           </compiler>

          <options>
             <post_trans>
               <options> <prepend_arg>--c</prepend_arg> </options>
              </post_trans>
           </options>
         </variant>

         <variant>
           <compiler>
             <comp_translator>multi_cxx</comp_translator>
             <comp_desc>UNIX like, standards compliant, C compiler</comp_desc>
             <comp_lang>C++</comp_lang>
           </compiler>
         </variant>

         <config_gen_info>
               Same as simple XML …
         </config_gen_info>

         <options>
           <compile_switch>-c</compile_switch>
           <preprocess_switch>-E</preprocess_switch>
           <preprocess_output>-</preprocess_output>

            <pre_trans>
               <options> 
                   <remove_arg>-c</remove_arg> </options>
            </pre_trans>
         </options>
      </build> 
   </config> 
</coverity>
```

Multiple compiler names can be specified in a Compiler Integration Toolkit (CIT) compiler
configuration for the same compiler type. This allows for easier configuration for
compilers with multiple names and are of the same type.

The compiler tags are as follows:

<comp_desc>
:   Descriptive text that is displayed in the configuration files, and when you use the
    `dump_info` option.

<could_require_regen>
:   Indicates `cov-translate` needs to invoke the native compiler to re-generate
    files (such as .TLH files) needed by compilation when it replays a compilation
    command.

<is_ide>
:   Indicates the configured target is an IDE binary.

<target_platform_fn>
:   Specifies the internal function to be used to determine target platform for code
    instrumentation.

<comp_lang>
:   Identifies the source language for the configuration. After determining the
    language of a given source file, the `cov-build` command uses
    this tag to select an appropriate configuration. The allowed values for the
    field are:

    - C
    - C++
    - C# (or CS)
    - CUDA
    - Go
    - Java
    - Kotlin
    - Non Compiler (or NC)
    - Objective-C (or ObjC)
    - Objective-C++ (or ObjC++)
    - Razor
    - Visual Basic (or VB)

<comp_next_type>
:   For multiple compiler definitions, this tag tells `cov-configure` to scan the
    next `<comp_translator>` section for more possible
    variants.

<comp_name> (optional)
:   Specifies the binary name that is expected for the compiler type.
    `cov-configure` uses `<comp_name>` in two
    ways:

    1. If the compiler type is not specified with the `cov-configure
       --comptype` switch, `cov-configure` attempts
       to find a compiler type by matching the binary name. In this scenario,
       `cov-configure` might get the wrong compiler type if
       more than one have the same binary name.
    2. If the binary name matches for the first occurrence of the compiler type
       *and* the compiler type specifies
       `comp_next_type`
       *and* that `comp_next_type` has a different binary
       name, `cov-configure` will search for that different
       binary and configure it as well, assuming that it is found.

    Multiple `<comp_name>` tags are supported for scenario
    1 above. For scenario 2, however, the search is only performed if the first
    `<comp_name>` matches the binary name, and it only
    searches for the first `<comp_name>` of the second
    compiler type.

<comp_translator>
:   The command-line translator to use for this compiler. This specifies which
    compiler command line the `cov-translate` program should imitate.
    You can get a list of supported translators by running `cov-configure
    --list-compiler-types`.
