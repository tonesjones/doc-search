---
title: "Operation: updateProject"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updateproject.html"
content_id: "6xQIp5Z2xZUi0O_96h6UOg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:12.818369+00:00"
---

# Operation: updateProject

## Name

updateProject

## Description

Update a project specification.

## Parameters

projectId
:   **Type:** 
    projectIdDataObj

    Passes the identifier for a project.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the project. |

projectSpec
:   **Type:** 
    projectSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | streams | streamIdDataObj | Name of an existing stream to associate with the project. When updating a project, you must list all of the streams that you want to retain except for streams with the __internal prefix to their name, such as Dynamic Analysis streams. You might see such internal streams listed when you call getProjects(). Zero or more stream name associations allowed. See the remark for additional details. |
    | streamLinks | streamIdDataObj | Name of a new or existing stream link to associate with the project. (Note that a stream link and the stream to which it links must belong to separate projects.) Zero or more stream link name associations allowed. |
    | description | string | Description of the project. |
    | name | string | Name for the project. Required when using createProject(). |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the project. See getAllRoles(), getRole(), and getAllPermissions(). By default, the username of the project creator is assigned the *projectOwner* role for the new stream. If updating role assignments, respecify any that you want to retain. Zero or more role associations allowed. |

## Remarks

The streams and streamLinks fields must include the complete list of streams or
stream links. Any stream or stream link that appears in the project but does not
appear in the corresponding projectSpecDataObj list will be deleted from the
project.
