---
title: "Operation: createComponentMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-createcomponentmap.html"
content_id: "mLA8kdzCDl~5roy3NtzWjg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:24.700782+00:00"
---

# Operation: createComponentMap

## Name

createComponentMap

## Description

Create a component map with or without one or more components.

## Parameters

componentMapSpec
:   **Type:** 
    componentMapSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | componentMapName | string | Required. Name of the component map. |
    | componentPathRules | componentPathRuleDataObj | Pattern matching a path to set of files to associate with a component for the component map. Multiple component map rules allowed. |
    | components | componentDataObj | Specification of the component that you are associating with the componentmap. Multiple component associations allowed. When *updating* (not creating) components, youmust specify the complete list of your components, including the "Other" component becauseany component in the component map that does not appear in the update list willbe deleted. Alternatively, you can pass **null** to retain all existingcomponents during an update. |
    | defectRules | componentDefectRuleDataObj | Default owner of the specified component. Each component can have an owner. |
    | description | string | Description of the component map. |
    | forceDeleteComponents | boolean | When set to `true`, components that do not appear in the update list and are chosen to be included in hierarchies will be deleted and removed from the hierarchies. When set to `false`, components that do not appear in the update list and are chosen to be included in hierarchies will *not* be deleted. In the latter case, an error message is returned. |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the component map at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations are allowed. If updating role assignments, respecify any that you want to retain. |
