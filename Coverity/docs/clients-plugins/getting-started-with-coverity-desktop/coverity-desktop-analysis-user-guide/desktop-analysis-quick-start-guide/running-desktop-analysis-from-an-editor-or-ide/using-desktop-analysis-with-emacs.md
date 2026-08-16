---
title: "Using Desktop Analysis with Emacs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-desktop-analysis-with-emacs.html"
content_id: "VQf0OQW7kOXptC6vXBE90w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:47.615744+00:00"
---

# Using Desktop Analysis with Emacs

To run Desktop Analysis from within Emacs, arrange to run
`cov-run-desktop` such that Emacs thinks it is running a compiler.
It will then parse the defect output as compiler syntax errors and navigate to them
accordingly. The Coverity Analysis tools include an example elisp
function to do that:

<install_dir>/doc/examples/desktop-scripts/coverity.el

To use this script, first load it. For example, copy it to the
.emacs.d subdirectory of your home directory, then add to your
.emacs or .emacs.d/init.el file the
following lines:

```
(if (file-readable-p "~/.emacs.d/coverity.el")
  (load-file "~/.emacs.d/coverity.el"))
```

Then, restart emacs. Now, navigate to a source file in a directory underneath where
coverity.conf is installed and type "`M-x
coverity`" (Alt-X, "coverity", Enter) or hit `M-F9` (Alt
F9).

This command will invoke `cov-run-desktop`, passing the current file's
name as an argument, in the directory where the open file is located.
`cov-run-desktop` will then search upward in the directory tree for
a coverity.conf file, which must exist for this command to work, as
it contains required information such as the server connection parameters. The console
output of `cov-run-desktop` will then be parsed by Emacs the same way
as compiler syntax errors. Use "`M-g n`" (Alt-G, "n") and "`M-g
p`" to navigate forward and backward through the "errors", which are in
reality defects and events detected by Coverity Desktop Analysis.
