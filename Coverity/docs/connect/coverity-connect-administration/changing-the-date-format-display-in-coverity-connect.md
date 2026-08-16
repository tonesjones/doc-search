---
title: "Changing the date format display in Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-the-date-format-display-in-coverity-connect.html"
content_id: "y4ZQYndpl4GpMQzK6xcwcw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:55.259148+00:00"
---

# Changing the date format display in Coverity Connect

You can change the way in which the date format is displayed for the English, Japanese,
Chinese, and Korean locales in certain view types and columns in Coverity Connect.

You can change the date format as follows:

1. Create a new properties file.

   For the English locale:

   ```
   <install_dir>/config/format_en.properties
   ```

   For the Japanese locale:

   ```
   <install_dir>/config/format_ja.properties
   ```

   For the Chinese
   locale:

   ```
   <install_dir>/config/format_zh_CN.properties
   ```

   For the Korean
   locale:

   ```
   <install_dir>/config/format_ko.properties
   ```
2. Add a new date format to the `dateFormat` property in the
   format_locale.properties file.
   The following table lists the date format properties that can be changed, their
   defaults, and where in Coverity Connect they will be displayed.
3. Restart the Coverity Connect server to enable the changes.

Table 1. Date properties

| Date property | Defaults to | Displayed in |
| --- | --- | --- |
| `dateFormat` | MM/dd/yy for English, yyyy/MM/dd for Japanese, Chinese, and Korean | - Date-valued columns in the Issues: by Snapshot view type   (First Detected, Last   Detected, Last   Triaged) and the Issues: Project Scope view   type (First Detected, Last   Detected). - The same columns (as above) in email notification table   data. - Dates for Detection History and   Triage History sidebars. |
| `timeFormat` | hh:mm a for English, Japanese, Chinese, and Korean | Date and time values in Coverity Connect configuration (that is, through the Configuration menu). The following use a combination of dateFormat and timeFormat:  - Projects & Streams > Snapshot > Created column - System > Sign In Log > Session Start column |
| `timeStampFormat` | yyyy-MM-dd HH:mm:ss for English, Japanese, Chinese, and Korean | Date+time-valued columns in Functions views (Last Impacted, Last Modified) and Snapshots (Date) views |
| `scmDateFormat` | Defaults to MMM d, yyyy for English, yyyy/MM/dd for Japanese, Chinese, and Korean | SCM display from the Show Source Gutter Menu in the source browser. |
| `emailNotification​Date​Format` | MMMM d, yyyy for English, yyyy年M月d日 for Japanese, yyyy年M月d天for Chinese, and yyyy년 M월 d일 for Korean | The date used in the body text of an email notification (table data uses `dateFormat` like the web view). |
| `policyManagerTrend.​​dayFormat` | MMM dd for English, Japanese, Chinese, and Korean | The date used for day-to-day Policy Manager trend reports. |
| `policyManagerTrend.​weekFormat` | MMM dd for English, Japanese, Chinese, and Korean | The date used for weekly Policy Manager trend reports. |
| `policyManagerTrend.​monthFormat` | MMM yyyy for English, Japanese, Chinese, and Korean | The month format used for monthly Policy Manager trend reports. |
| `policyManagerTrend.​yearFormat` | yyyy for English, Japanese, Chinese, and Korean | The year format used for year-to-year Policy Manager trend reports. |

The following example shows the format_ja.properties file, with the
date format set to the American date format.

```
dateFormat=MM/dd/yy
timeFormat=hh:mm
timeStampFormat=yyyy-MM-dd HH:mm:ss
scmDateFormat=yyyy/MM/dd
emailNotificationFormat=MMMM d, yyyy
policyManagerTrend.dayFormat=MMM dd
policyManagerTrend.weekFormat=MMM dd
policyManagerTrend.monthFormat=MMM yyyy
policyManagerTrend.yearFormat=yyyy
```

For more information about how date time strings function, see <http://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html>.
