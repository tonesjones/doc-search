---
title: "Options: Web and mobile application security"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-web-and-mobile-application-security.html"
content_id: "HZ9DG6tez8AQff2gil1ldw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:44.773011+00:00"
---

# Options: Web and mobile application security

--add-password-regex <regular_expression>
:   [Web and mobile application security option] Treats field and method
    parameter names that match the specified regular expression as a password
    source. You can specify this option multiple times. Note that if you use the
    `--add-password-regex` and
    `--replace-password-regex`, the default regular
    expression will be replaced, then extended.

    This option affects analysis by the WEAK_PASSWORD_HASH and
    SENSITIVE_DATA_LEAK checkers. See also,
    `--replace-password-regex`.

--allow-jsp-include-param-blacklist
:   [Java web application security option] Treats any servlet request parameters
    that are set through a `<jsp:include>` tag as
    untainted. This option reduces false positives when a servlet request
    parameter that is used from an included JSP file never contains tainted data
    but increases the risk of false negatives in cases where the parameter can
    be tainted.

    This setting changes the default behavior of the XSS checker, a web and
    mobile applications security checker.

--android-security
:   Enables the checkers used for Android application security analysis, including the default set of
    Sigma checks. Use these checkers only if you need them because the security
    analysis adds non-trivial time and memory requirements to the overall
    analysis.

    See "Running mobile
    application security analyses" in Coverity Analysis 2026.6.0 User and Administrator Guide for information about using this
    option.

    See also, --disable-android-security.

--directive-file <JSON_file>
:   [Security option] Takes a path to a JSON file with a number of user
    configuration directives, including Web and Android application security
    directives.

    For more information about security directives and the JSON file format, see Coverity 2026.6.0 Security Directives Reference.

    Use this option instead of `--webapp-security-config`.

--disable-webapp-security
:   [Web application security option] This option has been deprecated. Disables
    the Web application security checkers. Note that these checkers are disabled
    by default.

    See 
    `--webapp-security`.

--disable-webapp-security-preview
:   [Web application security option] This option has been deprecated. If you use
    this option, a warning will be displayed, but no other action will be
    taken.

--distrust-all
:   [Security option] This option is equivalent to setting all the
    `--distrust-*` options.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with `--trust-all`.

--distrust-mobile-other-app
:   [Mobile application security option] Specifies the default behavior of the
    analysis, which is to treat data as tainted when it is received from any
    mobile application that does not require a permission to communicate with
    the current application component.

    This option cannot be used with --trust-mobile-other-app.

--distrust-mobile-other-privileged-app
:   [Mobile application security option] Treats data as though it is tainted when
    it is received from any mobile application that requires a permission to
    communicate with the current application component. Such data is otherwise
    trusted by default.

    This option cannot be used with --trust-mobile-other-privileged-app.

--distrust-mobile-same-app
:   [Mobile application security option] Treats data received from the same
    mobile application as though it is tainted. Such data is otherwise trusted
    by default.

    This option cannot be used with --trust-mobile-same-app.

--distrust-mobile-user-input
:   [Mobile application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from user input as though it is
    tainted.

    This option cannot be used with --trust-mobile-user-input.

--distrust-command-line
:   [Web application security option] Treats command line arguments as though they are tainted. Such
    data is otherwise trusted by default. For details, see the "Tainted data
    overview" section in Customizing Coverity.

    See also, --trust-command-line.

--distrust-console
:   [Web application security option] Treats data obtained from a console (for
    example, reading from `System.in`) as though it is tainted.
    Such data is otherwise trusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    public class ConsoleInj {
      public void testInjection(Statement stmt) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String query = reader.readLine();
        stmt.executeQuery(query);
      }
    }
    ```

    This option cannot be used with --trust-console.

--distrust-cookie
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to distrust data from HTTP cookies and treat it as though
    it is tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    class SqlInjFromCookie extends HttpServlet {
        Statement sql_stmt;
        public void doPost(HttpServletRequest req, HttpServletResponse resp) {
            try {
                sql_stmt.executeQuery(req.getCookies()[0].getValue());
            } catch(Exception e) {
                // ...
            }
        }
    }
    ```

    This option cannot be used with --trust-cookie

