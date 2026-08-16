---
title: "The configuration: Invoking 'cov-configure'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-configuration-invoking-cov-configure-.html"
content_id: "SgxffMdd6NP8lw_fVYRm1w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:51.515421+00:00"
---

# The configuration: Invoking 'cov-configure'

Here are the `cov-configure` options to use for various commonly used languages.

Table 1. Commonly used options to cov-configure

| Language | Configuration Option | Notes |
| --- | --- | --- |
| C/C++ (for GNU GCC and G++) | `--gcc` | To perform a configuration for `gcc` and `g++`, you can use the `--gcc` command option. The console output for a successful configuration looks something like the following:   ``` Generated coverity_config.xml at location  /my_install_dir/config/coverity_config.xml Successfully generated configuration for the compilers: g++ gcc ``` |
| C, C++, Objective-C, and Objective-C++ (for `clang` and `clang++`) | `--clang` | See also Clang compiler |
| Dart | `--dart` |  |
| CUDA | `--cuda` (for all CUDA compilers) |  |
| Go | `--go` |  |
| Java build capture (for `java`, `javac`, `javaw`, `apt`) and JSPs | `--java` |  |
| Java buildless capture and JSPs | `--java-buildless` |  |
| JavaScript | `--javascript` |  |
| Kotlin | `--kotlin` |  |
| Microsoft C and C++ (for `cl.exe`) | `--msvc` |  |
| Microsoft C# (for `csc.exe`) | `--cs` | The console output for a successful configuration for C# looks something like the following:  ``` Generated coverity_config.xml at location  /my_install_dir/config/coverity_config.xml Successfully generated configuration for the compilers: csc ``` |
| PHP | `--php` |  |
| Python | `--python` |  |
| Ruby | `--ruby` |  |
| Rust | `--rust` | Only Cargo-based builds are captured; `rustc` builds without cargo are not captured. This is a beta feature. Do not use it in production. |
| Scala | `--scala` |  |
| TypeScript | `--typescript` |  |

Note:
To create configuration for compilers that are not listed here and to
understand configuration for a production environment,
see Configuring compilers for Coverity Analysis.

On some Windows platforms, you might need to use
Windows administrative privileges when you run `cov-configure`.

Typically, you can set the administrative permission
through an option in the right-click menu of the executable for the command interpreter
(for example, Cmd.exe or Cygwin) or Windows Explorer.

Important:
Typically you run `cov-configure` only once
per installation (or upgrade) and compiler type or scripting language because
the configuration process stores the configuration values for the compiler in
coverity_config.xml file. However, if you need to
perform a reconfiguration (for example, because the native compiler, build
environment, or hardware changes), see Changing a configuration for a compiler.
