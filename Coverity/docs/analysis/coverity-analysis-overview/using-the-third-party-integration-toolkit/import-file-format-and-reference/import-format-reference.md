---
title: "Import format reference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/import-format-reference.html"
content_id: "YWgjEL~asEPPjsRs4ztVvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:28.378049+00:00"
---

# Import format reference

The following syntax explains the structure of the JSON import file. Note the following:

- Items shown in bold are to be entered in your import file exactly as shown.
- Items shown in italics refer to subsequent items, or to items of JSON syntax.
- Items shown with ellipses (...) indicate that there can multiple occurrences of that
  item.
- Definitions and usage notes for the items are listed in Table 1.

```
file ← {
        "header": header,
        "sources" : [
   	         source , …
         ] ,
        "issues": [
             issue, …
         ] 
} 
header ← {
        "version" : integer ,
        "format" : string
}
source ← {
        "file" : string ,
        "language" : string ,
        "encoding" : string
}
issue ← {
        "checker" :  string ,
        "extra" :  string ,
        "file" : string ,
        "function" : string ,
        "domain" : string ,
        "subcategory" : string ,
        "properties" : properties ,
        "events" : [
   	         event, …
         ] 
}
properties ← {
        "category" : string ,
        "impact" : string ,
        "type" : string ,
        "cwe" : integer ,
        "longDescription" : string ,
        "localEffect" : string ,
        "issueKind" : string
}
event ← {
        "tag" : string ,
        "description" : string ,
        "file" : string ,
        "linkUrl" : string ,
        "linkText" : string ,
        "line" : integer ,
        "main" : boolean
}
```

The following table is a reference for the JSON elements that are used to construct the
import file and defines the following:

- *JSON element* is the name of the JSON element listed in the import file.
- *Required* tells if the element is required or optional.
- *Descriptions* defines the JSON element value.
- *GUI Display* shows in what area the element value is displayed in Coverity Connect
  using the example data provided in this section.
- *Merge Key* shows which elements in the file affect the way in which issues (CIDs) are
  merged and displayed in Coverity Connect.

  The Merge Key is a
  unique identifier for an issue. It is used to determine if two issues are
  the "same", for example, if they were detected in two slightly different
  versions of the same code base. Every CID corresponds to a single Merge
  Key.

  Every issue specified in the JSON file should include the checker
  name (issue.checker) and the file name
  (issue.file). While the function name
  (issue.function) is optional, it is strongly
  recommended to set it for all defects in code. It can be left unset for
  defects in configuration files, text files, or unparseable code, which are
  not applicable. Excluding the function name can produce unexpected
  results.

  If issue.function is set, then the merge
  key is exactly a function of the following:
  issue.checker, issue.extra, and
  issue.function. On the other hand, if
  issue.function is unset, then the merge key will
  instead be a function of issue.checker,
  issue.extra, and the file name (not the complete
  path) from issue.file.

  Note:

  Some Sigma checkers include parts of the file path in
  issue.extra. These are primarily checkers
  that report API misuse or report defects in configuration files.
  File path information is used to distinguish defects that appear in
  near-identical files with similar file names. Note that any part of
  the file path stripped out using the --strip-path
  option will not be added to issue.extra. CIDs may
  change if the argument to --strip-path is changed
  betwen scans.

  Any functions named `main` are handled
  specially, and also include the file name or the first parent directory from
  issue.file.

  The data used to calculate the
  Merge Key should generally be stable over time. If any one of the values
  change, a new Merge Key (and new CID) will result, and issues associated
  with the old Merge Key will no longer be detected, and will appear as
  "fixed".

Note: `cov-import-results` does not accept JSON import files that contain
Windows file paths. You must use forward slashes ("/") to separate paths for Windows and
include drive-letter syntax. For example:

```
"file" : "C:/projects/cov-import-test/doc_example/missing_indent_source.c",
```

For more information about JSON and its syntax, see <http://www.json.org/>.

Table 1. Import file item definitions

