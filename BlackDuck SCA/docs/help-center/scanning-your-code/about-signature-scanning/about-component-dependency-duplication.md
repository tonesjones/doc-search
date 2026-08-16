---
title: "About component dependency duplication"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-component-dependency-duplication.html"
content_id: "NzUV_ieQUKUsGZFc7OCoiQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:43.811922+00:00"
---

# About component dependency duplication

When scanning a project, several different types of matching processes can happen. The
signature match looks at the structure of directories and files and try to match the
“signatures” to what’s stored in the KnowledgeBase. The snippet match looks at code
snippets and looks for matches in what’s stored in the KnowledgeBase. The package
manager match uses external tools to examine build configuration files to find declared
dependencies and then find matching components in the KB.

After scan, match and BOM computation are completed, the Components tab will display all
the components detected with the above matching processes. The Match Type column will
display “Transitive Dependency” or “Direct Dependency” alone or together with other
types. These components are detected by the package manager matching process. The Source
column may show multiple matches representing the number of different paths in the
dependency tree.

## Viewing component dependency duplication

Clicking the matches link in the Sources column will direct you to the Source tab.
This view has a left pane that shows the dependency tree (in addition to source code
tree for signature match), and a right pane that shows components (possibly
filtered) under a tree node.

With default settings, all duplicate matches of a particular component will be
agglomerated into a single entry. This means that if a project has multiple paths
that lead to a specific component, only one entry will be displayed in the
right-hand pane of the Source tab.

## Changing how duplicate dependencies are displayed

Users with the system administrator role can define the depth of displayed component
duplication where 1 is no duplication and 10 will display all components up to a
maximum 10 levels of relation. Please note that setting this level too high will
result in reduced product performance. The default level is 1.

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Click **Scan**.
5. Under **Component Dependency Duplication Sensitivity**, enter an integer
   (1 to 10) for the number of levels to display more component dependency
   entries.
6. Click **Save**. To indicate that the default value has changed, the button
   changes to **Saved**.

## Maximum limit for component matches

Black Duck uses a system property to control the maximum number of nodes (matches)
per component added to resulting dependency tree in package manager scan:

```
blackduck.match.limit.per.component
```

This system property needs to be set for match engine container, therefore the
following must be added to the `MATCHENGINE_SERVICE_OPTS` environment
variable:

```
 -Dblackduck.match.limit.per.component=<value>
```

The default value of this system property is 10, thus the number of duplicated
components in the tree can not exceed the
`blackduck.match.limit.per.component` value (match limit per
component). The allowable range of values for this property is 1 to 100 inclusively.
If the setting falls outside of that range, it will automatically be set to default
value (with corresponding warning in the log).

Component Dependency Duplication Sensitivity still applies: match limit per component
restricts number of duplicates above Component Dependency Duplication Sensitivity
level, but if the node level is below Component Dependency Duplication Sensitivity,
the match is dropped regardless (under condition that it is already added to the
tree). In other words, `blackduck.match.limit.per.component` sets
maximum number of duplicates that can be added to the dependency tree above
Component Dependency Duplication Sensitivity level (below that level, duplicates are
dropped).

For example, say a component comes as transitive dependency from many other
components, so that there are 100 of these components in the dependency tree.

Black Duck parameters are set to:

- `blackduck.match.limit.per.component = 10`, and;

- Component Dependency Duplication Sensitivity = 5.

In this case, if there are 20 of said components on the level above 5, component
dependency tree will have 10 of these components.

If there are 7 components on the level above 5, resulting tree will have 7 components
(since remaining 93 components below level 5 will be dropped even when match limit
per component is not reached).
