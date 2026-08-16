---
title: "The compiler switch file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-compiler-switch-file.html"
content_id: "MFxfQHCSMHtxDsN1ezyCkA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:15.753079+00:00"
---

# The compiler switch file

The compiler switch file filters the compiler command-line options that are useful to the
process. The file also removes and "cleans up" the options that
`cov-emit` does not require. The compiler switch file exists in the
same directory as the Compiler Integration Toolkit (CIT) configuration and uses the
following naming convention:

compiler_switches.dat

A switch table can import switches from another switch table. For example, the following
statement, if used in a switch file, imports all the switches defined in`gnu_switches.dat` to the current switch table.
`$CONFIG_TEMPLATES_BASE_DIR$` is expanded to the absolute path name
of the directory that contains the configuration files.

```
import $CONFIG_TEMPLATES_BASE_DIR$/gnu/gnu_switches.dat
```

The compiler switch file requires an entry for every option that can be used with the
target compiler. If you do not specify an entry and the switch is encountered on the
command line, it is passed through to the next phase. If the target compiler switch is
never handled, it is only passed to `cov-emit` if
`cov-emit` understands the switch. Otherwise, the switch is dropped
and a warning is issued. However, this method of determining missing switches is not
reliable, as `cov-emit` might understand a switch differently than the
native compiler does. So, your switch table should never be incomplete. If a switch has
the same meaning to both the Coverity compiler and the native compiler, specify the
`oa_copy` flag in the switch's description.

If you just have one subtype of a compiler, then just the one compiler switch file is
read. The easiest way to support multiple compiler subtypes is to create independent
Compiler Integration Toolkit (CIT) configurations, each with its own compiler switch
file. If a compiler switch file exists in the subtype directory and the parent
directory, the two files will be appended together.

For every option that a compiler generates, there should be a line in the compiler switch
file that is in the following format:

`[option, option_type ]`

The option should be shown without any of the prefixes that the compiler might use. For
example, -I should be entered just as I without the dash. The option_type is a
combination of possible (or relevant) ways in which the option might be expressed. The
following table lists possible switch options:

Table 1. Flag options

