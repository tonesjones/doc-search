---
title: "Adding and removing custom files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-and-removing-custom-files.html"
content_id: "yOHXW4QrsEqd8cotsxSvQg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:59.084165+00:00"
---

# Adding and removing custom files

Coverity Connect administrators can add custom files, such as configuration files,
documentation, scripts, and so forth. Developers can then access these files from the
central Downloads page.

**To add a custom file:**

1. Copy your file to the following directory:

   <install_dir>/server/base/webapps/downloads
2. In the /downloads directory, edit the
   fileConfig.xml and add new file nodes for each custom
   file. For example:

   ```
    <customFiles>
           <!-- example file node entry -->
           <file>
               <fileName>example.txt</fileName> <!-- mandatory field -->
               <displayName>example display</displayName> <!-- optional field -->
               <fileDescription>example description</fileDescription> <!-- optional field -->
           </file>
   </customFiles>
   ```

   - The `fileName` tag is mandatory and corresponds to the name of the hosted file. If
     this is the only entry is present in the file node, then a link to this
     file name is displayed on the Downloads page.
   - The `displayName` tag is optional and when it is defined, it overwrites the
     `fileName` tag in the link that is displayed on the
     Downloads page.
   - The `fileDescription` tag is optional and when it is defined, it adds a
     description to the link on the Downloads page for the file in the same
     file tag.

**To remove a custom file:**

1. Remove file from the /downloads directory.
2. Edit the fileConfig.xml in the
   /downloads directory and remove the corresponding file
   tag.
