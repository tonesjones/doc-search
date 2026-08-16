---
title: "Generating a full configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-full-configuration.html"
content_id: "0hz7dchc8~Nupl2NKeDSMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:23.617430+00:00"
---

# Generating a full configuration

Each full configuration that is generated configures one specific compiler
installation on the system. Unlike a template configuration, which specifies the
executables configured at build time, a full configuration is a completed
configuration file that specifies exactly how `cov-translate` and
`cov-emit` are fully compatible with your native build's compilers.

Important:
You must run `cov-configure` in exactly the same
environment that you run your native compiler. If you run the command
without configuring the operating environment exactly as it is in your
native build
environment, the configuration will be inaccurate.

(For C/C++ compilers, `cov-configure` invokes the native compiler to determine its
built-in macro definitions and the system include directories.)

Because a full configuration applies to a compiler installation, not a single
compiler executable, a single invocation of `cov-configure` attempts to
configure both the C and C++ compilers in the specified installation if the compiler
names are not different than a standard installation.

Note:
A compiler configuration might be platform-specific. For example, if you configure a
gcc or g++ compiler on a 32-bit system, you cannot use it for a build on a 64-bit
system. Also, if you change a compiler's default options after configuring it, or
install a different version of the compiler, its behavior might change and invalidate
the configuration that you created earlier. Make sure that the compiler that you
configure exactly matches the compiler that your build uses.

Many C compilers can compile both C and C++ code depending on the compiler file's
extension. The `cov-configure` command creates a different
configuration file for each combination of compiler executable and language. Thus,
`> cov-configure --compiler gcc --comptype gcc` creates a configuration file for
each of the following compiler and language combinations:

- `gcc` as a C compiler
- `gcc` as a C++ compiler
- `g++` as a C++ compiler

Additional usage instructions:

- If you configure an ARM compiler, you must also configure its Thumb counterpart. Similarly,
  configuring javac configures any `java`, `apt`,
  and `javaw` (Windows systems only) commands found in the same
  JAVA_HOME directory tree.
- When invoking `cov-configure`, make sure to specify the `--comptype <type>` option.

  For example:

  ```
  > cov-configure --compiler i686-powerpc-gcc --comptype gcc
  ```
- Some compilers require additional options. For example, GNU compiler installations that use a
  nonstandard preprocessor (`cpp0`) path require the GNU
  `-B` option that specifies it:

  ```
  > cov-configure --compiler gcc --comptype gcc -- -B/home/coverity/gcc-cpp0-location/bin
  ```

  The double-hyphen (--) indicates the end of the `cov-configure` options.
