---
title: "Error handling with commands"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/error-handling-with-commands.html"
content_id: "UlBOgnl2WfEvKlOanM2kug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:07.488922+00:00"
---

# Error handling with commands

In general, commands return a non-zero exit code whenever there is a catastrophic failure
that prevents the command from proceeding. If a command appears to fail while still
returning an exit code of zero, there are two possibilities: either the failure that
appears to be reported did not prevent the command from continuing to run and is merely
a warning, or the command is not behaving properly, file a support ticket here:
<https://community.blackduck.com/s/contactsupport>.

The exceptions to the previous rule are the `cov-build`
and `cov-translate` commands. The `cov-build` command
returns a non-zero exit code when either there is a fatal error while attempting to
initialize the `cov-build` command's state before launching the build
command, or when there is a non-zero exit code from the build command specified on the
command line. If build failures are due to incompatibilities in the analyzed source
code, and if the error does not cause the native compiler to fail and the build to exit,
`cov-build` does exit with a non-zero status code. You can change
this behavior by using the option `--return-emit-failures`.

The `cov-translate` command is an exception to the
previous rule for the same reason. It does not return a non-zero exit code if
`cov-emit` fails to compile a source file. By default, the
`cov-translate` command ignores errors that do not prevent it from
attempting compilation. If you are calling `cov-translate` directly and
wish to receive a different return value for compilation failures, you can specify the
command-line option `--fail-stop`. For more information about this
option, see The 'cov-translate' command in place of the native compiler.
