---
title: "Triaging issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triaging-issues.html"
content_id: "NwVLBkD5_G72HZFqmPCF9Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:46:59.444216+00:00"
---

# Triaging issues

After viewing an issue in the Source pane (see Managing issues), you can
triage it by using the Triage pane to modify
one or more of its attributes.

Figure 1. Example: Triage pane
  
 [image: image]

Figure 1 shows the default attributes and a
built-in attribute (Legacy, which is not displayed by
default):

- Classification (default)
- Severity (default)
- Action (default)
- Legacy Target (built-in attribute)
- External (Ext.) Reference
  (default)
- Owner (default)
- Comment (default)
- **Deprecated Value** - This selection box allows you
  display attributes that have been marked as deprecated, or change the attribute
  value to a non-deprecated value. Administrators can designate an attribute as
  deprecated in the Configuration - Attributes page.

  If you select this option, you can see the deprecated attribute value, but cannot
  change the attribute value. If this option is not selected, you can change the
  attribute to any value (that has not been designated as deprecated).

Note: The attributes that you see in Figure 1 might
not match the attributes you see in your Coverity Connect instance because Coverity
Connect administrators can create and modify these attributes.

You can use filters to
find issues based on attributes in the Triage pane. For example, you might create a
view that finds all issues that are
classified as Bug. For details about the filter criteria that
you can use, see Filters.

Triaging multiple issues
:   It is possible to triage multiple CIDs at the same time after selecting all
    of them at once from the View pane, as shown in Figure 2.

    Figure 2. Example: Triaging multiple issues
      
     [image: image]

Selecting triage stores to update
:   If you can perform advanced triage on a CID, the Applying to all
    stores in the project button will appear below the Comment
    field in the Triage pane for that CID.

    Figure 3. Select triage stores
      
     [image: image]

    By default, Coverity Connect selects all triage stores that contain the
    CID. The button shown below the Comment field in Figure 3 opens to the
    advanced triage window (Apply Scoped... shown below),
    where you can select or deselect any triage stores that it lists. (Note that
    if all the streams in the project are associated with the same triage store,
    or if you only have permission to triage issues in one of the triage stores,
    the button will not appear because there is only one triage store that you
    can update.)

    Figure 4. Apply Scoped triage
      
     [image: image]

When triaging a single issue, you can also examine the following:

**CWE documentation**

- Links to the Common Weakness Enumeration documentation of the issue. For example,
  Figure 1 includes the [CWE-459](http://cwe.mitre.org/data/definitions/459.html) link to information on incomplete
  cleanup.

**Projects & Streams section**

- Identifies all streams in which the CID occurs in the current
  project. This section also links to other projects containing the CID.

**Detection History**

- Provides the history of when and in which snapshot the CID was first ever
  detected by Coverity analysis tools and last detected by Coverity. It also shows
  in which stream(s) the CID exists.

**Triage History**

- Provides information about changes to the triage states of the CID, such as
  classification, owner, comment, and so forth.

  You can select the Show only commented entries option to
  display only the history of the comments for the given CID.

  Figure 5. History section
    
   [image: image]

**Occurrences**

- Provides information about each instance of the CID that occurs in the
  current project. The pull-down menu at the top of this section contains
  instances in the other streams to which you have access in the project, allowing
  you to view the occurrence data for each.

  Each CID can have multiple occurrences, and each occurrence (also known as an
  instance) has a set of events that lead to the issue. See the
  Occurrences section in Figure 1. The example shows one occurrence
  of CID 10006, with three events. To view event information in the Source pane,
  click the individual event in this section. If necessary, the source will be
  reloaded.

  Coverity Connect keeps track of the total number of occurrences, recorded and
  unrecorded. When committing, Coverity Connect can store up to 15 occurrences of
  an issue. For example, if a function has a buffer that is overflowing with 20
  separate instances, then only 15 are recorded.

  The database stores all occurrences of an issue, but the
  Occurrences panel displays only the last 15. To see
  the total count, check the Count column in Coverity Connect while in Issues mode.

  For issues with more than 15 stream occurrences, the Projects &
  Streams panel displays only the last 15 streams. All project
  occurrences are displayed. To view an issue in a stream not shown in the panel,
  filter by that stream. The filtered stream replaces the last entry in the
  panel.

  You can use the property `allowAllDefectInstances=true` defined in
  `cim.properties` to disable the 15 occurrences-per-issue
  limit, and all occurrences will be recorded. However, be aware that this can
  lead to a drastic increase in database size. For this reason, the property is
  false by default.

  Coverity Connect also tracks (internally) the number of merged defects, which are
  sets of nearly identical instances in a data structure.

  Note: The number of stored occurrences does not affect the numbers of issues
  displayed by Coverity Connect. It also does not affect the number that is
  reported by the report generators, as they include merged defects into their
  count.

**Standard Attributes**

- The Standard Attributes panel displays standard-attribute
  value-description pairs associated with the selected CID. Value-description
  pairs are displayed only for standard-attribute columns that both have a value
  (other than None) and are enabled.

  If no standard-attribute column is enabled, the panel displays
  None for the selected CID (even if the selected CID
  has standard attributes whose values are not None).

  If all enabled standard-attribute columns have a value of
  None, the panel displays
  None.