--distrust-database
:   Treats data obtained from a database (for example, SQL query results and
    Hibernate objects) as though it is tainted. Such data is otherwise trusted
    by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    public class DatabaseInj {
      public void testInjection(int columnIndex, Statement stmt) throws Exception {
        ResultSet rs = stmt.executeQuery("SELECT * FROM *");
        String query = "SELECT * FROM " + rs.getString(columnIndex);
        stmt.executeQuery(query);
      }
    }
    ```

    This option cannot be used with --trust-database.

--distrust-environment
:   [Web application security option] Treats data that the checker identifies as
    environment variables as though it is tainted. Such data is otherwise
    trusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    public class EnvironmentInj {
      public void testInjection(Statement stmt, String getVar) throws Exception {
        String envVar = System.getEnv(getVar);
        String query = "SELECT * FROM " + envVar;
        stmt.executeQuery(query);
      }
    }
    ```

    This option cannot be used with --trust-environment.

--distrust-filesystem
:   [Web application security option] Treats data obtained from a file system as
    though it is tainted. Such data is otherwise trusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    public class FilesysInj {
      public void testRead(FileInputStream fis) throws Exception {
        byte[] b = new byte[50];
        fis.read(b);
        stmt.executeQuery("SELECT * FROM " + new String(b));
      }
    }
    ```

    This option cannot be used with --trust-filesystem.

--distrust-http
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat Web input (for example, `GET` and
    `POST` parameters) as though it is tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following Java example produces an issue report:

    ```
    class ServletInj extends HttpServlet {
      Statement sql_stmt;
      public void doPost(HttpServletRequest req, HttpServletResponse resp) {
        try {
           sql_stmt.executeQuery(req.getParameter("x"));
         } catch(Exception e) {
           // ...
         }
       }
                }
    ```

    This option cannot be used with --trust-http.

--distrust-http-header
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to distrust data from HTTP headers as though it is
    tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    class HttpHeaderInj extends HttpServlet {
      Statement sql_stmt;
      public void doPost(HttpServletRequest req, HttpServletResponse resp) {
        try {
          sql_stmt.executeQuery(req.getHeader("user-agent"));
        } catch(Exception e) {
           // ...
        }
      }
    }
    ```

    This option cannot be used with --trust-http-header.

--distrust-js-client-cookie
:   Treats data from `document.cookie` as though it is tainted.
    The default is to trust this data.

    This option cannot be used with
    `--trust-js-client-cookie`.

--distrust-js-client-external
:   Treats response data from the response to `XMLHttpRequest` and
    similar requests as though it is tainted. This is the default behavior for
    this option. See also,
    `--distrust-js-client-http-header`.

    This option cannot be used with
    `--trust-js-client-external`.

--distrust-js-client-html-element
:   Treats data from user input on HTML elements such as
    `textarea` and `input` elements as though
    it is tainted. The default is to trust this data.

    This option cannot be used with
    `--trust-js-client-html-element`.

--distrust-js-client-http-header
:   Treats data as tainted when it is from the HTTP response header of the
    response to `XMLHttpRequest` or to a similar request. This
    data is trusted by default. See also,
    `--distrust-js-client-external`.

    This option cannot be used with `--trust-js-client-http-header`.

--distrust-js-client-http-referer
:   Treats data from the `referer` HTTP header (from
    `document.referrer`) as though it is tainted. This is the
    default behavior.

    This option cannot be used with
    `--trust-js-client-http-referer`.

--distrust-js-client-other-origin
:   Treats data as tainted when it is from content in another
    `frame` or from another `origin`, for
    example, from `window.name`. This is the default
    behavior.

    This option cannot be used with
    `--trust-js-client-other-origin`.

