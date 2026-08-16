---
title: "Understanding the component information available from the Black Duck KB"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-the-component-information-available-from-the-black-duck-kb.html"
content_id: "zVC7Uf04oUe_J4KHeASxCw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:16.258637+00:00"
---

# Understanding the component information available from the Black Duck KB

The Black Duck KB
*Component Name* page displays information about the open source software (OSS)
component.

  
 [image: KB Component Name page]   

This page is comprised of two tabs: an **Overview** tab and a **Settings** tab.

## About the Overview tab

The **Overview** tab displays information such as a status, description, component
links, and tags, and information about each of the component versions that are
available in Black Duck KB.

A graph at the top of the page shows a history of high, medium, and low
vulnerabilities for each version of this component. Use this graph to quickly view
vulnerability information for component versions.

- Select **Previous** or **Next** to view older or newer versions.
- Hover over a data point in the graph to view the version, release date, and
  number of vulnerabilities for this version:

    
   [image: Vulnerability hover information]   

  To view information on versions that interest you, use the filter, located
  above the table, to filter the versions shown in the vulnerability graph and
  in the table below.

The following information is available for each version:

| Column | Description |
| --- | --- |
| Version | Release number of this version of the component.  Select the version number to display the *Component Name > Version* page. |
| Used Count | Number of project version BOMs in which this version of the OSS project is used.  Tip: Select the number to go to the **Overview** tab for this version of the OSS component. That tab lists each project and project version in which this version of the OSS component is used. |
| License | Declared license of this version of the OSS component. Other license types include:   - "Unknown" indicates that the OSS component version's   license is not known. - "License Not Found" indicates that although researched by   Black Duck, no declared license was found for the   component. - "No License" indicates that Black Duck has found a   declaration of 'No License' for the component.   For known licenses, select the license name to view license details and license text. |
| Released | The date this version of the OSS component was released. |
| Security Risk | A graph which shows the number of high risk, medium risk, low risk, and unknown vulnerabilities associated with this version of the OSS component. |

## About the Settings tab

The **Settings** tab shows details on this component. Information shown here
appears on the **Overview** tab.

  
 [image: Settings tab]   

Users with the Component Manager role
can use the **Settings** tab to edit the description, URL, notes, and status for
this KB component. Click here for information on editing component information and here for information on
modifying a component's status.

Users with the System Administrator role can use the **Settings** tab to edit the
component custom field
information. as shown in the **Additional Fields** section.
