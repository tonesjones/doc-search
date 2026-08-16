---
title: "Integrating Protex with Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/integrating-protex-with-black-duck.html"
content_id: "jMQciE2QpivwaZfZATO7Gw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:25.966327+00:00"
---

# Integrating Protex with Black Duck

Black Duck provides the ability to import Protex BOMs into Black Duck.

This feature gives Protex users the ability to use Black Duck to view
and manage security vulnerabilities in their existing BOMs. It also provides Black Duck customers the ability to use the greater language support
that is available in Protex.

There are three basic methods for importing Protex data into Black Duck:

- Components Only

  This option is akin to the mapping that is currently done between Protex and Code
  Center – the BOM in Code Center only has the list of component/versions and not
  any of the associated file mappings. Similarly, using this technique to import a
  Protex BoM into Black Duck only preserves the
  components/versions. As only the component and version information is being
  mapped, there is less of a performance impact compared to the other methods.

  This is the default output of the Protex BOM Tool.
- Components and Files

  This method maps the existing Protex BOM into a comparable BOM
  within Black Duck, preserving the identified components and the
  associated file mappings. Note that the resultant BOM in Black Duck is only as a good as the identifications that were
  made manually in Protex, therefore, it is important that the
  people doing the identification work in Protex pay attention to
  the versions they are selecting for each component. Historically, for license
  compliance, having the correct version for a component was less important as
  licenses rarely changed between versions of the same component. However, for
  security risk, having the correct version for a component is very important as
  vulnerabilities are mapped to specific versions of components. Therefore, if you
  will be using Protex with Black Duck, it is
  important for you to be aware of this as you are doing your identification
  work.

  The Protex BOM Tool can export a BOM from Protex and import it directly into Black Duck,
  mapping it to a specific project and release. Or, the tool can be used to export
  the BOM into a JSON file which can be later imported into Black Duck using the Black Duck UI.

  Note: The component and version identifiers are different between the Protex KB
  and Black Duck KB. During the import process, Black Duck application will remap each BOM component/version
  from its Protex KB identifier to the corresponding Black Duck KB identifier. Not all components will have a KB
  identifier and will therefore not be reflected in Black Duck
  BOM, for example, custom or local components, or components that do not have a
  corresponding ID in Black Duck KB.

  An audit log lists
  the Protex components and licenses that were mapped to Black Duck and provides details around any items that were
  unable to be mapped between the Protex KB and the Black Duck
  KB.

  To use this method, include the **--include-files** parameter when running the
  Protex BOM Tool.

  Note: Due to the amount of file information contained in many Protex BOMs, there may be some
  performance impact both during the import process and when navigating to UI
  pages involving these projects.
- File Metadata > Black Duck Signatures

  This method takes the original file metadata that was captured during the Protex scan and imports it into Black Duck such
  that Black Duck treats it as if the scanner was scanning the
  files and directories directly. A new Black Duck BOM is created
  which will likely be different from the original Protex BOM. As
  the scanner takes advantage of the full context of file and directory
  information, it can identify the correct version information for a component.
  Thus, in many cases you will see more accurate version information using this
  method and get better results for security use cases.

  To use this method, use the **–-dryRunWriteDir** and **--include-files**
  parameters when running the Protex BOM Tool.

  Note: For the best results using this approach, archives need to be expanded when running the
  Protex scan. This may produce longer scan times for some
  projects depending on the number of archives in the project.

## Understanding the Protex BOM integration process

The process for integrating a Protex BOM into Black Duck is:

1. Log in to Black Duck SCA.
2. Download and install the Protex BOM tool. The Protex BOM tool provides several different ways by which you
   can import a Protex BOM into Black Duck.
3. Export the Protex BOM file.

   Note: Only projects assigned to the user whose credentials are supplied in the tool will be
   available for export.
4. If you do not use the Protex BOM tool to import the BOM into Black Duck or map the BOM to a project, then use Black Duck UI to:
   - Import the Protex BOM file into Black Duck.
   - Map the Protex BOM to a Black Duck project.

Once the Protex BOM is imported and mapped, you can view and manage its
contents as you manage any other BOM in Black Duck.

## Requirements

To import a Protex BOM into Black Duck, you must be
running:

- Protex version 7.1.2 or higher
- Black Duck version 2.3 or higher

Note the following:

- Imported Protex data is processed in Black Duck and the Black Duck KB through a new KnowledgeBase matching service. This
  service converts all Protex Suite IDs to Black Duck
  KnowledgeBase IDs.
- Matched and unmatched file information is available in Black Duck. The following table lists the Protex discovery type, usage, and the corresponding Black Duck match type:

  | Protex Discovery Type | Protex Usage | Black Duck |
  | --- | --- | --- |
  | * | Component | Exact |
  | Code Match | File | Exact |
  | Code Match | Snippet | Partial |
  | String Search | Snippet | Partial |
  | Dependency | Snippet | Dependency |

- The following Protex BOM components are not available in Black Duck:

  - Custom Components
  - Custom Licenses

> These components are dropped during the import process.

- If you use Protex to make any changes to the Protex BOM, the changes persist when the Protex BOM is
  reimported to Black Duck: only the changes made in the
  imported Protex BOM are updated in the Black Duck
  project.

Tip: **Want to Learn More?** Check out the [Importing Your Protex BOM into Black Duck](https://blackduck.skilljar.com/page/black-duck) course at Black Duck Customer Education. You will learn
how to use the Protex BOM Tool which allows you to export your Protex BOM and import it into Black Duck to
discover the security vulnerabilities in your projects.
