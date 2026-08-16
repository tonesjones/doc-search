---
title: "Importing/exporting a Coverity Policy Manager hierarchy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/importing/exporting-a-coverity-policy-manager-hierarchy.html"
content_id: "rWIKAizyd4goE7VLg6wj4g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:04.397212+00:00"
---

# Importing/exporting a Coverity Policy Manager hierarchy

You can import and export one or more hierarchy files through the
Configuration - Hierarchies window in Coverity Policy Manager
(see Hierarchy
Buttons). These editable JSON files specify the name, description, and node
tree for the hierarchy.

Use Case
:   To expedite the specification of a hierarchy with many nodes, you might
    export an existing hierarchy to a file so that you can edit it manually
    (instead of using the UI for this purpose) and then import the edited
    version of the file to Coverity Policy Manager.

    To see working examples of a hierarchy configuration in the file, you might
    want to to create a small, representative portion of the hierarchy through
    the Coverity Policy Manager UI before exporting it. For details, see Creating a hierarchy.

Hierarchy Objects
use the following schema notation (not JSON):

- Braces and Brackets (examples: `{ }`, `[ ]`): These
  characters are verbatim.
- Italics (example: *`hierarchy`*): Items in italics represent objects defined elsewhere in the
  schema.
- Ellipsis (example: `thing...`): An item followed by an ellipsis
  represents zero or more repetitions of the item, separated by commas.
- Colon after word (example: `foo:`): A word followed by a colon
  represents that word in double quotes.
- Quotes (example: `"leaf"`): A string in quotes represents
  itself.
- `string`: This token represents a UTF-8 string in double
  quotes.
- Boolean (examples: `true`, `false`): This token
  represents either true or false.
- `(text)`: Text in parentheses is a comment. For example:
  `(constrained)`

All strings can be up to 256 characters long. Strings notated as (constrained) cannot
include control characters or the following characters: `` \ : / * ` ‘
" ``

**Hierarchy Objects**

Top-level object
:   ```
    { hierarchies : [<emphasis>hierarchy...</emphasis>] (You can import/export one or more hierarchies) }
    ```

*hierarchy* object
:   ```
    {
        name : string, (constrained)
        description : string, 
        tree : <emphasis>tree</emphasis>
    }
    ```

*tree* object
:   Either a leaf or a branch
    object.

*leaf* object
:   ```
    {
        class : "leaf",
        components : [ <emphasis>component</emphasis> … ],
        projectName : string, (constrained, may be null)
        componentsIncluded : boolean,
        name : string, (constrained)
        includeInPolicyEvaluation : boolean
    }
    ```

*branch* object
:   ```
    {
        class : "branch",
        children : [ <emphasis>tree</emphasis> … ],
        name : string, (constrained)
        includeInPolicyEvaluation : boolean
    }
    ```

*component* object
:   ```
    {
        componentMap : string, (constrained)
        componentName : string  (constrained)
    }
    ```

Example
:   ```
    {
      "hierarchies" : [ {
        "name" : "A tiny hierarchy",
        "description" : "Has 3 nodes",
        "tree" : {
          "class" : "branch",
          "children" : [ {
            "class" : "leaf",
            "components" : [ ],
            "projectName" : "sample-ces-app",
            "componentsIncluded" : true,
            "name" : "sample-ces-app",
            "includeInPolicyEvaluation" : true
          }, {
            "class" : "leaf",
            "components" : [ ],
            "projectName" : null,
            "componentsIncluded" : false,
            "name" : "i18n",
            "includeInPolicyEvaluation" : true
          } ],
          "name" : "Java",
          "includeInPolicyEvaluation" : true
        }
      } ]
    }
    ```

Note: If you import a hierarchy and export it again, the JSON will be the same with one
exception: Branch nodes with no children will be converted to leaf nodes with null
projects.

If you import a hierarchy that has a name that matches an existing
hierarchy, the existing hierarchy will be replaced by the imported one.

An
error occurs under the following conditions:

- If Coverity Connect cannot parse your JSON.
- If a node name in the tree is not unique within its container.
- If a project or component name does not refer to an existing project or
  component.
