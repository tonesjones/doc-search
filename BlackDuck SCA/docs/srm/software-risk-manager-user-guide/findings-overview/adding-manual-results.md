---
title: "Adding Manual Results"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/adding-manual-results.html"
content_id: "EifacKmecnDXjnlYJKk5Yg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:13.716376+00:00"
content_hash: "bf5a055d42ea37b35f5a9a21c7731a17bb74caf9437a82cd8de3315af25555fe"
---

# Adding Manual Results

Software Risk Manager allows users with the *create* role to enter manual results to
Findings data.

**To add a manual result:**

1. Click the Projects icon in the navigation bar to open the Projects page.

   [image: image]
2. Locate
   the project and click the Project findings link to open the Project Findings page.

   [image: image]
3. Click Add Result.

   [image: image]
4. Enter a name for the result and select a detection method.
5. Add the required data to the "General Information" and "Contextual Information"
   fields.

   See the sections that follow for additional information on these
   sections.
6. Click Add Result.

## General and Contextual Information

Information entered under the *Contextual Information* section describes the result
itself. Expanding the *General Information* section of the form will allow values
to be specified that will be shared among all manual results of the same name.
Contextual information will override general information if specified. Note that this
form creates *results*, which can be thought of as "evidence" for a finding.
Multiple results may be correlated to a single finding. As with tool results, two manual
results will typically be correlated if they have the same CWE, Location, and Detection
Method, even if their names are different.

[image: image]

If the result name entered matches a rule in the current rule set, then the manual result will be associated with the general
information for that rule. In this case, the general information can only be changed by
revising the rule set. Both the general and contextual information will be included on
the details page.

[image: image]

The *Tool* field allows the user to state that the manually-entered result actually
came from a tool. The options available to this field are configured on the admin page,
in the *Allowed Tools*section.

The *Host* field allows the user to describe the "host" on which the result was
discovered. This normally will only pertain to results with the *Network Analysis*
detection method, but could also relate to *Dynamic Analysis*. Host data entered on
this field is considered "raw" data, (as opposed to the "normalized" data seen on the
*Hosts* page). Raw host data may be joined with "normalized" host data through
a process called "host normalization". By default, the "Include Host data for this
result" checkbox is unchecked. Check it to expand the host data editor.

[image: image]

The *CVE* field allows the user to enter any number of CVEs that correspond to the
result. By default, no CVEs are included. To start adding CVEs, click the *Add a
CVE* button. When typing in a CVE text box, you can optionally start by only
typing the numbers; the text box will fill in the rest for you. If your Software Risk
Manager server is able to access the internet, it can check whether the CVEs entered by
the user are real CVEs in the CVE database. This verification comes in the form of a
checkmark or an "x" on the CVE textbox. Blank or invalid CVEs will be ignored when
submitting the form.

[image: image]

Once you’ve completed the form, clicking the *Add Result* button at the bottom will
dismiss the form and update the *Findings* page with the new finding. A
notification will appear, indicating the ID of the finding to which the result was
correlated. To delete or edit a manually added finding, click on the finding's ID in the
*Findings Table* to access its details view. The result will appear in the
*Evidence* section, where there will be buttons to edit and delete it.
