---
title: "Searching for components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/searching-for-components.html"
content_id: "GO2kVMCBrl63EjBYeh7rww"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:32.848776+00:00"
---

# Searching for components

You can search for component versions used in your BOMs.

To search for components :

1. Click [image: Search icon] to open the **Find** page.
2. Select the **Components** tab to find component versions used in your projects.
3. Type your search term in the Search field and/or optionally, select any filters, as described
   in the next section, "Using search filters".
4. Optionally, for component searches, save
   this search, so that the results appear on the Dashboard page.

The Find page displays the components that meet your search criteria.

  
 [image: Black Duck KnowledgeBase Search Results]   

You can also type your search term in the Search field located at the top of the application
and press **Enter** or click [image: Search icon] . The Find page appears displaying the search results. Note that entering a
global search term initiates a new search and resets any filters you previously
selected.

## Using search filters

Filters that appear depend on whether you are searching for components used in your
BOMs or searching Black Duck KnowledgeBase.

For each filter:

- Where necessary, click [image: image] to display the filter values; click [image: image] to hide them.
- If you select more than one type of filter, Black Duck displays items that
  match *all* values. If you select more than one value for a specific
  filter, Black Duck displays items that match either value.

  For example, if you use the License Risk filter and select high and medium,
  the search results display all components that have high *or* medium
  license risk. if you select a high License Risk filter and a critical
  Security Risk filter, the search results display only those projects that
  meet have a high license risk *and* critical security risks.

## Component filters

Use the following filters to narrow your results when searching components used in
your BOM:

- **Component Intelligence**. Check to display all components containing suspicious events
  or incidents where it is highly likely that malware or malicious code has
  been identified. See Operational Risk for more information on Component
  Intelligence.
- **Security Risk**. Select one or more security risk levels.
- **License Risk**. Select one or more license risk levels.
- **Operational Risk**. Select one or more operational risk levels.
- **First Detected**. Date when the component was first detected by Black Duck (such as by scanning, being manually added
  to a BOM, and so on).
- **License**. Select a license from the list.
- **License Family**. Select a license family from the list.
- **Missing Custom Field Data**. Select to view the components and/or component versions
  which have required custom fields and are missing data.
- **Released**. Date when the component was released according to the Black Duck KnowledgeBase.

## Components search results

The following information is shown for each component in your BOM that meets your
search criteria.

  
 [image: Search Results - Component]   

- Select the component name/version to display the *Component Name Version* page.
- View the number of Active and LTS project versions that use this component version as shown
  by the value next to **Used in Projects**.

    
   [image: Used By Text]   

  Select **Active** or **LTS** to open the **Used in** dialog box.

    
   [image: Used in Dialog Box]   

  This dialog box now displays the project versions that utilize this version of the
  component, including those in Long-Term Support (LTS) projects.

  | Column | Description |
  | --- | --- |
  | Project Name | Name of the project and version that uses this component version. Select the project name to display the project version's **Components** tab. |
  | License | License for this component version. |
  | Vulnerabilities | Lists the vulnerabilities for each severity level, from left to right: Critical, High, Medium, and Low.   [image: Vulnerability Numbers]   Select a value to access the Vulnerabilities tab on the *Component Version* page. This tab provides a detailed list of vulnerabilities linked to the specific version of the component. |
- Use the bar to quickly see the number of components with the highest
  policy severity level.

    
   [image: Policy Violation Bar Graph]   

  Select the bar to see the number of components with policy violations by
  severity level:

    
   [image: Policy Violations by Component]   

  Note: A component is only counted once with the highest policy severity level, not all policy
  severity levels affecting this component.
- Use the bar to quickly view the number of components with the highest
  level of license risk.

    
   [image: License Risk Bar Graph]   

  Select the bar to view the number of components in each risk
  category.

    
   [image: License Risk Popup]
- View the operational risk for this component version:

    
   [image: Operational Risk]
- View the number of vulnerabilities by severity associated with this component version.

    
   [image: Security Risk]
- Additional information relevant to the vulnerability:

    
   [image: image]   
  - **First Detected**. The specific date when a vulnerability was initially identified in
    a component within your project. This timestamp indicates when Black
    Duck SCA first associated the vulnerability with the component
    version during a scan or Knowledge Base (KB) update.
  - **Release Date**. The date when a vulnerability was officially disclosed or published
    by its source, such as the National Vulnerability Database (NVD) or
    a Black Duck Security Advisory (BDSA). This date marks when the
    vulnerability became publicly known and available for organizations
    to assess and address.
  - **Newer Versions**. The number of newer releases of a component or library that may
    address known vulnerabilities, improve functionality, or enhance
    performance.
  - **Last Vuln**: The most recent date when a vulnerability was added to the list of
    vulnerabilities associated with a specific component version.
- View the number of results found and the time the database was last updated:

    
   [image: Search results time stamp]   

  **Sorting the search results**

  Optionally, you can sort the results that appear on the page by selecting a value
  from the **Sort by** list: [image: Sort option]

  Note that if you sort the results and save this search, the Dashboard page
  displays the saved search in the sorted order.

Notice: Ignored components are excluded from the **Find** → **Component** page,
meaning they will not be counted in the component totals displayed there.

## Exporting to CSV

You can export your search results to CSV which converts the individual rows to tabular data.
To do so, click the [image: Export CSV button] button and select CSV.
