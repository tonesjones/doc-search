---
title: "Aqua SaaS Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/aqua-saas-configuration.html"
content_id: "ZexPCe4fLPy~NJidEiamWA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:38.442399+00:00"
content_hash: "15be231974042af781d7ebb01e6c8f0ff2c8bf4d6fbd071420e8edd4cdfabf39"
---

# Aqua SaaS Configuration

For Aqua Enterprise on-prem deployment, the connector only requires giving credentials
for an Aqua user with the necessary permissions. However, in an Aqua SaaS instance, the
process of getting the necessary credentials for the connector is more complicated. In
this case, Aqua SaaS requires creating a permission set, role, and an access token, as
shown below.

**To prepare credentials for the connector:**

1. Log into cloud.aquasec.com.
2. Create a permission set:
   1. Click the applications icon located in the top left corner and select
      Account Management from the dropdown menu.

      [image: image]
   2. Select User Management > Permission Sets from the left menu.
   3. Click "Add Permission Set" and enter a name in the Name field.
   4. Expand the Assets category, locate "Images," and enable "view" by
      clicking the corresponding icon.

      This is needed for access to
      images.

      [image: image]
   5. Expand the Compliance category, locate "Vulnerabilities," and click the
      view icon.

      This is needed for access to vulnerability reports on a
      finer, per-image-layer basis.

      Note: (Optional) SRM will detect
      when this permission is unavailable and alter its logic
      appropriately.
   6. Click Save.
3. Create a role and assign the previously created permission set:
   1. Select User Management from the left navigation menu and click
      Roles.
   2. Click Add Role.
   3. Enter a name in the Name field, select a permission set, and select an
      application scope.
   4. Click Save.
4. Create an API Key:
   1. Select Settings from the left navigation menu and click API Keys.
   2. Click Generate Key and save the API Key and Key Secret.
   3. Click the configuration icon to the right of the new API Key and select
      Edit.
   4. Disable "Global Permissions."
   5. Enable "roles:assign", "tokens:readwrite", permission (needed to
      authenticate with token).

      Note: For "tokens:readwrite", give it
      permission to use the role created previously.
   6. Click Save.

The role name from step 3 is used for the “Role Names” connector form field. The API Key
and Key Secret from step 4 are used in the “API Key” and “API Key Secret” connector form
fields.
