---
title: "Bill of materials data table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/bill-of-materials-data-table.html"
content_id: "pMLjoMqzq80HhW7A_~JKRA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:30.455006+00:00"
---

# Bill of materials data table

The Bill of materials (BOM) table contains the information about the components and
subprojects in this version of the project.

In the component list view of the BOM, click [image: image] located in the far-right
column to modify, ignore, and (for manually added components), delete components or subprojects from the BOM.

When you edit a component (using the BOM or Source tab), an information icon ( [image: Information icon] ) appears in the table row to indicate that a manual adjustment was made to this
component:

  
 [image: BOM page with adjustment]   

Click [image: Information icon] to open the Component Details dialog box which displays the edits made to this
component.

The data table has the following columns:

- First column
- Component
- Source
- Match Type
- Match Score
- Usage
- License
- Vulnerabilities
- Cryptography
- Operational Risk

## First column (N/A)

Icons shown to the left of the component or subproject name:

- [image: Policy violation icon]
  Policy
  violation.
- [image: Policy violation overriden icon] Policy violation has been overridden.
- [image: Unreviewed icon] Component or subproject has not been reviewed.
- [image: Reviewed icon] Component or subproject has been reviewed.

## Component column

The Component column lists the names and versions of all open source and third-party
components and AI models identified in the selected project version, as well as any
subprojects that
have been added as components. Each entry represents a specific component version or
subproject and serves as a link to more detailed information, including licence,
security, and usage data.

Components shown are top-level (parent) and subcomponents (children).

AI models are
marked with a distinctive icon ( [image: AI model icon] ) in the component list. This visual indicator appears at the beginning of
the row, preceding the model name.

- Selecting a component opens a slide-out
  panel for quick review or allows navigation to the full component
  details page.
- Select the version number to open Black Duck KB component version page which
  displays a list of the projects and project versions in which this version
  of the component is used.
- Select **?**, which indicates an unknown version, to open the Black Duck KB component page which provides
  general information about the component.
- Mouse over the component to view the origin and origin ID.

  If the component version has multiple origin IDs, they will be listed in the
  popup.

  [image: Component version with multiple origins]

  Note: If a component has more than one origin for a
  version, the table displays the highest risk values.

  If the component version's origin is not specified, the popup will notify you
  that the license risks for this component are estimated and that you should
  manually specify a version for a more accurate result.

  [image: Unknown component version popup]

  If the component's version cannot be identified, the popup will indicate as
  such.

  [image: Component version origin not identified]

## Source column

For components: Number of archives or files that match. For example: [image: Number of matches]

For automatic matches, the number of files that were identified in the component scan
and matched to this version of the component appears. Select the text to open the
Source tab.

For subprojects: Number of components in the subproject. For example: [image: Number of components]

Select the value to open the BOM for this project version. The BOM only appears if
you have permission to view the project.

## Match type column

Indicates how the match between the component in use in this version of your project
and a specific version of a project in Black Duck KB was made.

Possible values are:

- **Binary**. Binary match from Black Duck Binary
  Analysis.
- **Direct Dependency**. Direct dependency identified via package manager
  scanning.
- **Direct Dependency Binary**. Direct dependency identified from the Black
  Duck Binary Analysis.
- **Exact Directory**. Exact directory match from Signature scanning or
  Binary Analysis.
- **Exact File**. Exact file match from Signature scanning or Binary
  Analysis.
- **File Dependency**. Deprecated and no longer used.
- **Files Added/Deleted**. A fuzzy signature match to a directory where some
  of the OSS component's files were added, deleted, or modified in the scanned
  archive. This may be a match to a previous or subsequent version of the
  component, which might have been missing from Black Duck KB at the time that the match was made.
- **Files Modified**. A fuzzy signature match to a directory where some of
  the archive files were modified. This may be a match to a previous or
  subsequent version of the component, which might have been missing from Black Duck KB at the time that the match was made.
- **Manually Added**. Component manually added to BOM in Black Duck.
- **Manually Identified**. Manually identified BOM component related to
  signature match files.
- **Manually Identified Package**. Manually identified BOM component related
  to a identified package manager package.
