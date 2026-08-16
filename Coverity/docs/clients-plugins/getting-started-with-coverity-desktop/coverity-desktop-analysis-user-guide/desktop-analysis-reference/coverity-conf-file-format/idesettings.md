---
title: "IDESettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/idesettings.html"
content_id: "dyvNvp1Y1LTlZW8aKY7fPg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:33.513613+00:00"
---

# IDESettings

`IDESettings` are used by the Coverity Desktop Analysis plugins and
contain a few optional field settings that the user can configure. The following Desktop
Analysis IDE settings exist:

build_strategy?: string
:   When set to `CUSTOM`, the plugin will use the default custom build settings
    specified in `build_cmd`. If a build setting isn't specified
    while using the Desktop Analysis IDE, the plugin will use the IDE specified
    build commands.

    There is no default for this setting, so it must be set in a
    coverity.conf file or should be declared via
    command line.

path_mapping?: PathMapping
:   This setting allows you to specify strip and search paths for remote issues so that you can
    map them to local files.

For more information about where these settings exist in the IDE, see Coverity 2026.6.0 for Eclipse, Wind River Workbench, and QNX Momentics: User Guide.
