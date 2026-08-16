---
title: "Reference structure in XML format"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reference-structure-in-xml-format.html"
content_id: "P2uKoJ_U5DVeEt25g9KiCA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:43.281793+00:00"
---

# Reference structure in XML format

The reference structure is stored in XML format in the reference-structure file together with
its data type definition (dtd). Reference is made to the XSL-stylesheet file
_fck_tree.xsl which must be in the working directory. With a
suitable browser you can browse through the reference structure. Suitable browsers are
the one integrated in the Coverity Fortran Syntax Analysis IDE, Mozilla Firefox,
Microsoft Internet Explorer, Opera and Apple Safari. You can also transform the XML file
to an HTML file using an XSLT processor. The HTML file can then be explored using your
internet browser. Because the data are stored in xml format you also can write your own
programs to analyse and visualize the reference structure.
