---
title: "Searching the Black Duck KnowledgeBase"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/searching-the-black-duck-knowledgebase.html"
content_id: "b9HoLhdgsJXhcV1KkvrTGA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:35.267021+00:00"
---

# Searching the Black Duck KnowledgeBase

You can search for component versions used in your BOMs and/or components in the Black Duck
KnowledgeBase (KB).

To search for components :

1. Click [image: Search icon] to open the Find page.
2. Select the **Black Duck KnowledgeBase** tab. Note that using the Black Duck KnowledgeBase tab to search for components will not
   display any custom components used in your projects. Use the Components tab to include these in your
   search results.
3. Type your search term in the Search field and/or optionally, select any filters to refine
   your search.
4. Optionally, for component searches, save
   this search, so that the results appear on the Dashboard page.

The Find page displays the components that meet your search criteria.

  
 [image: Black Duck KnowledgeBase Search Results]   

You can also type your search term in the Search field located at the top of the
application and press **Enter** or click [image: Search icon] . The Find page appears displaying the search results. Note that entering a
global search term initiates a new search and resets any filters you previously
selected. Select the **Components** or **Black Duck KnowledgeBase** tab and
filters to refine the results, as described below.

## KnowledgeBase filters

Use the following filters to narrow your results when searching Black Duck KnowledgeBase:

- **Primary Language**. Primary language in which the component is written. The filter
  displays the list of available languages in descending order of frequency of
  use in components.
- **Tags**. Available for all components that have tags applied to them to provide
  additional metadata about the component.
- **Commit Activity**. Represents the trending commit activity level for the open source
  component over time.

Note: Primary language, tags, and commit activity information is provided by [Black Duck Open
Hub](https://www.openhub.net/).

## Black Duck KB component search results

The following information is shown for each KnowledgeBase component that meets
your search criteria:

  
 [image: KB Search Results]   

- Select the component name to open the Black Duck KB *Component Name* page.
- View the number of project versions that use this component as shown by
  the value next to **Used By**.

    
   [image: Usage Text]   

  Select **Project Versions** to open the Where Used dialog box.

    
   [image: Where Used Dialog Box]   

  This dialog box lists the projects that use a version of this
  component.

  | Column | Description |
  | --- | --- |
  | Project | Name of the project and version that uses this component. Select the project name to display the project version's **Components** tab. |
  | Phase | Project Phase. |
  | Component Version | Version of this component used in this project version. |
  | Security Risk | Lists the vulnerabilities for each severity level, from left to right: Critical, High, Medium, and Low.   [image: Vulnerability Numbers]   Select a value to display the **Vulnerabilities** tab of Black Duck KB *Component Name Version* page, which lists the vulnerabilities associated with this version of the component. |
- For each component, the search results show:
  - Commit Activity.
  - Last commit date.
  - Total number of versions for this component.
- Select **Tags** to view the tags for this component.
- The URL in the upper right corner is the URL for this component.

## Exporting to CSV

You can export your search results to CSV which converts the individual rows to tabular data.
To do so, click the [image: Export CSV button] button and select CSV.
