---
title: "Controlling How Sigma Executes"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/controlling-how-sigma-executes.html"
content_id: "02WHGPGQNCBdQfiCW_dy6g"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:20.076693+00:00"
---

# Controlling How Sigma Executes

In addition to the initial configuration, you can control how Sigma executes using the
Advanced dialog from the build step.

To display the dialog, click the Advanced button in the Build dialog.

[image: image]

The dialog allows you to specify the tool whose execution you want to control, whether
the tool should ignore policies, and a field to define Sigma command line arguments.

Any command you specify in the Sigma Command Line field will override the default command
line. If you leave this field empty, the plugin supplies the following Sigma command
line:

- With Ignore Policies selected:

  ```
  sigma analyze --ignore-policies --format jenkins
  ```
- Without Ignore Policies
  selected:

  ```
  sigma analyze --format jenkins
  ```

You can use Sigma commands for additional actions, such as:

- Adding Sigma Configuration Files
- Setting Sigma Policy Files
- Recording Issues
- Executing Other Sigma Commands
