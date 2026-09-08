---
title: "Helpers"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/helpers.html"
content_id: "TMosMUsi15i9EIjA1Jrczw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:17.310391+00:00"
content_hash: "e511fd7afa793bb041e90919f3a7759efaa56a5ae3824520e0a379020d7786c1"
---

# Helpers

Software Risk Manager includes all the [#if](https://handlebarsjs.com/guide/builtin-helpers.html#if), [#unless](https://handlebarsjs.com/guide/builtin-helpers.html#unless), [#each](https://handlebarsjs.com/guide/builtin-helpers.html#each), and [#with](https://handlebarsjs.com/guide/builtin-helpers.html#with) helpers provided by Handlebars. Several other helpers
are also provided to assist as well.

## formatDate

Note: It is recommended to use the new `formatDateTime` helper
which gives you more flexibility to define both custom input and output
format strings.

The `formatDate` helper allows you to format a date by specifying a
format string. For example:

`{{formatDate finding.firstSeenOnDate 'YYYY-MM-DD'}}`

will take the first-seen date for the finding and convert it into an ISO-8601 valid
format. You can use the symbols below to create your format string:

- `M` month: 1, 2, 11, etc.
- `MM` month: 01, 02, etc.
- `MMM` month: Jan, Feb, etc.
- `MMMM` full month name
- `D` day of month: 1, 2, 11, etc.
- `DD` day of month: 01, 02, 11, etc.
- `ddd` day of week: Sun, Mon, etc.
- `dddd` day of week: Sunday, Monday, etc.
- `YY` year: 98, 99, 00, 01, etc.
- `YYYY` year: 1998, 1999, 2000, 2001, etc.

The `formatDate` helper uses [Moment.js](http://momentjs.com/) under the hood, so you can look
at its [documentation](http://momentjs.com/docs/#/displaying/) for more formatting symbols.

## formatDateTime

The `formatDateTime` helper allows you to format a datetime by
converting it from a specified input format to a specified output format.
For example:

`{{formatDateTime finding.firstSeenOnDate 'YYYY-MM-DD' 'MM/DD/YYYY'}}`

will take the first-seen date for the finding and convert it into the specified output
format. You can use the symbols below to create your format strings:

- `M` month: 1, 2, 11, etc.
- `MM` month: 01, 02, etc.
- `MMM` month: Jan, Feb, etc.
- `MMMM` full month name
- `D` day of month: 1, 2, 11, etc.
- `DD` day of month: 01, 02, 11, etc.
- `YY` year: 98, 99, 00, 01, etc.
- `YYYY` year: 1998, 1999, 2000, 2001, etc.
- `H` hour of day: 1, 2, 11, 21, etc.
- `HH` hour of day: 01, 02, etc.
- `h` clock hour of AM/PM: 1, 2, 11, 12, etc.
- `hh` clock hour of AM/PM: 01, 02, 11, 12, etc.
- `m` minute of hour: 1, 2, 11, 31, etc.
- `mm` minute of hour: 01, 02, 11, 31, etc.
- `s` second of minute: 1, 11, 21, 51, etc.
- `ss` second of minute: 01, 11, 21, 51, etc.
- `S` fraction of second: 1, 11, 211, 351, etc.
- `SS` fraction of second: 01, 11, 211, 351, etc.
- `a` AM/PM of day: AM, PM
- `z` timezone name: GMT, EST, PST, etc.

The `formatDateTime` helper uses `java.time` under the hood,
so you can look at its
[documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) for more formatting symbols.

## makeOxfordList

The `makeOxfordList` helper assists in generating an Oxford list from
an array of elements. The body will be evaluated for every item in the list.

For example, to list all of the Software Risk Manager Finding IDs, the template

```
{{#makeOxfordList allFindings ',' 'and'}}{{this.id}}{{/makeOxfordList}}
```

will result in

```
39955, 39956, 39939, and 39940
```

when evaluated on a group of findings with the IDs 39955, 39956, 39939, and
39940.

## formatLocation

The `formatLocation` helper formats a location object into a
user-readable version similar to those displayed elsewhere in Software Risk
Manager.

For example, the template

```
{{formatLocation finding.location}}
```

will result in

```
AbstractLesson.java:182
```

when evaluated on a finding located in
`WEB-INF/classes/org/owasp/webgoat/lessons/AbstractLesson.java`
on line 182 (columns 25-50).

By default, the short name of the location is used, and any column numbers are
omitted. You may opt to show the complete location information by passing
`true` as the second parameter to this helper. For example, the
template

```
{{formatLocation finding.location true}}
```

will result in

```
WEB-INF/classes/org/owasp/webgoat/lessons/AbstractLesson.java:182:25-50
```

in the previous example.

## formatCWE

The `formatCWE` helper creates a more informative representation of a
finding's CWE (if one is available).

Note: When using this helper, the last two parameters are optional.

The true/false parameter determines if a link to MITRE will be available. The
`trackerType` parameter will default to the issue tracker type
currently being processed.

For example,

```
{{formatCWE finding.cwe true trackerType}}
```

will result in

```
CWE 78 - Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') ([MITRE|https://cwe.mitre.org/data/definitions/78.html])
```

when evaluated on a finding associated with CWE-78.

If the second argument provided is true, a MITRE link for the CWE will be included
(formatted properly for the issue tracker being used).

If no CWE is present on the finding, this helper will evaluate to an empty string if
the second argument is false, or to "No Common Weakness Enumeration information
available" if the second argument is true.

## stripHtmlMarkup

The `stripHtmlMarkup` helper takes an HTML string and returns a copy
with all HTML tags removed, with newlines/spaces inserted as necessary while
attempting to preserve native formatting. By default, HTML escape sequences will be
converted in the result; use `false` for the second parameter (as
seen below) instead to prevent this. Whitespace-equivalent escape sequences (e.g.,
`&nbsp;`) will simply be replaced with a space regardless of
the second parameter value.

For example, a finding with a description of the
following

```
<h1>Explanation</h1>
<p>
	Cross-site scripting vulnerabilities occur when:
	<ol>
		<li>Data enters through an untrusted source</li>
		<li>The data is included in dynamic content without being validated for malicious code</li>
	</ol>
</p>
```

and a template
with

```
{{{stripHtmlMarkup finding.descriptions.general.content true}}}
```

will result in

```
Explanation
Cross-site scripting vulnerabilities occur when:

- Data enters through an untrusted source
- The data is included in dynamic content without being validated for malicious code
```

The following are known issues and limitations:

- Ordered/unordered lists will produce the same `-` prefix on list
  items.
- Nested lists may be improperly formatted.
- Issue trackers that interpret plaintext as emojis (e.g., `:(`)
  (e.g., Jira) will still interpret as emojis.
- The un-escaped HTML content may be re-converted to the escape sequences
  automatically by Handlebars. (e.g., HTML content with
  `&amp;`is un-escaped to `&` by
  `stripHtmlMarkup`, but gets converted back to
  `&amp;` in the output by Handlebars.) Use
  `{{{}}}` instead of `{{}}` to prevent this
  behavior.

## makeMarkupFromHtml

The `makeMarkupFromHtml` helper takes an HTML string and reformats it
into appropriate markup for the current issue tracker. The helper uses the following
formats:

- **Jira.** Atlassian Wiki markup format.
- **Azure DevOps.** No processing/pass-through (HTML content supported by ADO).
- **ServiceNow.** Simple text extraction, acts as an alias for
  `stripHtmlMarkup` with unescaping enabled.
- **GitHub, GitLab.** Markdown.

The helper takes three arguments: the first is required and the following two are
optional: the HTML to convert and the name of the issue tracker type to target (use
`trackerType` if not manually overriding; accepted values are
`jira`, `azure`, `servicenow`,
`github` and `gitlab`), and a boolean flag
(`true`/`false`), indicating whether to pre-clean
the HTML of any non-textual elements (defaults to `false`). The
pre-cleaning flag is usually not necessary, but if there are formatting issues, the
pre-cleaning option may prevent these issues.

For example, a finding with a description of

```
<h1>Explanation</h1>
<p>
	Cross-site scripting vulnerabilities occur when:
	<ol>
		<li>Data enters through an untrusted source</li>
	</ol>
</p>
```

and a template with

```
{{{makeMarkupFromHtml finding.descriptions.general.content trackerType}}}
```

will approximately result in

```
(If configured tracker is Jira or using `jira` as the second argument value)
h1. Explanation

Cross-site scripting vulnerabilities occur when:

# Data enters through an untrusted source
```

```
(If configured tracker is Azure DevOps or using `azure` as the second argument value)
<h1>Explanation</h1><p>Cross-site scripting vulnerabilities occur when: <ol><li>Data enters through an untrusted source</li></ol></p>
```

```
(If configured tracker is ServiceNow, or using `servicenow` as the second argument value)
Explanation
Cross-site scripting vulnerabilities occur when:

- Data enters through an untrusted source
```

```
(If configured tracker is GitLab, or using `gitlab` as the second argument value)
# Explanation

Cross-site scripting vulnerabilities occur when:

1. Data enters through an untrusted source
```

```
(If configured tracker is GitHub, or using `github` as the second argument value)
# Explanation

Cross-site scripting vulnerabilities occur when:

1. Data enters through an untrusted source
```

Keep in mind that the use of `{{}}` vs `{{{}}}` will
affect how Handlebars escapes any HTML-like content—typically, the
`{{{}}}` literal format is appropriate.

The following are known issues and limitations:

- Jira/Atlassian conversion ignores `<pre>` code blocks
  (limitation of Atlassian Renderer).
- Super/sub-scripts are generally unsupported (Jira/Atlassian renderer
  supports it but has known bugs).
- Nested lists in any format may be improperly formatted.
- Issue trackers that interpret plaintext as emojis (e.g.,
  `:(`) (e.g., Jira) will still interpret as emojis.
- Issue trackers whose formatting is whitespace-sensitive (i.e., Jira, GitHub, GitLab)
  may have formatting issues due to trailing/leading whitespace (the use of
  [`~` for whitespace
  control](https://handlebarsjs.com/guide/expressions.html#whitespace-control) is recommended).

## jiraMarkupFromMd

The `jiraMarkupFromMd` helper is intended to be used
to translate descriptions formatted using markdown into Jira markup.

For example,

```
{{{jiraMarkupFromMd descriptions.contextual.content}}}
```

will transform the following description:

```
# Header

Here is a *description*

1. Number one
2. Number two
3. Number three
```

into:

```
h1. Header

Here is a _description_

# Number one
# Number two
# Number three
```

## makeSource Snippet

The `makeSourceSnippet` helper takes the
`finding.sourceSnippet` object and outputs a formatted source
snippet.

For
example,

```
{{makeSourceSnippet finding.sourceSnippet}}
```

will result in

```
function foo() {
	console.log('bar');
}
```

The following are known issues and limitations:

- Jira/Atlassian shows line numbers, but by default do not support configuring the
  line numbers. The line numbers will start at 1.
- Jira/Atlassian has an issue with preserving the first source line's level of
  indentation.
- Azure, GitHub, GitLab, and ServiceNow do not show line numbers.
- Service now only supports code blocks in specific fields, like the
  `Additional Comments` field.

## minBy and maxBy

The `minBy` and `maxBy` helpers will cause the provided
expression body to be evaluated against the object with the lowest or highest value.
The path to this value is provided as an argument.

For example,

```
{{#minBy allFindings "severity.key"}}
         The lowest severity is on finding {{id}} with severity of {{severity.name}}.
{{/minBy}}
```

will result
in

```
The lowest severity is on finding 10 with severity of Info.
```

when evaluated on a group of findings, where the lowest severity finding has the ID
of 10 and severity of info.

In the case of a tie (e.g., multiple findings or results with the minimum or maximum
value), the first item with that value will be used. As outlined in Finding Objects, in the
case of a tie, this will give the finding or result with the highest severity and
lowest numeric ID.

## minByDate and maxByDate

The `minByDate` and `maxByDate` helpers will cause the provided
expression body to be evaluated against the object with the lowest or highest date value in
`yyyy-MM-dd` format. The path to this value is provided as an argument.

For example,

```
{{#minByDate allFindings "fixByDate"}}
         The lowest date is on finding {{id}}.
{{/minBy}}
```

will result
in

```
The lowest date is on finding 10.
```

when evaluated on a group of findings, where the lowest Fix By Date finding has the ID
of 10.

In the case of a tie (e.g., multiple findings or results with the minimum or maximum
date), the first item with that value will be used.

## Nested Arrays

These helpers can also handle nested arrays in a more advanced use case. This is
signified by adding a `.[]` at any point the helper should continue
iterating over inner arrays. The expression body's context will be at the inner-most
object, and the parent object(s) may be referenced if desired.

Here are two examples to illustrate these
points:

```
{{#maxBy allFindings "results.[].severity.key"}}
	Finding {{../../id}}, Result {{descriptor.name}}, Severity {{severity.name}}
{{/maxBy}}
```

will result in

```
Finding 10, Result My Weakness, Severity Medium
```

when evaluated against a group of one or more findings where the highest severity
result across all of the findings is a result on finding 10, with a descriptor name
of "My Weakness" and medium
severity.

```
{{#maxBy allFindings "results.[].metadata.cvssV3"}}{{metadata.cvssV3}}{{/maxBy}}
```

will result in

```
9.8
```

when evaluated against a group of findings where the highest CVSS V3 metadata entry
on any of the findings' results is 9.8.

Notice that the finding ID is accessed using `{{../../id}}`. You may
have been expecting `{{../id}}` to fetch the finding ID, since the
finding is the parent of the result that was selected. However, the array of results
itself is the immediate parent, and the parent of that is the finding, so
`../..` is used.
