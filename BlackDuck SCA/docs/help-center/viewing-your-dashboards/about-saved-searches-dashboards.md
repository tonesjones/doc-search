---
title: "About saved searches dashboards"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-saved-searches-dashboards.html"
content_id: "pIzykCGGiJ1NS8GpxIH0gQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:12.476357+00:00"
---

# About saved searches dashboards

Use a saved search to view the project
versions, component versions,
and vulnerabilities that are important to
you.

For each saved search, Black Duck lists the date and time this
search was last updated.

  
 [image: Saved Search Summary]   

Select **Saved Search Settings** to view the filters for this saved search.

  
 [image: Saved Search Settings]   

Select **Edit Saved Search** to open the Find page displaying your saved search. Use
the page to edit and save this revised saved search.

## Project version saved searches

  
 [image: Dashboard Saved Project Search]   

The following information is shown for each project version:

  
 [image: Project Dashboard]   

- [image: Project Saved Search Icon] located in front of the saved search name indicates that this is a
  project saved search.
- To view policy violation information for a specific project version:
  - Use the bar to see the number of components with the highest policy
    severity level for this project version.

    For example, the
    following shows that while there are components with lower severity
    levels, the highest policy severity level for this project version
    is Blocker and there are five components that have Blocker as their
    highest policy severity level.

      
     [image: Policy Violations Bar Graph]   

    Note: The text states the number of components with the highest
    policy severity level for this project version, not all policy
    severity levels affecting this project version.
  - Hover over the bar to see the number of components with policy
    violations by the highest policy severity level:

      
     [image: Policy Violations Popup]   

    If a component has a policy violation, the component is only
    counted once and only its highest policy severity level is
    shown.

- To view risk information:

  - Use the risk bars to quickly view the number of components with the
    highest level of security, license, or operational risk.

    Security risk:

      
     [image: Security Risk Bar]   

    License risk:

      
     [image: License Risk Bar]   

    Operational risk:

      
     [image: Operational Risk Bar]   

    For example, the following shows that while there are components with
    lower risk, the highest security risk for this project version is
    High and that one component in this project version has a high level
    of security risk as their highest risk level:

      
     [image: Security Risk Bar]
  - Hover over the bar to see the number of components for each risk
    category.

      
     [image: Security Risk Popup - Project Version]   

    In this example, there is one component that has a high risk level as
    its highest risk, 10 components that have medium risk as their
    highest risk level, and six components that have low risk as their
    highest risk level.

    Note: Each component is only counted once and is shown with its highest
    risk level.
- Use the graphs to view overview information for all project versions in this
  dashboard categorized by policy severity and risk levels. The graphs lists
  the percentages for each level. You can also:

  - Hover over the graph to view the percentage of project versions with
    policy violations for each policy severity level.

      
     [image: Policy Violation Graph]
  - Hover over the graph to view the percentage of project versions in
    this dashboard for each risk level.

      
     [image: Security Risk Graph]
  - Hover over a value in the legend to highlight the value in the
    graph.
- For each project version, the dashboard also shows:
  - Number of components in this project version.
  - Last scan date.
  - Date when this project version was last updated, such as when a scan
    that was mapped to this project version was last run or when the BOM
    for this project version was last updated, either manually or by a
    new scan.
  - License of this project version.
  - Phase for this project version.
  - Distribution of this project version.
- Select the project or version name to view the BOM.
- Manage how the projects are shown in these dashboards:
  - Use the **Sort by** field to select an attribute to sort by and
    click an arrow to select the sort order [image: Ascending sort icon] (ascending) or [image: Descending sort icon] (descending).
  - Use the **Filter projects** field to filter the projects shown in
    the dashboard.

## Component saved searches

  
 [image: Saved Component Search Dashboard]   

The following information is shown for each component.

  
 [image: Search Results - Component]   

- [image: Component Saved Search Icon] located in front of the saved search name indicates that this
  is a component saved search.
- Select the component name/version to display the *Component Name Version* page.
- View the number of project versions that use this component version as
  shown by the value next to **Used By**.

    
   [image: Usage Text]   

  Select **Project Versions** to open the Where Used dialog box.

    
   [image: Where Used Dialog Box]   

  This dialog box shows the project versions that use this version of the
  component.

  | Column | Description |
  | --- | --- |
  | Project Name | Name of project and version that uses this component version. Select the project name to display the project version's **Components** tab. |
  | Phase | Project Phase. |
  | License | License for this component version. |
  | Review Status | Whether this component has been reviewed in this project version. |
  | Security Risk | Lists the vulnerabilities for each severity level, from left to right: Critical, High, Medium, and Low.   [image: Vulnerability Numbers]   Select a value to display the **Security** tab of the Black Duck KB*Component Name Version* page, which lists the vulnerabilities associated with this version of this component. |
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
- View the number of vulnerabilities by severity associated with this
  component version for each severity level, from left to right: Critical,
  High, Medium, and Low.

  The **Last Vuln** date is the date when a vulnerability for this
  component was last updated in Black Duck (by the Black Duck
  KnowledgeBase or a user).

    
   [image: Security Risk]   

  Select a value to display the **Security** tab of the Black Duck KB*Component Name Version* page, which
  lists the vulnerabilities associated with this version of this
  component.

    
   [image: Component Name Vsn Security Tab]
- For each component version, the search results also show:
  - Approval status. Status indicates whether this component version
    has been reviewed.
  - First detected date.
  - Date this component version was released.
  - Number of newer versions.
  - Date when a vulnerability for the component was last updated in
    Black Duck (by updates from Black Duck KnowledgeBase or a user
    manually changing the associated vulnerability and so
    on).
- Manage how the components are shown in these dashboards:

  - Use the **Sort by** field to select an attribute to sort by
    and click an arrow to select the sort order [image: Ascending sort icon] (ascending) or [image: Descending sort icon] (descending).
  - Use the filter field to filter the components shown in the
    dashboard.

## Vulnerability saved searches

  
 [image: Vulnerability Saved Search]   

The following information is shown for each vulnerability:

  
 [image: Vulnerability search results]   

- Select the vulnerability ID to view more information about the vulnerability,
  such as additional score values. You can view National Vulnerability
  Database (NVD) information by selecting the CVE number or view Black Duck Security Advisory (BDSA) information by
  selecting the BDSA
  number.
- View the number of project versions that affected by this vulnerability next
  to **Used By**.

    
   [image: Usage Text]   

  Select **Project Versions** to open the **Affected Projects** tab for
  the vulnerability which lists the project versions affected by this
  vulnerability.

    
   [image: Affected projects]
- View the overall risk score. The search results show the Temporal Score for
  BDSA vulnerabilities, or the Base Score for NVD vulnerabilities and the
  associated risk level. Note that the score shown and risk level depends on
  the selected security rankings.

  Select the score to view individual scores: temporal, base, exploitability,
  and impact for BDSA; base, exploitability, and impact for NVD.
- View whether a solution, workaround, or exploit is available:
  - [image: image] indicates
    that there is a solution or workaround available for this
    vulnerability.
  - [image: Exploit icon] indicates there is an exploit for this
    vulnerability.
- For each vulnerability, the search results also show:
  - First Detected.
  - Published date.
  - Last modified date.
  - Common Weakness Enumeration (CWE) number for this security
    vulnerability.
