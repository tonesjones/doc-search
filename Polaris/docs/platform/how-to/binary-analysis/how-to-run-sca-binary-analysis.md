---
title: "How to run SCA binary analysis"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/how-to-run-sca-binary-analysis.html"
content_id: "kO1ixBtT2l7TEGgb8ih7~Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:19.784594+00:00"
content_hash: "f5270ddbebeffdd941d1241a8313fe23315cae7d071224b2562fd9a256e3a00a"
---

# How to run SCA binary analysis

How to run an SCA Binary Analysis test on your project from the Polaris user interface.

From the Polaris user interface, you can:

- Run SCA (Binary Analysis) tests by manually uploading a binary file or a ZIP/tar of multiple binary files.

  Note: Before uploading, see the limitations for uploads here: Binary upload limitations.

## Test a SCA Binary File

Follow these steps to run an SCA Binary Analysis scan from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the three-dot [image: test project 3 dot icon] icon at the end of the project's row, and select New Test.
   - Go to Tests and select New Test.
2. Select the branch to scan with the Application, Project, and Branch dropdown menus.

   Note: Depending on how you start a test, the Application, Project, and Branch values may already be filled in.
3. Select the SCA - Binary Analysis checkbox.

   Note: See [Binary Analysis](../binary-analysis.md) for requirements and limitations.
4. Manually upload binary file and test it:
   1. Select Code Upload.

      [image: test a project binary]
   2. Drag and drop a binary file or ZIP/tar of multiple binary files into the Binary Analysis zone, or select Browse Files to find a file to test on your file system.

      Note: Filenames can include letters, digits, and the characters “.”, “-” and “\_”. No other characters or spaces are allowed.
5. Select Begin Test.

   Note: The Begin Test button is locked until the file upload completes.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or branch/profile tested.

Note: Unlike other SCA scans, binary scans of compiled executables/libraries often generate component names, but may be unable to identify the exact version/origin. In this case, a “?.?” is after the component name. Edit the component (see [Edit a component](../add-or-modify-components/edit-a-component.md)) if you know the version, to get a more complete and accurate vulnerability and license information.

Note: When you scan a project for the first time (using built-in test types), you may receive email communications from the Black Duck team that require a response in order for testing to finish.
