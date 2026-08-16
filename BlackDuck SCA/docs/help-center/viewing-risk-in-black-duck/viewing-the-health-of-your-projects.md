---
title: "Viewing the health of your projects"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-the-health-of-your-projects.html"
content_id: "COf0GtPFqw3RhFmHAiLZmA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:16.482169+00:00"
---

# Viewing the health of your projects

Use the **Summary** tab to view the overall health of your projects and identify areas
of concern. The page consists of widgets that provide business critical information
which you can use to quickly assess areas where you need to focus your attention.

  
 [image: Summary Dashboard]   

Note: The **Summary** tab only displays information for the projects you have permission
to view.

The following describes each widget shown on the **Summary** tab and, where available,
how to view additional information. Note that the security risk values shown use CVSS
v3.x or CVSS v4.x scores, depending on which security risk
calculation you selected; by default CVSS v3.x scores are shown.

## Top Policy Violations

  
 [image: Top Policy Violations widget]   

The **Top Policy Violations** widget displays up to the top five policy violations
across all projects that you have permission to view.

Policy rules are listed by severity level and then by the number of policy
violations, in descending order. If policy rules do not have severity levels
assigned to them, the widget displays the top five policy violations, in descending
order by the number of violations.

- If you do not have the Policy Management module, this widget will not appear
  on the page.
- A message appears if you have the Policy Management module but do not have
  any policy rules configured or have any policy violations.

Select a policy rule to view the My Projects tab filtered to display the projects
with a version that violates that policy rule.

## Project Security Risk

  
 [image: Project Security Risk]   

The **Project Security Risk** widget displays the number of
projects you have permission to view for each level of security
risk.

Note that this widget counts the highest security risk level for a
project, not all security levels affecting a project. For example,
if a project has medium and low security risks, it is counted as a
project with medium security risk; it is not included as a project
with low security risks.

Select a value to view the **My Projects** tab filtered to
display the projects that have that security risk level as the highest security
risk.

Hover over the graph to view the number of projects with that level of security
risk.

## Component Security Risk

  
 [image: Component Security Risk]   

The **Component Security Risk** widget displays the number of
components in projects you have permission to view for each security
risk level.

Note that the widget counts only the highest security risk for a
component. For example, if a component has medium and low security
risks, it is counted as one component with a medium security
risk.

Hover over the graph to view the number of components with that level
of security risk.

## Top Components

  
 [image: Top Components]   

The **Top Components with Security Risk** widget displays up to
the top five components used in the projects you have permission to
view. The information shown for each component is:

- Component name and number of versions used in your projects.
  If only one version is used, the specific version is listed
  here.
- Number of your projects that have this component.
- Number of security risks in this component, with the highest
  security risk listed here.

Components are organized by security risk, with those components with
the highest risk listed first.

Select the specific version or number of versions to view the Component Version Details page.

## Projects with critical/high vulnerabilities

  
 [image: Projects with critical/high vulnerabilities]   

The **Projects have a critical/high vulnerability** widget displays the number of
projects with versions that contain components with a critical and/or high security
risk.

## New vulnerable components this week

The **New vulnerable components this week** widget displays the number of
components the Black Duck KB mapped a vulnerability to in the past seven
days, including today.

## New projects created this week

  
 [image: New projects created this week widget]   

The **New projects created this week** widget displays the number
of projects that you have permission to view that have been created
in the past seven days, including today.

## Projects scanned this week

  
 [image: Projects scanned this week widget]   

The **Projects scanned this week** widget displays the number of
projects with scans from the past seven days, including today.

## Project Policy Violations by Tier

  
 [image: Project Policy Violations by Tier widget]   

The **Project Policy Violations by Tier** widget displays the
total number of projects by phase that have a policy violation,
grouped by tiers.

- If you do not use tiers for your projects, projects are
  grouped in a single category called **Unknown**.
- If you do not have the Policy Management module, this widget
  displays **Projects by Tier**.

For each tier, hover over a bar to see the number of projects in this
phase and the number of projects in this phase with a policy
violation.

## Statistics

  
 [image: Statistics widget]   

The **Statistics** widget displays the following information:

- **Projects** lists the number of your projects.
- **Versions** lists the number of project versions for your
  projects.
- **Vulnerabilities** lists the number of vulnerabilities in
  your projects.
- **Components** lists the number of components used in your
  projects, *including* ignored components.
- **Scanned Code** lists the number of GBs scanned for all
  scans.
