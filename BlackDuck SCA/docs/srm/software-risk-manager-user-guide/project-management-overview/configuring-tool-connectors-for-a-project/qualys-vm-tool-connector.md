---
title: "Qualys VM Tool Connector"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/qualys-vm-tool-connector.html"
content_id: "U613YqANIPDWe13B0P3OFg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:11.735443+00:00"
content_hash: "c6cecc04060a8b810dad345f301f22862b6f588f0e581983295f6c5f2d968cd9"
---

# Qualys VM Tool Connector

Note: This section is only applicable to Software Risk Manager users with the
InfraSec add-on.

The Qualys VM connector has two unique form configurations to choose from. The default
form configuration has customization options including severity types, *Asset Group
Titles*, *IP Ranges*, and *Include findings last seen* field.
*Include findings last seen* is a required field and determines how far back to
consider vulnerabilities that will be pulled into Software Risk Manager. *Asset Group
Titles* and *IP Ranges* are optional fields and act as filters. For example,
if you provide an IP range, only that information will be pulled into Software Risk
Manager. Additionally, if both fields are left blank, all vulnerability information in
Qualys will be pulled into Software Risk Manager. Multiple IPs can be specified by
separating them with a comma, and IP ranges can be specified by separating them with a
hyphen.

To access the second form configuration, select the *Import data using a Report
Template* option. This form will present you with a *Report Template*
dropdown and *Check on report every* field. Both fields are required for this
configuration. The *Check on report every* field determines how often Software Risk
Manager will interface with Qualys to get the status of the report being analyzed. The
*Report Template* dropdown is populated with report templates that have been
configured for your Qualys VM subscription. Software Risk Manager will request that
Qualys generate a report using the selected report template; once the report has been
generated, it will be imported into Software Risk Manager.

[image: image]
