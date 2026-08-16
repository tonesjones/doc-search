---
title: "Adding annotations to Java source"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-annotations-to-java-source.html"
content_id: "cEt7V5o0qcJInG8l4Y2W4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:28.512002+00:00"
---

# Adding annotations to Java source

1. Import the relevant annotations.

   The Coverity annotations are part of the
   `com.coverity.annotations` package, and a JAR file that
   contains the primitives is located in Coverity Analysis
   installation directory at
   <install_dir>/library/annotations.jar.

   Important: If you intend to distribute annotations.jar to a
   third party, please see the paragraph regarding
   annotations.jar in the *Legal Notice*.

   For descriptions of the annotations, see the HTML pages whose root is
   <install_dir>/doc/en/annotations/index.html.
2. In the project source, annotate methods or classes with the relevant
   attributes.

   These are checkers that support Java attributes, and the particular
   attributes they support (remember that the set of checkers can change with
   each release of Coverity):

   - CALL_SUPER

     `OverridersMustCall`,
     `OverridersNeedNotCall`
   - CHECKED_RETURN

     `@CheckReturnValue`
   - GUARDED_BY_VIOLATION

     `@GuardedBy`
   - MISSING_BREAK

     `@SuppressWarnings`
   - NULL_RETURNS

     `@CheckForNull`
   - OS_CMD_INJECTION

     `@Tainted`,
     `@NotTainted`
   - PATH_MANIPULATION

     `@Tainted`,
     `@NotTainted`
   - SENSITIVE_DATA_LEAK

     `@SensitiveData`
   - SQLI

     `@Tainted`, `@NotTainted`
   - TAINT_ASSERT

     `@NotTainted`
   - WEAK_PASSWORD_HASH

     `@SensitiveData`
   - XSS

     `@Tainted`, `@NotTainted`
3. Run `cov-analyze` to scan the annotated code.