- **Partial**. Deprecated no longer used.
- **Snippet**. Snippet scanning identified a portion of code in your file
  that matches code in one or more KnowledgeBase files. More details about
  snippets can be found [here](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/59beaead48c23a29152a540d3a038714.topic).
- **SBOM**. Imported from a SBOM.
- **Transitive Dependency**. Transitive dependency identified via package
  manager scanning.
- **Transitive Dependency Binary**. Transitive dependency identified from
  the Black Duck Binary Analysis.

When viewing Components in the various views (Component Tab, Source Tab, etc),
precedence of "Direct Dependency" over "Transitive Dependency" is given. If the
source hierarchy has a component as both a Direct and Transitive Dependency, the
"Match Type" field will always show that component as a Direct Dependency even when
viewing the transitive dependency in the Source Tree.

The following are automatic matches from an imported Protex BOM:

- **Exact**
- **Partial**
- **File Dependency**

Click here for more information.

The match type for subprojects is **Manually Added**.

## Match score column

Indicates the level of confidence that a particular matched component is in fact the
component and version displayed.

[image: image]

The overall match score is calculated based on two factors:

1. Degree of ambiguity: The number of possible matches for this component
   (including the one selected in Black Duck).
2. Percentage of KnowledgeBase artifact matched: This value represents the
   percent of a KnowledgeBase Download from the BOM Entry's data which matched
   the customer's scanned data. The KnowledgeBase's representation of the BOM
   Entry may have many downloads. The % of KnowledgeBase Artifact Matched is
   based on the Download with the highest percent match to the customer's
   scanned files.

The match score value does not change after a BOM component (resulting from a
signature scan) is edited or modified.

Note: Manually added components and components imported from SBOMs will always display
100% match confidence.

Important: When SCASS is enabled in Black Duck SCA, match scores are returned for package
manager scans.

The match score will appear as one of two colors:

- Yellow if the score is within the "warning" threshold
- Gray otherwise

Clicking on a match score displays a small popover that reveals the additional
details about the match score (including the other values discussed above):

[image: image]

## Usage column

For components: Indicates how this component is intended to be included in the
project when this version is released. For example, if scanning identified
development tools in scanned code or a Docker image, you will want to indicate in
the BOM that they will not actually be included in the released version of the
project.

Tip: To remove components from the project version's
risk calculations because they will not be released with the project, exclude them from the BOM.

The possible usage statuses are:

- **Dynamically linked**. A moderately-integrated component that is
  dynamically linked in, such as with DLLs or `.jar` files.
  This is the default value.
- **Statically linked**. A tightly-integrated component that is statically
  linked in and distributed with your project.
- **Source Code**. Source code such as `.java` or
  `.cpp` files. Could be used when packaging a component's
  sources with the build, a binary, or distribution; usually due to open
  source requirements.
- **Separate Work**. Intended for loosely-integrated components. Your work
  is not derived from the component. To be considered a separate work, your
  application has its own executables, with no linking between the component
  and your application. An example is including the free Acrobat PDF Viewer
  with your distribution media.
- **Merely Aggregated**. Intended for components that your project does not
  use or depend upon in any way, although they may be on the same media. For
  example, a sample version of an unrelated product included with your
  distribution.
- **Implementation of Standard**. Intended for cases where you implemented
  according to a standard. For example, a Java spec request that ships with
  your project.
- **Prerequisite**. Intended for components that are required but not
  provided by your distribution.
- **Dev. Tool / Excluded**. Component will not be included in the released
  project. For example, a component that is used internally for building,
  development, or testing. Examples are unit tests, IDE files, or a
  compiler.
- **Unspecified**. The usage for this component has not yet been determined.
  You can use **Unspecified** to indicate that you need to investigate the
  usage of this component.

For subprojects, usage defaults to **Dynamically Linked**, as described above.

## License column

Declared license of the component or subproject in use in this version of your
project.

- [image: high license risk] indicates that the component/subproject has a high license risk.
- [image: medium license riskv] indicates that the component/subproject has a medium license
  risk.
- [image: low license risk] indicates that the component/subproject has a low license risk.
- [image: no license risk] (white box) indicates that there is no license risk.

