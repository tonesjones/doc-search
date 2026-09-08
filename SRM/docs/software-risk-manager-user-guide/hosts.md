---
title: "Hosts"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/hosts.html"
content_id: "gVFjB7ug7NO14~QHGXb3_g"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:39.572055+00:00"
content_hash: "9ac74a5f21c84b1074fd57523cbc7543718ae1257d9e174f632046727fbb9755"
---

# Hosts

**Note:** this section is only applicable to Software Risk Manager users with the
InfraSec add-on.

When Software Risk Manager ingests *Network Security* results, the location of those
results is typically expressed in terms of a "host," with the level of detail varying
from tool to tool. The Hosts page is Software Risk Manager's location for interacting
with host data directly, outside the context of Findings or Projects. Users will be able
to access the Hosts page but the *Associated Projects* column will only populate
for projects they belong to. Only the Software Risk Manager user with admin privileges
will be able to create, edit, update, or delete host information.

Click the Hosts icon in the navigation bar to open the Host Scopes page.

[image: image]

This page shows a list of global host scopes with the following information:

- FQDN
- Hostname
- NetBIOS Name
- IP Address
- MAC Address
- Operating System
- Environment
- Associated Projects. Click the project name to open the project page.

Note: There's a basic filter field to sort hosts along with advanced filter options. Also,
you can use the "View" button to select which columns to display (or hide).

Tasks include the following:

- Creating a host
- Editing a host
- Deleting a host
- Managing host scopes. Click the Manage Host Scopes button to access the following
  options:
  - Importing host scopes
  - Exporting host scopes

## Editing a Host Scope

**To edit a host scope:**

1. Click the Hosts icon in the navigation bar to open the Host Scopes page.
2. Click the dropdown list icon located in the last column of each row.

   [image: image]
3. Select Edit Host.

   [image: image]
4. Make changes as necessary.
   - Click the delete icon to delete an existing value.
   - Click the value button to add a field.
5. Click OK to save the changes.

## Deleting a Host Scope

**To delete a host scope:**

1. Click the Hosts icon in the navigation bar to open the Host Scopes page.
2. Click the dropdown list icon located in the last column of each row.

   [image: image]
3. Select Delete Host.
4. Click Delete to confirm.

## Creating a Host Scope

To create a host:

1. Click the Hosts icon in the navigation bar to open the Host Scopes
   page.
2. Click Create Host.

   [image: image]
3. Click the appropriate button to add values to the following fields.
   - FQDN
   - Hostname
   - NetBios Name
   - IP Address
   - MAC Address
   - Operating System
   - Environment
4. Click OK to save.

### For more information

For information on host scope and the hosts table, see the following topics:

- Host Scopes
- Hosts Table
