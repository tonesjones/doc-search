---
title: "View component history (and activity log)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/view-component-history-and-activity-log-.html"
content_id: "nAroVTZ9uA65kDUbPX4t2w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:35.373425+00:00"
content_hash: "3dbc9fe2390b8b4eec44cfc0a80c66136cb8ce5f82fa83a2ed448b81e227412e"
---

# View component history (and activity log)

You can view a component's triage history and activity log when you triage the component.

To view a component's history and activity log, follow these steps:

1. Go to Portfolio, select an application, select a project, and open the Components tab.
2. (Optional) Select a non-default branch using the dropdown near the top of the page.
3. Select a component with the checkbox on the left side of the table.

   Note: Component history does not appear when you select multiple components.
4. Click Triage 1 Selected or (if you only have observer access to the application) View Triage History.

   The Triage Selected Component panel appears.

   [image: component triage]

   Up to 4 of the component's most recent triage history events appear by default. Select Show More + (near the bottom of the panel) to load 100 more.

   Note: Component triage history is not branch-specific. All of the triage events for a component (across branches in the same project) appear here.
5. To view the component's activity log, select Activity Log.

   [image: component activity]   

   Earlier events appear near the top of the list. Component events include:

   - Component Added: A user in your organization manually added the component to the project.
   - Component Edited: A user modified the component (including changing the component's origins).
   - Component Reset: A user reset the component after it was modified.
   - Fix Pull Request Created: A user created a Fix PR.
   - Fix Pull Request Disabled: A user disabled a Fix PR.

   Note: Component activity is branch-specific. Events for the same component can vary between branches.