| Flag | Description |
| --- | --- |
| `oa_abbrev_match` | May be abbreviated by any amount up to the short form in capitals. |
| `oa_additional` | Indicates that there are *two* arguments that follow a switch, with the second one always of the "unattached" variety. The first can be attached, unattached, or optional. Here is a Sun compiler example where both arguments to `Qoption` are unattached:  ``` -Qoption ccfe -features=bool,-features=iddollar ``` |
| `oa_alternate_table` | Designates that the switch is for specifying switches to another program, such as the preprocessor, and to use an alternate switch table to interpret it. For example, the following signifies that the value to Xpreprocessor should be interpreted by  compiler_preprocessor_switches.dat and the results should be appended to the command line:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_append}, ``` |
| `oa_append` | Options interpreted by the alternate switch table should be appended to the end of the command line. This flag is only valid in conjunction with `oa_alternate_table`. For example:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_append}, ``` |
| `oa_attached` | Must have an argument attached to the switch, for example `-DMACRO`. |
| `oa_case_insensitive` | Will accept upper or lower case, for example: `-D` or `-d` |
| `oa_copy` | Passes all instances to `cov-emit`, for example: `-I`. |
| `oa_copy_c_only` | Passes to `cov-emit` when compiling C file. This flag overrides `oa_copy` only when language sensitivity is set to true in the translation routine. Otherwise, it behaves identically to `oa_copy`. Most of the Compiler Integration Toolkit (CIT) compilers default to no language sensitivity, but this generally does not cause a problem as a language-sensitive argument only occurs when compiling that mode. Alternatively, you can use `oa_map` instead and map to `–coverity_c_switch,<original switch>`. |
| `oa_copy_cxx_only` | Passes to `cov-emit` when compiling C++ file. This flag overrides `oa_copy` only when language sensitivity is set to true in the translation routine. Otherwise, it behaves identically to `oa_copy`. Most of the Compiler Integration Toolkit (CIT) compilers default to no language sensitivity, but this generally does not cause a problem as a language-sensitive argument only occurs when compiling that mode. Alternatively, you can use `oa_map` instead and map to `–coverity_cxx_switch,<original switch>`. |
| `oa_copy_single` | Passes switch along, however, collapse the switch and its argument into a single argument. For example, `-I dir` would become `-Idir`. |
| `oa_custom` | Indicates that this switch will be handled in the custom code of a custom translator. |
| `oa_dash` | May be preceded by a dash (`-`), for example: -D |
| `oa_dash_dash` | May be preceded by two dashes (`--`, for example: `--D`) |
| `oa_discard_prefix` | This is the default option for `oa_alternate_table` and is the opposite of `oa_keep_prefix`. `oa_discard_prefix` will take precedence if `oa_keep_prefix` is specified on the `oa_alternate_table` switch and `oa_discard_prefix` is specified in the switch found in the alternate table. With the following switch table configuration using `<compiler>_switches.dat`:   ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend|oa_keep_prefix}, ```  and  compiler_preprocessor_switches.dat:  ``` {"D", oa_dash|oa_attached|oa_copy|oa_discard_prefix}, {"I", oa_dash|oa_attached|oa_copy}, ```  The following command line:  ``` compiler -Xpreprocessor -DTRUE=1 -Xpreprocessor -Idir source_file ```  will translate into:  ``` compiler -DTRUE=1 -Xpreprocessor -Idir source_file ``` |
| `oa_equal` | May have an argument following an equal sign (`=`, for example: `-D=value`) |
| `oa_hyphen_is_underscore` | Allows non-prefix hyphens within a switch to be interchangeable with underscores. For example, all of the following are recognized as the same switch:  - `--this-is-a-switch` - `--this_is_a_switch` - `--this-is_a_switch` |
| `oa_keep_duplicate_prefix` | By default, switches that are interpreted by an alternate table will cause the switch that specified the alternate table to be dropped. For example, given these switch tables in `<compiler>_switches.dat`:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend}, ```  and in `<compiler>_preprocessor_switches.dat`:  ``` {"F", oa_dash|oa_unattached|oa_copy}, ```  The following command line:  ``` <compiler> -Xpreprocessor -F -Xpreprocessor foo <source_file> ```  will result in:  ``` -F foo <source_file> ```  However, if `<compiler>_preprocessor_switches.dat` instead has the following:  ``` {"F", oa_dash|oa_unattached|oa_copy|oa_keep_prefix}, ```  Then the following command line will be unaltered in translation:  ``` -Xpreprocessor -F -Xpreprocessor foo <source_file> ```  `oa_keep_duplicate_prefix` can be specified in the primary table as a default for the table:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend|oa_keep_duplicate_prefix}, ```  Note that `oa_keep_duplicate_prefix` and `oa_keep_prefix` differ in the sense that with `oa_keep_prefix`, only the first instance of the prefix is kept, so when `oa_keep_prefix` is used, the command line `<compiler> -Xpreprocessor -F -Xpreprocessor foo <source_file>` yields this result:  ``` -Xpreprocessor -F foo <source_file> ``` |
| `oa_keep_prefix` | By default, switches interpreted by an alternate table will have the switch that specified the alternate table dropped. For example, given switch tables in compiler_switches.dat:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend}, ```  and in  compiler_preprocessor_switches.dat:  ``` {"D", oa_dash|oa_attached|oa_copy}, ```  The following command line:  ``` compiler -Xpreprocessor -DTRUE=1 source_file ```  will result in:  ``` -DTRUE=1 source_file ```  However, if  compiler_preprocessor_switches.dat instead has the following:  ``` {"D", oa_dash|oa_attached|oa_copy|oa_keep_prefix}, ```  Then the following command line will be unaltered in translation.:  ``` -Xpreprocessor -DTRUE=1 source_file ```  oa_keep_prefix can be specified in the primary table as a default for the table:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend|oa_keep_prefix}, ``` |
| `oa_map` | Specifies a switch mapping. For example, to map switch `-i`, which takes an argument either attached or unattached, to `-I` which takes the argument attached, specify: `{"i", oa_dash|oa_attached|oa_unattached|oa_map, "I", oa_dash|oa_attached }` |
| `oa_merge` | Removes white space from values with commas, for example: `-Ival, val2` becomes `-Ival,val2` |
| `oa_optional` | Adds an optional argument to a compiler switch. This flag is mutually exclusive with oa_unattached. |
| `oa_parens` | Must have an argument specified in parentheses that is either attached or unattached to the switch. For example: "`-D(MACRO)`" or "`-D (MACRO)`". |
| `oa_path` | Indicates that an `oa_required` switch is a path and should be converted to an absolute path during probing. If `oa_path` is not paired with `oa_required`, `oa_path` will have no effect. |
| `oa_plus` | May be preceded by a plus sign (`+`), for example: +D |
| `oa_prepend` | Options interpreted by the alternate switch table should be prepended to the beginning of the command line. This flag is only valid in conjunction with `oa_alternate_table`. For example:  ``` {"Xpreprocessor", oa_dash|oa_alternate_table, "preprocessor", oa_prepend}, ``` |
| `oa_required` | Indicates to `cov-configure` that the switch significantly changes the behaviour of the compiler in ways that might invalidate the results of the Coverity compiler's probes (For example, `-m32` or `–m64` for GCC). This tells `cov-configure` to require that a configuration be created with the same combination of required arguments as those that are present on the command line. In the event of template configurations, `cov-translate` and `cov-build` will automatically instantiate the needed configuration if one is not already made. If no template is present, `cov-translate` and `cov-build` will fail when encountering a missing configuration. |
| `oa_skip_arg` | Indicates that compiler invocations that use the switch are to be skipped by `cov-translate`. This flag imposes similar semantics as the `<skip_arg>` family of compiler configuration option tags, but with the following improvements:  - Allowed switch prefixes and case insensitivity will be   correctly matched without the need for duplicate   `<skip_arg>` tags (e.g.,   `<skip_arg>-E</skip_arg><skip_arg>/E</skip_arg>)`   or use of regular expressions (e.g.,   `<skip_arg>--?clr</skip_arg>`). - Switches that can appear in operands of options associated   with an alternate switch table are correctly matched. For   example,   `<skip_arg>-E</skip_arg>`   won't match `gcc -Wp`,`-E`,   but if the `-E` option is specified with   `oa_skip_arg`, the compiler invocation will be correctly   skipped. - Compiler configurations that import switch definition files   from other compiler configurations will automatically attain   the intended skip arg semantics without having to duplicate   a set of `<skip_arg>` directives. |
| `oa_slash` | May be preceded by a slash (`/`), for example: /D |
| `oa_split` | Breaks apart values that are really a list of values. A delimiter should follow `oa_split`, such as in `oa_split","` to split on commas. For example, an input switch of `-Iinc1,inc2` with `oa_dash|oa_attached|oa_copy|oa_split","` will result in `-Iinc1 -Iinc2`. |
| `oa_strip_quotes` | If there are quotes within the value of the switch, erase the outermost set of matching quotes. For example, `"-DMACRO='VALUE'"` will become `"-DMACRO=VALUE"`. This argument is passed to the compiler after all shell processing of quotes has occurred. |
| `oa_unattached` | May have a value after a whitespace, for example: `-D value` |
| `oa_unsupported` | Indicates that the switch is unsupported. If `cov-translate` encounters this switch it will issue an error and exit with a nonzero result. |

Note: The Compiler Integration Toolkit (CIT) only supports one switch per line. In addition,
you cannot break a switch's description across multiple lines, as this will cause the
translation to not properly execute.

The options can be combined by ORing them together. For example, if the compiler accepts
`-Dvalue` and `-D value`, then the
`option_type` is set to: `oa_dash | oa_attached |
oa_unattached`.

If a particular option is to be passed through to `cov-emit`, then one
of the `oa_copy` options should also be used. In the case of
`-Dvalue`, you can use `oa_dash | oa_attached | oa_unattached
| oa_copy`.

The compiler switch files are sorted (longest switches first) to prevent accidental bugs
caused by similar switches overlapping. For example, in the following scenario, the
description for `-D` would prevent the description for
`-DCPU` from ever being used:

`{ "D", oa_dash|oa_attached }`

`{"DCPU", oa_dash|oa_equal|oa_required }`

With switch sorting, this scenario does not occur, and `-DCPU=XXX`
appropriately flags a new configuration.
