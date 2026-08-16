---
title: "Planning your project and stream configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/planning-your-project-and-stream-configuration.html"
content_id: "gkgpMLokpPS4OM0y4MmuLA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:58.335804+00:00"
---

# Planning your project and stream configuration

To effectively view and manage the data on issues in your code base, you need to think
carefully about how to set up streams for your code base and how to organize those
streams into Coverity Connect projects.

The following figure provides examples of possible Coverity Connect stream configurations
for two products. Product 1 contains a development branch and an
integration (trunk) branch. Each branch has one assumed target (represented by dotted
lines). Product 2 also contains a development branch and a trunk
branch, but in this case, both branches are built for two target platforms.

Figure 1. Coverity Connect streams
  
 [image: image]

In this example, there are six possible streams. Certain streams, or combinations of
streams, are useful to certain roles within your enterprise. For example:

- Developers might be interested in branches for a specific product. Developers for
  Product 1 will focus on Stream 1
  or Stream 2. Developers for Product 2
  will focus on Stream 3 and Stream 4,
  or Stream 5 and Stream 6.
- QA engineers might be interested in a particular platform target, so they will
  focus on each individual stream, Stream 1 through
  Stream 6.
- A Program manager might want to monitor the integrity of all of the products on a
  particular branch, so a person in this position will focus on Stream
  1, Stream 3, and Stream
  4 of the Dev branches, and Stream
  2, Stream 5, and Stream
  6 of the Trunk branches.

Coverity Connect allows you to organize your streams into projects to give you easy
access to the most important information for your job. The following figure focuses on
Product 2 in Figure 1 and shows how the streams can be
associated with projects appropriate to the role discussed above:

- Project 1 through Project 4 contain
  individual streams for use by QA engineers.
- Project 5 contains Stream 3 and
  Stream 4. Project 6 contains
  Stream 5 and Stream 6. Both
  projects are organized by branch for use by developers and program
  managers.

Figure 2. Coverity Connect projects
  
 [image: image]

Note: If you want to associate the same stream with multiple projects, you can use stream
links. For more information, see Associating a stream with multiple projects and Primary projects and stream links.
