---
title: "Applying adjustments to all versions of a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/applying-adjustments-to-all-versions-of-a-project.html"
content_id: "vyFlP5Q2zY6NRdPtugFS5g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:32.681573+00:00"
---

# Applying adjustments to all versions of a project

You can select whether adjustments to a component apply to a specific version of a project or
if adjustments apply to all versions of a project.

## What is the Component Adjustments setting?

Component Adjustments in the Project settings ensures that adjustments made to components are
consistently applied across all versions of a project. However, it is important to
understand how this setting interacts with manually added components.

## Functionality of Component Adjustments

When you make adjustments to components that are shared across multiple project versions,
those adjustments will be applied to all versions where the component exists. This
means that if you mark a component as ignored in one project version, it will also
be ignored in all other versions of that project where the component is present.

If you enable Component Adjustments then adjustments apply to all existing versions
of a project, excluding archived
versions of projects and manually added components, and will also be
carried forward as additional scans are completed at the same code or Docker
image.

For example, if you edit a matched component to a different component, then all other
versions of the project that have that same matched component will have the match
adjusted and all versions going forward will also have this match adjusted.

## Manual Addition of Components

If a component is manually added to a specific project version, it does not automatically
create a corresponding entry in other project versions. Each project version needs
to have the component manually added if it is not already present. However, once a
component is added to multiple versions, any further adjustments will apply
universally to all instances of that component.

Note: There are instances when adjustments may not propagate to all versions. See Component Adjustment examples
below.

Component Adjustments are enabled by default when you create a
project.

CAUTION:

Please exercise caution when changing this option in order to avoid the Component Adjustment examples below. Projects created prior
to release 3.1.0 will have this feature disabled by default. See the examples described
below as those results will apply If you enable this feature to those projects.

When you edit a component (using the BOM or Source page), a [image: Information icon] appears in the table row to indicate that a manual adjustment was made to this
component:

  
 [image: BOM page showing an adjustment]   

Note: A [image: Information icon] appears on the BOM page for any edits that you make to a BOM.

There is also the option of cloning
project versions which enables you to baseline a project version.

## Component Adjustments examples

Component Adjustments may appear to work differently than expected depending on the status of
persistent edits and when the adjustments are made.

In the examples below, a project has several versions, none of which are
archived.

Table 1. Scenario 1

| Steps | Example | Final Result |
| --- | --- | --- |
| Component Adjustments are enabled. |  |  |
| An adjustment is made to an item in a component in one version of the project. | The license for Component A is changed in Version 1 of the project. | The adjustment is propagated to all versions of the project. |
| Component Adjustments are then disabled. |  |  |
| An adjustment is made to the *same item* in Component A in a version of the project. | The license for Component A is changed in Version 1 (or Version 2) of the project. | Although Component Adjustments are disabled, the edit is propagated to *all versions* of the project as the original adjustment was made when Component Adjustments were enabled. |

Table 2. Scenario 2

| Steps | Example | Final Result |
| --- | --- | --- |
| Component Adjustments are disabled. |  |  |
| An adjustment is made to an item in a component in one version of the project. | The license for Component A is changed in Version 1 of the project. | The adjustment appears in only Version 1 of the project. |
| Component Adjustments are then enabled. |  |  |
| An adjustment is made to the same item in the same component in the same version. | The license for Component A is changed again in Version 1 of the project. | The adjustment is applied to only that version of the project (Version 1 in our example). The adjustment does not propagate to other versions of the project as the original adjustment was made when Component Adjustments were disabled. |

Table 3. Scenario 3

| Steps | Example | Final Result |
| --- | --- | --- |
| Component Adjustments are disabled. |  |  |
| An adjustment is made to an item in a component in one version of the project. | The license for Component A is changed in Version 1 of the project. | The adjustment appears in only Version 1 of the project. |
| Component Adjustments are then enabled. |  |  |
| An adjustment is made to the same item in a component in a different version of the project. | The license for Component A is changed in Version 2 of the project. | The adjustment is propagated to all versions *except* Version 1. |

## Enabling or disabling Component Adjustments for a project

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the **Settings** tab.

     
    [image: Project page Settings tab]
4. Check or uncheck the **Component Adjustments** check box to enable or disable persistent
   edits. Archived project versions and manually added components are
   excluded.
5. Click **Save**.
