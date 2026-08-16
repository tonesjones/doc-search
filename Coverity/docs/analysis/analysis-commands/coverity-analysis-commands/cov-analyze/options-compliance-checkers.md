---
title: "Options: Compliance checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-compliance-checkers.html"
content_id: "QIvAyYWf9wwzv9nZy5tx3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:38.044373+00:00"
---

# Options: Compliance checkers

--coding-standard-config <path/to/codingstandard_configuration_file>
:   This option provides the path to a configuration file for a coding standard
    to run as part of the analysis. You can provide the option multiple times,
    with different configuration files to use multiple coding standards in an
    analysis run. Note that you cannot specify two configurations for the same
    standard in a single run.

    Note:
    Any analysis involving `--coding-standard-config` requires
    the information generated during `cov-build` when including
    the `--emit-complementary-info` option.

    You can find sample configuration files in
    <install_dir>/config/coding-standards/<name_of_standard>.
    We recommend that you create a custom configuration based on these samples.

    Coding standard analysis normally runs along with regular analysis. To
    analyze only for a single coding standard, use the `--disable-default
    option` along with `--coding-standard-config`

    A configuration file can specify one of the following standards. These
    examples enable all supported rules for their respective standards.

    - MISRA C 2004

      [C MISRA option, required for a MISRA analysis.] Content for a
      configuration file for all supported 2004 standards (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "misrac2004",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - MISRA C 2012

      [C MISRA option, required for a MISRA analysis.] Content for a
      configuration file for all 2012 standards (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "misrac2012",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - MISRA C 2023

      [C MISRA option, required for a MISRA analysis.] Content for a
      configuration file for all 2023 standards (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "misrac2023",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - MISRA C++ 2008

      [C++ MISRA option, required for a MISRA analysis.] Content for a
      configuration file for all supported 2008 standards (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "misrac++2008",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - MISRA C++ 2023

      [C++ MISRA option, required for a MISRA analysis.] Content for a
      configuration file for all supported 2023 standards (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "misrac++2023",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - CERT-C/CPP

      The product is shipped with predefined configuration files (for example,
      cert-c-all.config,
      cert-c-L1-L3.config,
      cert-c-L2-L3.config,
      cert-c-L3-only.config,
      cert-c-L1-L2.config,
      cert-c-L1-only.config, and
      cert-c-L2-only.config) under
      `<install>/config/coding-standards/cert*/`.

      The levels are documented in the CERT-C/CPP specifications:

      - If you want to target only a specific level or
        permutation of levels, you can point to the predefined
        configuration file that matches, or you can define your
        own configuration file with your own custom
        deviations.
      - If you want the entire set of standards rules that we
        support, you can use the
        `cert-c-all.config` file.

      Content for a configuration file for all rules in CERT-C standard
      (and no deviations):

      ```
      {   
          "version"    : "2.0",
          "standard"   : "cert-c",
          "title"      : "your_title_here",
          "deviations" : []
      }
      ```
    - CERT-C Recommendation

      The configuration files are all in the following directory:

      ```
      <install-dir>/config/coding-standards/cert-c-recommendation/cert-c-recommendation-all.config
      ```
    - CERT-Java

      The configuration files are all in the following directory:

      ```
      <install-dir>/config/coding-standards/cert-java/cert-java-all.config
      ```
    - AUTOSAR

      The configuration files are all in the following directory:

      ```
      <install-dir>/config/coding-standards/autosarcpp14/autosarcpp14-all.config
      ```
    - ISO TS 17961

      The configuration files are all in the following directory:

      ```
      <install-dir>/config/coding-standards/iso-ts17961/iso-ts17961-all.config
      ```

    You can also use the HIS Metrics checker to measure MISRA coding standards.
    This is an optional checker setting that is enabled by adding the HIS
    Metrics settings to your MISRA configuration file. Once the checker is
    enabled, the defects that are found by the HIS Metrics checker are included
    in the emit process.

    You can run the HIS Metrics checker by adding the following HIS Metrics
    settings to your MISRA configuration file:

    ```
    {
        "HIS_Metrics" : {
            "raw_metrics_filename" : "raw-metrics.txt",
            "html_report_filename" : "HIS_report.html",
            "policies" : [
                {
                    "name" :  "COMF",
                    "compliant_range" : {"low" : 0.4, "high" : 1,}
                },
            ]
        }
    }
    ```

    The following comments apply to the `"HIS_Metrics"` field:

    `"raw_metrics_filename"`
    :   Specifies the name of the file in the output folder in which to store the raw metrics for each function.

    `"html_report_filename"`
    :   Specifies name of the HTML report file.

    `"policies"` array
    :   This array is optional. It can contain any number of entries.

        `"name"`
        :   Can be one of the following values:
            `"COMF"`, `"PATH"`, `"GOTO"`, `"CCM"`, `"CALLING"`,
            `"CALLS"`, `"PARAM"`, `"STMT"`, `"LEVEL"`, `RETURN"`,
            `"VOCF"`, `"CYCLE"`.

        `"compliant_range"`
        :   Sets the high and low values for the compliance range for this particular metric.
            Each of these values is optional, and either can be set to `null`.

    The `high` and `low` values set the compliance
    range for this metric. They are optional, and each of them is nullable. If a
    limit is *not* specified, analysis uses the default limit. If a limit
    is set to `null`, the limit is not enforced and no defects
    will be reported for violating that limit. If both `high` and
    `low` limits are `null`, then effectively
    this disables the policy checker.

    Here is an example of disabling the `low` limit of the
    `COMF` policy:

    ```
        "HIS_Metrics" : {
            "policies" : [
                {
                    "name" : "COMF",
                    "compliant_range" : { "high" : 100.0, "low" : null },
                }
            ]
        }
    ```

    Here is what the config looks like after adding the HIS Metrics settings to
    the MISRA configuration file. The `"raw-metrics.txt"` file is
    the file in the output folder to which the raw metrics for each function are
    stored. The `"HIS_report.html"` file is the HTML report
    file.

    ```
    {
        "version": "2.0",
        "standard": "misrac2012",
        "title": "MISRA C-2012 All Rules",
        "deviations": [],
        "HIS_Metrics" : {
            "raw_metrics_filename" : "raw-metrics.txt",     
            "html_report_filename" : "HIS_report.html",   
            "policies" : [  
                {
                    "name" :  "COMF",          
                    "compliant_range" : {"low" : 0.0, "high" : 1,}   
                },
            ]
        }
    }
    ```

    To commit the HIS Metrics checker results, run the `cov-analyze
    --coding-standard-config` command prompt. Then, type the
    `cov-commit-defects` command to commit all of the found
    HIS Metrics checker defects. The coding standard violations are then
    reported to Coverity Connect as an HIS Metric
    Violation.

    Each metric has its own range of compliant values. If one or more HIS Metrics
    are unspecified in the configuration file, then the missing metric will
    typically default to the range specified in the following table. Note that
    for two of the HIS Metrics the Coverity default acceptable range is
    different than the standard HIS Metrics range and it is recommended that you
    review and, if needed, modify the upper or lower bounds.

    - The Coverity HIS Metrics checker for COMF defaults
      to a range between 0.2 and 100 (while the standard default range is
      > 0.2). It is recommended that the upper bound is modified to a
      value that makes sense for your project.
    - The Coverity HIS Metrics checker for CALLING
      defaults to a range between 1 and 5 (while the standard default
      range is between 0 and 5), meaning that if a function has no
      callers, Coverity will report a violation.

    Table 1. HIS metrics description

    | Metric | Description | Scope | Default Coverity range |
    | --- | --- | --- | --- |
    | CALLING | Number of distinct functions that call the current function. | function | 1–5 (the standard range is 0–5). |
    | CALLS | Number of distinct functions that the current function invokes. The following count as functions:   - Overloaded operators (each overload counts as a separate function). - Constructors - Destructors - "operator new" - "operator delete" - Virtual calls (but only the function being called virtually counts).   The following do not count as functions:   - Indirect calls - Function pointer calls | function | 0–7 |
    | CCM | Cyclomatic Complexity, which is the number of linearly independent paths in the function body. | function | 1–10 |
    | COMF | Comment density, which is the ratio of the number of comments (outside of and within functions) to the number of statements. Note: Comment density in reported on a per-function basis. For a specific function, Coverity counts the comments within the function body, and adds one if there are comments before the function definition. | module | 0.2–100 (the standard range is >0.2) |
    | CYCLE | Number of call graph recursions over one or more functions. | project | 0 |
    | GOTO | Number of goto statements. | function | 0 |
    | LEVEL | Maximum depth of nesting of control flow structures such as `do`, `for`, `if`, `switch`,`try`, `while`. | function | 0–4 |
    | PARAM | Number of function arguments. | function | 0–5 |
    | PATH | Number of non cyclic paths. | function | 1–80 |
    | RETURN | Number of return points within a function. | function | 0–1 |
    | STMT | Number of statements per function. | function | 1–50 |
    | VOCF | Language scope. It is calculated as VOCF = (N1 + N2) / (n1 + n2), where:  - n1 = Number of different operators - N1 = Sum of all operators - n2 = Number of different operands - N2 = Sum of all operands   For the purposes of calculating VOCF (vocabulary frequency), the following conditions apply:   - Assignment using `=` counts as 1 operator When used to initialize a variable, `=` does not count as an operator.   For example, the count for `int x = 10` includes 1 operand but 0 operators. - A compound assignment (`+=`, `-=`, and so on) counts as 2 operators. - Accessing a structure, a pointer, and an access passed by reference are counted as 1 operator. - The comma operator (for example `(1, 2)`) is counted as 2 operators. The operands on either side of the comma might include operators of their own. - A cast is counted as 1 operator. - Array access using `[]` is counted as 1 operator per each dimension specified. The array variable is counted as 1 operand and each parameter enclosed in brackets (`[]`) is counted as 1 operand. - The parentheses (`()`) used in a function call count as 1 operator. - A function can be an operand. - The `sizeof()` operator is counted as 1 operator. In addition to `sizeof()` itself, the operand it is called on might include operators of its own. | function | 1–4 |

    The sample configuration files in
    <install_dir>/config/coding-standards/<name_of_standard>
    specify a configuration and any deviations, along with the rules covered by
    the configuration. No violations will be reported for the rules specified in
    the `deviations` field.

    Configuration example with deviations:

    In the following sample configuration, the deviations are Rules 5.6, 6.1, and 20.1.

    ```
    {
        "version" : "2.0",
        "standard" : "c2004",
        "title" : "C-2004 example with some deviations",
        "deviations" : [
    	    { "deviation" : "Rule 5.6",   "reason" : "Currently disabled in the analysis configuration." },
    	    { "deviation" : "Rule 6.1",   "reason" : "Currently disabled in the analysis configuration." },
    	    { "deviation" : "Rule 20.1",  "reason" : "Currently disabled in the analysis configuration." }
        ]
    }
    ```

    Note that for MISRA, the deviations are reported in the MISRA report, so they
    should explain why the deviation is claimed (either explaining in-line the
    measures being taken to mitigate risk or citing a separate document that
    does so) as per MISRA documentation. To keep a record of the claimed
    deviations, you might choose to store your configuration file in your source
    revision control repository.

    The file names of the sample configuration files identify what category of
    rules are run. The categories of rules vary between standards, but for
    example in MISRA_c2004, the configuration file
    misrac2004-required-only.config will run only the
    rules in the category required. In CERT,
    cert-c-L1-L2.config will run the rules in the
    categories L1 and L2.

    For your custom configuration file, you can create and edit a copy of one of
    the samples instead of editing the file that Coverity provides. Using the
    copy will prevent the loss of your configuration upon upgrade and avoid the
    potential for other undesired behavior. Coverity also recommends adding the
    copy to your source stream to ensure that the history of changes to that
    file are tracked.

    For MISRA rules and directives,
    see "MISRA rules and directives" in the Coverity 2026.6.0 Checker Reference.
