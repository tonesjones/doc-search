---
title: "Match Review"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/match-review.html"
content_id: "Na66SGAwuP89aTW_BG5~3A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:15:03.542949+00:00"
---

# Match Review

The Match Review feature provides a dedicated workspace for reviewing and managing
component matches that require additional verification before being included in your
project's Bill of Materials (BOM). This feature helps ensure the accuracy of component
identification by allowing you to review and confirm matches that have some degree of
uncertainty or ambiguity.

## What Components Appear in Match Review

Components appear in the Match Review page when they meet specific criteria that
indicate potential uncertainty in their identification:

- **Components with unknown versions** (from binary scans)
- **Components below the match score threshold** (configurable globally via
  component match
  review settings)
- **Unmatched components or external IDs** from package manager and SBOM
  import scans
- **Ignored components** from the BOM when the **Ignored** filter is
  activated

Important: Components in Match Review are not included in reports or SBOMs
until they are reviewed and promoted to the main BOM page.

## Accessing Match Review

To access the Match Review page:

1. Navigate to your project version
2. Go to the **Components** section
3. Select the **Match Review** tab

## Match Review Page Overview

The Match Review page contains the following features; the **review categories
filters** and the **match review table**.

At the top of the page, you'll find **review category filters** that display the
count of components in each review state: **Unknown Version**, **Low Match
Score**, **Unmatched**, and **Ignored**. Clicking on any category will
filter the table to show only components in that specific state, allowing you to
focus on particular types of matches that require attention.

Important:
Ignored components are not displayed in the Match Review table unless the Ignored filter is activated.

The central **match review table** displays all components requiring review in a
structured format. Each row represents a component with columns showing key
information:

- **Policy Violation**
  [image: image] : Indicates whether the component has any
  associated policy violations
- **Component/ID**: Displays the component name and identifier
  information
- **Match Type**: Indicates the type of match (e.g., exact match, binary, SBOM)
- **Score**: Shows the match score for the component match
- **License**: Displays license information associated with the
  component
- **Vulnerabilities**: Shows the number of vulnerabilities identified for
  the component
- **Operational Risk**: Indicates the operational risk level of the component
- **Actions**: Provides an options menu for performing review actions on individual
  components.

## Match Review Sidebar

Selecting a component or ID opens the Match Review sidebar. The Match Review sidebar
displays comprehensive details about the selected component, enabling users to make
informed decisions regarding matches.

In cases where multiple potential matches exist, the sidebar also shows a list of
alternative matches. Each alternative entry includes key identifying information,
and users can choose to match the component to any of these alternatives directly
from the sidebar. This makes it easier to evaluate available options and quickly
correct or refine the match without navigating away from the review workflow.

The panel is organized as follows:

1. **Component/ID**: The name and identifier of the component are displayed
   at the top for quick reference.
2. **Action Buttons**: Below the component name, users can take actions on
   the match with available buttons:

   - **Match**: Unmatched components offer additional capabilities for
     handling internal or proprietary components:

     - **Local Matching (Project Version Specific)**

       - **Local match to existing KB/custom component**:
         Affects only this project version
       - **Local match to new custom component**: Create a
         new custom component for this project version
         only
     - **Global Matching (Requires a user with both the Component
       Manager and Project Manager roles)**

       - **Global match to existing custom component**:
         Future scans with the same external ID will
         automatically match to this component
       - **Global match to new custom component**: Create a
         new custom component that will be used for future
         matches across all projects
   - **Confirm**: Approve the match and promote it to the BOM.
   - **Edit**: Modify the match details if necessary.
   - **Ignore**: Mark the match as a false positive.
   - **Unignore**: If the component was ignored in the BOM, it can be
     unignored in Match Review. This returns the component to the BOM.
     Components that were ignored in Match Review remain there as either
     ignored or unignored.
3. **Match Type**: The type of match is indicated, which may include:

   - Unknown Version
   - Low Match Score
   - Unmatched
   - Ignored
4. **Vulnerabilities and Licenses**: This section displays any associated
   vulnerabilities and licenses for the component.
5. **Source Information**:

   - **Match Score**: Displays the score level of the match.
   - **KB Artifacts Matched**: Indicates the number of Knowledge Base
     artifacts matched.
   - **Version Ambiguity**: Shows the number of component versions
     involved.
   - **Match ID**: Lists the identifier for the match.
   - **Type**: Describes the match type.
   - **File Path**: Provides the path related to the match.
6. **Fields Section**:

   - **SBOM Fields**: Displays any SBOM
     Fields activated.
   - **Custom Fields**: Indicates if there are any custom
     fields associated with the component.
7. **Comments Section**: Users can add and view comments related to the
   match, facilitating collaboration and discussion.
8. **Details Section**:

   - **Component Links**: Provides a URL link to more information about
     the component.
   - **Description**: Offers a brief description of the component.
   - **Tags**: Lists any relevant tags associated with the
     component.

## Review Actions

When reviewing components, you have several options available:

- **Confirm Match**: Approve the component and promote it to the main
  BOM/Components page
- **Edit**: Manually change the match to a different component and/or
  version
- **SBOM Fields**: Access and edit SBOM-specific field
  information
- **Comments**: Optionally add comments for any review action
- **Ignore**: Mark as a false positive and move to ignored state
- **Unignore**: If the component was ignored in the BOM, it can be
  unignored in Match Review. This returns the component to the BOM.
  Components that were ignored in Match Review remain there as either
  ignored or unignored.
- **Generate Support Bundle**: If you find discrepancies in
  component identification, licensing, or vulnerability data in your
  project's Bill of Materials (BOM), you can generate a KnowledgeBase (KB) support bundle directly from here.
  This bundle automatically gathers all necessary component data for
  the support team, streamlining the investigation process and
  reducing the need for additional communication when opening a
  support case.

Match Review supports bulk operations for efficiency:

- **Confirm**: Approve multiple selected components simultaneously
- **Comment**: Add a comment to multiple selected components
  simultaneously
- **Ignore**: Mark multiple components as false positives
- **Unignore**: Mark multiple previously ignored components as active
  again
- **Generate Support Bundle**: If you find discrepancies in component
  identification, licensing, or vulnerability data in your project's Bill of
  Materials (BOM), you can generate a KnowledgeBase (KB)
  support bundle directly from here. This bundle automatically
  gathers all necessary component data for the support team, streamlining the
  investigation process and reducing the need for additional communication
  when opening a support case.

Note: Bulk actions are not supported for unmatched components, except for the
ignore action.

## Important Considerations

When using the Match Review feature, it's essential to note the following:

- **Exclusion from Reports**: Items listed in the Match Review are not
  included in the current reports generated by Black Duck SCA.
  This includes:

  - **Notices Report**: Components marked for review will not appear
    in the Notices File
    report.
  - **Version Details > Components
    Report**: Components in Match Review are excluded
    from this report as well.
  - **SBOM Report**: Items from Match Review are not reflected in the
    SBOM report.
- **Inclusion in Vulnerabilities**: Although components in Match Review are
  excluded from reports, their associated vulnerabilities **are** included
  in the project version's **Vulnerabilities** tab. This means the
  Vulnerabilities tab may display risks from components that have not yet been
  confirmed and promoted to the BOM.
