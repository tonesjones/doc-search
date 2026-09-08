---
title: "Manual Entry Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/manual-entry-configuration.html"
content_id: "WWL0OFfKwaQEfrqqKqoBHw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:57.402834+00:00"
content_hash: "483953eba010381e54e2767818fade09ecf78705ac15b182fa44acbc8e409477"
---

# Manual Entry Configuration

The Manual Entry Configuration page allows Software Risk Manager administrators to define
custom values which can be entered into certain fields in the Manual Results.

Click the Settings icon in the navigation bar and select Manual Entry Configuration from
the left menu to open the Manual Entry Configuration page.

[image: image]

This page displays a list of existing detection methods and allowed tools. From here, you
can add, delete, or rename detection methods, and add or remove allowed tools.

For more information on detection methods and allowed tools, see the following
topics:

- Managing Detection
  Methods
- Managing Allowed Tools

## Managing Detection Methods

Software Risk Manager provides built-in detection methods, which explains how a
finding was discovered. These built-in detection methods reflect the types of tools
currently supported by Software Risk Manager. For manual entry, you may wish to
specify your own custom detection methods.

### Adding a Detection Method

**To add a new detection method:**

1. Click the Settings icon from the navigation bar and select Manual Entry
   Config from the left menu.

   [image: image]
2. Click Add Detection Method.

   [image: image]
3. Enter a name for the detection method.
4. Click Save.

### Renaming a Detection Method

You can rename your custom detection methods as needed. However, the built-in
detection methods cannot be edited in any way (indicated by the lock icon next
to their edit/delete buttons).

**To rename a detection method:**

1. Click the Settings icon from the navigation bar and select Manual Entry
   Config from the left menu.

   [image: image]
2. Click the dropdown configuration icon to the right of the detection method
   and select Rename.

   [image: image]

   This opens the Rename Detection Method window.

   [image: image]
3. Enter a different name for the detection method.
4. Click Save.

### Deleting a Detection Method

You can delete any unused custom detection methods (i.e., as long as no manually
entered results use it as their own detection method). If your custom detection
method is in use when you try to delete it, you will have to choose a
replacement. All results using that detection method will be edited to use the
replacement detection method instead. This will likely trigger the recorrelation prompt, since
detection method is one of the correlation criteria.

**To delete a detection method:**

1. Click the Settings icon from the navigation bar and select Manual Entry
   Config from the left menu.

   [image: image]
2. Click the dropdown configuration icon and select Delete.

   [image: image]

   This opens the Delete Detection Method window.

   [image: image]
3. Click Delete to confirm.

## Managing Allowed Tools

The Allowed Tools section lets you define which tools will appear in the Tool
dropdown in the Manual Result form. The names you add to this list do not
necessarily need to correspond to a tool known to Software Risk Manager, or even a
real tool, for that matter: you can enter any tool name you want.

Note: Unlike the Detection Methods delete, you don't need to pick a replacement to
delete an item in this list; this list only controls which tools are available when
creating a new manual result, not which tools exist.

### Adding an Allowed Tool

**To add an allowed tool:**

1. Click the Settings icon from the navigation bar and select Manual Entry
   Config from the left menu.

   [image: image]
2. Click the Add Allowed Tool button.

   [image: image]
3. Enter the name of the tool.
4. Click Save.

### Deleting an Allowed Tool

**To delete an allowed tool:**

1. Click the Settings icon from the navigation bar and select Manual Entry
   Config from the left menu.

   [image: image]
2. Click the dropdown configuration icon to the right of the allowed tool and
   select Delete.

   [image: image]

   This opens the Delete Allowed Tool window.

   [image: image]
3. Click Delete to confirm.
