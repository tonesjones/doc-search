---
title: "Creating policy rules for approved or barred items"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-policy-rules-for-approved-or-barred-items.html"
content_id: "mH0tXNNFmcL7lKyQBfW3Cg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:13.267163+00:00"
---

# Creating policy rules for approved or barred items

You can create policy rules that enforce your company's policy of approved or barred
items. For example, you can create a policy rule to:

- pre-approve a component version in your BOM: any component version that does not
  match your approval list triggers a policy violation.
- bar a component version from your BOM: a policy violation is automatically
  triggered for any component version that matches your list of barred
  components.

## Pre-approved policy rule examples

Suppose you want to create a policy rule whereby externally distributed projects with
permissive licenses are pre-approved: any component versions that have
non-permissive licenses will trigger a policy violation.

To create this policy rule, follow the instructions for creating a policy rule, and
set these conditions:

  
 [image: policy conditions]   

Suppose you want to create a policy rule whereby only a specific version of a
component is approved: all other component versions trigger a policy violation.

To create this policy rule, follow the instructions for creating a policy rule, and
set these conditions:

  
 [image: policy conditions]   

In this example, a policy violation is triggered when the Apache Tomcat version is
not 8.0.1.

Suppose you want to create a policy rule whereby multiple versions of a component are
approved: all other component versions trigger a policy violation.

To create this policy rule, follow the instructions for creating a policy rule, and
set these conditions:

  
 [image: policy conditions]   

In this example, a policy violation is triggered when the Apache Tomcat version is
not 8.0.1 or 8.0.3.

To create this condition:

1. Select the component, the equals operator, and the component.
2. For the second condition: select the component, the 'not in' operator, and
   the approved versions. To select multiple versions, select the version and
   click **Set selected component**, Repeat selecting approved versions and
   clicking **Set selected component** until all approved versions are
   selected.

## Barred policy rule example

Suppose you want to create a policy rule whereby any component versions in SaaS
distributed projects in the development or planning phase with licenses in the AGPL
license family trigger a policy violation.

To create this policy rule, follow the instructions for creating a policy rule, and
set these conditions:

  
 [image: policy conditions]
