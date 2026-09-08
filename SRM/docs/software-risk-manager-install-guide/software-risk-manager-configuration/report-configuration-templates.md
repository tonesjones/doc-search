---
title: "Report Configuration Templates"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/report-configuration-templates.html"
content_id: "hxOHtmna_xGgr3CAHgw5SA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:29.872877+00:00"
content_hash: "9a94faf7c59e712637a783743e34be51da43ebc3106fdb8fe2d6c873c5c7777f"
---

# Report Configuration Templates

Several report configuration options accept templates for their values. These
templates may contain plain text and various substitutions, surrounded by
`{{` and `}}`. To include a `{`
`}` or `\`, prefix them with a backslash (e.g.,
`{`).

The available substitutions are as follows:

- `{{report.name}}` or `{{report.type}}` - the
  type of report, e.g., 'PDF.'
- `{{report.title}}` - the title of the report, e.g.,
  'Assessment Report' or 'HIPAA Report.'
- `{{project.id}}` and `{{project.name}}` - the
  ID or name of the project the report was generated for.
- `{{user.name}}` - the display name of the user who generated
  the report.
- `{{date:pattern}}` - the current date/time formatted with the
  given pattern; details on acceptable patterns may be found [here](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html).

Software Risk Manager users may also include project metadata values as well:

- `{{meta:foo}}` or `{{metadata:foo}}` - provides
  the contents of the metadata field named "foo" for the project (or a blank
  string if that value is not specified).
- `{{meta.id:bar}}` or `{{metadata.id:bar}}` -
  provides the ID of the chosen metadata value for the field named "bar" (or a
  blank string if one was not given).

The following modifiers may be applied to any value:

- `ltruncate:length` - will take up to the last
  `length` characters (truncated from the left of the
  string).
- `truncate:length` or `rtruncate:length` - will
  take up to the first `length` characters (truncated from the
  right of the string).
- `labbreviate:length` - will take up to the last
  `length` characters, inserting an ellipsis on the left if
  the string was truncated.
- `mabbreviate:length` or `cabbreviate:length` -
  will take up to `length` characters from the string,
  inserting an ellipsis in the center of the string, if necessary.
- `abbreviate:length` or `rabbreviate:length` -
  will take up to the first `length` characters, inserting an
  ellipsis on the right if the string was truncated.

For example, `{{project.name|abbreviate:8}}` will limit the length of
the project name to the first 5 characters followed by an ellipse. A project name of
"My Project" would be truncated to "My Pr..." for display purposes.

## Report Filename

The template used to generate filenames for reports may be customized. This can be
done by setting the `report.filename-template` property. See the previous section for details on valid values.

The default template is `{{project.name}} ({{date:dd MMM YYYY}})` -
which will produce filenames such as "My Project (27 Mar 2017).xml."

## Custom Logo

Users can add their company logo to a PDF report through a prop setting in
`codedx.props`. The custom logo will appear on the cover of the
PDF report. You can place the logo in the same folder as the properties file or
specify an absolute path. For best results, the specified image should be at least
432 pixels wide and/or 144 pixels tall.

For an image file named "logo.png" placed in the same folder as the properties
file, the setting in `codedx.props` would be as follows:

```
report.pdf.custom-logo = logo.png
```

## Skip Sending Report With No Findings

Each report template configuration has a "Skip sending report with no findings" checkbox
in the Schedule tab. This can be used to skip sending reports if there are no findings at
a per-report level. This checkbox is disabled by default.

If needed, the default value can be changed to be enabled in the UI. This can be done by setting
the `ui.report.skip-sending-report-with-no-findings-default` property to `true`.
Note that doing so will only affect the default value shown for the checkbox in the UI - the option
can still be configured at an individual report template level.
