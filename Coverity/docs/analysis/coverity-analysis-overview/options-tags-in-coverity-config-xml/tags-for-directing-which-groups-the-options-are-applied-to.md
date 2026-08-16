---
title: "Tags for directing which groups the options are applied to"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-directing-which-groups-the-options-are-applied-to.html"
content_id: "NHLsnLjpg9_QBigHjk6Z_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:08.439778+00:00"
---

# Tags for directing which groups the options are applied to

option_group
:   The options within this group are applied to the variants specified by the
    <applies_to> tag. Please see the following
    example:

    ```
    <options>
         <option_group>
             <applies_to>gcc,g++</applies_to>
             <compile_switch>-c</compile_switch>
             <preprocess_switch>-E</preprocess_switch>
         </option_group>
     </options>
    ```
