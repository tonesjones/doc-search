---
title: "Run cov-run-desktop --setup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/run-cov-run-desktop-setup.html"
content_id: "gnd3pa~KfFtcEm5mWdYfDw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:44.771869+00:00"
---

# Run cov-run-desktop --setup

Run the following command:

```
> cov-run-desktop --setup
```

This will first attempt to create an "authentication key". It prompts for your
Coverity Connect password. Once the key is created, you will not have to enter your password
again to use desktop analysis.

It then configures your compilers and filesystem capture. The default configuration works for
GNU, Microsoft, Oracle Java, Kotlin compiler and Clang compilers, as well as all
filesystem capture languages that Coverity supports on your platform.
See `compiler_configurations` if you are using
another compiler or need customizations such as different file extensions for filesystem
capture.

Finally, it runs the `clean_cmd` and `build_cmd` in
coverity.conf (if non-empty) to capture a clean build of your
compiled code so that Coverity tools know how to compile all of your compiled source
files.

To capture compiled code not captured during `--setup`, such as adding new files
to your project, use `cov-run-desktop --build <build_cmd>`, where
`<build_cmd>` only has to compile the uncaptured files.
If the command lines to compile the source files change, you will need first to delete the contents of the
intermediate directory, idir/, and then run `cov-run-desktop --setup` again.

You can avoid manual recompilation by configuring a script to compile specific files on demand
(see Compiling files on demand for details).

Note:
Interpreted code does not depend on compiler invocations, and so it will be captured automatically later, as needed.
