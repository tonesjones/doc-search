---
title: "Heatmaps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/heatmaps.html"
content_id: "REUGjlnE_9aDH8XV7r_3fg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:56.634209+00:00"
---

# Heatmaps

Tree, Sunburst, and Banded Trend maps divide your
code base into segments that are color-coded according to their level of compliance with
policies that you specify for them.
Higher-level map nodes reflect overall compliance based on policy-related data that is
aggregated from lower-level segments.

In addition to containing red (in violation), yellow (at risk), and green (in compliance)
segments, heatmaps can also contain gray segments. Data within the scope of a gray
segment (for example, the Libraries node in the following figure) is excluded from
higher-level segments that contain the gray segment. The gray segments might include
uninteresting or peripheral data on libraries, certain third-party code, infrequently
used legacy code, or some other area of your code base. (Note that the Other node is
blue because it has been selected.)

**Tree Map**

- Tree maps contain an all-inclusive root with branching segments.

  Figure 1. Example: Tree Map
    
   [image: image]

**Sunburst Map**

- The Sunburst map displays data in rings, with the center ring as the most
  inclusive node (for example, the root node) and the surrounding rings as
  segments of the parent ring. The segments of the Sunburst are sized according to
  the relative number of lines of code they represent. Otherwise, the Tree and
  Sunburst maps provide identical data.

  Figure 2. Example: Sunburst Map
    
   [image: image]

Notice that the Other node is selected in both Figure 2 and Figure 1 to display information about it in the
Other pop-up window. In addition to showing the issue density
value, this window provides a link to the issue list (see View
issues) for this node and allows you to display this node and any
subnodes it contains (see Go to this level).

**Banded Trend Map**

- The Banded Trend map applies policy bands to data in a trend report. Figure 3 shows the issue density for
  the past 10 weeks. It also shows the selection of the data point to reveal the
  precise issue density on the selected day.

  Figure 3. Example: Banded Trend Map
    
   [image: image]

The Tree and Sunburst maps can display up to four levels of the node tree. However, all
heatmaps provide navigation
breadcrumbs (located above each heatmap) so that you can view heatmap data
for a node at any level in the hierarchy (from the root, to any branch, to any leaf).
You can also save a heatmap to file and print out hard copies of the file (see Performing common Coverity Policy Manager actions).
In addition, you can add one or more heatmaps to a Coverity Policy Manager dashboard.

To set up a heatmap, see Setting up Coverity Policy Manager heatmaps.
