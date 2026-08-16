---
title: "Creating a heatmap in Excel on Mac"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-heatmap-in-excel-on-mac.html"
content_id: "x7cd0~ViLJn_AiDenbUZow"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:31.333027+00:00"
---

# Creating a heatmap in Excel on Mac

Users with the System Administrator role can download
a zipped file that contains the current log files.

To create a heatmap in Excel:

1. Log in to Black Duck with the System Administrator role.
2. Download the log files.
3. Extract the logs to a folder.
4. Open a new and blank workbook using Microsoft Excel. Using other
   spreadsheet/workbook programs may yield different results or differ in the steps
   below.
5. On the first top empty cell of an empty worksheet:

   1. Click the Data tab > Get Data > From text
   2. Navigate to the location of your download logs folder/debug folder
   3. Select the Heatmap CSV file (scan-heatmap-YYYY-MM-##########.csv)
   4. Click Import
6. From the Text Import Wizard perform following:

   1. Enable the Delimited radio button
   2. Start import at row <1>
   3. Click the Next button
   4. Uncheck the Tab (as delimiter) box
   5. Check the Comma (as delimiter) box
   6. Click the Next button
   7. Click the Finish button
7. In the Import Data modal:
   1. Select either the Existing sheet or New Sheet from ‘Where do you want to
      put data’
8. Select the entire data that has been imported
9. Click the Insert tab
10. Click the Table icon
11. In the Create Table modal that appears, click OK. If an alert pop-up appears,
    select Yes. The imported data should now be a table with the first row as
    filters. This is the raw data for the Heatmap. Note the Table name in the top
    left corner of Excel (i.e. Table1).
12. In a new worksheet:

    1. Click on any cell
    2. Click the Insert tab
    3. Click the Pivot icon
13. In the Create PivotTable dialog box, do the following:

    1. Type the table name (in this case ‘Table1’) in the *Select a Table or
       Range* text field
    2. Select Existing worksheet in the *Choose where to place the
       PivotTable* section
    3. Click the OK button

       Your worksheet should look like this:

         
        [image: image]
14. Click in the Blank Pivot created, this should open the Pivot column panel.

      
     [image: image]
15. Drag the following to filter section in this order:

    1. Year
    2. Month
    3. Scan_Type
    4. Status
    5. Status_Message
    6. Project, Version
    7. Code_Location_Name
16. Drag the Hour field to the Columns section.
17. Drag the Day field to the Rows section.
18. Drag the Scans field to the Values section. It should show as ‘Sum of Scans’.
19. Rename Column header from Row Labels to Days
20. Rename ‘Column Labels’ Filter in second column to Hours

    The presentation in Excel should now look like this:

      
     [image: image]
21. Select all the cells that fall within the range between the first to last Hours
    column (do not include filter top row, ‘Grand Total’ bottom row or last column
    (Grand Total)

      
     [image: image]
22. Click the Home menu item
23. From the Conditional Formatting > Color Scales, select Red - Yellow - Green
    scale

      
     [image: image]
24. Select the cells in bottom Grand Total row and apply the same color scale
    (excluding first and last column. Only Hours data cells).

      
     [image: image]
25. Select the cells in the rightmost Grand Total column and apply the same color
    scale.

      
     [image: image]
26. Select the bottom right corner cell alone and provide it with a blue
    background.

      
     [image: image]
27. To analyze the data behind any cell, double click on it.

## Maximum Scan Size Heatmap

1. Add a blank new sheet to the workbook.
2. In the new worksheet, click on any cell, click on Insert tab, click on Pivot
   icon.
3. Click on the Blank Pivot created, this should open the Pivot column
   panel.
4. Drag the following to filter section in this order:

   1. Year
   2. Month
   3. Scan_Type
   4. Status
   5. Status_Message
   6. Project
   7. Version
   8. Code_Location_Name
5. Drag the Hour field to the Columns section.
6. Drag the Day field to the Rows section.
7. Drag avg_scan_size_in_gb field to the Values section
8. Change to show Maximum such that it should display ‘Max of
   avg_scan_size_in_gb’:

   1. Click on the field in the values section. This will launch the
      PivotTable field.
   2. Choose Maximum instead of Sum.
   3. Click the OK button.
9. Select all the cells that fall within the range between the first to last
   Hours column (do not include filter top row, ‘Grand Total’ bottom row or
   last column (Grand Total)
10. Click the Home tab, Conditional Formatting > Color Scales > Yellow - Green
    color scale.
11. Select the cells in bottom Grand Total row and apply the same color
    scale.
12. Select the cells in the rightmost Grand Total column and apply the same color
    scale.
13. Select the bottom right corner cell alone and provide it with a blue
    background.

## Scan Weight Heatmap

1. Add a blank new sheet to the workbook.
2. In the new worksheet, click on any cell, click on Insert tab, click on Pivot
   icon.
3. Click on the Blank Pivot created, this should open the Pivot column
   panel.
4. Drag the following to filter section in this order:

   1. Year
   2. Month
   3. Scan_Type
   4. Status
   5. Status_Message
   6. Project
   7. Version
   8. Code_Location_Name
5. Drag the Hour field to the Columns section.
6. Drag scan_weight field to the Values section and change to show Maximum such
   that it should display ‘Avg of scan_weight’. This can be set by clicking on
   the field in the values section and then choosing Average instead of
   Sum.
7. Drag the Scans field to the Values section. It should show as ‘Sum of
   Scans’.
8. Select all the cells that fall within the range between the first to last
   Hours column (do not include filter top row, ‘Grand Total’ bottom row or
   last column (Grand Total)
9. Click the Home tab, Conditional Formatting > Color Scales > Red - White color
   scale.
10. Select the cells in bottom Grand Total row and apply the same color
    scale.
11. Select the cells in the rightmost Grand Total column and apply the same color
    scale.
