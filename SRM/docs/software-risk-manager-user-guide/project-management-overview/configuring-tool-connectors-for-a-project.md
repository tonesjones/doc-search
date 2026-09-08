---
title: "Configuring Tool Connectors for a Project"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuring-tool-connectors-for-a-project.html"
content_id: "HKfkZduGFE5T6kAW7Jidwg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:10.373043+00:00"
content_hash: "8f6c957757c135b82b7c2142a6e4c821c2a4cad19c1a5c8fcff364d5f05c15f1"
---

# Configuring Tool Connectors for a Project

Tool Connectors allow Software Risk Manager to pull results directly from external tools
without manually exporting the results from those tools and uploading them. Software
Risk Manager provides tool connectors for a variety of app-sec tools. For a complete
list, click here.

Note: Users with the manage role need only configure a connection to their tools
once.

The Tool Connectors window for a project can be accessed from the project's dropdown
configuration icon on the Projects page.

This window shows any tool connectors that have already been added, along with any tool
connectors configured via central configuration, as well as a list of available tool
connectors.

[image: image]

On a new project, no tool connectors will be configured.

Clicking a link in the bottom section will open a form to configure a connector for the
link's respective tool.

Each tool connector configuration form includes a set of fields and tabs, starting with a
Config Name field, which can be anything you choose. (The name won't affect the
connector's functionality; it simply identifies this particular configuration. Since
users may configure multiple connectors for a single tool, it may be useful to choose
different names for each connector.)

Configuration tabs and fields are as follows:

- **Connection tab**
  - **Tool-Specific Fields.** To connect to a tool's API, SRM requires
    valid credentials for that tool. Different tools will require different
    fields; however, typically there will be a URL in combination with user
    authentication, such as a username/password combination or API Token.
- **Project tab**
  - **Project (or similar).** Different tools may use different
    terminology, such as *Build* or *Application*. This field is
    used to tell Software Risk Manager which of the tool's projects to pull
    from. This tab will be disabled until valid credentials have been
    entered.
- **Version tab**
  - **Target SRM Branch.** This specifies the name of an SRM branch that
    the user wants to run analyses with the selected tool connector.
  - **Derive version information based on SRM branch name during
    analysis.** This checkbox, when available, disables other fields
    from the integration. For example, if there was a "branch" dropdown from
    the integration, and you selected this checkbox, the "branch" dropdown
    would be disabled. This allows SRM to determine the rest of the
    configuration based on the SRM branch where you are running the
    analysis.
  - Fields defined by the integration.
- **Options tab**
  - Available options depend on the specific tool connector.
- **Schedule tab**
  - **Auto-update.** Selecting Auto-update along with one of the options
    below it tells Software Risk Manager to automatically perform an
    analysis using the configured connector at a regular interval. Selecting
    the first option will tell Software Risk Manager to auto-update at a
    fixed time interval, e.g., *every 12 hours*. Selecting the second
    option will tell Software Risk Manager to auto-update at a specified
    time each day.
  - **Run this connector during normal analyses.** This selection will
    cause the tool connector to appear on the New Analysis page as if it
    were a bundled tool, allowing the tool connector to run during a normal
    analysis, alongside any other files you might want to upload for
    analysis.

Note: Credentials entered for tool connector configurations will be stored (encrypted, but
still reversible) by Software Risk Manager. For added security, it is recommended that
users create one-off accounts in a tool, with the sole purpose of connecting Software
Risk Manager to that tool.

Some tools support a "branch" abstraction (though each tool may have its own name for it,
such as "Stream" or "Version"), allowing you to choose different incarnations of a
selected project. When supported by Software Risk Manager, the corresponding field in
that tool's connector config form will include a checkbox that allows you to opt in to
sync that tool's "branch" with a corresponding *Software Risk Manager Branch.* The
sync setting affects the auto-update
behavior of the tool connector, as well as setting the default behavior of the *Run
Now* form when you manually run the tool connector. When enabled, Software Risk
Manager will try to run the tool connector on a *Software Risk Manager Branch*
whose name corresponds to the selected value in the tool connector configuration
dropdown.

Once all of the fields are completed, click OK to save the configuration and return to
the connectors list.

Each configured connector has three buttons:

- **Run Now.** This can be used to start an analysis using a particular tool
  connector. This process is independent of the auto-update setting: it can be
  done regardless of whether or not the connector is configured to auto-update and
  will not interrupt the auto-update schedule. Users with the create role
  (specifically, the `project:manage-tool-connectors` and
  `analysis:create` permissions) for the project will be able
  to interact with this button.
- **Edit.** This reopens the configuration form for an individual tool
  connector. Only users with the manage role will be able to interact with this
  button.
- **Delete.** This deletes an individual tool connector. Only users with the
  manage role (specifically, the `project:manage-tool-connectors`
  permission) will be able to interact with this button.

After clicking Run Now in the list of configured connectors, a form will appear, allowing
you to choose the *Software Risk Manager Branch* in which the analysis will be run.
If you configured one of your tool connector's fields to sync with a *Software Risk
Manager Branch*, the form will default to the corresponding branch. If the
configured sync target branch does not exist, you must also select a parent branch so
that Software Risk Manager can create a new branch, forked from your selected parent
branch, to correspond with the sync target from your connector configuration. Once you
complete the branch selection in the form, submit it by clicking Run Now. This will
initiate a new analysis to run the connector in the background, close the Tool
Connectors dialog, and display a notification.

## Qualys VM Tool Connector and Scheduling Auto Update

For more information, see the following sections:

- Qualys VM Tool
  Connector
- Scheduling Auto Update
