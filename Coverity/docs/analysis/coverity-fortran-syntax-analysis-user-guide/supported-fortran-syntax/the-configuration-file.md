---
title: "The configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-configuration-file.html"
content_id: "lsQY54dmmRZGIroym4zHMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:13.878116+00:00"
---

# The configuration file

The configuration file is composed of the following sections:

**Sections of the configuration file**

- GENERAL
- EXTENSIONS
- INTRINSICS
- OCI
- MESSAGES
- VARIOUS

The sections are identified by a header with the section name within brackets. In
the following sections, each configuration file section is described. Lines
beginning with ”`!`” are treated as comment. To enable a specific
configuration file, see The usage of language extensions.

**Mnemonic of the emulated compiler, Fortran conformance level**

The first line specifies the lowest Coverity Fortran Syntax Analysis version
number which can read this configuration file. The next line ”Mnemonic of the
emulated compiler, Fortran conformance level” specifies the following:

1. Mnemonic of the emulated compiler. This is a eight character string which
   will be presented at program startup and in the headers of the list file. It
   has no effect on the analysis.
2. Fortran conformance level. This is a three character string and can be:
   ”F77”, ”F90”, ”F95”, ”F03”, or ”F08”. All extensions are relative to the
   language level specified and all syntax of this language level will be
   enabled.

**Type information**

The next subsection ”Type information” specifies the types and kinds supported,
and the limits of the types.

1. Number of bits, difference between ABS(min) and max value of default
   integer.
2. Number of bits for an address as used for integer POINTER (extension
   55).
3. Number of bits for the various integer types.
4. Number of significant binary digits of reals.
5. Decimal exponent range of reals.
6. Maximum exponent of reals.
7. Minimum exponent of reals.
8. Minimum real which is not zero.
9. The maximum length of character constants and variables.
10. Type mnemonics.
11. Default byte-lengths of the various types
12. Byte-lengths with short-length option enabled.
13. Byte-lengths with short-length option disabled.
14. Supported types
15. Supported types for generic procedures.
16. Table of available kinds and byte lengths for non-character types (4
    lines).
17. Available character set names, kinds and byte lengths for type
    character.

**Miscellanious**

The next subsection ”Miscellanious” is composed of the following lines:

1. Default file name extensions: source, include. List-option delimiter for
   `INCLUDE` line.
2. Maximum number of continuation lines in fixed source form, and free source
   form, 0: unlimited, so accept the maximum Coverity Fortran Syntax Analysis
   can handle.
3. Maximum length of identifiers: local names, entry names, common-block names,
   0: unlimited, so accept the maximum Coverity Fortran Syntax Analysis can
   handle.
4. Compiler directive strings. Two strings can be specified with a maximum
   length of 10 characters each. For cpp preprocessing one of these strings
   must be ’#’.
5. Free-form continuation characters. The first character specified is the
   character which indicates the current line will be continued. Except in
   character context, if the last nonblank character before a ! is this
   character, the line will be continued. The sec­ond character is a character
   which can be used to indicate a continuation line.
6. First column free-form comment characters. Two characters can be specified
   which indicate for free-form input a comment line when placed in the first
   column.
