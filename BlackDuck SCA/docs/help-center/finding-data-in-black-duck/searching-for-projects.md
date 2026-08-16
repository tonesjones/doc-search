---
title: "Searching for projects"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/searching-for-projects.html"
content_id: "OnNyzs4WXSRzqmWPhwM9oA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:31.676554+00:00"
---

# Searching for projects

You can search for project versions that meet your search criteria.

To search for projects:

1. Click [image: Search icon] to open the Find page and select the **Projects** tab.
2. Type your search term in the Search field.
3. Optionally, select any filters, as described in the next section, "Using search filters".
4. Optionally, save this search, so
   that you can easily view them on your dashboard.

The Find page displays the project versions that meet your search criteria.

  
 [image: Project Search Results]   

You can also type your search term in the Search field located at the top of the
application and press **Enter** or click [image: Search icon] . The Find page appears displaying the search results. Note that entering a
global search term initiates a new search and resets any filters you previously
selected. Select the **Projects** tab and filters to refine the results, as described
below.

## About the search results

Search results show all project versions that meet your search criteria. The
following information is shown for each project version:

  
 [image: Project Version Search Information]   

- Use the bars to quickly view the number of components with the highest level
  of security, license, or operational risk.

  For example, the following shows that while there is a component with lower
  risk, the highest security risk for this project version is High and that
  four components in this project version have a high level of security risk
  as their highest risk level:

    
   [image: Security Risk Bar]
- Hover over the bar to see the number of components for each risk
  category.

    
   [image: Security Risk Popup - Project Version]   

  In this example, there is one component that has a high risk level as their
  highest risk. 10 components that have medium risk as their highest risk
  level, and six components that have low risk as their highest risk
  level.

  Note: Each component is only counted once and is shown with its highest risk severity
  level.
- Use the bar to see the number of components with the highest policy severity
  level for this project version.

  For example, the following shows that while there are components with lower
  severity levels, the highest policy severity level for this project version
  is Blocker and there is one component that has Blocker as its highest policy
  severity level.

    
   [image: Policy Violations Bar]   

  Note: The text shown states the number of components with the highest policy severity level for
  this project version, not all policy severity levels affecting this project
  version.
- Hover over the bar to see the number of components with policy violations by
  severity level:

    
   [image: Policy Violations Popup]
- View the number of results found and the time the database was last
  updated:

    
   [image: Search results time stamp]
- For each project version, the search results also show:
  - Number of components in this project version.
  - Last scan date.
  - When this project version was last updated.
  - License of this project version.
  - Phase for this project version.
  - Distribution of this project version.
- Select the project or version name to view the BOM.

## Using search filters

If your search query returns many projects, use filters to narrow your results.

Note that:

- Where necessary, click **+** to display the filter values; click **–**
  to hide them.
- If you select more than one type of filter, Black Duck displays items that
  match *all* values. If you select more than one value for a specific
  filter, Black Duck displays items that match either value.

  For example, if you use the License Risk filter and select high and medium,
  the search results display all projects that have high *or* medium
  license risk. if you select a high License Risk filter and a critical
  Security Risk filter, the search results display only those projects that
  meet have a high license risk *and* critical security risks.

Possible project filters are:

- Never Scanned. Select whether this project has never been scanned.
- Watching. Select whether this project is a watched project.
- Security Risk. Select one or more security risk levels.
- License Risk. Select one or more license risk levels.
- Operational Risk. Select one or more operational risk levels.
- Policy Rule. Select a policy rule from the list to find the projects that
  violate this policy.
- Policy Violations. Severity level of the policy rule.
- IaC Issues: Select from Open, Dismissed, or Not Reported.
- Last Scanned. Select a time period when this project was last scanned.
- Not Scanned Since. Select the time period since this project was last
  scanned.
- Project Group. Select one or more project groups.
- Release Phase. Select one or more release phases.
- Tags. Select one of more tags.

## Sorting the search results

Optionally, you can sort the results that appear on the page by selecting a value
from the **Sort by** list: [image: Sort option]

Note that if you sort the results and save this search, the Dashboard page displays
the saved search in the sorted order.

## Exporting to CSV

You can export your search results to CSV which converts the individual rows to tabular data.
To do so, click the [image: Export CSV button] button and select CSV.
