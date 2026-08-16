---
title: "Using Desktop Analysis with Vim"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-desktop-analysis-with-vim.html"
content_id: "s2m0ZUGKD4t15Mf6qp~g5g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:48.268258+00:00"
---

# Using Desktop Analysis with Vim

As with Emacs, to use Desktop Analysis with Vim, invoke
`cov-run-desktop` so Vim thinks it is running a compiler. One minor
difference is that `cov-run-desktop` should be passed the
"`--text-output-style oneline`" switch, as that produces an output
format more suited to the way Vim displays and navigates syntax errors. An example
script that does this is included with the Coverity Analysis tools:

<install_dir>/doc/examples/desktop-scripts/coverity.vimrc

To load this into Vim, copy that file to someplace like the .vim
subdirectory of your home directory, and add the following lines to your
.vimrc file:

```
" load Coverity command
let coverity_vimrc = $HOME . "/.vim/coverity.vimrc"
if filereadable(coverity_vimrc)
  execute "source " . fnameescape(coverity_vimrc)
endif
```

Then start or restart Vim, and the "`:Coverity`" command will be defined.
Invoke it when editing a source file that is underneath the directory where
coverity.conf is installed to analyze that file. Use
"`:copen`" to see the error list, "`:cnext`" and
"`:cprev`" to navigate, and "`:cclose`" to close the
error list, among other commands. Web search for "vim quickfix" for additional commands
and documentation.
