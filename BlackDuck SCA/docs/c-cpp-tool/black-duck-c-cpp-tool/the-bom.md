---
title: "The BOM"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/the-bom.html"
content_id: "D7LtuVm19vILSkpbazvpYw"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:58.246511+00:00"
---

# The BOM

**Direct Dependencies**: These are files which are being linked in to the built
executable directly or header files included by source code as identified by Coverity
Build Capture.

**Package Manager**: The Package Manager of the Linux system is queried about the
source of the files - if recognized, these are added to the BOM as "Direct
Dependencies".

**Transitive Dependencies**: These are files which are needed by the Direct
Dependencies.

**LDD**: LDD is used to List the files (Dynamic Dependencies) of the Direct
Dependencies. These files are then used to query the package manager and results are
added to the BOM as "Transitive Dependencies".

**Binary Matches BDBA**: Any linked object files not identified by the package manager
are sent to BDBA (Binary) for matching.

**Signature Matches**: Any linked object and header files not identified by the
package manager as well as all source code identified by Coverity Build Capture are then
sent to the Knowledge Base for signature matching.
