---
title: "Adding a custom coding standard"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-custom-coding-standard.html"
content_id: "APrW9xIEvhXGS8REc0ugGw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:33.489575+00:00"
---

# Adding a custom coding standard

You can add a custom coding standard to a report.
Adding a custom standard adds a column to the Issues: By Snapshot and Issues: Project Scope views,
and adds a Segmentation and Issues filter option to Policy Manager reports.

To add a custom coding standard, log in to Coverity Connect and follow these steps:

1. If an existing standard is similar to what you want, download its JSON file: Highlight a standard and then click Download Selected.

   If no existing standard is quite what you want, download the template: Click Download Template.
   See Downloading the template file.
2. If you downloaded a standard, use a text editor to find the row with the issue type whose value you want to change (this text is on the left side).

   Replace that value (on the right side) with the value you prefer, and add the line to the `"mapping"` object.
3. In either case, save the updated standard.

   The file name must end with a `.json` filename extension. The name itself doesn't matter:
   The name specified by the `"name"` field in the new standard is what matters for the Coverity Connect interface.
4. Click +Standard, and upload the edited JSON file.

As a use case, suppose you want reports to include a custom impact value for INFINITE_LOOP.
INFINITE_LOOP has a built-in Impact value (= `"Medium"`).
Your team believes loops are a more serious issue than `"Medium"`.
You can't change the Impact that INFINITE_LOOP reports,
but you can set up an alternative, parallel value. To do so, you might add the following mappings:

```
{
    "name": "Custom Impact"
    "mapping": {
        "infinite_loop:no_escape": "High",
        "infinite_loop:unsatisfiable_exit_condition": "High"
    }
}
```

After you add the new Custom Impact standard, issue views will include a column labeled Standard: Custom Impact that
shows the adjusted, elevated Impact values. (Values from the original, built-in standard continue to display.)

Figure 1. Example: Values from a custom OWASP report appear in the column to the right
  
 [image: In Coverity Connect, values from a custom report appear in a column at the right.]
