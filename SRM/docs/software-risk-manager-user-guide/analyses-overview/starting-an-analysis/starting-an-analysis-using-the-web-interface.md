---
title: "Starting an Analysis Using the Web Interface"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/starting-an-analysis-using-the-web-interface.html"
content_id: "XGlKMGjK1jNwKsdPArntRg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:41.478744+00:00"
content_hash: "90cb50790073da7dfb09211cc032fdf1cfe18623d190df3076559d370a31e522"
---

# Starting an Analysis Using the Web Interface

Analyses can be prepared and initiated manually from the Software Risk Manager web
interface.

Note: To start an analysis, you will need a defined project and a current analysis
configuration.

**To start an analysis:**

1. Click the Projects icon on the navigation bar to open the Projects page.
2. Click the project's dropdown configuration icon and select New Analysis.
3. Select a target branch from the Target Branch dropdown menu.

   You can choose
   an existing branch or create a new one by typing a new (unique) name into
   the branch field. Entering text will also filter the existing branch
   names.
4. Click Add File to upload files for analysis.

   As you add files, they will be
   uploaded to the SRM server for identification. Once the server has
   identified the file contents, SRM will display the following information:
   - Detected Content
   - Tools to Run

   Use the checkbox on the tag to disable (or re-enable) that tag.
   Disabling a tag in the Tools to Run section will tell SRM not to run that
   tool, even though it is applicable to that file.
5. Click Begin Analysis.

   Analysis is conducted as a "job." The work order is
   placed in the job queue and will be executed once enough resources are free.
   Often, the time spent in the queue is negligible, but you might still see a
   message stating that the analysis has been queued. Once the analysis job is
   finished queueing, the analysis will begin. The page will display a timer to
   indicate the current duration of the analysis.

The actual duration of the analysis depends on several factors, including the following:

- *How big is your application?* An application's size is likely the most
  significant factor in determining the duration of an analysis. Smaller apps
  usually take around 30 seconds, medium-size apps can take tens of minutes, and
  large apps can take hours or more.
- *Is Software Risk Manager running tools for you?* If so, the analysis
  duration will include the time it takes to run these tools. The time it takes to
  run a tool on your application will usually grow as your application grows.
- *How much activity is going on in Software Risk Manager?* More activity by
  users of Software Risk Manager means more load on the database, which can slow
  down analysis to some degree.
- *How many findings can be discovered?* This is difficult to know ahead of
  time, but the number of tool results/findings in a project will also affect the
  analysis duration. In this manner, a small application with many vulnerabilities
  might take longer to analyze than a large application with very few
  vulnerabilities.

Once the analysis has been queued, it is safe to leave the page. The analysis will
continue in the background. Keep the page open, however, is recommended in order to see
any warnings or errors that might occur during the analysis.

If the analysis completes successfully, the analysis timer will become a link to the
Findings page. Any currently-opened Findings pages will be updated to reflect the latest
analysis results.

## Deploying Intelligent Orchestration

If your Software Risk Manager implementation includes Intelligent Orchestration (IO),
applying an IO policy to a project will generate *prescriptions* for the best
tools to use in analyzing the code. Those prescribed tools will be automatically
selected in the *Tools to Run* section of the New Analysis page. For more
information on Intelligent Orchestration, see Intelligent
Orchestration.

## Inputs from Git Repositories

If you set up a *Git
Configuration* for a project, the New Analysis page will
automatically include the latest contents of the configured branch of the configured
repository as an input.

Normally, Software Risk Manager will update the local clone and check out the
appropriate branch before sending the files to the analysis. As development is done
on that branch, analysis of that branch will change along with the contents. But if
you want to analyze a specific point in the repository, you can configure Software
Risk Manager to use a specific branch, commit, or tag by clicking on the underlined
section of the input. Select the branch, commit, or tag and click Use this.
