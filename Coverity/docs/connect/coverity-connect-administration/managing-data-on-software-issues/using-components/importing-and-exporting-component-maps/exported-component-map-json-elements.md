---
title: "Exported component map JSON elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exported-component-map-json-elements.html"
content_id: "7nhagv8gyH8Hp4a4VM~evw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:17.420148+00:00"
---

# Exported component map JSON elements

The following table lists and describes the elements contained in the JSON file that is
produced when you use the Export button in the Component Maps
menu.

Table 1. Exported component map JSON elements

| Element | Description |
| --- | --- |
| `version` | Specifies the version of the component map JSON format. This may be excluded, but if present, the value must be 1. |
| `name` | The name of the component map. This is a required element. |
| `description` | Optional description of the component map. |
| `components` | Contains each of the components within the component map. Each component object contains the following child elements: `name, description, defaultOwner,` and `rbacSettings`. |
| `name` | The name of the component. This is a required element. No duplicate names are allowed in the JSON file. |
| `defaultOwner` | The username of the default owner in the format `username@ldap` (or just `username` if `ldap` is null). |
| `rbacSettings` | Contains desired RBAC settings for the component map. This element is optional for import. If it is missing, the existing RBAC settings will be unchanged. The rbacSettings element contains the following child elements: `groupOrUser, principalName,` and `roles`. |
| `groupOrUser` | Specifies whether the RBAC settings apply to a group or a single user. This element is required (if `rbacSettings` is present) with a value of "`group`" or "`user`". |
| `principalName` | Specifies the group or username the RBAC settings apply to. This is a required element if `rbacSettings` is present. |
| `roles` | A list of role names that apply to the group or user specified by `principalName`. This is a required element (if `rbacSettings` is present), and must contain a non-empty list of role names. |
| `fileRules` | Contains each of the file rules within the component map. Each file rule object contains the `componentName` and `pathPattern` child elements. This element may be excluded, which will be interpreted as a request to delete all existing file rules. |
| `componentName` | Component name that exists in this JSON file. This component will be mapped to all files that match the sibling `pathPattern` element. This is a required element if `fileRules` is present. |
| `pathPattern` | A valid regex pattern. Any files matching the pattern will be mapped to the component specified by the sibling `componentName` element. This is a required element if `fileRules` is present. |
