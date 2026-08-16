---
title: "Report-filtering elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/report-filtering-elements.html"
content_id: "tMtbyUrW_jIzBv7X5mWrBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:59.628849+00:00"
---

# Report-filtering elements

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `components` | String | An optional comma-separated list of Coverity Connect component names, which include component map names. If the components are listed here, the report will include data only for the listed components; for example: Default.lib or Default.src. | The report includes data for all components. | No |
| `issue-kind` | String | An optional comma-separated list of Coverity Connect issue kinds. If issue kinds are listed here, the report will include only issues of the listed kinds.  The possible values for `issue-kind` are as follows:   - `Quality` - `Security`   The following line is an example of using this option:   ``` issue-kind: Quality ``` | The report includes both quality and security issues. | No |
