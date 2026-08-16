---
title: "Viewing SBOM fields"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-sbom-fields.html"
content_id: "SYH9amFb~Kccl8VgKr_p~Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:23.972882+00:00"
---

# Viewing SBOM fields

After creating or activating a
SBOM template, you can find them in their relevant sections. See the sections below for
the specific areas where the SBOM fields appear:

- BOM
  Component
- Component
- Component
  Version
- Project
- Project
  Group
- Project
  Version

## BOM component

SBOM BOM component fields are viewed and edited in the component version row on the
project's BOM page. They are shown in the output of SPDX and CycloneDX
reports. Users with the Global Project Administrator, Global Project
Manager, Component Manager, or Project Manager (for the projects they are associated
with) role can enable or disable the values for the SBOM fields.

To view and add information on the component version level:

1. Navigate to the project's BOM page.
2. Click [image: Options button] at the end of the desired component version row.
3. Select **SBOM Fields** and enter the information for the custom fields. This
   opens the **SBOM Fields** dialog box.

     
    [image: SBOM Fields dialog box]

The SBOM fields are not mandatory, but must be populated with correctly formed
information:

- **Originator**: If the package identified in the SBOM file originated from
  a different person or organization than identified as Package Supplier, this
  field identifies the origin of the package. Select Organization or Person.
  If either entity is selected, the Name field becomes mandatory. The email
  address field remains optional.
- **Supplier**: The organization that supplied the component that the BOM
  describes. Select Organization or Person. If either entity is selected, the
  Name field becomes mandatory. The email address field remains optional.
- **Hash**: These fields act as intrinsic identifiers for components and
  support stronger traceability across scans and SBOMs. The **Hash Value**
  field is used to verify the component's integrity or detect changes over
  time. The **Hash Algorithm** field indicates how the hash value was
  computed (e.g., SHA-256). If either the **Hash Value** or **Hash
  Algorithm** field is populated, both fields are required. This ensures
  the component hash can be correctly interpreted and validated.
- **PURL (Package URL)**: A Package URL (PURL) is a standardized way to
  identify and locate software packages across different package managers and
  ecosystems. It provides a consistent format to specify the package type,
  namespace, name, version, and other qualifiers, helping tools accurately
  track and manage software components.

  When a component version has multiple PURL matches, all matching origin IDs
  will be displayed in the BOM. For example, if there are several PURL
  matches, the UI will indicate the number of matches available. You can
  select one of the displayed matches or enter your own custom PURL to
  override the default selection. Each selected PURL will be included in your
  SBOM report.

  [image: Component version with multiple PURL matches]

  For more information, please consult PURL specification documentation
  online.
- **Package Comment**: General comments about the package being described.
- **Package Valid Until Date**: The end of the support period for a package
  from the supplier.
- **Download Location**: The URL or other specific location within a version
  control system (VCS) where the component was downloaded. Please note that in
  SPDX and CycloneDX, an instance of a component can have multiple download
  locations. However, in Black Duck, a component version can only have one
  download location. When an SBOM is imported, only the first URL is imported
  and the rest are ignored.
- **CPE (Common Platform Enumeration)**. CPE is a standardized method of
  describing and identifying classes of applications, operating systems, and
  hardware devices present among an enterprise's computing assets.

  Enter a valid Common Platform Enumeration identifier
  (`[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}`).

  See Defining the default CPE for component versions for more
  information.

## Component

SBOM component fields are viewed and edited on the component page. The output is
displayed in SPDX
and CycloneDX reports. Users with the Global Project Administrator,
Global Project Manager, Component Manager, or Project Manager (for the projects they
are associated with) role can enable or disable the values for the SBOM fields.

To view and add information on the component level:

1. Click the component in your project's BOM. This will take you to the
   component version page.
2. Click the component name.

   [image: Component version page]
3. Click the **Settings** tab on the top right.
4. Click the **SBOM Fields** tab in the lefthand menu.

   [image: SBOM Fields tab of the Component page]

The SBOM fields are not mandatory, but must be populated with correctly formed
information:

- **Originator**: Select Organization or Person. If either entity is
  selected, the Name field becomes mandatory. The email address field remains
  optional.
- **Description**: Enter any text describing the package.

## Component Version

Component version SBOM fields are viewed and edited on the component version's
settings page. Users with the Global Project Manager, or Project Manager (for the
projects they are associated with) role can enable or disable the values for the
SBOM additional fields.

To change information on the component version level:

- Click the component in your project's BOM. This will take you to the
  component version page.
- Select the **Settings** tab.
- Select **SBOM Fields**.

  [image: Component Version page]
- Edit the desired SBOM field:

  - **Download Location**. The URL or a specific location within a
    version control system (VCS) that the component was downloaded
    from.
  - **CPE (Common Platform Enumeration)**. CPE is a standardized
    method of describing and identifying classes of applications,
    operating systems, and hardware devices present among an
    enterprise's computing assets. See Defining the default CPE for component versions for more
    information.

## Project

SBOM project fields are viewed and edited on the project settings page. Users with
the Global Project Manager, or Project Manager (for the projects they are associated
with) role can enable or disable the values for the SBOM additional fields.

To change information on the project level:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the **Settings** tab.
3. Select **SBOM Fields**.

   [image: image]
