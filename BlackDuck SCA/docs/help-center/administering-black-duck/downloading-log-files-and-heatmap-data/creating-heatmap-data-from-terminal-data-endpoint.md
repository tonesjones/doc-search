---
title: "Creating heatmap data from terminal-data endpoint"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-heatmap-data-from-terminal-data-endpoint.html"
content_id: "yoXl3Wi9U8ehJ9FPrtLSiA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:29.872726+00:00"
---

# Creating heatmap data from terminal-data endpoint

The data contained in the heatmap download link from the **System Information** page
is in a different format (ISO 861 UTC) as opposed to what is contained in the
**debug** folder. This means that a heatmap can't be generated easily from that
data set. To overcome this, follow these steps:

1. Open the heatmap-scan-terminal csv. You will see something like this - note the hour
   column is a combined date/time column with a time stamp:

   [image: image]
2. Create new columns to facilitate the data required:

   | Cell number | Value |
   | --- | --- |
   | L1 | epoch_time |
   | M1 | full_date |
   | N1 | actual_hour |
   | O1 | year |
   | P1 | month |
   | Q1 | day |
3. Add the following formulae into these new rows to get the data points
   desired:

   | Column name | Formula |
   | --- | --- |
   | epoch_time | =DATEVALUE(MID(A2,1,10))+TIMEVALUE(MID(A2,12,8)) |
   | full_date | =INT(L2) |
   | actual_hour | =L2-M2 |
   | year | =YEAR(L2) |
   | month | =MONTH(L2) |
   | day | =DAY(L2) |

   The end result should end up looking something like this:

   [image: image]
4. Propagate the data into the rest of the rows by double-clicking on the autofill
   handle (the little green square at the bottom right of the highlighted cell -
   your cursor will turn into a cross when you're over it):

   [image: image]
5. Create a heatmap as usual including the new columns.

   [image: image]
