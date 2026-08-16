---
title: "Analysis Configurations... dialog"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-configurations...-dialog.html"
content_id: "5DPktm8FRuhOULzdL~HhWw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:39.983401+00:00"
---

# Analysis Configurations... dialog

Analysis options and Coverity Connect server information are provided to
Coverity Desktop through grouped settings known as analysis
configurations. Upon installation of the plug-in, you will have a default analysis
configuration in place, which requires some additional settings and connection
information to be used for analysis. You may also choose to create additional
configurations, to toggle between different options or streams from analysis to
analysis.

The Analysis Configurations Dialog, accessible via the Coverity Desktop
toolbar or Coverity > Analysis Configurations... menu item, allows you to create and edit analysis configurations for Coverity Desktop. To create a new configuration, select New
Configuration from the Active Configuration
drop-down, choose a name for the configuration, and then fill out the appropriate
information in each of the dialog's subsequent tabs. Optionally, when creating a new
configuration, you can copy the settings from an existing configuration (if any) and
then edit them in place. The following sections contain details for each of the
configuration tabs.

Note: To edit an existing configuration, select its name from the Active
Configuration drop-down, and update the information in the configuration
tabs accordingly.

Additionally, the Edit Configurations option
(in the Active Configuration drop-down) allows you to rename
or remove any existing analysis configurations.

## Resetting individual fields/values

Many of the fields in the Analysis Configurations dialog are
accompanied by a small grey (or black) "reset box". When you hover over these boxes,
they will display how the value was configured (either locally configured, inherited
from a coverity.conf  configuration file, or the Coverity Desktop default value). If the box is black, this means
that the value has been set locally. To reset to the original value, click on the
box and select Reset. This will use the value specified by
the coverity.conf file, if one exists, or reset to the Coverity Desktop default.

See the Coverity
Desktop Analysis
2026.6.0 User Guide for more information on
coverity.conf.
