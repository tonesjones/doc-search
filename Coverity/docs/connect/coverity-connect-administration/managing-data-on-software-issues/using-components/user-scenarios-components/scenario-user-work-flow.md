---
title: "Scenario: User work-flow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-user-work-flow.html"
content_id: "~xWXIliMKpGhwnJLUNUQUg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:20.308634+00:00"
---

# Scenario: User work-flow

**User:**
user1

**Goal:** This scenario describes the work-flow of the default owner,
User1. From the User1's perspective, the
work-flow does not greatly differ from a "normal" work-flow; that is, one without
component definitions. So, this scenario describes the specifics of how the component
mechanism works within the flow.

**Filtering issues:**

1. user1 signs into Coverity Connect and selects the
   busybox project.
2. Observes Component as a default column in the Issues: By
   Snapshot list.
3. Observes that either core_libs or IO
   (the components to which user1 belongs) is the component
   name for each issue.

   Note: If more than one component map exists in the project, the component name is
   identified as follows:
   `component_map_name.component_name`

   For example, `busybox.core_libs`

   In this case,
   only one component map exists, so the name displays as
   `core_libs`.
4. Observes that user1 is the owner for all issues that occur
   in core_libs.

   user1 was designated as the default owner during the
   component's configuration.
5. Selects core_libs and Include in the
   Components filter.

   The issues list displays only the issues contained in
   core_libs.

   Component filtering is CID-based, so an issue is included even if only one of its
   occurrences is in the included component. Components that are invisible to
   user1 (through access control or exclusion) do not
   appear in the filter.

   The Include selection displays only the issues for the
   component specified in the filter. The Exclude button
   displays all of the issues that user1 has access to outside
   of the specified component.

**Examining, locating, and triaging issues:**

1. Clicks the Files view type and then the In Latest Snapshot view to observe the
   correct issue markers and file trees that indicate the existence of issues in
   files, directories, and components.

   user1 can only view and open the files and issues to which
   he or she is assigned access.
2. Observes issues that are not in the latest snapshot (fixed/dismissed) as
   associated with components according to the current component mapping.
3. Clicks the gear icon to edit filters.
4. Selects core_libs and Include in the
   Components filter to focus the list of issues. This includes issue links in
   source file display (when no issue is open). Filtering is CID-based; that is, an
   issue is included even if only one of its occurrences happens to be in the
   included component.
5. Observes the issue markers in the file tree, which was filtered according to
   issue filtering criteria.
6. After the list of issues is filtered and a group of issues is selected into the
   desired order, user1 begins to triage the list of
   issues.

   The process of triaging issues is described in Triaging issues.
   However, the following notes apply to triaging issues through the use of
   components:

   - user1 can only select an owner for the issue
     from the list of users that can access the issue based on their
     component assignment.
   - user1 can only retrieve or update stream issues
     that are contained in the assigned components
     (core_libs and
     IO).
   - user1 can only view issues that are contained in
     the assigned components (core_libs and
     IO) in the issue history.

**Monitoring issues:**

Monitoring issues allows user1 to track and create reports of the
issues in the components to which he or she is assigned. For more information, see Coverity Connect usage.

**Setting up component-based notification:**

1. Clicks Preferences from the User Session tool
   bar.
2. Clicks the Components Subscriptions tab.

   Note: Component notification requires the setup of a notification script using the
   Web Services API.
3. Subscribes to new issue notification by selecting the
   busybox component map, and the
   core_libs and IO components.

   Figure 1. Component Subscriptions window
     
    [image: image]
4. Clicks Done.

   user1 will receive new issue notifications when new issues
   are committed.

   Users are alerted if they subscribe to a restricted component to which they have
   no access.
