---
title: "Customization: Compilation mnemonics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/customization-compilation-mnemonics.html"
content_id: "WMWcnsqvsGGsirVY1A58Ag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:40.760120+00:00"
---

# Customization: Compilation mnemonics

Which Bazel actions are treated as build commands is determined by the mnemonic of the
action. For now, the only mnemonics that are treated as a build commands by default are
`CppCompile`, `Javac` and `Compile`.
These are the mnemonics that the built-in `cc_binary/cc_library` rules,
the built-in `java_binary/java_library` rules and the standard
`csharp_binary/csharp_library` rules use for their compilation
actions, respectively.

If you have custom rules that generate actions that should be treated as build commands, add
--bazel-extra-compile-mnemonic <YourCompilationMnemonic> to the
cov-build command so that we can treat that as a compilation as
well. This option can be passed more than once if you have multiple extra compilation
mnemonics to use.
