---
title: "How to test from the web UI"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/how-to-test-from-the-web-ui.html"
content_id: "sGPJ~h3_OYJ_ZiV8I5Ma0Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:18.372579+00:00"
content_hash: "b0eb5b0f65bf769fedf78e2a1c8a0a7ffecd7e40b2902a8e64ce6bce5daadc96"
---

# How to test from the web UI

How to run a test on your project from the Polaris user interface.

From the Polaris user interface, you can:

- Run SAST and SCA (Package Manager) tests using:
  - Source code you upload manually.

    Note: Before uploading, see the limitations for uploads here: Source code upload limitations.
  - A branch of a repository.

    Note: To scan branches in a repository, you need to set up an SCM integration first. For more information, see [Connect a Polaris project to a repository in your SCM](connect-a-polaris-project-to-a-repository-in-your-scm.md). Before *or after* you set up an SCM integration, you can add branches to a project that aren't connected to a repository.
- Run SCA (Binary Analysis) tests using:
  - Binary files you upload manually.

    Note: Before uploading, see the limitations for uploads here: Binary upload limitations.
- Run External Analysis tests to import SAST and SCA issues captured in third-party tools.

  Note: You can upload one file (up to 2GB) for each external analysis test. Each file you upload can only include one type of issue data (SAST or SCA). Different file formats are accepted for different third-party tools. See Supported third-party tools for a full list of supported tools, along with accepted file formats for each.
- Run DAST tests on web application and API targets.

## Test a SAST & SCA project

Follow these steps to run SAST and/or SCA (Package Manager) tests from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the three-dot [image: test project 3 dot icon] icon at the end of the project's row, and select New Test.
   - Go to Tests and select New Test.
2. Select the branch to scan with the Application, Project, and Branch dropdown menus.

   Note: Depending on how you start a test, the Application, Project, and Branch values may already be filled in.
3. Use the SAST and/or SCA checkboxes to select tests to run.

   Note: These options depend on what your Application Admin has made available for the project.
4. To manually upload code and test it:
   1. Select Code Upload.

      [image: test a project uploaded]
   2. Drag and drop the files you want to test into the Source code zone, or select Browse Files to find files to test on your file system.

      Note: For Code Uploads, source code filenames can include letters, digits, and the characters “.”, “-” and “\_”. No other characters or spaces are allowed.
5. To test a branch in a repository:
   1. Select Repository.

      Note: The Repository option is only available when you select a branch that is connected to a repository.

      [image: test a project repo]
   2. Select Test your connection.
6. To import results from a third-party tool:
   1. Drag and drop the file you want to import into the Import Results zone, or select Browse Files to find the file to import on your file system.

      [image: test a project external]

      Note: You can upload one file (up to 2GB) for each external analysis test. Each file you upload can only include one type of issue data (SAST or SCA). Different file formats are accepted for different third-party tools. See Supported third-party tools for a full list of supported tools, along with accepted file formats for each.
7. Select Begin Test.

   Note: The Begin Test button is locked until either, Polaris successfully connects to the repository or the file upload completes.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or branch/profile tested.

Note: When you scan a project for the first time (using built-in test types), you may receive email communications from the Black Duck team that require a response in order for testing to finish.

Note: If the test fails, you can download test artifacts for troubleshooting. See [Download test artifacts](download-test-artifacts.md) for more information.

## Run a Binary Analysis SCA test

Follow these steps to run an SCA Binary Analysis scan from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the three-dot [image: test project 3 dot icon] icon at the end of the project's row, and select New Test.
   - Go to Tests and select New Test.
2. Select the branch to scan with the Application, Project, and Branch dropdown menus.

   Note: Depending on how you start a test, the Application, Project, and Branch values may already be filled in.
3. Select the SCA - Binary Analysis checkbox.

   Note: See [Binary Analysis](binary-analysis.md) for requirements and limitations.