For known licenses, select the license name to view license details and license
text.

In the component list view, if the license text on the BOM page indicates that there
is more than one license for this component version (for example the text states
"Apache 2.0 and 3 more..."), hover over the license name to view the names of all
licenses.

Click here for more information on how license risk for a component is
determined.

## Vulnerabilities column

Number of critical/high or high risk (100% red), medium risk (50% red), and low risk
(100% gray) vulnerabilities associated with this version of the component or with
the subproject:

  
 [image: High, medium, and low security risk icons]   

Select a value to open the project version page Vulnerabilities tab which displays the vulnerabilities for
that component or subproject. If the component has an unknown version, a modal will
be displayed detailing the estimated security
risk for the component.

  
 [image: image]   

For subprojects, the value shown is the total number of vulnerabilities for all
components. Note that the values shown here may not match the values shown on the
subproject version's BOM page as that lists the number of components with a
vulnerability.

Note: If you do not have permission to view the project, you will
not be able to access this page.

Attention: Risk counts do not include items that are in match review.

## Cryptography [image: image]

Indicates that this component version has encryption algorithms.

## Operational risk column

Operational risk level for the component or subproject in use in this
version of your project:

- [image: High operational risk] High risk
- [image: Medium operational risk] Medium risk
- [image: Low operational risk] Low risk

The operational risk level in this version of your project is calculated using a
combination of:

- Version status. Part of the component's operational risk calculation is based
  on the version of the component used compared to the number of newer
  versions that have been released and the time since the newest version was
  released. Using older versions of a component is considered risky when newer
  versions are available.
- Activity status. Part of the component's operational risk calculation is
  based on the commit activity trend for the component over the last 12
  months. Increasing or stable commit activity over the time frame is
  considered less risky than decreasing commit activity over that time
  frame.

The final operational risk will be the higher of these two risk calculations. [HUB-5341]

In the component list view, for components, hover over the value to view the factors
that determined the value shown:

  
 [image: Operational risk - hover view]   

In the component list view, for subprojects, hover over the value to see the number
of components in this project version for each operational risk level:

  
 [image: number of components - operational risk]   

Note: The values shown here may not match the values shown on the
subproject version's BOM page. As a subproject, the value shown is the total number
of components that have an operational risk. As listed on the BOM page, the
operational risk values are for top-level components.

## Component slide-out panel

When you select a component, subproject, or AI model from the Components column, a slide-out
panel opens from the right side of the page. This panel provides a quick summary of
important information without navigating away from the Bill of Materials view.

The slide-out panel for component and subproject includes:

- **Vulnerabilities**: The number of known security vulnerabilities
  associated with the component.
- **License**: The license associated to the component version.
- **Upgrade Recommendation**: Suggested versions, if any, to remediate known
  vulnerabilties or policy violations. Short-term typically reflects upgrading
  a component's minor or patch version. Long-term will focus on upgrading a
  component's major version.
- **Source**: The origin of the component.
- **Fields**: Values such as CPE, PURL, and any populated custom fields.
- **More Details**: Additional information such as component links, description,
  tags, and approval status.

The slide-out panel for AI models includes:

- **Source**: The origin of the AI model.
- **More Details**: Additional information such as model description, tags, and approval
  status.

Clicking the link at the top of the slide-out panel opens the corresponding page for the
component, component version, subproject, or AI model depending on the type of item
selected.

## Understanding direct and transitive dependencies

When analyzing your project's bill of materials (BOM), it's important to understand
the difference between direct and transitive dependencies:

- **Direct dependency**: A component that your project explicitly declares and includes in
  its code or configuration files. These are dependencies you directly add to
  your project.

  For example, if your project's configuration file includes `library-A`, then
  `library-A` is a direct dependency.
- **Transitive dependency**: A component that is not directly declared by your project, but
  is required by one of your direct dependencies. These are automatically
  included through the dependency chain.

  For example, if `library-A` (your direct dependency) includes
  `library-B`, then `library-B` is a
  transitive dependency in your project.

Understanding this distinction helps you make informed decisions about risk,
remediation, and license compliance when managing open source components in your
project.
