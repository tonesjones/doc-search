---
title: "Detecting embedded licenses"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/detecting-embedded-licenses.html"
content_id: "GDcofYT5gSbEel2pPbz3vw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:40.345269+00:00"
---

# Detecting embedded licenses

Black Duck can detect instances of embedded open source licenses not
declared by Black Duck KnowledgeBase for a component.

By enabling detection of deep license data when scanning code, users focused on license
compliance can view the licenses that were detected in their open source to ensure there
are no problematic licenses and that all licenses are accounted for in their BOM.

With this feature, Black Duck performs a search for license string text
and displays the licenses found in the **Source** tab.

By displaying this information in the **Source** tab, you can easily find the files
and directories that interest you and determine if embedded licenses are located
there.

  
 [image: Discoveries list]   

Black Duck groups the detected licenses into one of two categories:

- **Licenses**. An exact match to a license and version.
- **License References**. A "fuzzy" match to a license; license version
  information was not found.

For each license statement found, Black Duck displays the number of:

- "Hits". The number of instances that license text was found in all files.
- Files where these "hits" were found.

In the example shown above, there were five instances of Apache License text found in two
files, while there was 224 instances of Apache License Version 2.0 found in 219
files.

Black Duck also lists the total number of files affected for each
category. Note that this value may not equal the total number of files shown for each
license in that category as a file can have multiple different licenses, as shown above
for the **Licenses** category.

Optionally, to help you review this information, upload your source files so that BOM
reviewers can view discovered license text from within the **Source** tab. When
source files are uploaded, Black Duck provides a list of embedded
licenses and displays the highlighted license text in the file. This can help BOM
reviewers evaluate the license text.

  
 [image: Discoveries dialog box with file text]   

If you do not upload the source files, the Black Duck UI only displays the location of
the discovered license text in the file, by line number:

  
 [image: Discoveries dialog box]   

To include your source files, after your administrator has enabled source uploads, as
described in the installation guide, include the upload source parameter when
scanning.

Note: Regardless whether you upload your source files or not, embedded license detection cannot be
completed offline as it requires communication with the Black Duck
server.

## Supported file extensions/ file names

Embedded license search occurs in file extensions such as `.bat` or
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

## License detection process

The process to view embedded licenses is:

1. Enable detecting of deep license data when scanning and optionally, enable
   uploading source files for viewing embedded licenses within the file.
2. Review embedded licenses.

### Enable detecting of deep license data

All scanning methods have an option to enable license string search:

- Signature Scanner command line
- Black Duck Detect Desktop
  Black Duck Detect
- Black Duck Detect

#### Using the Signature Scanner command line

Use the **--license-search** parameter to enable embedded licenses.

Click here for more information on using the command line.

#### Using Black Duck Detect Desktop or Black Duck Detect

Use the **--detect.blackduck.signature.scanner.license.search** property
to enable deep license data detection. This property is available in Black Duck Detect version 6.2 and later.

## Reviewing embedded licenses

Black Duck displays the location of these licenses in your code
tree.

To review embedded licenses :

1. After enabling license search, select the **Source** tab from your project
   version BOM page.
2. Select a folder in the code tree that you want to determine if there are
   embedded licenses.

   Optionally, select **All Subfolders** to view information for all
   subfolders.

   The table displays information in the table for the selected location. By
   default the **Files** option is selected.

     
    [image: Source tab]
3. Select **Discoveries** to view the list of embedded licenses for this
   location.

     
    [image: Source tab]
4. Select a license to view the **Source** tab filtered to display the files
   that contain the selected embedded license text.

     
    [image: Source tab]   

   Optionally, select a file name to view the location of the file in the code
   tree. If you uploaded your source files, the file contents appears on the
   page.

     
    [image: Source tab]
5. Select a type of discovery (**License** or **License Reference**) from
   the **Discovery Type** column to open the Discoveries dialog box.

     
    [image: Source Discoveries dialog box]   

   The Discoveries dialog box shows all licenses and license references found
   for the selected file.

   The information that appears here depends on whether you uploaded source
   files.

   In the example shown above, source files were uploaded in the scan.
6. Select a license to view the highlighted license text indicating the embedded
   license text found.

     
    [image: Discoveries dialog box]   

   If you did not upload source files, the Discoveries dialog box displays the
   location of the discovered license text in the file, by line number:

     
    [image: image]
