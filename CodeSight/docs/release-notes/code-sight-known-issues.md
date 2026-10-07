---
title: "Code Sight Known Issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-known-issues.html"
content_id: "wY4khsnE_hv3UpV36zzZuA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:57.670640+00:00"
---

# Code Sight Known Issues

These are issues known to be present in the current Code Sight
release.

- **Eclipse Compatibility:**
  Code Sight is currently incompatible with Eclipse versions
  2025-12 and later due to a known upstream [Eclipse Equinox defect](https://github.com/eclipse-equinox/p2/issues/1119). Please use Eclipse
  2025-09 or earlier.
- When opening Code Sight Setting links under VS Code Settings
  > Extensions > Code Sight the open setting will not be
  loaded properly. This is because Code Sight does not support
  [Model Editors](https://code.visualstudio.com/docs/getstarted/userinterface#_modal-editors) yet. UD-16199

  **Workaround:**

  - Set `workbench.editor.useModal` to off.
  - Open the setting view via command pallete.
  - Click “Open Model Editor in Main View” on the modal. This will open
    Settings in a webview.
- Using an x86-architecture version of Eclipse or IntelliJ on an Apple silicon
  machine downloads the x86 Coverity tools instead of the Apple
  silicon tools. UD-12727
- In Visual Studio, on occasion, when you open an extremely large code base the
  Sigma language server (used for auto
  scanning) can fail to start. UD-12351

  **Workaround:** Restart Visual Studio. Usually this will resolve the
  issue. If the issue persists, please contact Black Duck Support.
- In Eclipse, opening a YAML file with the Generic Text Editor causes the issue
  markers to not display properly (for example, light bulb icons appear instead of
  the purple markers). UD-11150

  **Workaround:** Open the YAML file with the Text Editor. To do this,
  right-click the file in the File Explorer, then choose Open
  With → Text Editor.

  You can save this workaround choice as a preference by going to
  Settings → Generic →
  Editors → File
  Associations.
- Sometimes Eclipse displays a “Problem Occurred” error dialog that contains a
  message such as, ” ‘Requesting Java AST [Abstract Syntax Tree] from selection’
  has encountered a problem” and that references an `isSurrogate`
  method. This seems to be related to a method that was removed from a third-party
  library that is used by Eclipse. UD-10895

  **Workarounds:** Either of two workarounds can resolve this issue:

  - Turn off Mark Occurrences in the Eclipse
    Preferences (found under C/C++ →
    Editor → Mark
    Occurrences or Java →
    Editor → Mark
    Occurrences).
  - Upgrade to Eclipse 2022-09 (4.25) or a newer version.
- System proxy support (specifically, support for PAC or manual proxy) from the
  OS settings doesn’t work for Ubuntu 20.04.4 and later versions. UD-10238
- Code Sight sometimes cannot download larger binaries. This
  happens when Code Sight uses a proxy server that is not
  configured to stream response packets as it receives them from the server. In
  this case, Code Sight will abort the download attempt after its
  HTTP response timeout limit (currently set to 20 seconds) is reached. UD-9628

  **Workaround:** Configure the proxy server to stream response packets as
  it receives them from the server. This allows Code Sight to
  get an initial response back within the timeout period.
- While Code Sight uses an HTTPS proxy, analysis summaries from
  Coverity Connect do not download, and Code Sight fails to prompt for running a local summary. There is no
  such issue while the proxy is configured to use the HTTP protocol. UD-8064
- If Code Sight has already been running, updating
  `coverity.conf` does not automatically rebuild the
  configuration files used by Coverity. UD-7488

  This is
  noticeable, for example, when adding nonstandard filename extensions to
  `coverity.conf`. Code Sight will still
  not recognize files whose name has the new extension.

  **Workaround:**

  1. Delete the intermediate directory, idir/, for the
     project you have been scanning.

     The location of the intermediate
     directory depends on the operating system you use. See the following
     table:

     | Platform | Location of intermediate directory/folder for Coverity scans |
     | --- | --- |
     | Linux or Mac | /Users/<username>/.blackduck/desktop/controller/idirs/<project_directory>/ |
     | Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\controller\idirs\<project_folder>\ |
  2. Launch a new scan.

     This forces Coverity to build a
     new intermediate directory and to regenerate the configuration.

     Note: The following table shows the location of the
     configuration files that Coverity generates:

     | Platform | Location of generated Coverity configuration files |
     | --- | --- |
     | Linux or Mac | /Users/<username>/.blackduck/desktop/controller/data/<project_directory>/coverity-analysis-Fast/<Coverity_version>/config/ |
     | Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\controller\data\<project_folder>\coverity-analysis-Fast\<Coverity_version>\config\ |
