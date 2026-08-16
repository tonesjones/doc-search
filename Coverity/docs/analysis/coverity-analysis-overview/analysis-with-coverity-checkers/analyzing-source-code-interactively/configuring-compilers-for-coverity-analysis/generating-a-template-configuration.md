---
title: "Generating a template configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-template-configuration.html"
content_id: "lwpmI5vizlffrOOgnVCgbQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:22.971385+00:00"
---

# Generating a template configuration

To generate a template configuration, you can invoke `cov-configure` with the `--template` argument.

For example, here is a template configuration for the `gcc` C/C++ compiler:

```
> cov-configure --template --compiler gcc --comptype gcc
```

We specifically recommend that you use template configuration for the following compilers: gcc, g++, qnx, tmcc,
Tensilica Xtensa, Green Hills, and MetaWare.

The following alternatives generate a template configuration for the GNU GCC and G++ compilers
(using `gcc`), Microsoft C and C++ compilers (using
`msvc`), Java compilers (using `java`, not
`javac`), and C# compilers (using
`csc`).

The next example shows an alternative template configuration for the `gcc` C/C++ compiler:

```
> cov-configure --gcc
```

[Recommended for C#] Here is an alternative template configuration for the Microsoft C# compiler:

```
> cov-configure --cs
```

[Recommended for Java] Here is an alternative template configuration for build capture with the Java compiler:

```
> cov-configure --java
```

[Recommended for Java] Here is an alternative template configuration for Java buildless capture:

```
> cov-configure --java-buildless
```

For more information about creating a template configuration, see the
`--template` option in the cov-configure description.

The previous commands would generate the following files:

- The <install_dir>/config/coverity_config.xml
  configuration file
- The <install_dir>/config/template-gcc-config-0
  sub-directory with its own coverity_config.xml file

The configuration file specifies that `cov-build` configure
`gcc` executables as compilers and that
`cov-translate` treat them as compilers.

For Java programs, `cov-build` configures the executable and treats it
as a Java compiler.

Creating a template configuration for one compiler also creates templates for any related
compiler, just as in a full configuration.

For example:

- `gcc` implies `g++` (`cc` links to `gcc` as well on some platforms).
- `javac` implies `java`, `apt`, and `javaw` (on Windows systems).

To see a full list of supported compiler types, run the `cov-configure --list-compiler-types` option.
