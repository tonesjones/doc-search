---
title: "Move all projects in an application to a different application"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/move-all-projects-in-an-application-to-a-different-application.html"
content_id: "dc3MZvek926lQwWrjiasOA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:10.032374+00:00"
content_hash: "aac7f202fb4cc6ef690bf055e0779416597d2328b1ed931596dbcda31b31d7a1"
---

# Move all projects in an application to a different application

Learn how to move all of an application's projects to another application.

Note: Only Organization Admins, Organization Application Managers, Application Admins, and other users with permissions to move projects can move projects between applications. Please note:

- Application Admins must have Application Admin access to both the source and destination applications.
- Users who have been granted explicit permissions to move projects (via roles and groups) can also move projects between applications, as long as they have the necessary permissions for both the source and destination applications.

Before you proceed, we strongly recommend reviewing the prerequisites and limitations for moving projects between applications.

1. Go to Portfolio.
2. Select the [image: icon polaris options] icon next to the application that contains the projects you wish to move, and then select Move projects in application.

   The Move projects window appears.
3. Select the application you wish to move the projects into using the Destination application dropdown.

   Only applications that use the team member model (concurrent subscription) are shown.
4. Under Application Settings, choose how the projects' settings will change after they move:
   - Inherit new application settings: The projects will inherit settings from the new application. Modified settings will remain unchanged.
   - Keep previous application settings: Polaris will preserve the projects' settings.
5. Select Move projects.

   Note: Project settings are locked until the move is complete.
