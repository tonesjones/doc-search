---
title: "Importing and exporting component maps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/importing-and-exporting-component-maps.html"
content_id: "Pxfi2NHFr_tev3AUgtJ6CA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:16.811986+00:00"
---

# Importing and exporting component maps

The Component Maps configuration screen also allows you to import
and export previously configured component maps.

UI Location: Configuration > Component Maps > Import/Export

Figure 1. Component map import/export
  
 [image: image]

Export
:   The Export feature creates a JSON file with all of the
    relevant information for the selected component map. This includes
    components, file rules, and default owners.

    The downloaded file can then be edited and imported back into Coverity
    Connect.

    See Exported component map JSON elements for details on the
    exported JSON elements.

Import
:   The Import feature accepts a component map JSON file,
    and uses it to overwrite the components, file rules, and default owners for
    the selected component map. Exported component map JSON elements contains information on
    the various component map JSON elements.

    There are several important considerations for formatting the import file:

    - The format of the import file should match the exported JSON.
      Aside from required elements, missing fields will be considered
      empty, and will be deleted if they existed prior to the import.
      The only exceptions to this are the
      `defaultOwners` and
      `rbacSettings` fields. An empty
      `defaultOwners` or
      `rbacSettings` field will simply be
      ignored.

      If you want to delete `defaultOwners` or
      `rbacSettings` through import, set their
      value to `null`.
    - The imported JSON must contain exactly one component with the
      name "`Other`".
    - Import can not be used to create component maps. If you want to
      import into a new component map, you need to create a new
      component map by clicking Add, and then
      import the component map data.
    - If a component's `name` is changed in the JSON,
      any file rules (`fileRules`) that refer to that
      component must also use the new component name (via the
      `componentName` field).
