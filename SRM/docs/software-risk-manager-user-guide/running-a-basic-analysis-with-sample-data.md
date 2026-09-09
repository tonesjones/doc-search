---
title: "Running a Basic Analysis with Sample Data"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/running-a-basic-analysis-with-sample-data.html"
content_id: "pu~YvCNyUxduQkJY2OeNmQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:49.886615+00:00"
content_hash: "d1e9f32b597906f530b5805c5ab31c0f8ba4f9eb81fb6470458a7c51ae0f0a8b"
---

# Running a Basic Analysis with Sample Data

To provide an overview of how to use Software Risk Manager to run an analysis, the
following is an outline of the process:

1. Make sure SRM has been installed and configured.
2. Launch the app and log in.
3. Create a project.
4. Configure the parameters for a new analysis.
5. Upload the source files.
6. Manually start a New Analysis for the project.

   SRM will begin analyzing the
   code. (The analysis will run in the background until complete.)
7. Inspect the findings from the project Findings page or the Dashboard.

## Sample Data Sets

If you would like to use sample code for testing purposes, the following are some
datasets that are all intentionally vulnerable applications used for educational and
training purposes. They're referenced by their primary language, although some of
them are multi-language.

- Java - [WebGoat](https://github.com/WebGoat/WebGoat)

  We recommend you use one of the WebGoat
  released war files directly as the input for Software Risk Manager since
  those tend to package everything, including the source, bytecode, and
  third-party dependencies. For instance, try [this release](https://github.com/WebGoat/WebGoat-Legacy/releases/download/v6.0.1/WebGoat-6.0.1.war).
- .NET - [WebGoat.NET](https://github.com/jerryhoff/WebGoat.NET)

  Since the Software Risk Manager .NET
  scanners require compiled assemblies, you will need to download the
  WebGoat.NET source and build it on your machine. Instructions for how to do
  so are at the link above.

For the following datasets, you can configure your new project's *Git Config* to fetch the
source directly from GitHub using their git URL.

- Ruby on Rails - [RailsGoat](https://github.com/OWASP/railsgoat)

  git URL: <https://github.com/OWASP/railsgoat.git>
- JavaScript - [NodeGoat](https://github.com/OWASP/NodeGoat)

  git URL: <https://github.com/OWASP/NodeGoat.git>

For other datasets, we recommend that you browse GitHub for different projects and scan
some of them for testing purposes. Here are some queries to get you started:

- [Java](https://github.com/search?utf8=%E2%9C%93&q=language%3AJava&type=Repositories&ref=searchresults)
- [C](https://github.com/search?utf8=%E2%9C%93&q=language%3AC&type=Repositories&ref=advsearch&l=C)
- [C++](https://github.com/search?utf8=%E2%9C%93&q=language%3AC%2B%2B&type=Repositories&ref=advsearch&l=C%2B%2B)
- [PHP](https://github.com/search?utf8=%E2%9C%93&q=language%3Aphp&type=Repositories&ref=searchresults)
- [Scala](https://github.com/search?utf8=%E2%9C%93&q=language%3Ascala&type=Repositories&ref=searchresults)
- [Python](https://github.com/search?utf8=%E2%9C%93&q=language%3Apython&type=Repositories&ref=searchresults)
- [Ruby on Rails](https://github.com/search?utf8=%E2%9C%93&q=language%3Aruby+on+rails&type=Repositories&ref=searchresults)
- [JavaScript](https://github.com/search?utf8=%E2%9C%93&q=language%3Ajavascript&type=Repositories&ref=searchresults)
