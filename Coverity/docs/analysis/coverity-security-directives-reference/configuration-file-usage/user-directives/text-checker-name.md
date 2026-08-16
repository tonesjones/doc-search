---
title: "text_checker_name"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/text_checker_name.html"
content_id: "p~UKVUuNEy1_tRhJQC2uFg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:04.975315+00:00"
---

# text_checker_name

**File Types: Text, XML**

The `text_checker_name` directive defines a
TEXT.*CUSTOM_CHECKER*.

## Fields

The custom text checker directive uses the following fields:

`text_checker_name`
:   A JSON string that specifies the checker name. This string must start
    with `TEXT.`, and what follows must consist of all
    capital letters or the underscore character.

    For example, `TEXT.MY_CHECKER` is a valid name, but
    neither `TEXT.My_Checker` nor `MY_CHECKER`
    would be valid.

`file_pattern`
:   A RegularExpression value that
    describes filename paths in which defects will be reported. Files whose
    name does not match this pattern are not analyzed. This directive treats
    file names and paths in the following standardized manner:

    - The name is made absolute, including the drive letter on Windows
      systems.
    - The forward-slash character ( `/` ) separates name
      components.
    - When no drive letter is present, the name begins with a
      forward-slash character ( `/` ); otherwise, a
      forward-slash character ( `/` ) follows the drive
      letter.

`defect_pattern`
:   A RegularExpression value that
    specifies a pattern to match in files being analyzed. Analysis will
    report a defect at each location that matches this pattern.

`defect_message`
:   (Optional) A JSON string to print in the defect event message.

`remediation_advice`
:   (Optional) A JSON string to print as remediation advice in each defect
    report.

`new_issue_type`
:   (Optional) An IssueTypeDefinition
    object that specifies the checker properties, a CWE mapping, and issue
    taxonomy.

    When used as a `new_issue_type` value, all of the
    `IssueTypeDefinition` fields are optional.
