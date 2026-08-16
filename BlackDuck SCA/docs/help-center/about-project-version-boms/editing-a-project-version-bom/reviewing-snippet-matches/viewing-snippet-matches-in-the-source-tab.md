---
title: "Viewing snippet matches in the Source tab"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-snippet-matches-in-the-source-tab.html"
content_id: "2j1pDikr~XU04Xpegv_g~g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:44.944630+00:00"
---

# Viewing snippet matches in the Source tab

Selecting the badge in the BOM displays the **Source** tab filtered to show
unconfirmed snippet matches:

  
 [image: Source tab with snippets]   

Note: You can also view the **Source** tab filtered to a specific match by selecting it
when viewing unconfirmed matches.

- The left pane shows the top-level directory. Select the directory to view the
  tree structure of the files.

  [image: Unconfirmed snippet icon] indicates the location of an unconfirmed snippet. Clicking the link
  opens the Snippet View.
- The table provides information, such as the name, component, match type, license, and usage.

  - [image: Unconfirmed snippet icon] indicates an unconfirmed snippet match.
  - [image: Ignored snipped match] indicates an ignored snippet match.
  - [image: Confirmed snippet match] indicates a confirmed snippet match.
  - [image: Source File icon] indicates there is a source file to view. This icon only
    appears if you uploaded source
    files.

    Clicking [image: Source File icon] opens the Source Code View which displays the content of
    this file.

      
     [image: Source Code View]

## Confirming, ignoring, and editing snippet matches

To confirm/unconfirm a snippet match:

1. Check the box next to the file.
2. Click [image: Snippet Adjustments button] .
3. Select **Confirm Match** or **Undo Confirmation**.

To ignore/unignore a snippet match:

1. Check the box next to the file.
2. Click [image: Snippet Adjustments button] .
3. Select **Ignore Match** or **Unignore Match**.

To edit a snippet match:

1. Check the box next to the file and then click [image: Edit button] , or;

   Click the [image: Options button] button at the end of the file's row and select Edit.
2. Use this dialog box to modify the component, version, or origin ID.
3. Select **Adjust Snippets and Confirm** which adjusts and automatically
   confirms the snippet match.
4. Click **Update**.

## Bulk confirming, ignoring, and editing snippet matches

Bulk confirming or ignoring snippet matches works similarly to process of confirming
or ignoring individual snippet matches described above.

To bulk confirm or ignore multiple snippet matches:

1. Check the box next to the desired snippet matches, or the box next to the
   **Name** column header to select all snippet matches.
2. Click [image: Snippet Adjustments button] .
3. Select **Confirm Match**, **Undo Confirmation**, **Ignore Match**,
   or **Unignore Match**, based on your intended action.

To bulk edit snippet matches:

1. Check the box next to the desired snippet matches, or the box next to the
   **Name** column header to select all snippet matches.
2. Click [image: Edit button] .

   The Bulk Edit Components dialog box appears.

     
    [image: Bulk Edit Components dialog box]
3. Use this dialog box to modify the component or version.
4. Select **Adjust Snippets and Confirm** which adjusts and automatically
   confirms the snippet match.
5. Click **Update**.
