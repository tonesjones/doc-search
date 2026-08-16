---
title: "About custom scan signatures"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-custom-scan-signatures.html"
content_id: "iojf6X~crmQy~5vSrcWU4w"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:47.999582+00:00"
---

# About custom scan signatures

Your software projects may contain a mix of open source, third-party, and proprietary
software components. While Black Duck KnowledgeBase can identify your open source
components, it cannot identify third-party or proprietary software components. As such,
your BOM may not include all the software components used in your code.

To ensure that your BOM tracks all your code, you can enable custom scan signatures which
you can use to identify third-party and proprietary software used in your code. Once
identified, and displayed in your BOM, you can track the use of proprietary code within
your organization and ensure that you meet the license obligations required by your
third-party software,

## Understanding the custom scan signature process

Custom code signatures is an optional feature. Once enabled, the match service uses these
signatures to identify where internal components are used in your applications. The
internal component would need to be scanned by Black Duck with custom scan
signatures enabled with Retain Unmatched File Data enabled.

Unlike Black Duck KnowledgeBase, custom scan signatures reside on your local Black Duck instance (whether the server is on premises or hosted by
Black Duck).

Please note, there may be performance issues when using this feature.

## Identifying custom code signatures in your code

As the scan client scans the code, it generates “signatures” of the files and
directories it is scanning. After the scan completes, these signatures are
initially sent to the Black Duck KnowledgeBase (KB) web service
where the match service uses the signatures to identify the open source
components/versions that are contained in the code being scanned. After
identifying the open source components, these signatures are then sent to your
local Black Duck instance where the match service compares the
signatures to the custom scan signatures. After identifying the custom code
signatures that are in the scanned code, the BOM is then created.

By default, custom scan signatures have been limited to the top five levels in
the directory structure. System Administrators can modify the global default
value. Global Project Administrators and Project Managers can modify the setting
for a specific project.

## Defining default scanning levels

Users with the system administrator role can define the depth of the scan, as
measured by number of levels in the directory structure, from root, to perform
custom signature scanning. The default level is 5.

To configure the default custom signature scanning level:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Select **Scan** from the lefthand menu.
5. In the **Custom Scan Signature Level** section, enter an integer for the
   number of levels to perform custom signature scanning. You cannot enter
   0.
6. Click **Save**. To indicate that the default value has changed, the button
   changes to **Saved**.

## Custom scan signatures on the project level

To enable custom scan signatures for a project:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the **Settings** tab.
4. Check the **Custom Scan Signature** checkbox. You can also set the custom scan signature depth.

   [image: Custom scan signature checkbox]
5. Click **Save**.

## Creating custom scan signatures

Custom code signatures are managed as projects and after identifying the code the
custom code signatures are pulled into the BOM as a subproject.

Note: A project needs to be created before and custom signatures must be enabled for that project
before taking advantage of this feature. Also, ensure purging unmatched
data is disabled **before** running a scan.

To create custom scan signatures:

1. Scan the third-party or proprietary code you wish to identify as a custom
   scan signature.

   Use the **--detect.blackduck.signature.scanner.individual.file.matching** property set to
   **ALL** in Black Duck Detect.
2. Map the scan to a project version.
3. Identify this project as a custom scan signature in the project's
   **Settings** tab:
   1. Enable the feature
   2. Optionally, select the depth, as measured by the number of levels in
      the directory structure, from root, to perform custom signature
      scanning. The value shown here is the default value, as defined by
      your system administrator.
   3. Click **Save**.
4. Scan your code. The custom scan signature appears in your BOM as a
   subproject:

     
    [image: BOM with custom signature]   

   The **Source** column displays the number of components in the
   subproject.

Note the following:

- If a project contains several versions of a custom scan signature project,
  the BOM will display only one match to one version of the custom code
  signature project.
- If the custom scan signature project contains open source components, values
  for security and operational risk may also appear in the BOM.
- Although you may have selected only one custom code signature project, if you
  have scanned several projects, you will experience performance issues.
- Policy violations within the subproject will not appear in the BOM. However,
  a policy violation will appear in the BOM for the subproject if a policy
  rule is violated at the project level.
- Users who do not have permission to the subproject will not be able to drill
  down to view additional data about that project version.
- A Custom Scan Signature filter has been added to the Project dashboard and
  the BOM page to help you find custom scan signature projects.

## Associating custom components to custom scan signatures

1. Create the custom component.

   Users with the Component Manager role can create custom components.
2. Create a custom scan signature, as described above:
   1. Scan the code for the custom component and map the scan(s) to a
      project version.
   2. In the project's **Settings** tab, select the option to enable
      custom scan signatures.
   3. Define the number of levels to scan. The value shown here on the
      Settings tab
   4. Click **Save**.
3. Select to view the project version created in step 2.
4. From the BOM page, select the **Source** tab and select the top node.
5. Modify the match for the custom component:
   1. Click **Edit** to open the Edit Component dialog box.
   2. Select the custom component created previously and click
      **Update**.

Click here for more information on using the **Source** tab.

## Disabling custom scan signatures

If you experience significant performance degradation in scanning, you can disable
this feature.

To disable custom scan signatures:

1. Clear the custom scan signature option for *all* projects.
2. Rescan your code.
