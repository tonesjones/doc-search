---
title: "Complex type: projectDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-projectdataobj.html"
content_id: "fCI5N3eGsEx9KX8nP6P2eQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:44.062773+00:00"
---

# Complex type: projectDataObj

## Description

Returns project data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| streams | streamDataObj | Name of a stream that is associated with the project. |
| streamLinks | streamDataObj | Name of a stream link that is associated with the project. |
| roleAssignments | roleAssignmentDataObj | Role of a user or group that is associated with the project. |
| dateCreated | dateTime | Date and time that the project was created in the database. |
| dateModified | dateTime | Date and time that the project was last modified. Can be the creation date and time. |
| description | string | Description of the project. |
| id | projectIdDataObj | Identifier for the project. |
| projectKey | long | Unique numeric identifier for the project. |
| userCreated | string | Name of the user who created the project. |
| userModified | string | Name of the user who last updated the project. |
