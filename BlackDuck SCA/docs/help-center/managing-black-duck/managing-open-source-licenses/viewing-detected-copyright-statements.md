---
title: "Viewing detected copyright statements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-detected-copyright-statements.html"
content_id: "yiEQmD8FkeEQEZVMPQmwkQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:03.341829+00:00"
---

# Viewing detected copyright statements

Black Duck can detect instances of copyright statements for a component.
By enabling detection of copyright data when scanning code, users focused on license
compliance can reduce license compliance risks by detecting and managing open source
software and proprietary copyrights statements.

With this feature, Black Duck performs a search for copyright string
text and displays the text found in the **Source** tab.

By displaying this information in the **Source** tab, you can easily find the files
and directories that interest you and determine if copyright text is located there.

  
 [image: Source tab with copyrights]   

Black Duck groups the detected copyright statements into the **Copyright
Searches** section.

For the copyright text found, Black Duck displays the number of:

- "Hits". The number of instances that copyright text was found in all files.
- Files where these "hits" were found.

In the example shown above, there were three instances of copyright text found in seven
files.

Black Duck also lists the total number of files. Note that this value may
not equal the total number of files shown for the copyright text as a file can have
multiple different copyright statements.

Optionally, to help you review this information, upload your source files so that
reviewers can view discovered copyright text from within the **Source** tab. When
source files are uploaded, Black Duck provides a list of copyright
statements. Select a copyright statement to highlight the text in the file. This can
help reviewers evaluate the copyright text.

  
 [image: Discoveries Dialog Box]   

If you do not upload the source files, the Black Duck UI only displays the location of
the discovered text in the file, by line number:

  
 [image: Discoveries Dialog Box]   

To include your source files, after your administrator has enabled source uploads, as
described in the installation guide, include the upload source parameter when
scanning.

Note: Regardless whether you upload your source files or not, copyright detection cannot be
completed offline as it requires communication with the Black Duck
server.

## Supported file extensions/file names

Copyright text search occurs in file extensions such as `.bat` or
`.js` and for these file names, or file names that include the
following text, regardless of case:

- bdsl
- copying
- copyright
- control
- dad
- gpl
- install
- legal
- lgpl
- license
- licence
- licenses
- licences
- notice
- readme

## Copyright detection process

The process to view copyright text is:

1. Enable detecting of copyright data when scanning and optionally, enable uploading source
   files for viewing copyright text within the file. The following scanning
   methods have an option to enable copyright string search:

   - Signature Scanner command line: Use the
     `-copyright-search` parameter.
   - Black Duck Detect Desktop: Enable the Signature Scanner Copyright
     Search option in **Scan Settings**.
   - [Black Duck Detect](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/62c4c406cd41875f23cf0a8c2848be66.topic):
     Use the
     `--detect.blackduck.signature.scanner.copyright.search=true`
     parameter.
2. Review the copyright text.

   Black Duck displays the location of these copyright statements in
   your code tree.

   To review copyright text:

   1. After enabling copyright text search, select the **Source** tab from your
      project version BOM page.
   2. Select a folder in the code tree that you want to determine if there is
      copyright text.

      Optionally, select **All Subfolders** to view information for all
      subfolders.

      The table displays information in the table for the selected location. By
      default the **Files** option is selected.

        
       [image: Source Tab - File Tab]
   3. Select **Discoveries** to view the list of copyright text, shown in the
      **Copyright Searches** section.

        
       [image: Source Tab - Discoveries List]
   4. Select a copyright statement to view the **Source** tab filtered to
      display the files that contain the selected copyright text.

        
       [image: Source Tab - Files list]   

      Optionally, select a file name to view the location of the file in the code
      tree. If you uploaded your source files, the file contents appears on the
      page.

        
       [image: Source Tab - Copyright Text]
   5. Select **Copyright** from the **Discovery Type** column to open the
      Discoveries dialog box.

        
       [image: Discoveries Dialog Box]   

      The Discoveries dialog box shows all copyright text found for the selected
      file. If embedded licenses and license references were also found, that text
      is also shown.

      The information that appears here depends on whether you uploaded source
      files.

      In the example shown above, source files were uploaded in the scan.
   6. Select the copyright text to view the highlighted text.

        
       [image: Discoveries Dialog Box]
