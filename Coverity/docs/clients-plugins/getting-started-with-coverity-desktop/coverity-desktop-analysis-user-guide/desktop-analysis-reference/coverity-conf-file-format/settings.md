---
title: "Settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/settings.html"
content_id: "PAMDFCvou3vWGBDFuFHhYQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:16.486238+00:00"
---

# Settings

The `Settings` class contains the configuration parameters that directly
influence the operation of tools. It contains the following attributes:

add_compiler_configurations?: CompilerConfiguration[]
:   A supplementary set of compiler configurations. These do not override anything; instead,
    all active configuration sources'
    `add_compiler_configurations` attributes contribute
    additional configurations to the total set that will be active.

codexm_files?: CodeXMFiles
:   This property contains CodeXMFiles objects that define individual CodeXM
    checkers which are provided for analysis. CodeXM checkers are enabled once
    they are specified in the codexm_files property.

compiler_config_file?: path
:   The name of the coverity_config.xml file where the compiler
    configuration information shall be stored. It corresponds to the
    `--config` command line option.

    The default value is
    "`$(code_base_dir)/data-coverity/v$(version)/config/coverity_config.xml`".

compiler_configurations?: CompilerConfiguration[]
:   This array contains specifications for how to configure compilers. Each element corresponds
    to one invocation of `cov-configure` to run when setting up
    desktop analysis on the developer's workstation.

    The default value
    is:

    ```
        "compiler_configurations": [
          {
            "cov_configure_args": [
              "--javascript",
              "--if-supported-platform"
            ]
          },
          {
            "cov_configure_args": [
              "--php",
              "--if-supported-platform"
            ]
          },
          {
            "cov_configure_args": [
              "--python",
              "--if-supported-platform"
            ]
          },
          {
            "cov_configure_args": [
              "--ruby",
              "--if-supported-platform"
            ]
          },
          {
            "cov_configure_args": [
              "--gcc"
            ]
          },
          {
            "cov_configure_args": [
              "--java"
            ]
          },
          {
            "cov_configure_args": [
              "--kotlin"
            ]
          },
          {
            "cov_configure_args": [
              "--scala"
            ]
          },
          {
            "cov_configure_args": [
              "--msvc"
            ]
          },
          {
            "cov_configure_args": [
              "--cs"
            ]
          },
          {
            "cov_configure_args": [
              "--clang"
            ]
          }
        ]
    ```

    That means that you only need to set this value if using a compiler
    other than GNU C/C++ under the name `gcc` or
    `g++`, Microsoft C/C++/C#, Oracle Java, or Clang. All
    interpreted languages (filesystem capture) supported for Coverity
    analysis on the current platform are part of this default
    configuration.

    Otherwise, you need to create one
    `CompilerConfiguration` element for each compiler
    used during the build. For example, if you are using [ccache](https://ccache.samba.org/) with GCC, then you should set
    `compiler_configurations` to:

    ```
          [
            {
              // cov-configure --gcc
              "cov_configure_args": ["--gcc"]
            },
            {
              // cov-configure --compiler ccache --comptype prefix
              "cov_configure_args": ["--compiler", "ccache", "--comptype", "prefix"]
            }
          ]
    ```

    See "Configuring compilers for Coverity Analysis" in Coverity Analysis 2026.6.0 User and Administrator Guide for more information on how to
    use `cov-configure`. Once you have a set of
    `cov-configure` command lines that configure your
    compilers, put them in `compiler_configurations` or
    `add_compiler_configurations`.

    If an
    overriding configuration specification (from another file, or from a
    conditional configuration) specifies this attribute, then the
    *entire* set of configurations is replaced with the overriding
    set.

cov_run_desktop?: CovRunDesktopSettings
:   Settings specific to the operation of `cov-run-desktop`, see the Coverity 2026.6.0 Command Reference.

extend_directories?: ExtendDirectories
:   `ExtendDirectory` objects which define the individual custom checkers
    provided for analysis. The extend checker names defined here are used in the
    extend_checkers property of
    `CovRunDesktopSettings`.

intermediate_dir?: path
:   Specifies the location of the intermediate directory, which is one piece of the local state
    maintained by desktop analysis. It corresponds to the `--dir`
    command line option.

    The default value is "`$(code_base_dir)/data-coverity/v$(version)/idir`".

    Note: Note that Desktop
    Analysis can only be run on an intermediate directory created on the
    same machine, and in the same source code directory, as the analysis
    will take place (i.e. the build and analysis processes must take place
    on the same machine and directory, and the intermediate directory must
    not be moved).

known_installations?: KnownInstallation[]
:   Sequence of known installations of Coverity tools.

license_file_dir?: path
:   Directory where automatically downloaded license files are stored.

    The default value is
    "`$(code_base_dir)/data-coverity/v$(version)/lic`".

server?: Server
:   Settings that specify how to access the Coverity Connect server.

stream?: string
:   The name of the Coverity Connect stream from which to get analysis summaries. The stream
    should contain snapshots obtained by analyzing the same code base and branch
    as will be analyzed on the desktop.

    There is no default for this setting,
    so it must be set in a coverity.conf file or on the
    command line.

scm?: SCMSettings
:   Settings for interacting with the SCM.

tmpdir?: path
:   Directory in which to store temporary data (data that, under normal circumstances, is
    removed by the same process that created it). The default value is
    determined based on operating system.
