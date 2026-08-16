---
title: "Reviewing snippet matches"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/reviewing-snippet-matches.html"
content_id: "gaWRTY0k9VtHLDckPJO_dw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:44.074567+00:00"
---

# Reviewing snippet matches

Use the **Source** tab to determine if the snippet belongs in your BOM and if so, if
the snippet match is correct.

Click here for more information on using the **Source** tab.

## Snippets in the BOM

If a snippet scan has been run and snippet matches were found, a snippet badge
appears next to the risk charts in the BOM indicating the number of snippets that
need confirmation.

  
 [image: Snippet message in BOM page]   

By default, the BOM does not display your unconfirmed snippet matches. Unlike
reviewing a component in the BOM (which marks all instances of that component as
reviewed) snippet matches are confirmed on the match level. Only after a snippet
match has been confirmed will it appear unfiltered in the BOM.

  
 [image: BOM - unconfirmed snippet]

## Retaining partial snippet identifications

By default, identifications you made to partial snippet matches are not retained in
subsequent snippet rescans.

You can change this default setting so that you can minimize the number of snippet
matches you need to re-identify: in the project's **Settings** tab, in the
**Snippet Adjustments** section, select **Apply IDs from partial snippet
matches to new exact file matches**.