4. Edit the desired SBOM field:

   - **Originator**. If the package identified in the SBOM file
     originated from a different person or organization than identified
     as Package Supplier, this field identifies the origin of the
     package.

     Select either Organization or Person from the **Entity** dropdown
     menu. Enter a name in the Name field. This is a mandatory field.

     Optionally, you can add an email address for the entity in the
     **Email** field.
   - **Project Alias**. Project Alias masks the name of your project
     version name in SBOM reports. Enter a new project name in the
     **Project Alias** field to be used in a SBOM report.
   - **VEX Document Tracking ID**. The VEX Document Tracking ID is used
     to determine the filename of the CSAF VEX report. It also can be
     used in combination with the namespace field to create a globally
     unique and resolvable identity. This ID will appear in both the
     global CSAF VEX
     report and project
     version CSAF VEX report.

     Important: The VEX Product ID must be unique within a single
     Black Duck SCA instance. Uniqueness across multiple Black Duck SCA
     instances cannot be guaranteed or enforced.

     Note: VEX Product ID configuration is currently available for
     single-project VEX reports.
   - **VEX Traffic Light Protocol (TLP)**. The Traffic Light Protocol
     (TLP) is designed to enhance the sharing of potentially sensitive
     information and facilitate effective collaboration. TLP utilizes
     four labels to indicate the sharing boundaries for information being
     communicated from an information source to one or more
     recipients:

     - **TLP:RED** is designated for information intended solely
       for the specific recipients, with no further disclosure
       permitted. This label is used when sharing information poses
       a significant risk to the privacy, reputation, or operations
       of the involved organizations. Recipients are prohibited
       from sharing TLP:RED information with others. For example,
       in a meeting context, TLP:RED information is restricted to
       those present at the meeting.
     - **TLP:AMBER** is used for limited disclosure, allowing
       recipients to share information within their organization
       and with clients on a need-to-know basis. This designation
       is appropriate when the information requires support to be
       effectively acted upon but poses risks to privacy,
       reputation, or operations if shared externally. Recipients
       may share TLP:AMBER information with colleagues and clients,
       but they must ensure that it is done cautiously to protect
       all parties involved.

       It is important to note that while TLP:AMBER+STRICT is a
       valid option according to FIRST.org, it will not be
       supported because the CSAF 2.0 specification does not
       accommodate it.
     - **TLP:GREEN** is designated for limited disclosure,
       allowing recipients to share information within their
       community. This label is applicable when the information is
       beneficial for raising awareness among peers and partner
       organizations. Recipients may share TLP:GREEN information
       with others in their community, but it must not be
       distributed through publicly accessible channels.
       Additionally, TLP:GREEN information should not be shared
       outside of the defined community. If "community" is not
       specified, it is assumed to refer to the cybersecurity and
       defense community.
     - **TLP:CLEAR** allows recipients to share information
       freely with no restrictions on disclosure. This designation
       is used when the information poses minimal or no foreseeable
       risk of misuse, following applicable rules and procedures
       for public release. Subject to standard copyright
       regulations, TLP:CLEAR information can be shared without
       limitation.

     For more information, please refer to the [FIRST TLP documentation](https://www.first.org/tlp/).

## Project group

SBOM project group fields are viewed and edited on the project group page. Users with
the Global Project Group Administrator, Project Administrator (for the projects they
are associated with), or Project Manager (for the projects they are associated with)
role can enable or disable the values for the SBOM additional fields.

When enabled, all project groups under this group will inherit the field values, but
they can be overriden in each group.

To view and add information on the project group level:

1. Click [image: image] and then
   select **Project Groups**.
2. Click the blue **Manage** button on the top right of the page.
3. Select **SBOM Fields**.

   [image: image]

The **Creator** section contains the following fields:

- **Organization**: Mandatory. This field must contain the name of an
  organization. It is pre-populated with COMPANY NAME, but can be replaced
  with the name of your organization.
- **Organization's email**: Optional. Enter the email address for the
  organization.
- **Person**: Optional. Enter the name of a person representing the
  organization.
- **Person's Email**: Optional. Enter the email address for the person
  representing the organization.

**Creator Comments**: Optional. A field for creators of the SPDX file to provide
general comments about the creation of the SPDX file or any other relevant comment
not included in the other fields.

**Propagate field values to all child groups**: Enable this checkbox if you want
the all project groups under this group to inherit the field values above. They can
be overriden in each group.

## Project version

These are additional fields that can be included in the SBOM report. These field
values will propagate when this project is used as subproject, you can override them
at the BOM level. SBOM project version fields are viewed and edited on the project
version page. Users with the Global Project Administrator, Global Project Manager,
Project Administrator (for the projects they are associated with), or Project
Manager (for the projects they are associated with) role can enable or disable the
values for the SBOM fields.

To view and add information on the project version level:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the desired project version.
3. Select the **Settings** tab.
4. Select **SBOM Fields**.

   [image: image]
5. The SBOM fields are not mandatory, but must be populated with correctly
   formed information:

   - **Supplier**: Select Organzation or Person. If either entity is
     selected, the Name field becomes mandatory. The email address field
     remains optional.
   - **PURL**: Enter a valid package URL
     (`scheme:type/namespace/name@version?qualifiers#subpath`).
     For more information, please consult PURL specification
     documentation online.
   - **CPE**: Enter a valid Common Platform Enumeration identifier
     (`[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}`).
     For more information, please consult CPE specification documentation
     online.
   - **Package Comment**: General comments about the package being
     described.
   - **Package Valid Until Date**: The end of the support period for a
     package from the supplier.
   - **Download Location**: The URL or other specific location within a
     version control system (VCS) where the component was downloaded.
     Please note that in SPDX and CycloneDX, an instance of a component
     can have multiple download locations. However, in Black Duck, a
     component version can only have one download location. When an SBOM
     is imported, only the first URL is imported and the rest are
     ignored.
