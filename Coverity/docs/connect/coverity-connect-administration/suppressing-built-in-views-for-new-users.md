---
title: "Suppressing built-in views for new users"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/suppressing-built-in-views-for-new-users.html"
content_id: "5UGY1IwecCW1IFR8uAwszg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:54.601607+00:00"
---

# Suppressing built-in views for new users

Coverity Connect allows you prevent the display of any of the built-in views from new users. This feature is useful for any
views that are not needed by your company. This process requires you to modify a
Coverity Connect properties file.

For example, if you want to suppress the built-in Low Impact
Outstanding and Medium Impact Outstanding views,
you need to add the following line to cim.properties (located in
<install_dir>/config):

```
suppressedFactoryViews=issues.mediumimpactoutstanding,issues.lowimpactoutstanding
```

Note: You do not need to restart Coverity Connect after suppressing views through
cim.properties.

This change affects new users only. You
cannot suppress the views from users who already have them. However, the users could
delete the views through the UI. See Delete.

Table 1. Coverity Connect view properties

| View Type | Internal View Type Property | View Name | Internal View Property |
| --- | --- | --- | --- |
| Issues: By Snapshot | issues | High Impact Outstanding | highimpactoutstanding |
| Outstanding Untriaged | alluntriaged |
| My Outstanding | myoutstanding |
| Outstanding Defects | outstandingdefects |
| Outstanding Security Risks | outstandingsecurityrisks |
| Outstanding Test Rules Violations | outstandingtestruleviolations |
| Issues: Project Scope | issues | All in Project | allinproject |
| Files | files | In Latest Snapshot | inlatestsnapshot |
| Uncovered By Tests | uncoveredbytests |
| Functions | functions | High CCM (>15) | highccm |
| In Latest Snapshot | inlatestsnapshot |
| With Outstanding Issues | withoutstandingissues |
| Uncovered By Tests | uncoveredbytests |
| Components | components | All In Project | allinproject |
| High Issue Density (> 1) | highdefectdensity |
| With Outstanding Issues | withoutstandingissues |
| With Untriaged Issues | withuntriagedissues |
| Checkers | checkers | All In Project | allinproject |
| Owners | owners | All In Project | allinproject |
| Snapshots | snapshots | All In Project | allinproject |
| Tests | tests | All Tests | inlatestsnapshot |
| Currently Failing | currentlyfailing |
