---
title: "Desktop deployment model (local analysis)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktop-deployment-model-local-analysis-.html"
content_id: "7xkzAMgzu2ThQGVaAaxRmg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:40.642102+00:00"
---

# Desktop deployment model (local analysis)

This deployment model, which adds to the central Coverity Analysis build model, allows
developers to analyze code locally, and fix defects before checking their source code
changes into the repository, which means fewer issues reported in the central Coverity
Connect database. Desktop developers also have the ability to focus the analysis on a
specific set of source files, which speeds up the analysis considerably, and work with
issues directly within their editor or IDE.

[image: image]

It is suggested that the desktop model be deployed individually alongside a central build
and analysis. The central analysis should run periodically (perhaps nightly) in order to
maintain current analysis data for the full code base. Once this is in place, developers
can use Desktop Analysis to get rapid, accurate feedback from Coverity Analysis, drawing
on summary data from the central build.

Coverity provides the Desktop Analysis tool, which can be used in one of three ways: from
the command line, with a text editor, or with Coverity Desktop, a plug-in to the
Eclipse, Wind River WorkBench, QNX Momentics, or Visual Studio IDEs. Coverity Desktop
allows you to perform an analysis of your code, then view and triage any issues within
the IDE. For more information about Desktop Analysis, see the Coverity
Desktop Analysis
2026.6.0 User Guide.

The plugins for each IDE are designed to store various configuration settings in a file,
coverity.conf. The file can be stored in a directory that is
part of source control, so that developers working on a common code base will
automatically receive the same settings in some parts of their IDE.
