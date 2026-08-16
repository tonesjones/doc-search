---
title: "Reviewing basic CodeXM concepts and exercises"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reviewing-basic-codexm-concepts-and-exercises.html"
content_id: "54QLtxj2B2k1LmpGbI428w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:38.071554+00:00"
---

# Reviewing basic CodeXM concepts and exercises

Let's take a moment to assimilate what we've learned.
(If you haven't gone through the QuickStart tutorial, please do so now.)

CodeXM checkers examine your project's source code by looking for specific kinds of code constructs.
These can be fairly simple (like specific statement types) or they can be much more complex.
More sophisticated checkers (which we'll take a look at later on), look for more complex patterns.
The main idea is that CodeXM checkers look for patterns.

## Further exploration

Now that we know how to write a basic checker that finds `goto` statements
(using the `gotoStatement` pattern we invoked in the QuickStart), try modifying your `NO_GOTO` checker
to look for an `ifStatement` pattern, `forLoop` pattern, and `returnStatement`.
Since any of these are likely to occur in your own code, you can just run the analysis against your code base.

You can also modify the `NO_GOTO` source file to include the new checkers.
Be sure to re-run `cov-build` so analysis will detect the changes you made.

To illustrate, in the next section we write a simple checker, named `VAR_DECL`, to detect all declarations of variables.
