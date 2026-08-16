---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "gl5G0b1vvY8SJJIMlhQJKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:57.745334+00:00"
---

# Options

--checkoutPath <reponame> <path> <commit_hash>
:   This option can be provided more than once if there are multiple checked-out
    repositories within the code directories that are analyzed. Together with
    the GitHub URL, this allows any analyzed filepath to be converted to a
    GitHub URL that can be used to display the source code.

    - <reponame> - the GitHub repository name in <user>/<repo> format
    - <path> - the file path to the checked-out repository.
    - <commit_hash> - the commit hash that was checked out.

--githubUrl <url>
:   The base GitHub URL used to access repositories. If omitted, this defaults to
    <https://github.com>.

--inputFile <filename>
:   A JSON file containing the Coverity Analysis results to be converted into
    SARIF.

    Coverity Analysis results should be provided in the "v10" JSON format produced by the
    --json-output-v10 option of the
    cov-format-errors command or the
    cov-run-desktop command. (For more information about
    the v10 format, see "Desktop Analysis JSON output syntax" in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.)

--outputFile <filename>
:   The file where to write the SARIF result.

--repoName <reponame>
:   The main GitHub repository under analysis in the form <user>/<repo>.
