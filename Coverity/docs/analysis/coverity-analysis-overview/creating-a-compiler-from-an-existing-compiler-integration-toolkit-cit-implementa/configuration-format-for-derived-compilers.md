---
title: "Configuration format for derived compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuration-format-for-derived-compilers.html"
content_id: "67NO5KX3dxOITixki66TDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:19.006091+00:00"
---

# Configuration format for derived compilers

There is a new config format for derived compilers, as shown in the following example. Note
that lines with a asterisk (*) at the end indicate mandatory tags:

```
<config>
  <build>
    <comp_derived_from>example:compiler</comp_derived_from>*
    <derived_compiler>*
      <comp_name>newCompilerName</comp_name>*
      <default_comp_name>newCompilerDefaultName</default_comp_name>*
      <comp_translator>new:compilercc</comp_translator>*
      <derived_comp_type>example:compilercc</derived_comp_type>*
      <comp_desc>New Compiler CC (CIT)</comp_desc>*

      <comp_family_head>true</comp_family_head>
      <comp_next_type>new:compilercpp</comp_next_type>
      <extra_comp>
        ...
      </extra_comp>
      <config_gen_info>
        ...
      </config_gen_info>
      <options>
        ...
      </options>
    </derived_compiler>*
//OPTIONAL EXTRA DERIVED COMPILER(S)
    <derived_compiler>
      <comp_name>newCompilerName</comp_name>
      <default_comp_name>newCompilerDefaultName</default_comp_name>
      <comp_translator>new:compilercpp</comp_translator>
      <derived_comp_type>example:compilercpp</derived_comp_type>
      <comp_desc>New Compiler CPP (CIT)</comp_desc>

      <config_gen_info>
        ...
      </config_gen_info>
      <options>
        ...
      </options>
    </derived_compiler>

    <config_gen_info>
      ...Config gen info not specific
    </config_gen_info>

    <options>
      ...
    </options>
  </build>
</config>
```

Each listed `derived_compiler` is analogous to a variant from the regular configuration structure. You can
add compiler-specific configuration generation information and options under each
derived compiler tag, as well as more general configuration generation info and options
that will be used for every derived compiler that is listed.

The `derived_compiler` tags are:

comp_derived_from
:   Used to "find" the configuration file of the compiler that is being derived from. As an
    example, if you were to derive from the IAR R32C
    compiler:

    ```
    <comp_derived_from>iar:r32c</comp_derived_from>
    ```

    This
    corresponds to the directory and subdirectory of the compiler being derived
    from in the Compiler Integration Toolkit (CIT) templates directory.

derived_comp_type
:   Used to find the correct compiler to match within the config file of the compiler being
    derived from. For example, when deriving from the IAR R32C
    compiler:

    ```
    <derived_comp_type>renesascc:r32c</derived_comp_type>
    ```

All of the other tags used in the previous example have identical structure and functionality
to how they are used in normal configuration files. For more information, see The Compiler Integration Toolkit (CIT) compiler configuration file.

Anything that can be specified in a normal configuration file can be specified within the
proper section in the derived compiler configuration. In order to override something
specified in the configuration file that is being derived from there must be an opposing
option. For example, if there is a test that is disabled under the
`config_gen_info` tag for the compiler being
derived from, you only need to enable the test in the derived compiler configuration
file.
