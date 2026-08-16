---
title: "Find component upgrade guidance"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/find-component-upgrade-guidance.html"
content_id: "Ss1aEZueiXCKC7r0P0bmfA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:33.567890+00:00"
content_hash: "f85cd3028ee7270b94328bca5e748e6b1a042f56b42442afa78c202666b6110b"
---

# Find component upgrade guidance

How to find upgrade guidance for the vulnerable components in a project.

After you run an SCA test, follow these steps:

1. Go to Portfolio, select an application, select a project, and open the Components tab.
2. Select a component.

   The Component Details tab opens. Find Upgrade Guidance on the right.
     
    [image: transitive guidance]   

   Use the Component Origins dropdown menu to select different origins. Each origin represents a location (like GitHub, Maven, Linux distros, ... etc.) from which the same component is obtained.

   Note: If the component origin you select is a transitive dependency of another component in the project (in this example, **org.apache.tomcat:tomcat-api:7.0.65** is a transitive dependency of **org.apache.tomcat:tomcat-jasper:7.0.65**), upgrade guidance is categorized. Use upgrade guidance under For Direct Dependencies to update the parent component.

   Upgrade Guidance may include:

   - A Short Term Recommendation: An upgrade that maintains the component's major version number.
   - A Long Term Recommendation: An upgrade that changes the component's major version number.
