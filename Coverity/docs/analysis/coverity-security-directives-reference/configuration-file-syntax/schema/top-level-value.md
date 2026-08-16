---
title: "Top-level value"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/top-level-value.html"
content_id: "p5LLLT9EiTNAyM_zHO0a~Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:31.779710+00:00"
---

# Top-level value

The top-level value is a JSON object that has the following fields:

- `type`: Must be the string `"Coverity analysis
  configuration"`.
- `format_version`: A number indicating the version of the
  directives format for this file.

  The current directives format is version 12.

  The `type` and `format_version` fields ensure that
  the provided file is compatible with the current version of
  `cov-analyze`. Different versions support different
  directives for different languages. Coverity Analysis continues to support
  certain earlier, legacy formats: See Currently supported versions for details.

  Tip: If you analyze code from several languages in the same intermediate
  directory, you should use version 4 or later because the
  `language` field restricts the evaluation of directives to
  source code in the specified language or languages, and therefore avoids
  unintended application of directives and useless evaluation of directives on
  unintended languages.
- `language`: Directives in this file apply only to source code in
  the specified language or language family. The following table describes valid
  values for the `language` field values in release 2026.6.0 (matches are case insensitive).

  Table 1. 
  `language` values

  | Value | Meaning |
  | --- | --- |
  | `C-like` | Directives apply to C, C++, Objective-C, and Objective-C++ code. |
  | `C#` | Directives apply to C# code. Note that unsafe C# code blocks and raw pointer types are not supported. |
  | `Java` | Directives apply to Java code. |
  | `JavaScript` | Directives apply to all JavaScript code, including client-side JavaScript, JavaScript in HTML, and Node.js® code. |
  | `.NET` | Directives apply to all C# and Visual Basic code. This is only usable at the top level. |
  | `Visual Basic` | Directives apply to all Visual Basic code. |

  Important: You can specify a maximum of one `language`
  field and value per file. For example, imagine that you have some directives
  that you want to apply to Objective-C, others that you want to apply to C++
  code, and yet others that you want to apply to C# code. You need at least two
  directives files, one with `"language"` :
  `"C-like"` for the Objective-C and C++ directives and one
  with `"language"` : `"C#"` for the C# directives.

  Starting in version 4, this field became mandatory. In `format_version :
  4` and earlier, there is no `language` field. In
  those versions, the `"dc_checker_name"` and
  `"method_set_for_dc_checker"` directives for
  DC.*CUSTOM_CHECKER* apply to the `C-like`,
  `Java`, and `C#` languages. Other directives
  apply only to Java.
- `directives`: An array of User directives values.

The `directives` array contains the directive fields that specify this
particular configuration.

Schema example:
:   ```
    {
        "type" : "Coverity analysis configuration",
        "format_version" : 12,
        "language" : "Java", 
        "directives" : [
            // directives appropriate for Java go here
        ]
    }
    ```