| JSON element | Required | Description | GUI Display | Merge Key |
| --- | --- | --- | --- | --- |
| `header` | required | The object that identifies the file format. Do not change the values. |  |  |
| `version` | required | The value is "`1`". |  |  |
| `format` | required | The value is `"cov-import-results input"`. |  |  |
| `sources [ ]` | required | An array of source objects. Source objects identify information pertaining to a source file that contains the issue. You can specify 0 or more sources. |  |  |
| `source.file` | required | The full pathname and filename of the source file that you want to import so that it displays in the Source browser in Coverity Connect. On Windows systems, you must use the drive letter format and forward slashes ("/") to denote path separation, such as `"C:/path/filename"`. You can trim portions of the pathname using the `--strip-path` option. |  |  |
| `source.​encoding` | optional | The encoding type for the file. The encoding types are the same that are accepted by the `cov-emit` command. Defaults to the system default encoding. |  |  |
| `source.​language` | optional | The primary source language of the source file. |  |  |
| `issues [ ]` | required | An array of issue objects. Issue objects describe all of the information about the specific third-party issues and how that information is displayed in the Coverity Connect UI. You can specify 0 or more issues. |  |  |
| `issue.checker` | required | Name of the checker that found the issue. The checker name lengths must be between 3 and 256 characters. | 3 | Yes |
| `issue.domain` | optional | The analysis domain associated with this issue. |  |  |
| `issue.extra` | required | A string that allows Coverity Connect to determine if a given issue is new, or if it is an additional instance of an existing issue. Coverity Connect combines the checker, file name, function, and extra fields to define a unique signature for each issue. If the signature matches an existing signature, the two issues are considered to be the same (merged). |  | Yes |
| `issue.file` | required | The full pathname and filename of the source file that contains the issue. You can trim portions of the pathname using the `--strip-path` option. The file must match a source file in the “sources” array, or a source file already present in the intermediate directory (placed there by a preceding invocation of `cov-build` or `cov-import-results`).  On Windows systems, you must use the drive letter format and forward slashes ("/") to denote path separation, such as such as "C:/path/filename". | 3, 4 | Yes, but only if issue.function is not present, or is present but is ambiguous. |
| `issue.​function` | optional | The name of the function that contains the issue. Name mangling is optional. | 2 | Yes |
| `issue.​subcategory` | required | The `subcategory` and tag attributes, along with the domain definition specified in `cov-import-results`, are used to identify the issue's type. type is a brief description of the kind of issue that was uncovered by one or several checkers, and is displayed in the event's message in the source browser. If you want to categorize, and accordingly display type for an issue, a custom checker description must be defined in Coverity Connect.  If you do not define a custom checker description, the issue's type is displayed as Other violation in Coverity Connect.  For more information, see "Configuring custom checker descriptions" in the Coverity Platform 2026.6.0 User and Administrator Guide. | 1, 3 |  |
| `properties` | optional | The object that identifies properties of software issues, the same sort of properties that are associated with issues found by checkers. If this element is present in the file, all of its fields *except for cwe* are required. Invalid values will be rejected by `cov-import-results`. |  |  |
| `property.​category` | Required only if `properties` is present in the JSON file. | A string between 1 and 100 characters long that identifies an issue category. See issue category. |  |  |
| `property.​impact` | required | A string that describes the impact of the issue. It is displayed in Coverity Connect UI elements, such as columns and filters. See impact. Valid values: "Low", "Medium", "High". |  |  |
| `property.type` | required | A string between 1 and 100 characters long that describes the checker type. It is displayed in Coverity Connect UI elements, such as columns and filters. See type. |  |  |
| `property.cwe` | optional | Integer that maps issues found by the checker to a Common Weakness Enumeration for software weaknesses. It is displayed in Coverity Connect UI elements, such as columns and filters. See CWE. |  |  |
| `property.​localEffect` | required | A string of 0 to unlimited length that is displayed in the Coverity Connect triage pane. See local effect. |  |  |
| `property.​longDescription` | required | A string of 0 to unlimited length that serves as a description of the issue. It is displayed in the Coverity Connect triage pane. See long description. |  |  |
| `property.​issueKind` | required | A string that identifies the kind of issue found. It is displayed in Coverity Connect UI elements, such as columns and filters. See kind.​ Valid strings: "QUALITY", "SECURITY", "TEST", or "QUALITY,SECURITY". |  |  |
| `events [ ]` | required | Array of event objects. Event objects describe all of the even information that leads to the issue. You can specify 0 or more event objects. |  |  |
| `event.tag` | required | See subcategory. | 4 |  |
| `event.​description` | required | A description of the event, helping you to identify the impact of the issue. Event descriptions should be a single, short sentence, providing explanatory information for Coverity Connect users. For example, an event message for the existing `RESOURCE_LEAK` checker is "At (3): Variable "p" going out of scope leaks the storage it points to." See JSON file - example.json for more event description examples. | 3 |  |
| `event.file` | optional | The full pathname and filename of the file containing the event. This is normally not needed. The default is the filename of the issue. On Windows systems, you must use the drive letter format and forward slashes ("/") to denote path separation, such as "C:/path/filename". |  |  |
| `event.​linkUrl` | optional | Any valid URL that you wish to include as part of the event message, such as a link to an internal site containing more information about the issue. You can only specify one link for each event. | 3 |  |
| `event.​linkText` | optional | The text that is displayed in the event message that serves as the hyperlink to the URL provided in `event.linkUrl`. | 3 |  |
| `event.line` | required | The line number of the source code in which the event occurs. You must specify one or more. | 3 |  |
| `event.main` | optional | Denotes the nature of the event's path. The value can be true or false. It is `true` if this event is the main event. | 3 |  |