--distrust-js-client-url-query-or-fragment
:   Treats data as tainted when it is from the query or fragment part of the URL,
    for example, `location.hash` or
    `location.query`. This is the default behavior.

    This option cannot be used with
    `--trust-js-client-url-query-or-fragment`.

--distrust-llm
:   [Web application security option] Specifies the default behavior of the analysis, which is
    to treat data obtained from a Large Language Model (LLM) API (for example,
    ChatGPT) as though it is tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the section
    "Tainted data
    overview" section in Customizing Coverity.

    Note: The checker-level version of this option (not available to all checkers
    in this group) overrides the command-level version.

    The following Java example would produce an issue report:

    ```
    public class LlmInj {
         public void testRead(ChatChoice choice) throws Exception {
    	     stmt.executeQuery("SELECT * FROM " + choice.GetMessage().getContent() );
        }
    }
    ```

    This option cannot be used with `--trust-llm`.

--distrust-network
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from a network connection (for
    example, a TCP socket or HTTP connection) as though it is tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    class NetworkInj {
      public void func(Socket s, Statement stmt) throws SQLException, IOException {
        InputStream is = s.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader br = new BufferedReader(isr);
        String query = br.readLine();

        query = "SELECT * FROM " + query;
        stmt.executeQuery(query);
      }
    }
    ```

    This option cannot be used with --trust-network.

--distrust-rpc
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to distrust data obtained from a Remote Procedure Call
    (RPC) as though it is tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example, which uses an Enterprise Java Bean (EJB), produces an
    issue report:

    ```
    @Remote(RemoteInterface.class)
    public class TestEJB implements RemoteInterface {
      Statement stmt;
      public void testWrite(String taint) {
        ResultSet rs = stmt.executeQuery("SELECT * FROM *");
        String query = "SELECT * FROM " + rs.getString(columnIndex);
        stmt.executeQuery(query);
      }
    }
    ```

    This option cannot be used with --trust-rpc.

--distrust-servlet
:   [Deprecated Web application security option] This option has been deprecated
    as of version 7.7.0 and will be removed from a future release. Use --distrust-http, instead.

    This option cannot be used with --trust-servlet.

--distrust-system-properties
:   [Web application security option] Treats system properties (those obtained
    from `System.getProperty()`) as though they are tainted. Such
    properties are otherwise trusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the checker-level version of this option
    (not available to all checkers in this group) overrides the command-level version.

    The following example produces an issue report:

    ```
    public class SystemPropertiesInj {
       public void testInjection(Statement stmt, String p) throws Exception {
         stmt.executeQuery("SELECT * FROM " + System.getProperty(p));
       }
    }
    ```

    This option cannot be used with --trust-system-properties.

--framework-analyzer-timeout
:   [Web application security option] Increase the timeout (specified in minutes)
    for the framework analyzer. The default value is `60` (60
    minutes).

    Use this option if the framework analyzer takes too long and is killed. Note
    that the need to use this option suggests that the hardware in use is most
    likely overloaded and not powerful enough for the analysis.

--not-tainted-field <fully_qualified_field_name>
:   [Web application security option] The value
    <fully_qualified_field_name> is a Perl
    regular expression describing a fully qualified field name. Any matching
    fields will be asserted to be untainted. Additional defects may be reported
    by the TAINT_ASSERT checker, but reported issues
    involving unsafe uses of the value will be suppressed in the Web application
    security checkers.

    The option can be specified multiple times on a single command line.

    See "Adding
    assertions that fields are tainted or not tainted" in Customizing Coverity for details.

--recommended-security-checkers
:   This is the default option used by the Coverity CLI on Polaris.

    This option has the same effect as
    specifying both `--android-security` and
    `--webapp-security`. It enables checkers that are used
    for Android application security analysis and web application security
    analysis, including the default set of Sigma
    checkers.

--replace-password-regex <regular_expression>
:   [Web application security option] Replaces the default regular expression
    that the checker uses to infer passwords. You can specify this option only
    once. Note that if you use the `--add-password-regex` and
    `--replace-password-regex`, the default regular
    expression will be replaced, then extended.

    This option affects analysis by the WEAK_PASSWORD_HASH and
    SENSITIVE_DATA_LEAK checkers. See also, `--add-password-regex`.

--report-null-field-address
:   When you specify this option, the analysis considers `&p->field` as
    dereferencing p. Specifying this option would cause the
    "check NULL dereferencing" checkers (for example
    FORWARD_NULL, NULL_RETURNS,
    NULL_FIELD,etc.) to report more defects. While it is
    undefined behavior to form `p->field` when
    p is null, in practice
    "`&p->field`" just adds a constant to the value of
    p without performing a dereference. Some code relies
    on this behavior to delay the null check on p, so by
    default, this is not reported as a defect. See also --field-offset-escape.

--skip-android-app-sanity-check
:   [Android application security option] Suppresses the warning message that
    normally appears if Android application security checkers are enabled with
    the `--android-security option`, but no Android application
    was captured.

    The check, which this option overrides, is designed to catch the case where someone intended
    to run Android application security checkers but forgot to capture the
    Android application using `coverity capture`.

--skip-webapp-sanity-check
:   [Java-only Web application security option] Suppresses the warning message
    that normally appears if any Web application security checkers are enabled
    but `cov-emit-java --webapp-archive` was not used to emit
    the Web application (web-app) archive or directory.

    The check, which this option overrides, is designed to catch the case where
    someone intended to run Web application security checkers but forgot to emit
    the WAR file. It is technically possible, but highly unlikely, for Java
    classes to contain an entire Web application (without any JSPs or framework
    configuration), in which case there would be no need for a WAR file.

    For additional details, see --webapp-security and --skip-war-sanity-check.

--tainted-field <fully_qualified_field_name>
:   [Web application security option] Takes a Perl-style regular expression that
    describes a fully qualified field name. Any matching fields will be asserted
    to be tainted. Additional defects may be reported by the Web application
    security checkers, if any of the specified fields are used in an unsafe
    manner. The option can be specified multiple times on a single command line.
    As an example, passing the command line option `-tainted-field
    com.coverity.examples.Table.*` will assert that the fields title
    and values are tainted in the following code.

    ```
    Package com.coverity.examples;

    class Table {
      String title;
      String value;
      int id;
    }
    ```

    See "Adding
    assertions that fields are tainted or not tainted" in Customizing Coverity for more information.

--trust-all
:   [Security option] This option is equivalent to providing all the
    `--trust-*` options.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-all.

--trust-mobile-other-app
:   [Mobile application security option] Trusts data received from any mobile
    application when it does not require a permission to communicate with the
    current application component. Such data is otherwise distrusted by
    default.

    This option cannot be used with --distrust-mobile-other-app.

--trust-mobile-other-privileged-app
:   [Mobile application security option] Specifies the default behavior of the
    analysis, which is to trust data received from any mobile application that
    requires a permission to communicate with the current application
    component.

    This option cannot be used with --distrust-mobile-other-privileged-app.

--trust-mobile-same-app
:   [Mobile application security option] Specifies the default behavior of the
    analysis, which is to trust data received from the same mobile
    application.

    This option cannot be used with --distrust-mobile-same-app.

--trust-mobile-user-input
:   [Mobile application security option] The analysis treats data obtained from
    user input as though it is not tainted. Such data is otherwise distrusted by
    default.

    This option cannot be used with --distrust-mobile-user-input.

--trust-command-line
:   [Web application security option] Specifies the default behavior of the analysis, which is to
    treat command line arguments as though they are not tainted. For details, see the "Tainted data
    overview" section in Customizing Coverity.

    See also, --distrust-command-line.

--trust-console
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from a console (for example,
    reading from `System.in`) as though it is not tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-console.

--trust-cookie
:   [Web application security option] Treats data that is obtained from an HTTP
    cookie as though it is not tainted. Such data is otherwise distrusted by
    default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-cookie

--trust-database
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from a database (for example, SQL
    query results and Hibernate objects) as though it is not tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-database.

--trust-environment
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data from environment variables as though it is
    not tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the analysis trusts data from environment variables by default.

    This option cannot be used with --distrust-environment.

--trust-filesystem
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from a file system as though it is
    not tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    Note that the analysis trusts data from filesystem sources by default.

    This option cannot be used with --distrust-filesystem.

--trust-http
:   [Web application security option] Treats Web input (for example,
    `GET` and `POST` parameters) as though it
    is not tainted. Web input is otherwise treated as tainted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-http.

--trust-http-header
:   [Web application security option] Treats data that is obtained from an HTTP
    header as though it is not tainted. Such data is otherwise distrusted by
    default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-http-header.

--trust-js-client-cookie
:   Trusts data from `document.cookie`.

    This option cannot be used with `--distrust-js-client-cookie`.
    This is the default behavior.

--trust-js-client-external
:   Trusts response data from the response to `XMLHttpRequest` and
    similar requests. The default is to distrust this data. See also,
    `--trust-js-client-http-header`.

    This option cannot be used with
    `--distrust-js-client-external`.

--trust-js-client-html-element
:   Trusts data from user input on HTML elements such as
    `textarea` and `input` elements. This is
    the default behavior.

    This option cannot be used with
    `--distrust-js-client-html-element`.

--trust-js-client-http-referer
:   Trusts data from the `referer` HTTP header (from
    `document.referrer`). The default is to distrust this
    data.

    This option cannot be used with
    `--distrust-js-client-http-referer`.

--trust-js-client-http-header
:   Trusts data from the HTTP response header of the response to
    `XMLHttpRequest` and similar requests. This is the
    default behavior. See also, `--trust-js-client-external`.

    This option cannot be used with
    `--distrust-js-client-http-header`.

--trust-js-client-other-origin
:   Trusts data from content in another `frame` or from another
    `origin`, for example, from `window.name`.
    The default is to distrust this data.

    This option cannot be used with
    `--distrust-js-client-other-origin`.

--trust-js-client-url-query-or-fragment
:   Trusts data from the query or fragment part of the URL, for example,
    `location.hash` or `location.query`. The
    default is to distrust this data.

    This option cannot be used with
    `--distrust-js-client-url-query-or-fragment`.

--trust-llm
:   [Web application security option] Treats data obtained from a Large Language Model (LLM)
    API (for example, ChatGPT) as though it is not tainted. Such data is otherwise
    distrusted by default.

    This option applies to all the checkers in the group
    Security (Tainted dataflow checker). For details, see the section "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with the `--distrust-llm` option.

--trust-network
:   [Web application security option] Treats data obtained from a network
    connection (for example, a TCP socket or HTTP connection) as though it is
    not tainted. Such data is otherwise distrusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-network.

--trust-rpc
:   [Web application security option] Treats data obtained from a Remote
    Procedure Call (RPC) as though it is not tainted. Such data is otherwise
    distrusted by default.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-rpc.

--trust-servlet
:   [Web application security option] This option has been deprecated as of
    version 7.7.0 and will be removed from a future release. Use with --trust-http, instead.

    This option cannot be used with `--distrust-servlet`.

--trust-system-properties
:   [Web application security option] Specifies the default behavior of the
    analysis, which is to treat data obtained from system properties (for
    example, `System.getProperty()`) as though it is not
    tainted.

    This option applies to all the checkers in
    the group Security (Tainted dataflow checker). For details, see the "Tainted data
    overview" section in Customizing Coverity.

    This option cannot be used with --distrust-system-properties.

--webapp-security
:   [Web application security option] Enables the checkers that are used for Web application security
    analysis, including the default set of Sigma checks.

    Java Prerequisite: Prior use of the --webapp-archive option to `cov-emit-java` for
    the WAR file. See "Running a security analysis on a Java Web
    application" in the Coverity Analysis 2026.6.0 User and Administrator Guide for
    details.

    .NET Recommendation: Coverity highly recommends ensuring that `cov-build`
    captured your Web application template and configuration files. See "Running a
    security analysis on an ASP.NET Web application" in the Coverity Analysis 2026.6.0 User and Administrator Guide for details.

    Note: Use these checkers only if you need them because the security analysis
    adds non-trivial time and memory requirements to the overall
    analysis.

--webapp-security-aggressiveness-level <low|medium|high>
:   [Web application security option] Tunes the aggressiveness of assumptions
    that the analysis makes to find potential security vulnerabilities (security
    defects). Higher levels report more defects, but the analysis time increases
    and memory usage is likely to increase. Higher levels also increase the
    likelihood that any given defect is a false positive. Values for level are
    `low`, `medium`, or `high`.
    Default is `low`.

    This option can assist security auditors who need to see more defects than
    developers might need to see.

    When analyzing code that uses unsupported Web application frameworks, medium
    or high aggressiveness levels can be more useful than the default.

    The following checkers are affected (for details, see the checker's description):

    - ANGULAR_EXPRESSION_INJECTION,
    - ASPNET_MVC_VERSION_HEADER,
    - COOKIE_INJECTION,
    - CSRF,
    - CSS_INJECTION,
    - DISTRUSTED_DATA_DESERIALIZATION,
    - DOM_XSS,
    - EL_INJECTION,
    - HARDCODED_CREDENTIALS,
    - HEADER_INJECTION,
    - INSECURE_RANDOM,
    - INSUFFICIENT_LOGGING,
    - JAVA_CODE_INJECTION,
    - JCR_INJECTION,
    - JSP_DYNAMIC_INCLUDE,
    - JSP_SQL_INJECTION,
    - LDAP_INJECTION,
    - LOCALSTORAGE_MANIPULATION,
    - LOG_INJECTION,
    - MASS_ASSIGNMENT,
    - MISSING_AUTHZ,
    - MISSING_IFRAME_SANDBOX,
    - NOSQL_QUERY_INJECTION,
    - OGNL_INJECTION,
    - OPEN_REDIRECT,
    - OS_CMD_INJECTION,
    - PATH_MANIPULATION,
    - REGEX_INJECTION,
    - SCRIPT_CODE_INJECTION,
    - SENSITIVE_DATA_LEAK,
    - SESSION_FIXATION,
    - SESSIONSTORAGE_MANIPULATION,
    - SQLI,
    - TAINTED_ENVIRONMENT_WITH_EXECUTION,
    - TEMPLATE_INJECTION,
    - TRUST_BOUNDARY_VIOLATION,
    - UNENCRYPTED_SENSITIVE_DATA,
    - UNKNOWN_LANGUAGE_INJECTION,
    - UNRESTRICTED_DISPATCH,
    - UNSAFE_DESERIALIZATION,
    - UNSAFE_JNI,
    - UNSAFE_NAMED_QUERY,
    - UNSAFE_REFLECTION,
    - URL_MANIPULATION,
    - WEAK_GUARD,
    - WEAK_PASSWORD_HASH,
    - XML_EXTERNAL_ENTITY,
    - XML_INJECTION,
    - XPATH_INJECTION,
    - XSS.

    Remember: Setting
    `--webapp-security--agressiveness-level` to
    `high` includes the effect of setting
    `--distrust-all`.

--webapp-security-config <JSON_file>
:   [Java Web application security option] Alias for --directive-file.

--webapp-security-preview
:   [Web application security option] Deprecated. Does the same thing as
    `--webapp-security`.

    See also `--webapp-security`.
