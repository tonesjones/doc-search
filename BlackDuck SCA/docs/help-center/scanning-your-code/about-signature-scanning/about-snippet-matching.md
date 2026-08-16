---
title: "About snippet matching"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-snippet-matching.html"
content_id: "OcbO6WPeaGlCuKGqIlR7iQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:46.353817+00:00"
---

# About snippet matching

Snippets are small reusable pieces of computer code. A snippet of open source software
can easily find its way into your proprietary files. For example, a developer may find a
useful function from an open source program and cut and paste that code into their
program.

Snippet matching is beneficial to managing legal risk and detecting possible license
infringement. A snippet match occurs when a portion of code in your file matches code in
one or more KnowledgeBase files.

As the use of open source software is managed through licenses that allow you to use,
modify, and/or share the software under defined terms and conditions, it is important to
identify the open source software used in your proprietary code so that you can manage
the legal risk and detect possible license infringement. Although your proprietary code
may include only a portion of open source software code, you still must comply with the
license associated with that open source software.

Snippet matching finds these fragments of open source code used in your proprietary files
or open source files moved into your proprietary directories and matches that code with
open source code found in one or more Black Duck KnowledgeBase files. Though many of the
details are proprietary, the mechanism to find snippets is through creating “codeprints”
over the contents of scanned source files with a sliding window algorithm. Then, a
statistically relevant sampling of those codeprints is sent to the Black Duck
KnowledgeBase for matching and the results are presented to the user for review in the
Black Duck UI. Codeprints are a type of one-way cryptographic hash which cannot be
decomposed back into the original source code. Codeprints are analogous to fingerprints
used for crime scene investigation: a fingerprint can be used to identify a person, but
a fingerprint cannot be turned into that person. Codeprints allow the Black Duck
application to securely and accurately scan code for snippet reuse.

Typically, five to seven lines of average source code can generate a match depending upon
the density of non-ignored characters in the line of code. The scanner will ignore white
space, tabs, and other non-relevant characters (for example, lines of ******). One line
of code can generate a match if it has enough words/characters in it (see certain
javascript libraries). Very short lines of code may require more than 20 lines for a
match. So, the density of the information content over those lines plays a factor into
generating matches. However, other factors can also come into effect and Black Duck has
a variety of rules and exclusions to optimize the scanning process and reduce false
positives, but which can also impact what gets scanned and what is detected.

Click here for the list of
file extensions supported for snippet scanning.

## Snippet scanning process

All scanning methods have an option to enable snippet scanning. Enabling the snippet
scanning option scans files not identified as open source (proprietary files). The
methods to scan your code for snippets are by using:

- Signature Scanner command line
- Black Duck Detect Desktop
- Black Duck Detect

The process for snippet scanning is:

1. **Run component analysis**.

   The component scan is completed first. This identifies the open source
   components using directory/file-level signatures.
2. **Generate snippet codeprints**.

   If enabled, a second-pass snippet scan is performed. This scan analyzes the
   unmatched files in the initial component scan. For example, individually
   matched files or files in directories which are matched to open source
   components do not get scanned for snippets, as they have already been
   identified and to further scan them for snippets is unnecessary for the
   typical scanning process. The unmatched files are those which, under the
   component scan, did not show indications of being open source and have a
   file extension which indicates they are a source file. These files are the
   candidates for further analysis.

   Note that Black Duck analyzes only the first 1 to 4 MB of data for
   codeprints. The maximum snippet size can be configured within this range,
   with the default setting set to 1 MB.
3. **Perform snippet matching**.

   Snippet codeprints for the file candidates are generated and sent to Black
   Duck which then sends them to the Black Duck KB Snippet Matching Service.
   Depending upon the scan parameters selected (see below), Black Duck will
   send the codeprints for all files or only changed files (delta scans) to the
   Black Duck KB for matching. The matching service first looks for an exact
   file match before looking for a snippet match. If any matches are found for
   the file, a list of matches is produced and a heuristic is run to select the
   best match as a likely source. Due to the nature of using codeprints over a
   sliding window, fuzzy matches (inexact or modified textual areas from the
   original) can be detected. All the matches are then consolidated and
   available for review in the Black Duck UI.
4. **The user reviews match details**.

   Unlike components detected via signature or package management scans,
   components detected via snippet scans are not automatically added to the
   BOM. This is because the source of a snippet match can often be in many
   places. Black Duck attempts to choose the best match and show alternative
   options, but ultimately it is up to the individual users to review these
   matches and confirm them before they are added to their BOM. While
   reviewing, a user can look at the matched open source code and (optionally)
   compare their scanned code with the matched open source code. Please note
   however, that when viewing the matched area to an open source file, due to
   the nature of hashed-based scanning using a sliding window algorithm, the
   highlighted text is only an approximation of the matched area for references
   purposes. Parts of the match may exceed, and unmatched matched parts may be
   displayed, in this highlighted area.

Each snippet scanning option is discussed as follows.

## Using the Signature Scanner command line

If the **Snippets** feature is registered on your product registration, you gain access to
the following parameters:

- **--snippet-matching**. Using this parameter enables a two-phase approach to scanning.
  First, a signature scan is completed. Once the signature scan is completed,
  a snippet scan is performed on unmatched files or files belonging to
  unmatched directories/archives.

  Black Duck recommends using this parameter for snippet scanning.
- **--snippet-matching-only**. When using this parameter, a snippet scan is performed on
  unmatched files or files belonging to unmatched directories/archives; a
  signature scan is not executed, but it must already exist. Its purpose is to
  add a snippet scan to an already existing component scan.

  You must have successfully completed a full file scan prior to selecting
  this parameter, otherwise the scan will error.

  Note: Snippet-only scans require unmatched file retention to be enabled.

If you have the **Full Snippet Matching** registered on your product registration, you gain
additional snippet analysis capabilities, allowing for more comprehensive detection
of code matches. These parameters become available:

- **--snippet-matching-all-source**. First, a signature scan is completed. Once that scan is
  completed, a snippet scan is performed for all files with supported
  extensions (whether they belong to unmatched directories/archives or
  not).
- **--full-snippet-scan**. Selecting this parameter performs a snippet scan on *all
  applicable* files, regardless of if they have changed or not. It
  effectively overrides the delta scanning capability at the cost of scan
  performance. On a first time scan, as all snippet candidates are analyzed
  for matching, this parameter will have no impact.

  This parameter must be used with the **--snippet-matching** or
  **--snippet-matching-only** parameter:

  - With the **--snippet-matching** parameter: First, a component
    scan is completed whereby only files that have changed since the
    previous scan are scanned. Once that scan is completed, a
    snippet scan is performed on *all* snippet candidate
    files.
  - With the **--snippet-matching-only** parameter: A snippet scan
    is performed on *all* snippet candidate files; a component
    scan is *not* completed.

  Using this option may cause significant performance and scalability issues,
  and should only be used in extreme situations.. If you are interested in
  enabling this feature on your registration key, please contact Black Duck Support for assistance.

Click here for more
information on using the command line.

Note: Snippet scanning cannot be completed offline as it requires communication with the Black Duck server.

## Using Black Duck Detect Desktop

To enable scanning for snippets, select the select **Snippet Scanning** from
the **Settings** options and enable it. Selecting this option runs the
scanner using the command line **--snippet-matching** parameter, as described
above.

## Using Black Duck Detect

Use the **--detect.blackduck.signature.scanner.snippet.matching** property to
enable snippet scanning in Black Duck Detect. With this property
enabled, Black Duck Detect uses the command line
**--snippet-matching** parameter, as described above.

## Uploading source files for snippet matching

Black Duck provides the ability for you to upload your source files
so that BOM reviewers can see the file contents for reviewing snippet matches from
within the Black Duck UI. When source files are uploaded, Black Duck provides a side-by-side comparison of the source file to
the match which can help BOM reviewers in the evaluation and review of the snippet
match.

After your administrator has enabled source uploads, as described in the installation
guides, use the Signature Scanner and include the **--upload-source** parameter
when using the **--snippet-matching** or **--snippet-matching-only**
parameter.

## Reviewing snippet matches

It can be difficult to determine where a snippet of code originated; in other words,
which open source supplied the snippet of code. The matching process attempts to
select the best match for a snippet of code by selecting a component and version in
the following order:

1. Highest KB ranked component/version.
2. Highest license risk component/version.
3. Earliest version of component by release date.
4. Component with the most versions for which a match appears.

As snippet matching is an imprecise technique, snippet matches must be reviewed prior
to including these matches in your BOM. Use the **Source** tab, as described
here, to
determine if the snippet match is relevant; in other words, does this snippet belong
in your BOM? If so, determine if the snippet match is correct.

After reviewing the snippet match, add it to your BOM. The component is shown
with:

- Match type = Snippet
- Usage = Source Code

Any policies you have created execute.

## Retaining partial snippet identifications

By default, identifications you made to partial snippet matches are not retained in
subsequent snippet rescans.

You can change this default setting so that you can minimize the number of snippet
matches you need to re-identify: in the project's **Settings** tab, in the
**Snippet Adjustments** section, select **Apply IDs from partial snippet
matches to new exact file matches**.

## Snippet matches and Vulnerabilities

[HUB-16619, 16621]Black Duck does not include any vulnerabilities related to
components/versions that are identified through snippet matching *only*:
vulnerabilities are not counted when showing the total number of vulnerabilities for
a project/project version and are also excluded from vulnerability reports. Black Duck will add vulnerabilities/security risk identified by a
snippet match if another type match type (for example, exact) identified the same
component/version.

## Modifying the default maximum snippet file size

By default, Black Duck only analyzes the first 1MB of data for snippet codeprints.

You can modify this default value and select a value from 1MB to 4MB.

To modify the default maximum snippet file size:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Click **Scan** in the left-hand menu.
5. In the **Snippet Max File Size** section, enter a value from 1 to 4 to set the maximum
   file size in MB for snippet scanning.
6. Click **Save**.