4. Manually upload binary file and test it:
   1. Select Code Upload.

      [image: test a project binary]
   2. Drag and drop a binary file or ZIP/tar of multiple binary files into the Binary Analysis zone, or select Browse Files to find a file to test on your file system.

      Note: Filenames can include letters, digits, and the characters “.”, “-” and “\_”. No other characters or spaces are allowed.
5. Select Begin Test.

   Note: The Begin Test button is locked until the file upload completes.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or branch/profile tested.

Note: Unlike other SCA scans, binary scans of compiled executables/libraries often generate component names, but may be unable to identify the exact version/origin. In this case, a “?.?” is after the component name. Edit the component (see [Edit a component](add-or-modify-components/edit-a-component.md)) if you know the version, to get a more complete and accurate vulnerability and license information.

Note: When you scan a project for the first time (using built-in test types), you may receive email communications from the Black Duck team that require a response in order for testing to finish.

## Test a DAST project

Follow these steps to run a DAST test from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the three-dot [image: test project 3 dot icon] icon at the end of the project's row, and select New Test.
   - Go to Portfolio, select an application, select a DAST project, and open the DAST Profiles page. Click the three-dot [image: test project 3 dot icon] icon at the end of the profile's row, and select New Test.
   - Go to Tests and select New Test.
2. Select the DAST profile to scan with the Application and Project dropdown menus.

   [image: test dast proj]

   Note: Depending on how you start a test, the Application, Project, and Profile values may already be filled in.
3. (Optional) Select Test Connection.

   This test can take a few minutes to complete and ensures:
   - The Entry Point URL is valid.
   - Polaris can connect to the web application.
   - Polaris can authenticate with the web application.
4. Select Begin Test.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or branch/profile tested.

Note: If the test fails, you can download test artifacts for troubleshooting. See [Download test artifacts](download-test-artifacts.md) for more information.

## Handling of queued tests

For a specific project and test type, Polaris supports *one running (active) test* and *one queued test* at any given time. When both slots are filled, if users start further tests of the same type on the same project, the first (last requested) test is queued and all additional tests are assigned the Not Run status. Tests in Not Run status are not queued and will not be executed. This behavior also applies if tests are requested on different branches of the same project (SAST and SCA tests only).

Example of a test in Not Run status:

[image: Tests page: A test with a Test Status of Not Run, tool tip "Found another test is in progress for the same project"]

## Queued tests example

A *test scheduler* manages multiple test initiation requests made on the same project. Running once per minute, the test scheduler evaluates all tests in Queuing status for a given project (and its branches, if applicable) and picks which test to execute next. To illustrate how the test scheduler works, consider the following example:

At 10:01, one SCA test is active (running) and one SCA test is queued for project 1. Four other SCA tests have subsequently been requested for project 1; these tests have been placed in the Queuing status.

At 10:02, the test scheduler runs and evaluates the four SCA tests in the queue. Two tests (test 2 and test 3) were requested on the same branch (branch 2):

Table 1.

| SCA test requested (in time order) | Project / branch | Test Status before scheduler runs (10:01) | Test Status after scheduler runs (10:02) |
| --- | --- | --- | --- |
| test 1 | project 1 / branch 1 | Queuing | Scanning (picked first) |
| test 2 | project 1 / branch 2 | Queuing | Not Run |
| test 3 | project 1 / branch 2 | Queuing | Scanning (picked second) |
| test 4 | project 1 / branch 3 | Queuing | Scanning (picked third) |

The test scheduler evaluates the four tests as follows:

1. Test 1 is picked for execution first—this is the first (most recently requested) test in the queue.
2. Test 3 was created after test 2 on the same branch. Therefore, test 2 is assigned to Not Run status.
3. Test 3 and test 4 remain in the queue.
4. After test 1 completes, test 3 is picked for execution next.
5. After test 3 completes, test 4 is picked for execution next.

This scenario assumes that no further tests were requested.
