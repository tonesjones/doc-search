---
title: "Host Scopes"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/host-scopes.html"
content_id: "f9JPm2kfu0MxJdfbZ86w3g"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:40.489579+00:00"
content_hash: "5ff1701efec25a6a400e76ac2ec87b7a1cbc44934c0ca677e43cd6c79cb68350"
---

# Host Scopes

A Host Scope is effectively just a set of projects that share host information with each
other. A Host Scope can be used to model a network where each project in a Host Scope
contains vulnerability information for a vulnerable application that is housed on a
potentially vulnerable host. Alternatively, one can simply use Host Scopes to isolate
host information to particular sets of projects so that overlapping pieces of host
information between Host Scopes don't interact with each other during Host Normalization
and Finding Correlation. Each Host Scope can have multiple projects attached to them but
each project can only be linked to one Host Scope. See Host Scope Associations for more information
on how to set up projects with Host Scopes.

Click the Hosts icon in the navigation bar to open the Hosts page. Use the Hosts and Host
Scopes buttons to display the associated data.

[image: image]

## Managing Host Scopes

By default, the Global Host Scope will be the only one available. However, you can
create new Host Scopes by clicking Add Host Scope.

[image: image]

Enter a name and click Save to create your Host Scope.

Once a host scope has been created, you can Import, Export, or Delete it.

[image: image]

Clicking Import will allow you to import a custom set of host information into the
Host Scope for which you clicked Import. Software Risk Manager currently only
supports importing hosts defined in a `.json` file. Hosts are
expected to be provided as JSON Objects of the form: `field-type: [values...]`SRM currently supports the following field-types: Hostname, FQDN, NetBIOS
Name, IP Address, MAC Address, Operating System, Ports. Every value for a field type
is simply a string, except for Ports, which is a special case expecting each value
to be another JSON Object with the following structure:

```
"Ports": {
	"Port": <port_number>
	"Protocol": <port_protocol>
	"State": <port_state>
}
```

Note: The Import button for non-selected Host Scopes will be disabled by default as you
can only import hosts into the selected Host Scope.

Clicking *Export* will provide you a `.json` file containing all
the normalized hosts in the Host Scope for which you clicked Export. The structure
of the `.json` file matches that of the structure required for
importing hosts into a Host Scope.

Clicking Delete will bring up a window allowing you to confirm that you would like to
delete the relevant Host Scope. Deleting a Host Scope will delete all normalized
host information belonging to that Host Scope. To delete a Host Scope, you will
first need to delete any projects associated with that Host Scope.

[image: image]

You can confirm that you would like to delete the relevant Host Scope by clicking OK.
