---
title: "Complex type: componentDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-componentdataobj.html"
content_id: "TLtWQhoNaFJIu72QtspTOw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:24.801807+00:00"
---

# Complex type: componentDataObj

## Description

Component data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| roleAssignments | roleAssignmentDataObj | Set of roles assigned to a user or group for the specified component. |
| componentId | componentIdDataObj | Component to which the roles and/or subscribers apply. |
| subscribers | string | Set of usernames that subscribe to component notifications for this component map. Depends on proper usage of the notify() operation. |
