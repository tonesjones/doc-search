---
title: "Tags for handling response files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-handling-response-files.html"
content_id: "uCkdqkXS2kGOdR8rFH0w4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:07.145193+00:00"
---

# Tags for handling response files

You can specify a function that should be used to split text found in response files into
separate arguments.

Similar to the `<pre_translate>` function the internal function can
be overridden by an external executable if necessary. The added configuration options
are both located in the `<options>` section of the
`<expand>` tag are as follows:

<intern_split_response_file_fn>
:   Specify the function that should be used with the function name as the value. For
    example:

    ```
    <expand>
        <options>
           <option>
             <intern_split_response_file_fn>foo</intern_split_response_file_fn>
           </option>
        </options>
    </expand>
    ```

    The choices for internal function:

    - `arm_split` - Specifies ARM compilers. ARM
      compilers have a specific syntax, so they need a different
      function.
    - `default_split` - The default choice. Should
      handle most cases.
    - `line_split` - Specifies that each full line in
      the response file is an argument (that is, not separated by tabs
      or spaces). This value is currently set by Compiler Integration
      Toolkit (CIT) for the Java configuration.

<extern_split_response_file_exe>
:   Specifies the function that should override the internal function, with the name of the
    executable that should be used. For example:

    ```
    <expand>
        <options>
           <option>    
             <extern_split_response_file_exe>foo</extern_split_response_file_exe>
           </option>
        </options>
        </expand>
    ```

    If both
    `<intern_split_response_file_fn>` and
    `<extern_split_response_file_exe>` appear in
    the configuration, the external executable takes precedence.

<response_file_filter>
:   Allows regex filters to process the response file prior to parsing it for arguments. These
    filters are cleared between phases in case different response file formats are
    used.

<response_file_extension>
:   Allows for an optional extension to apply to the response file. If the specified response
    file does not exist, this extension is used to find the response file.
