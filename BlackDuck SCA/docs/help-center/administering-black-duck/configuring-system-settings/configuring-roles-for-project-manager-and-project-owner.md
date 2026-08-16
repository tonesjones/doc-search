---
title: "Configuring Roles for Project Manager and Project Owner"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-roles-for-project-manager-and-project-owner.html"
content_id: "Y85uv~NdpuAXUWYYCi~qSw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:06.947581+00:00"
---

# Configuring Roles for Project Manager and Project Owner

Black Duck SCA allows administrators to configure additional permissions for users with
the Project Manager role and Project Owners. By selecting specific roles, you can grant
these users the permissions associated with those roles, enabling them to perform
additional tasks within their projects.

## Available Roles

The following roles can be applied to enhance the permissions of Project Managers and
Project Owners:

- **Policy Violation Reviewer**: Grants permissions to review and manage policy
  violations within projects.
- **Security Manager**: Grants permissions to manage security-related settings
  and assessments for projects.

## Configuring Roles

To configure which roles should have their permissions applied to the Project Manager
role and Project Owner:

1. Log in as a system administrator user and navigate to **Admin** →
   **System Settings** → **Roles** configuration page.
2. Select the checkboxes for the roles you want to apply:

   - **Policy Violation Reviewer**
   - **Security Manager**
3. **Save** your changes.

Once configured, users with the Project Manager role or designated as Project Owners
will automatically inherit the permissions associated with the selected roles.

## Restriction Considerations

The ability to assign certain project-level roles may be restricted based on the
setting above. Understanding these restrictions is important for administrators
managing user permissions across projects.

When the relevant role setting is disabled, users with the global roles listed below
cannot assign the **Security Manager** role at the project level. This
restriction is enforced to maintain consistency with the system's security
configuration.

- Global Project Group Administrator
- Global Project Manager
- Global Project Viewer
- Global Security Manager
