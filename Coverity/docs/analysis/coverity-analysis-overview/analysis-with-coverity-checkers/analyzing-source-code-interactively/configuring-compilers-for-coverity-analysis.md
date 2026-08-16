---
title: "Configuring compilers for Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-compilers-for-coverity-analysis.html"
content_id: "svgMBxXKF2wpy5s3mxFOSQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:22.337116+00:00"
---

# Configuring compilers for Coverity Analysis

Before you configure compilers for your production environment,
please be sure that you will be using compilers supported by Coverity Analysis.

Unsupported compilers can cause incompatibilities when the Coverity
compiler attempts to parse your code. Support for additional compilers is based
on a variety of factors including customer need, the compiler's availability,
and how many customers are using it.

To request that Coverity extend support to
your compiler, open a support case at <https://community.blackduck.com/s/contactsupport>.

Use the following command to list the supported compiler types and the values
that are used for identifying them for compiler
configurations:

```
> cov-configure --list-compiler-types
```

The following example shows a small portion of the output:

```
csc,csc,C#,FAMILY HEAD,Microsoft C# Compiler
g++,g++,CXX,SINGLE,GNU C++ compiler
gcc,gcc,C,FAMILY HEAD,GNU C compiler
java,java,JAVA,SINGLE,Oracle Java compiler (java)
javac,javac,JAVA,FAMILY HEAD,Oracle Java compiler (javac)
msvc,cl,C,FAMILY HEAD,Microsoft Visual Studio
```

In the example, `csc` is the value used to identify the compiler, and
`Microsoft C# Compiler` is the name of the supported
compiler. More generally, the output contains compiler configuration values for
the `--comptype` and `--compiler` options and
related information. Note that FAMILY HEAD values are used to configure a
related family of compilers (for example, `gcc` for GNU gcc and
g++ compilers), while SINGLE values are for single-compiler configurations (for
example, `g++` for the GNU g++ compiler only).

For support documentation, see supported compiler information in "Supported languages, compilers, and frameworks for Coverity Analysis"
in the Coverity 2026.6.0 Installation and Upgrade Guide.

There are two types of configurations: template configuration or full configuration.
Use template configuration unless you need to address a specific problem that makes a full configuration necessary.

In this section:

- Generating a template configuration
- Generating a full configuration
- Using 'ccache' or 'distcc'
- Compiler-specific configurations
- Using predefined macros for Coverity Analysis-specific compilations
- Modifying preprocessor behavior to improve compatibility
