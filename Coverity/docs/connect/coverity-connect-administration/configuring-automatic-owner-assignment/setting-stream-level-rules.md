---
title: "Setting stream-level rules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-stream-level-rules.html"
content_id: "941TYuNSkKdTfKy_Xl3AUw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:32.115116+00:00"
---

# Setting stream-level rules

The Owner Assignment tab allows you to set the owner assignment
rule that will compute automatic owner assignment for issues displayed in Coverity
Connect.

Figure 1. Stream settings for automatic owner assignment
  
 [image: image]

1. Go to Configuration > Projects & Streams.
2. Expand a project to see the list of streams.
3. Select the stream for which you want to apply the rule.
4. Select the Owner Assignment tab.
5. Click Edit and choose one of the following rules:

   Set to component's default owner.
   :   The owner will be the default component owner for a component
       configuration. This option is the default and will not trigger
       Coverity Analysis to attempt to retrieve any SCM historical data. If
       this option is selected, but the component to which the stream
       belongs does not have the default owner assigned, the owner will be
       left as Unassigned for the issue.

       For more information, see Using components.

   Derived from SCM (Source Code Management)
   :   The owner will be based on the SCM Derivation Rule set in Table 1.

   None (leave issues unassigned)
   :   Unassigned Issues will not automatically be assigned an owner. The
       Owner field in Coverity Connect will be
       left as Unassigned.

   This tab assigns owners for unassigned issues in the selected stream. Owners will
   be assigned when new snapshots are added based on the owner assignment
   rules.
