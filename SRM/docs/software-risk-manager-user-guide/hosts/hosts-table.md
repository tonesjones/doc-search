---
title: "Hosts Table"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/hosts-table.html"
content_id: "maL77xkFD_FwqJG0b3Dqpg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:41.471668+00:00"
content_hash: "5984943b506be77b6676c3d03afe2933197fe40a568fe2cb5cb446a9808f3313"
---

# Hosts Table

Selecting a Host Scope in the Host Scope management menu will populate the Hosts Table
with normalized host information from the selected Host Scope. Normalized hosts are sets
of hosts reported by different tools that are correlated to each other. Thus the
information that the table is populated with is an aggregation of the host information
from various tools that are referencing the same host.

## Viewing Host Information

Each row in the table contains all of the host information that Software Risk Manager is aware of
for a particular host, and each column in the table is a set of values appropriate
for a particular field of interest. Currently, Software Risk Manager only displays FQDN, NetBIOS
Name, IP Address, MAC Address, Operating System, Open Ports, Environment, and
Associated Projects.

[image: image]

Click View in the top right corner and use the toggles to select what information to
display.

[image: image]

## Manually Adding and Editing Hosts

Software Risk Manager allows you to manually add new hosts to the selected Host Scope. The
*Create Host* button is to the top right of the Hosts Table.

[image: image]

Clicking on it will bring up an interactive table where you can define the host that
you are adding.

[image: image]

Clicking *Add Value* will produce a text field where you can enter a new value
for the column you're editing. Note that a default value will be shown if the text
field is empty and serves as an example of a valid value.

[image: image]

There is some validation applied to IP Address, MAC Address, and Open Ports. Typing
in an invalid value for that field will cause the text field to be highlighted in
red. Each invalid value is considered non-existent when clicking *OK* to create
a Host with the specified values, and consequently will not appear in the Hosts
Table when a host with invalid values is successfully created.

If you do not wish to include a value on a host, you may click the trash bin located
at the far right of the cell to delete the value from consideration.

[image: image]

You can include any number of values for any particular column in the editor. Note
that Associated Projects is not present in the editor. This is because Associated
Projects is a derived field, found by determining if a host exists in a particular
project. Also note that any columns that are missing in the Hosts Table as a
consequence of disabling them in the "View" menu will still be shown while editing
the hosts.

Software Risk Manager also allows you to manually edit existing normalized hosts in the Hosts
Table. If you click on the button in the right most column of the Hosts Table, a
drop down menu will appear. The first element in the drop down menu is "Edit
Host".

[image: image]

Clicking on "Edit Host" will bring up the same interactive table that appears when
you're manually adding a new host, except now you will see it in the table, as
opposed to above it.

[image: image]

Software Risk Manager also allows you to delete existing normalized hosts. In the same drop down
menu that "Edit Host" appears, you will also see "Delete Host".

[image: image]

Clicking on it will prompt you with a message detailing the consequences of deleting
a host.

[image: image]

You may confirm the delete by clicking the "Delete" button. Clicking *Cancel*
will bring you back to the Hosts Table without deleting the host. Note that only the
normalized host is deleted when clicking *Delete*. No host information acquired
from results during an analysis will be lost.

When creating or editing a host, you may end up introducing values for field-types
that Software Risk Manager considers "identifying". Identifying fields for Hosts are the FQDN,
Hostname, NetBIOS Name, IP Address, and MAC Address fields. If you introduce a value
for an "identifying" field-type and it already exists on a host in the current Host
Scope, clicking on "OK" will cause the editor to expand to include two new
non-interactive tables.

[image: image]

The first new table will show you the host you tried to add, and the second new table
will show you all hosts that already have some of the values for "identifying"
field-types the host you tried to add has. Clicking *Merge* will cause the host
you tried to add to be joined together with the other hosts that shared values for
"identifying" field-types with that host. Clicking *Cancel* will bring you back
to the editor and will not join the host with any other hosts. Note that you will be
unable to edit the host you're trying to add until you either click *Merge* or
*Cancel*.

## Filtering Hosts

Software Risk Manager also allows you to filter the hosts that appear in the Hosts Table. Above the
table, you should see a text field.

[image: image]

This is the "Generic" filter. Any value provided here will be used to display only
hosts for which at least one field value for any of the field-types satisfies the
filter defined by the provided value.

Clicking *advanced*, which is next to the "Generic" Filter, will bring up the
Advanced Filters sidebar.

[image: image]

These filters are specific to a host field-type, and providing a value for any of
these will display only hosts in the table for which the specified value exists in
the specified column for that host. Note that each filter available will only filter
by one value, so attempting to filter by multiple values for a particular field-type
(or in the "Generic" filter) won't work.
