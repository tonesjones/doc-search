---
title: "Using the Snippet View"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-the-snippet-view.html"
content_id: "v1OuodBo_spu2JsmVVRTJA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:45.881908+00:00"
---

# Using the Snippet View

Clicking *#* **snippet** displays the Snippet View. The information
shown here depends on whether you uploaded source files during the snippet scan.

- If you uploaded source files, the Snippet View displays the source
  file on the left pane and the matched component on the right
  pane:

    
   [image: Snippet - Side-by-Side View]   

  Highlighted code indicates the lines of code that were
  matched in the source file to the component in the current
  match.
- If you did not upload source files, the matched component appears in
  the right pane:

    
   [image: Source tab - No files uploaded]   

  Highlighted text shows the lines of code of the component
  that were matched by the selected (current) match.
- If the file has more than one snippet match, a message appears at the
  bottom of the Snippet View, letting you navigate to the next snippet
  match.
- The Snippet View provides the following information for the current
  match (and any alternative matches):

  - Component name and version.
  - Component license.
  - Release date.
  - Match file path.
  - Percentage of the scanned file that matches the component
    file.  
   [image: Snippet - Current Match information]   

  The **Alternative Matches** drop-down list shows
  alternative components and/or component versions which could be
  possible matches for the selected snippet. The match which is
  currently assigned to the selected snippet is the default. Selecting
  a match from the drop-down list displays the code for that component
  or component version.
- Snippet adjustments that are available are:

  - **Confirm Match**
  - **Undo Confirmation**
  - **Ignore Match**
  - **Unignore Match**

## Reviewing a snippet match in the Snippet View

1. In the **Source** tab, select *#* **snippet** in the **Match Type** column for
   the snippet match you wish to review.

   Select one of these options:

   - **Confirm**. If the snippet match has not been confirmed.
   - **Undo Confirmation**. If the snippet match has been confirmed and you want to unconfirm
     it.
   - **Ignore Match**. If the snippet match has not been ignored.
   - **Unignore Match**. If the snippet match has been ignored and you want to unignore it.
2. Select **Alternative Matches** to view other possible matches. You can:

   - Select one of possible alternative matches.
   - Select to manually enter an alternative
     match.

     Selecting this option displays fields from
     which you can select the component, version, and/or origin
     ID. After selecting the values, click
     **Confirm**.
